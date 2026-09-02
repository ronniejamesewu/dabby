"""menu_price.py -- deal-aware pricing over dispensary menu Rows.

Owns shopping/deals/. Reads Row dicts from menu_fetch (STORES registry,
fetch_store, load_rows_json) and the deals schema documented in
shopping/deals/SCHEMA.md, and answers "what does this actually cost" and
"what day should I buy it" questions.

Design principles (binding, shared with the rest of the shopping layer):
retrieval is code; stock and prices are ephemeral and never committed;
public register in any committed text; no fabricated specifics -- an
unknown fact is written `unknown`, never a plausible fill.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import date, datetime, time as dtime, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
    DENVER = ZoneInfo("America/Denver")
except Exception:  # pragma: no cover - stdlib should always have zoneinfo on 3.9+
    DENVER = None

import menu_fetch

DEALS_DIR = Path(__file__).resolve().parent / "shopping" / "deals"
ASSUMED_TAX_RATE = 0.30  # labeled assumption used only when a store's tax basis is unknown
DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


# --------------------------------------------------------------------------
# deals loading
# --------------------------------------------------------------------------

def _load_json(path: Path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_deals(store_key: str):
    """Merge <store_key>.json (posted) and <store_key>_feed.json (feed).

    Returns a list of deal dicts. Each deal carries its own `source`
    ('feed' or 'posted') plus an injected `_captured` (from its file's
    top-level `captured`) and `_file_source` (the file's top-level
    `source` text/URL) for staleness/provenance reporting.
    """
    deals = []
    posted = _load_json(DEALS_DIR / f"{store_key}.json")
    if posted:
        for d in posted.get("deals", []):
            d = dict(d)
            d.setdefault("source", "posted")
            d["_captured"] = posted.get("captured")
            d["_file_source"] = posted.get("source")
            deals.append(d)
    feed = _load_json(DEALS_DIR / f"{store_key}_feed.json")
    if feed:
        for d in feed.get("deals", []):
            d = dict(d)
            d.setdefault("source", "feed")
            d["_captured"] = feed.get("captured")
            d["_file_source"] = feed.get("source")
            deals.append(d)
    return deals


# --------------------------------------------------------------------------
# brand / applicability matching
# --------------------------------------------------------------------------

def _norm_brand(s):
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


_INHOUSE_FAMILY = {
    "in house", "in-house", "inhouse", "in house melts",
    "erva x in house", "erva by in house melts", "erva x inhouse",
}


def _is_inhouse(norm):
    if norm in _INHOUSE_FAMILY:
        return True
    return "in house" in norm or "inhouse" in norm


def _brand_matches(deal_brand, row):
    if not deal_brand:
        return False  # a brand/product-scoped deal with no target never prices anything; it is listed only
    db = _norm_brand(deal_brand)
    rb = _norm_brand(row.get("brand") or "")
    if _is_inhouse(db) and _is_inhouse(rb):
        return True
    if db and (db == rb or db in rb or rb in db):
        return True
    raw = _norm_brand(row.get("raw_name") or "")
    if db and db in raw:
        return True
    return False


def _dow_sun0(when: datetime) -> int:
    """Python weekday() is Mon=0..Sun=6; deals schema is Sun=0..Sat=6."""
    return (when.weekday() + 1) % 7


def _parse_hhmm(s):
    h, m = s.split(":")
    return dtime(int(h), int(m))


def applicable(deal: dict, row: dict, when: datetime) -> bool:
    """day-of-week -> hours -> start/end date -> menu_type -> scope/brand/
    category -> excludes/includes (tested against raw_name)."""
    days = deal.get("days")
    if days is not None and _dow_sun0(when) not in days:
        return False

    hours = deal.get("hours")
    if hours:
        t = when.time()
        if not (_parse_hhmm(hours["start"]) <= t <= _parse_hhmm(hours["end"])):
            return False

    d = when.date()
    start_d = deal.get("start")
    if start_d and d < date.fromisoformat(start_d):
        return False
    end_d = deal.get("end")
    if end_d and d > date.fromisoformat(end_d):
        return False

    menu_type = deal.get("menu_type", "both")
    if menu_type and menu_type != "both":
        row_menu_type = row.get("menu_type") or "rec"
        if menu_type != row_menu_type:
            return False

    scope = deal.get("scope", "product")
    if scope == "store":
        pass
    elif scope == "brand" or scope == "product":
        if not _brand_matches(deal.get("brand"), row):
            return False
    elif scope == "category":
        cat = (deal.get("category") or "").lower()
        haystack = f"{row.get('form') or ''} {row.get('raw_name') or ''}".lower()
        if cat and cat not in haystack:
            return False
        if deal.get("brand") and not _brand_matches(deal.get("brand"), row):
            return False

    raw = row.get("raw_name") or ""
    for pat in deal.get("excludes") or []:
        if re.search(pat, raw):
            return False
    includes = deal.get("includes")
    if includes:
        if not any(re.search(pat, raw) for pat in includes):
            return False

    return True


# --------------------------------------------------------------------------
# pricing
# --------------------------------------------------------------------------

def price_on(row: dict, deals: list, when: datetime, store: dict) -> dict:
    """Apply the store's stacking rule to every applicable percent deal.

    Two candidate prices exist whenever a feed special is present: the
    special itself, un-stacked ("best single offer" may just be the
    special), or the menu price with a posted deal applied. 'compound'
    means stack the feed special *and* the posted deal(s) together.
    """
    tax = store.get("tax", {}) if store else {}
    stacking_rule = (store.get("stacking", {}) or {}).get("rule", "unknown") if store else "unknown"

    menu = row.get("price")
    special = row.get("special_price")
    special_active = special is not None

    percent_deals = [
        d for d in deals
        if d.get("kind") == "percent" and isinstance(d.get("value"), (int, float)) and not d.get("requires_id") and applicable(d, row, when)
    ]
    other_deals = [
        d for d in deals
        if (d.get("kind") != "percent" or d.get("requires_id") or not isinstance(d.get("value"), (int, float))) and applicable(d, row, when)
    ]

    deal_price = None
    deal_names = []
    stacking_note = None
    best_single_price = None
    compound_price = None

    if stacking_rule == "none":
        if special_active:
            deal_price = round(special, 2)
            if percent_deals:
                stacking_note = (
                    f"{len(percent_deals)} posted deal(s) not applied on top of feed special "
                    f"(stacking=none)"
                )
        elif percent_deals:
            choices = [(menu * (1 - d["value"] / 100.0), d) for d in percent_deals]
            price, best_deal = min(choices, key=lambda c: c[0])
            deal_price = round(price, 2)
            deal_names = [best_deal["name"]]
    elif percent_deals:
        candidates = []
        if special_active:
            candidates.append((special, None))
        for d in percent_deals:
            candidates.append((menu * (1 - d["value"] / 100.0), d))
        best_price, best_deal = min(candidates, key=lambda c: c[0])
        best_single_price = round(best_price, 2)
        best_single_names = [best_deal["name"]] if best_deal is not None else []

        base_for_compound = special if special_active else menu
        p = base_for_compound
        for d in percent_deals:
            p = p * (1 - d["value"] / 100.0)
        compound_price = round(p, 2)
        compound_names = [d["name"] for d in percent_deals]

        if stacking_rule == "best-single":
            deal_price = best_single_price
            deal_names = best_single_names
        elif stacking_rule == "compound":
            deal_price = compound_price
            deal_names = compound_names
        else:  # unknown -- report both, default display is best-single
            deal_price = best_single_price
            deal_names = best_single_names
            stacking_note = (
                f"stacking unknown (best-single shown; compound would be "
                f"${compound_price:.2f})"
            )
    else:
        deal_price = round(special, 2) if special_active else None

    price_used = deal_price if deal_price is not None else (special if special_active else menu)

    basis = tax.get("basis", "unknown")
    rate = tax.get("rate")
    otd = None
    otd_if_pretax = None
    if basis == "pre-tax" and rate is not None:
        otd = round(price_used * (1 + rate), 2)
    elif basis == "otd":
        otd = round(price_used, 2)
    else:
        basis = "unknown"
        otd_if_pretax = round(price_used * (1 + ASSUMED_TAX_RATE), 2)

    size_g = row.get("size_g")
    denom = otd if otd is not None else price_used
    per_gram = round(denom / size_g, 2) if size_g else None

    return {
        "menu": menu,
        "special": special,
        "deal_price": deal_price,
        "deal_names": deal_names,
        "otd": otd,
        "otd_basis": basis,
        "otd_if_pretax": otd_if_pretax,
        "per_gram": per_gram,
        "stacking_note": stacking_note,
        "stacking_rule": stacking_rule,
        "best_single": best_single_price,
        "compound": compound_price,
        "other_deals": [d["name"] for d in other_deals],
        "qty": row.get("qty"),
    }


# --------------------------------------------------------------------------
# row loading / filtering
# --------------------------------------------------------------------------

def _rows_from_json_arg(arg: str):
    """`--json path:store_key` -- menu_fetch.load_rows_json(path, store_key)
    needs the store key to normalize a dutchie-embed dump (it looks up tax/
    stacking/grammar from STORES), so the store key is required here, not
    optional -- a bare path with no colon is a usage error."""
    path_s, store_key = arg, None
    if ":" in arg and not (len(arg) > 2 and arg[1:3] == ":\\" and arg.count(":") == 1):
        path_s, store_key = arg.rsplit(":", 1)
    if store_key is None:
        # A bare path: already-normalized rows written by `menu_fetch.py fetch/join --json`.
        data = _load_json(Path(path_s))
        if isinstance(data, list) and data and isinstance(data[0], dict) and "raw_name" in data[0] and "store" in data[0]:
            return data
        raise ValueError(f"--json {arg!r}: bare paths must hold normalized rows from menu_fetch (else use path:store_key)")
    return menu_fetch.load_rows_json(path_s, store_key)


def collect_rows(json_args, fetch_keys):
    rows = []
    for arg in json_args or []:
        rows.extend(_rows_from_json_arg(arg))
    for key in fetch_keys or []:
        rows.extend(menu_fetch.fetch_store(key))
    return rows


def _matches_query(row, query, brand=None):
    q = (query or "").lower()
    strain = (row.get("strain") or "").lower()
    if q and q not in strain:
        return False
    if brand:
        b = brand.lower()
        if b not in (row.get("brand") or "").lower():
            return False
    return True


def _store_info(store_key):
    return menu_fetch.STORES.get(store_key, {})


def _parse_when(day_s, time_s):
    if day_s:
        d = date.fromisoformat(day_s)
    else:
        d = datetime.now(DENVER).date() if DENVER else date.today()
    if time_s:
        h, m = time_s.split(":")
        t = dtime(int(h), int(m))
    else:
        t = dtime(15, 0)  # default 3pm -- lands inside windowed tiers when forecasting
    return datetime.combine(d, t, tzinfo=DENVER)


# --------------------------------------------------------------------------
# CLI: price
# --------------------------------------------------------------------------

def cmd_price(args):
    rows = collect_rows(args.json, args.fetch)
    if not rows:
        print("no rows loaded -- pass --json or --fetch", file=sys.stderr)
        return 1

    when = _parse_when(args.day, getattr(args, "time", None))
    print(f"# {when.strftime('%A %Y-%m-%d %H:%M')} America/Denver "
          f"(default time 15:00 unless --time given)")

    matches = [r for r in rows if _matches_query(r, args.query, args.brand)]
    if not matches:
        print("no matching rows")
        return 0

    results = []
    for row in matches:
        store_key = row.get("store")
        store = _store_info(store_key)
        deals = load_deals(store_key)
        p = price_on(row, deals, when, store)
        results.append((row, p))

    results.sort(key=lambda rp: (rp[1]["per_gram"] is None, rp[1]["per_gram"] or 0))

    for row, p in results:
        store_name = row.get("store_name") or row.get("store")
        line = (
            f"{store_name} | {row.get('brand')} | {row.get('strain')} | "
            f"{row.get('form')} | {row.get('size_label')} | "
            f"Menu ${row.get('price'):.2f}"
        )
        if row.get("special_price") is not None:
            line += f" | Special ${row.get('special_price'):.2f}"
        if p["deal_price"] is not None and p["deal_names"]:
            line += f" | Deal ${p['deal_price']:.2f} ({', '.join(p['deal_names'])})"
        if p["otd"] is not None:
            line += f" | OTD ${p['otd']:.2f} ({p['otd_basis']})"
        else:
            line += (
                f" | as-listed ${(p['deal_price'] if p['deal_price'] is not None else (row.get('special_price') or row.get('price'))):.2f}"
                f" (tax unknown; if pre-tax @{int(ASSUMED_TAX_RATE*100)}%: ${p['otd_if_pretax']:.2f})"
            )
        if p["per_gram"] is not None:
            line += f" | ${p['per_gram']:.2f}/g"
        qty = row.get("qty")
        if qty is not None:
            line += f" | Qty {qty}"
        if p["stacking_note"]:
            line += f" | note: {p['stacking_note']}"
        print(line)
    return 0


# --------------------------------------------------------------------------
# CLI: forecast
# --------------------------------------------------------------------------

def cmd_forecast(args):
    rows = collect_rows(args.json, args.fetch)
    if not rows:
        print("no rows loaded -- pass --json or --fetch", file=sys.stderr)
        return 1

    matches = [r for r in rows if _matches_query(r, args.query, args.brand)]
    if not matches:
        print("no matching rows")
        return 0

    start_day = date.fromisoformat(args.day) if args.day else (
        datetime.now(DENVER).date() if DENVER else date.today()
    )
    time_s = getattr(args, "time", None)
    print(f"# forecast starting {start_day.isoformat()}, {args.days} day(s), "
          f"default time 15:00 unless --time given, America/Denver")

    # staleness note (posted files older than 7 days)
    stores_seen = {r.get("store") for r in matches}
    for store_key in stores_seen:
        posted = _load_json(DEALS_DIR / f"{store_key}.json")
        if posted and posted.get("captured"):
            captured = date.fromisoformat(posted["captured"])
            if (start_day - captured).days > 7:
                print(f"note: {store_key} posted deals stale (captured {captured.isoformat()})")

    for row in matches:
        store_key = row.get("store")
        store = _store_info(store_key)
        deals = load_deals(store_key)
        store_name = row.get("store_name") or store_key
        header = (
            f"{store_name} | {row.get('brand')} | {row.get('strain')} | "
            f"{row.get('form')} | {row.get('size_label')}"
        )
        print(header)

        day_results = []
        for i in range(args.days):
            d = start_day + timedelta(days=i)
            when = _parse_when(d.isoformat(), time_s)
            p = price_on(row, deals, when, store)
            day_results.append((d, when, p))

        best = min(
            day_results,
            key=lambda dwp: dwp[2]["per_gram"] if dwp[2]["per_gram"] is not None else float("inf"),
        )
        bd, bwhen, bp = best
        names = ", ".join(bp["deal_names"]) if bp["deal_names"] else "no deal"
        best_price = bp["otd"] if bp["otd"] is not None else bp["deal_price"] or row.get("price")
        print(f"  best day: {DAY_NAMES[_dow_sun0(bwhen)]} {bd.isoformat()} -- "
              f"${best_price:.2f} ({names})")

        for d, when, p in day_results:
            price_used = p["otd"] if p["otd"] is not None else p["deal_price"] or row.get("price")
            names = ", ".join(p["deal_names"]) if p["deal_names"] else "-"
            grid_line = f"    {DAY_NAMES[_dow_sun0(when)]} {d.isoformat()}: ${price_used:.2f} ({names})"
            notes = []
            if p["stacking_note"]:
                notes.append(p["stacking_note"])
            if p["otd_basis"] == "unknown":
                notes.append(f"tax basis unknown (if pre-tax @{int(ASSUMED_TAX_RATE*100)}%: ${p['otd_if_pretax']:.2f})")
            if row.get("qty") == 1:
                notes.append("qty 1")
            if notes:
                grid_line += " | " + "; ".join(notes)
            print(grid_line)
    return 0


# --------------------------------------------------------------------------
# CLI: deals fetch / list
# --------------------------------------------------------------------------

_IGADI_SPECIALS_QUERY = """
query($id:ID!){ specials(retailerId:$id){ id name type menuType
  scheduleConfiguration{ startStamp endStamp days setEndDate endDate recurringStartTime recurringEndTime }
  menuDisplayConfiguration{ name description } } }
"""


def _feed_from_igadi_specials(store_key):
    """IgadI (dutchie-wp) specials query -- spec section A. Own small extractor
    (same proxy/UA as menu_fetch's menu query, different GraphQL document)."""
    store = menu_fetch.STORES[store_key]
    ids = store["ids"]
    headers = dict(menu_fetch.UA, **{
        "Content-Type": "application/json", "Accept": "application/json", "Referer": ids["referer"],
    })
    body = json.dumps({"query": _IGADI_SPECIALS_QUERY, "variables": {"id": ids["retailer_id"]}}).encode()
    req = urllib.request.Request(ids["proxy"], data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    if "errors" in data:
        raise RuntimeError(f"IgadI specials GraphQL errors: {json.dumps(data['errors'])[:400]}")
    specials = (data.get("data") or {}).get("specials") or []

    deals = []
    for sp in specials:
        sched = sp.get("scheduleConfiguration") or {}
        days = sched.get("days")
        start = sched.get("startStamp")
        end = sched.get("endStamp") or sched.get("endDate")
        hours = None
        if sched.get("recurringStartTime") and sched.get("recurringEndTime"):
            hours = {"start": sched["recurringStartTime"][:5], "end": sched["recurringEndTime"][:5]}
        display = sp.get("menuDisplayConfiguration") or {}
        pct = None
        desc = display.get("description") or ""
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", desc) or re.search(r"(\d+(?:\.\d+)?)\s*%\s*off", sp.get("name") or "", re.I)
        if m:
            pct = float(m.group(1))
        nm = sp.get("name") or display.get("name") or ""
        kind = "bogo" if re.search(r"\bbogo\b|buy \d+", nm, re.I) else ("target_price" if re.search(r"\$\d", nm) else "percent")
        ig_brand = _brand_in_text(nm)
        deals.append({
            "id": f"igadi_{sp.get('id')}",
            "name": nm,
            "kind": kind,
            "value": pct,
            "brand": ig_brand,
            "scope": "brand" if ig_brand else "product",
            "category": None,
            "days": days,
            "start": start[:10] if isinstance(start, str) else None,
            "end": end[:10] if isinstance(end, str) else None,
            "hours": hours,
            "excludes": [],
            "includes": None,
            "menu_type": (sp.get("menuType") or "rec").lower(),
            "stack": "no",
            "notes": (
                "IgadI specials text: prices pre-tax, cannot be stacked with other discounts. "
                + ("percent parsed from menuDisplayConfiguration.description" if pct is not None else
                   "percent not found in description text -- see priceRec/specialPriceRec on the row instead")
            ),
        })
    return deals


def _feed_from_dispense_discounts(store_key):
    """Dispense per-product discounts, aggregated by (brand, value, days) --
    spec section C. Re-hits the products endpoint directly (own extractor)
    because the Row shape doesn't carry the raw discounts[] array."""
    store = menu_fetch.STORES[store_key]
    ids = store["ids"]
    api_key = menu_fetch._find_dispense_api_key(ids["page_url"])
    headers = dict(menu_fetch.UA, **{"api-key": api_key})
    products, skip, limit = [], 0, 100
    while True:
        url = (f"{ids['api_base']}/v1/venues/{ids['venue_id']}/product-categories/"
               f"{ids['category_id']}/products?limit={limit}&skip={skip}&orderPickUpType=IN_STORE")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
        batch = data.get("data") or []
        products.extend(batch)
        if len(batch) < limit:
            break
        skip += limit

    agg = {}
    for p in products:
        brand = (p.get("brand") or {}).get("name")
        for disc in p.get("discounts") or []:
            key = (brand, disc.get("value"), tuple(disc.get("days") or []))
            agg.setdefault(key, {
                "brand": brand, "value": disc.get("value"), "days": disc.get("days") or None,
                "disableStacking": disc.get("disableStacking"), "scheduleEnabled": disc.get("scheduleEnabled"),
            })
    deals = []
    for i, (key, info) in enumerate(agg.items()):
        deals.append({
            "id": f"{store_key}_disc_{i}",
            "name": f"{info['brand']} {(info['value'] * 100 if isinstance(info['value'], (int, float)) and info['value'] <= 1 else info['value']):g}%",
            "kind": "percent",
            "value": (info["value"] * 100 if isinstance(info["value"], (int, float)) and info["value"] <= 1 else info["value"]),
            "brand": info["brand"],
            "scope": "brand",
            "category": None,
            "days": info["days"] if info["scheduleEnabled"] else None,
            "start": None,
            "end": None,
            "hours": None,
            "excludes": [],
            "includes": None,
            "menu_type": "rec",
            "stack": "no" if info.get("disableStacking") else "unknown",
            "notes": "aggregated from per-product discounts[] (type PERCENT only)",
        })
    return deals


_KNOWN_DEAL_BRANDS = [
    "In House", "Erva", "Wyld", "Wana", "PAX", "Batch", "Bud & Mary's", "Fat Grams", "Mighty Melts",
    "Might Melts", "Dialed In", "Keef", "710 Labs", "Soiku Bano", "Sunshine", "Leiffa", "Green Dot",
    "Trichome Collective", "Good Trees", "Edun", "Malek's", "Seed & Smith", "Harmony", "Lazercat",
]


def _brand_in_text(text):
    """First known brand named in a special's title, else None (scope stays 'product', listed only)."""
    low = (text or "").lower()
    for b in _KNOWN_DEAL_BRANDS:
        if b.lower() in low:
            return "In House Melts" if b == "In House" else b
    return None


def _pct_from_text(*texts):
    for t in texts:
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", t or "")
        if m:
            return float(m.group(1))
    return None


def _brand_from_promo_name(name):
    """'Malek's Melts 15% Off' -> "Malek's Melts"; names without a leading brand before the percent -> None."""
    m = re.match(r"^(.*?)\s+\d+(?:\.\d+)?\s*%", name or "")
    b = (m.group(1).strip() if m else "")
    return b or None


def _feed_from_sweed_promotions(store_key):
    """Sweed GetPromotionsList -- spec section E."""
    store = menu_fetch.STORES[store_key]
    ids = store["ids"]
    headers = dict(menu_fetch.UA, **{"StoreId": ids["store_id"], "Content-Type": "application/json"})
    req = urllib.request.Request(f"{ids['api_base']}/_api/Products/GetPromotionsList",
                                  data=b"{}", headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        promos = json.loads(r.read())
    if isinstance(promos, dict):
        promos = promos.get("list") or promos.get("data") or []

    _DOW = {"sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6}

    def _days_from_schedule_text(txt):
        if not txt:
            return None
        days = []
        for token in re.split(r"[/,]", txt):
            token = token.strip()[:3].lower()
            if token in _DOW:
                days.append(_DOW[token])
        return days or None

    deals = []
    for pr in promos:
        sched = pr.get("scheduleDisplayText")
        sched_text = sched if isinstance(sched, str) else (sched or {}).get("days") if isinstance(sched, dict) else None
        deals.append({
            "id": f"{store_key}_promo_{pr.get('id')}",
            "name": pr.get("name") or pr.get("shortName"),
            "kind": "bogo" if pr.get("isBogo") else "percent",
            "value": pr.get("discountPercent") if pr.get("discountPercent") is not None else _pct_from_text(pr.get("shortName") or "", pr.get("name") or ""),
            "brand": _brand_from_promo_name(pr.get("name") or ""),
            "scope": "brand" if _brand_from_promo_name(pr.get("name") or "") else "product",
            "category": None,
            "days": _days_from_schedule_text(sched_text),
            "start": pr.get("startDate"),
            "end": pr.get("endDate"),
            "hours": None,
            "excludes": [],
            "includes": None,
            "menu_type": "rec",
            "stack": "unknown",
            "notes": (
                "promo prices fill only on the promo's scheduled days; value is null when Sweed "
                "does not expose discountPercent for this promo -- see variant.promoPrice/promos[] "
                "on the row instead."
            ),
        })
    return deals


FEED_FETCHERS = {}
for _k, _v in menu_fetch.STORES.items():
    if _v["platform"] == "dutchie-wp":
        FEED_FETCHERS[_k] = _feed_from_igadi_specials
    elif _v["platform"] == "dispense":
        FEED_FETCHERS[_k] = _feed_from_dispense_discounts
    elif _v["platform"] == "sweed":
        FEED_FETCHERS[_k] = _feed_from_sweed_promotions


def cmd_deals_fetch(args):
    store_key = args.store_key
    fn = FEED_FETCHERS.get(store_key)
    if not fn:
        print(f"no feed fetcher registered for {store_key} "
              f"(script-fetchable feed deals only: {sorted(FEED_FETCHERS)}; "
              f"dutchie-embed stores use `deals load --json <dump> {store_key}` instead)",
              file=sys.stderr)
        return 1
    deals = fn(store_key)
    out = {
        "store": store_key,
        "captured": date.today().isoformat(),
        "source": f"{store_key} feed (live fetch)",
        "deals": deals,
    }
    out_path = DEALS_DIR / f"{store_key}_feed.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {out_path} ({len(deals)} deals)")
    return 0


def _deal_from_dutchie_special(sp):
    """One data.filteredSpecials.specials[] entry -> one schema Deal (spec B)."""
    recurring = sp.get("recurring") or {}
    days = recurring.get("days")
    start_stamp = sp.get("startStamp")
    end_stamp = sp.get("endStamp") or recurring.get("endDate")

    def _ms_to_iso_date(ms):
        if not ms:
            return None
        try:
            return datetime.fromtimestamp(int(ms) / 1000, tz=DENVER).date().isoformat()
        except (ValueError, TypeError):
            return None

    hours = None
    if recurring.get("startTime") and recurring.get("endTime"):
        hours = {"start": recurring["startTime"], "end": recurring["endTime"]}

    sale = (sp.get("saleDiscounts") or [{}])[0]
    kind = "bogo" if sp.get("specialType") == "bogo" else (
        "target_price" if sale.get("discountType") == "targetPrice" else "percent"
    )
    value = sale.get("targetPrice") if kind == "target_price" else sale.get("discountAmount")

    brands = sale.get("brands") or []
    excludes = []
    excluded = sp.get("excludedProducts") or []
    notes = []
    if excluded:
        for name in excluded:
            if isinstance(name, str) and name:
                excludes.append(re.escape(name))
            else:
                notes.append("excludedProducts present without names")
                break

    return {
        "id": f"dutchie_{sp.get('id')}" if sp.get("id") else None,
        "name": sp.get("name"),
        "kind": kind,
        "value": value,
        "brand": brands[0] if len(brands) == 1 else None,
        "scope": "brand" if brands else "store",
        "category": None,
        "days": days,
        "start": _ms_to_iso_date(start_stamp),
        "end": _ms_to_iso_date(end_stamp),
        "hours": hours,
        "excludes": excludes,
        "includes": None,
        "menu_type": (sp.get("menuType") or "rec").lower(),
        "stack": "no" if sp.get("stackingMode") == "non-stacking" else "unknown",
        "notes": "; ".join(notes) if notes else (
            f"{len(brands)} brands in feed brands[]" if len(brands) > 1 else "none noted"
        ),
    }


def cmd_deals_load(args):
    with open(args.json_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    specials = raw.get("data", {}).get("filteredSpecials", {}).get("specials", raw) if isinstance(raw, dict) else raw
    if isinstance(specials, dict):
        specials = specials.get("specials", [])
    deals = [_deal_from_dutchie_special(sp) for sp in specials]
    out = {
        "store": args.store_key,
        "captured": date.today().isoformat(),
        "source": f"{args.store_key} FilteredSpecials dump ({args.json_path})",
        "deals": deals,
    }
    out_path = DEALS_DIR / f"{args.store_key}_feed.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {out_path} ({len(deals)} deals)")
    return 0


DUTCHIE_EMBED_SPECIALS_HASH = "886165ee0b4c9bb6e60de35700d6ff1fd93de4add22bc45ba0bfd363f6ea6e8a"


def cmd_deals_snippet(args):
    store_key = args.store_key
    store = _store_info(store_key)
    dispensary_id = (store.get("ids") or {}).get("dispensary_id") or (store.get("ids") or {}).get("id")
    variables = {
        "includeEnterpriseSpecials": False,
        "specialsFilter": {
            "dispensaryId": dispensary_id,
            "current": True,
            "platformType": "ONLINE_MENU",
            "preOrderType": None,
        },
    }
    extensions = {"persistedQuery": {"version": 1, "sha256Hash": DUTCHIE_EMBED_SPECIALS_HASH}}
    js = f"""
// paste into the dutchie.com/embedded-menu/{dispensary_id}/... tab console,
// or run via the browser pane's javascript_tool -- CSRF check needs the
// content-type header set explicitly.
const variables = {json.dumps(variables)};
const extensions = {json.dumps(extensions)};
const qs = new URLSearchParams({{
  operationName: "FilteredSpecials",
  variables: JSON.stringify(variables),
  extensions: JSON.stringify(extensions),
}});
const res = await fetch("https://dutchie.com/api-0/graphql?" + qs.toString(), {{
  headers: {{ "content-type": "application/json" }},
}});
const data = await res.json();
copy(JSON.stringify(data));  // then: menu_price.py deals load --json <pasted file> {store_key}
console.log(data);
"""
    print(js.strip())
    return 0


def cmd_deals_list(args):
    when = _parse_when(args.day, getattr(args, "time", None))
    deals = load_deals(args.store_key)
    print(f"# {args.store_key} deals as of {when.strftime('%A %Y-%m-%d %H:%M')} America/Denver "
          f"({len(deals)} total)")
    fake_row = {"raw_name": "", "brand": None, "strain": None, "form": None}
    for d in deals:
        applies_generically = d.get("scope") == "store" and not d.get("days")
        day_ok = d.get("days") is None or _dow_sun0(when) in d["days"]
        hours_ok = True
        if d.get("hours"):
            t = when.time()
            hours_ok = _parse_hhmm(d["hours"]["start"]) <= t <= _parse_hhmm(d["hours"]["end"])
        active = day_ok and hours_ok
        marker = "ACTIVE" if active else "-"
        print(f"  [{marker}] {d['id']} ({d.get('source')}) {d.get('name')} "
              f"kind={d.get('kind')} value={d.get('value')} brand={d.get('brand')} "
              f"days={d.get('days')} hours={d.get('hours')} notes={d.get('notes')}")
    return 0


# --------------------------------------------------------------------------
# argparse wiring
# --------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(prog="menu_price.py", description="deal-aware pricing over menu Rows")
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("price", help="price a strain query across loaded rows")
    pp.add_argument("query")
    pp.add_argument("--brand", default=None)
    pp.add_argument("--json", action="append", default=[], help="rows.json[:store_key], repeatable")
    pp.add_argument("--fetch", action="append", default=[], help="store_key to fetch live, repeatable")
    pp.add_argument("--day", default=None, help="YYYY-MM-DD (default: today, Denver)")
    pp.add_argument("--time", default=None, help="HH:MM local (default 15:00)")
    pp.set_defaults(func=cmd_price)

    pf = sub.add_parser("forecast", help="best day to buy over a window")
    pf.add_argument("query")
    pf.add_argument("--brand", default=None)
    pf.add_argument("--days", type=int, default=7)
    pf.add_argument("--json", action="append", default=[])
    pf.add_argument("--fetch", action="append", default=[])
    pf.add_argument("--day", default=None, help="start date YYYY-MM-DD (default: today, Denver)")
    pf.add_argument("--time", default=None, help="HH:MM local (default 15:00)")
    pf.set_defaults(func=cmd_forecast)

    pd = sub.add_parser("deals", help="deals subcommands")
    dsub = pd.add_subparsers(dest="deals_cmd", required=True)

    pdf = dsub.add_parser("fetch", help="fetch a script store's feed deals")
    pdf.add_argument("store_key")
    pdf.set_defaults(func=cmd_deals_fetch)

    pdl = dsub.add_parser("load", help="convert a dutchie-embed FilteredSpecials dump to the schema")
    pdl.add_argument("--json", dest="json_path", required=True)
    pdl.add_argument("store_key")
    pdl.set_defaults(func=cmd_deals_load)

    pds = dsub.add_parser("snippet", help="print the browser JS for a dutchie-embed store's specials")
    pds.add_argument("store_key")
    pds.set_defaults(func=cmd_deals_snippet)

    pdli = dsub.add_parser("list", help="list merged deals with applicability for a day")
    pdli.add_argument("store_key")
    pdli.add_argument("--day", default=None)
    pdli.add_argument("--time", default=None)
    pdli.set_defaults(func=cmd_deals_list)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args) or 0
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except (ValueError, KeyError, AttributeError, NotImplementedError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
