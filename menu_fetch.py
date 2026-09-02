"""
menu_fetch.py -- planned-trip menu pull across every store in the shopping
layer (per shopping/BUILD_SPEC_tmp.md). Pulls a store's in-stock concentrate
list, normalizes it into a flat Row list, joins product names against the
research/ catalog (and jar_manifest / classics stop-list), and prints a
paste-ready rundown table.

Design principles (binding, see BUILD_SPEC_tmp.md): retrieval is code; stock
and prices are ephemeral and never committed; when a fact is unknown the
registry says the literal string 'unknown', never a plausible fill.

Platforms
  dutchie-wp     IgadI (8 locations) -- script, existing proxy adapter.
  dutchie-embed  Lightshade FH, Magnolia Broomfield, Reefer Madness ND/SB --
                 Cloudflare-walled to scripts. `fetch_store` refuses and
                 tells you to run `snippet <store_key>` in the browser pane
                 (paste it into the console on the store's embedded-menu
                 page), save the returned JSON array under shopping/rows/,
                 then run `join --json <path>:<store_key>`.
  dispense       The Dab Broomfield -- script; the API key is extracted at
                 run time from the site's Next.js bundle (never committed).
  weedmaps       Maikoh Boulder/Denver -- script.
  sweed          Krystaleaves Denver -- script.

Row dict keys (the fixed interface other workers code against): store,
store_name, platform, brand, strain, form, size_g, size_label, price,
special_price, qty, potency, potency_unit, potency_flag, raw_name,
lineage_claim, match_tier, match_slug, fetched_at. An extra 'subcategory'
key rides along for --sub filtering; it is not part of the fixed set.

Usage
  python menu_fetch.py list
  python menu_fetch.py discover https://<cp-dutchie site>/shop/
  python menu_fetch.py fetch igadi_lafayette,thedab_broomfield [--sub ROSIN,HASH]
                       [--brands "In House,Erva"] [--json out.json]
  python menu_fetch.py fetch all-script [--json out.json]
  python menu_fetch.py join --json shopping/rows/dutchie_reefer_nd_raw.json:reefer_nd [--json out.json]
  python menu_fetch.py snippet lightshade_fh
  python menu_fetch.py fixtures

`shopping/rows/` (fetched rows, browser dumps) is gitignored. Never commit
the Dispense API key. No platform returns out-of-stock products; Dutchie
embed dumps can carry zero-quantity variants (product still listed) -- those
are kept and shown, never filtered.
"""

import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STRAINS_DIR = ROOT / "research" / "strains"
NODES_FILE = ROOT / "research" / "lineage_nodes.md"
CLASSICS_FILE = ROOT / ".claude" / "skills" / "research-strain" / "references" / "classics_stoplist.md"
FIXTURES_DIR = ROOT / "shopping" / "fixtures"

UA = {"User-Agent": "Mozilla/5.0"}


# ── Store registry ───────────────────────────────────────────────────────────
# The Dispense key is deliberately absent -- fetch_store('thedab_broomfield')
# pulls it from the live page bundle every run and never writes it anywhere.

_IGADI_LOCATIONS = {  # discovered Sept 2, 2026 via `discover https://igadiltd.com/shop/concentrates/`
    "golden":        "c60092e6-b16c-49c3-8b3b-5749174a2255",
    "granby":        "6c586832-ec38-46b0-bb5b-b52f1170ff2a",
    "idaho-springs": "44933038-77c5-41d6-8a63-d6eba138eb38",
    "lafayette":     "27195e36-fd0b-439b-a8b2-88490db01bd1",
    "louisville":    "2d9ed0f8-6ff5-4e9c-9ec4-ee6cde2fb334",
    "lyons":         "1a7bffee-86c0-48f9-ad07-bf4c7964c53a",
    "nederland":     "d46c121c-9bca-4612-9677-042a5e6482bf",
    "northglenn":    "7e907883-d4d3-414d-9f4e-d44ac38da047",
}

_IGADI_TAX = {"basis": "pre-tax", "rate": None, "source": "specials text (rate unknown)", "date": "2026-09-02"}
_IGADI_STACKING = {"rule": "none", "source": "specials text", "date": "2026-09-02"}

STORES = {}

for _loc, _rid in _IGADI_LOCATIONS.items():
    STORES[f"igadi_{_loc.replace('-', '_')}"] = {
        "name": f"IgadI {_loc.replace('-', ' ').title()}",
        "platform": "dutchie-wp",
        "ids": {
            "proxy": "https://igadiltd.com/wp-json/cannaplanners/v1/graphql/",
            "referer": "https://igadiltd.com/shop/concentrates/",
            "retailer_id": _rid,
        },
        "grammar": "igadi",
        "tax": _IGADI_TAX,
        "stacking": _IGADI_STACKING,
        "retrieval": "script",
    }

STORES["lightshade_fh"] = {
    "name": "Lightshade Federal Heights",
    "platform": "dutchie-embed",
    "ids": {"dispensary_id": "6112d9ef745e1500b0fd0238", "slug": "lightshade-federal-heights-rec-dispensary"},
    "grammar": "lightshade",
    "tax": {"basis": "pre-tax", "rate": 0.2585, "source": "Dutchie taxConfig / r/LightshadeDispensary", "date": "2026-09-02"},
    "stacking": {"rule": "best-single", "source": "Dutchie specialsSettings (favorCustomer)", "date": "2026-09-02"},
    "retrieval": "browser",
}
STORES["magnolia_broomfield"] = {
    "name": "Magnolia Road Broomfield",
    "platform": "dutchie-embed",
    "ids": {"dispensary_id": "62fffd46174ea900b316fc06", "slug": "unknown"},
    "grammar": "magnolia",
    "tax": {
        "basis": "pre-tax", "rate": 0.324,
        "source": "Dutchie taxConfig lists 8.15% sales + 24.25% cannabis (config says compound; "
                   "menu prices x 1.324 hit round dollars, so cumulative in practice -- flagged, both readings recorded",
        "date": "2026-09-02",
    },
    "stacking": {"rule": "best-single", "source": "Dutchie specialsSettings (favorCustomer)", "date": "2026-09-02"},
    "retrieval": "browser",
}
STORES["reefer_nd"] = {
    "name": "Reefer Madness (46th Ave, Denver)",
    "platform": "dutchie-embed",
    "ids": {"dispensary_id": "648a21c227a5790009edaf0f", "slug": "reefer-madness-46th-recreational"},
    "grammar": "reefer",
    "tax": {"basis": "unknown", "rate": None, "source": "Dutchie taxConfig taxes[] empty", "date": "2026-09-02"},
    "stacking": {
        "rule": "unknown",
        "source": "store-level discountStacking=true (compound) but each special says non-stacking/favorCustomer -- conflicting, both readings recorded",
        "date": "2026-09-02",
    },
    "retrieval": "browser",
}
STORES["reefer_sb"] = {
    "name": "Reefer Madness (South Broadway)",
    "platform": "dutchie-embed",
    "ids": {"dispensary_id": "648a21fa0dfe230009e7732b", "slug": "unknown"},
    "grammar": "reefer",
    "tax": {"basis": "unknown", "rate": None, "source": "Dutchie taxConfig taxes[] empty", "date": "2026-09-02"},
    "stacking": {
        "rule": "unknown",
        "source": "store-level discountStacking=true (compound) but each special says non-stacking/favorCustomer -- conflicting, both readings recorded",
        "date": "2026-09-02",
    },
    "retrieval": "browser",
}
STORES["thedab_broomfield"] = {
    "name": "The Dab Broomfield",
    "platform": "dispense",
    "ids": {
        "venue_id": "abcadb1b37145f0c",
        "category_id": "d665b2f5d0518c3d",
        "page_url": "https://thedab.com/menu/broomfield/categories/concentrates",
        "api_base": "https://api.dispenseapp.com",
    },
    "grammar": "dispense",
    "tax": {"basis": "otd", "rate": None, "source": "venue taxes=0 + site text 'Listed Prices Include Tax' (inferred)", "date": "2026-09-02"},
    "stacking": {"rule": "none", "source": "venue discountStackingMode NO_DOUBLE_STACKING", "date": "2026-09-02"},
    "retrieval": "script",
}
STORES["maikoh_boulder"] = {
    "name": "Maikoh Holistics Boulder",
    "platform": "weedmaps",
    "ids": {"slug": "maikoh-holistics"},
    "grammar": "weedmaps",
    "tax": {"basis": "unknown", "rate": None, "source": "meta.has_taxes_included=false, rate not published", "date": "2026-09-02"},
    "stacking": {"rule": "unknown", "source": "not published", "date": "2026-09-02"},
    "retrieval": "script",
}
STORES["maikoh_denver"] = {
    "name": "Maikoh Holistics Denver",
    "platform": "weedmaps",
    "ids": {"slug": "maikoh-holistics-denver"},
    "grammar": "weedmaps",
    "tax": {"basis": "unknown", "rate": None, "source": "meta.has_taxes_included=false, rate not published", "date": "2026-09-02"},
    "stacking": {"rule": "unknown", "source": "not published", "date": "2026-09-02"},
    "retrieval": "script",
}
STORES["krystaleaves_denver"] = {
    "name": "Krystal Leaves Denver",
    "platform": "sweed",
    "ids": {"store_id": "984", "category_ids": [10212], "api_base": "https://shop.krystaleaves.com"},
    "grammar": "sweed",
    "tax": {"basis": "unknown", "rate": None, "source": "not published", "date": "2026-09-02"},
    "stacking": {"rule": "unknown", "source": "not published", "date": "2026-09-02"},
    "retrieval": "script",
}


# ── Grammar: parse_name ──────────────────────────────────────────────────────

_TYPE_TAG_RE = re.compile(r"\s*\((?:[ISH](?:/[ISH])?)\)\s*$", re.I)
_STAR_NOTE_RE = re.compile(r"\*[^*]*\*")
_SIZE_TOKEN_RE = re.compile(r"^\d*\.?\d+\s*(g|oz)$", re.I)


def _strip_quotes(s):
    return s.strip().strip('"').strip("'").strip()


def _collapse_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def parse_igadi(raw_name):
    """'Erva | 90u Live Rosin | Cherry Plantains' -> (brand, form, strain, None).
    Names without pipes return ('', '', name, None). Trailing '(Indica)' /
    size tags are dropped."""
    parts = [p.strip() for p in raw_name.split("|")]
    if len(parts) >= 3:
        brand, form, strain = parts[0], " | ".join(parts[1:-1]), parts[-1]
    elif len(parts) == 2:
        brand, form, strain = parts[0], "", parts[1]
    else:
        brand, form, strain = "", "", parts[0]
    strain = re.sub(r"\s*\((?:indica|sativa|hybrid|\d+(?:\.\d+)?\s*(?:g|mg|oz))[^)]*\)\s*$", "", strain, flags=re.I)
    return brand, form, _collapse_ws(strain), None


def parse_lightshade(raw_name):
    """'710 Labs Persy Badder 1g - Do Lato #10' -> strain after the LAST ' - '.
    No clean brand segment in this grammar -- brand comes from the platform
    field, so this returns ''."""
    name = _collapse_ws(raw_name)
    if " - " in name:
        left, strain = name.rsplit(" - ", 1)
    else:
        left, strain = "", name
    return "", left, strain.strip(), None


def parse_magnolia(raw_name):
    """'Rainbow Chem (H) - Black Label Cold Cure Rosin - Soiku Bano'
    -> strain = first segment (type tag/quotes stripped), form = middle, brand = last."""
    name = _collapse_ws(raw_name)
    parts = [p.strip() for p in name.split(" - ") if p.strip()]
    if not parts:
        return "", "", "", None
    strain = _TYPE_TAG_RE.sub("", parts[0]).strip()
    strain = _strip_quotes(strain)
    if len(parts) >= 3:
        form, brand = parts[1], parts[-1]
    elif len(parts) == 2:
        form, brand = "", parts[1]
    else:
        form, brand = "", ""
    return brand, form, strain, None


def parse_reefer(raw_name):
    """'REC - Soiku Bano - Blockberry / Live Rosin' -> strain between the 2nd
    ' - ' and '/'. '*...*' notes stripped. Unprefixed names (rare) fall back
    to size-stripped whole name as strain (documented limitation)."""
    name = _collapse_ws(_STAR_NOTE_RE.sub("", raw_name))
    if name.upper().startswith("REC -"):
        rest = name.split(" - ", 1)[1] if " - " in name else ""
        if " - " in rest:
            brand, tail = rest.split(" - ", 1)
        else:
            brand, tail = "", rest
        if "/" in tail:
            strain, form = tail.split("/", 1)
        else:
            strain, form = tail, ""
        return brand.strip(), form.strip(), strain.strip(), None
    stripped = re.sub(r"\b\d*\.?\d+\s*(g|oz)\b", "", name, flags=re.I).strip()
    return "", "", _collapse_ws(stripped), None


_DISPENSE_TIER_WORDS = {"full spec", "premium", "90u", "full spectrum"}
_DISPENSE_TYPE_CODES = {"i", "s", "h", "ih", "sh", "i/h", "s/h"}


def parse_dispense(raw_name):
    """'Leiffa | Live Rosin | Cold Cure | 3g | - "Fossil Fuel" | IH' -> take
    text from the first '|'-segment starting with '-' onward, split on '|',
    drop tier words / sizes, drop a trailing type code, strain = what's left."""
    segs = [s.strip() for s in raw_name.split("|")]
    marker_idx = next((i for i, s in enumerate(segs) if s.startswith("-")), None)
    if marker_idx is None:
        brand = segs[0] if len(segs) > 1 else ""
        form = segs[1] if len(segs) > 2 else ""
        strain = _strip_quotes(segs[-1])
        return brand, form, strain, None
    brand = segs[0] if marker_idx > 0 else ""
    form = segs[1] if marker_idx > 1 and len(segs) > 1 else ""
    after = list(segs[marker_idx:])
    after[0] = after[0].lstrip("-").strip()
    cleaned = []
    for seg in after:
        seg = seg.strip()
        if not seg:
            continue
        low = seg.lower()
        if low in _DISPENSE_TIER_WORDS or _SIZE_TOKEN_RE.match(low):
            continue
        cleaned.append(seg)
    if cleaned and cleaned[-1].lower() in _DISPENSE_TYPE_CODES:
        cleaned.pop()
    strain = _strip_quotes(cleaned[-1]) if cleaned else ""
    return brand, form, strain, None


_WM_LINEAGE_RE = re.compile(r"[{(]([^{}()]*(?:\bx\b|\+|×|unknown|mystery)[^{}()]*)[})]\s*$", re.I)
_WM_TYPE_TAG_RE = re.compile(r"\s*\((?:I|S|H|I/H|S/H|H/I|H/S|Indica|Sativa|Hybrid)\)\s*$", re.I)
_WM_KNOWN_BRANDS = [
    "ERVA x In House Melts", "ERVA x In House", "In House Melts", "710 Labs", "Soiku Bano", "Green Dot Black Label", "Green Dot",
    "Greenery", "Sunshine", "Rivers", "Erva", "Maikoh", "Lazercat", "GDL", "Locol Love", "Malek's Melts",
]
_WM_FORM_WORDS = {
    "persy", "ultrapremo", "premo", "rosin", "badder", "wax", "hash", "live", "resin",
    "cold", "cure", "full", "spec", "spectrum", "solventless", "black", "label",
    "bucket", "reserve", "brick", "geode", "babber", "concentrate", "90u", "fs",
}


def _wm_strip_trailing_form_words(s):
    words = s.split()
    kept = []
    while words and re.sub(r"[^\w]", "", words[-1]).lower() in _WM_FORM_WORDS:
        words.pop()
    return " ".join(words).strip()


def parse_weedmaps(raw_name):
    """Three grammars in one store. Lineage claims in '{A x B}' braces are
    captured verbatim. 'Lazercat | Strain | Form | size' and bare
    'Strain | Form | size' (no brand) use pipes; brand-prefixed names like
    '710 Labs Garlic Cocktail #7 Persy Rosin Badder 1g' have no delimiter
    between strain and form -- resolved via a known-brand prefix list and a
    trailing form-word strip (best effort, not exact for every SKU)."""
    lineage = None
    m = _WM_LINEAGE_RE.search(raw_name)
    name = raw_name
    if m:
        lineage = m.group(1).strip()
        name = (raw_name[:m.start()] + raw_name[m.end():]).strip()
    name = _collapse_ws(_WM_TYPE_TAG_RE.sub("", name))

    if "|" in name:
        segs = [s.strip() for s in name.split("|")]
        if segs and segs[0].lower() == "lazercat":
            brand, strain = segs[0], (segs[1] if len(segs) > 1 else "")
            rest = [s for s in segs[2:] if not _SIZE_TOKEN_RE.match(s)]
            form = " ".join(rest)
        elif len(segs) > 2 and re.search(r"rosin|badder|hash|wax|gdl", segs[0], re.I):
            # "GDL Live Rosin Badder (1g) | GDL Originals | Belgium Blu": form-first, strain last non-size segment.
            brand = ""
            for b in _WM_KNOWN_BRANDS:
                if segs[0].lower().startswith(b.lower()):
                    brand = b
                    break
            rest = [x for x in segs[1:] if not _SIZE_TOKEN_RE.match(x)]
            strain = rest[-1] if rest else ""
            form = " ".join([segs[0]] + rest[:-1])
        else:
            brand, strain = "", segs[0]
            form = segs[1] if len(segs) > 1 else ""
        return brand, form, _strip_quotes(strain), lineage

    brand = ""
    rest = name
    for b in _WM_KNOWN_BRANDS:
        if rest.lower().startswith(b.lower()):
            brand, rest = b, rest[len(b):].strip()
            break
    if "-" in rest:
        left, strain = rest.rsplit("-", 1)
        form = left.strip()
    else:
        rest2 = re.sub(r"\b\d*\.?\d+\s*g\b", "", rest, flags=re.I).strip()
        words = rest2.split()
        form_words = []
        while words and re.sub(r"[^\w]", "", words[-1]).lower() in _WM_FORM_WORDS:
            form_words.insert(0, words.pop())
        strain = " ".join(words).strip()
        form = " ".join(form_words).strip()
    return brand, form, _strip_quotes(strain.strip()), lineage


_SWEED_FORM_WORDS = {
    "fs", "full", "spectrum", "90u", "cc", "cold", "cure", "live", "rosin", "badder",
    "babber", "geode", "concentrate", "bubble", "hash", "brick", "extractors",
    "choice", "premium",
}
_SWEED_TRAILING_BRAND_WORDS = {"in house", "royal jelly"}


def parse_sweed(raw_name):
    """'High Country Honey - 2g Rosin - Royal Jelly' -> strain with trailing
    form words stripped; a trailing ' - ' segment that reads as a brand is
    dropped from the strain and returned as brand."""
    segs = [s.strip() for s in raw_name.split(" - ") if s.strip()]
    brand = ""
    if len(segs) > 1 and segs[-1].lower() in _SWEED_TRAILING_BRAND_WORDS:
        brand = segs[-1]
        segs = segs[:-1]
    core = " - ".join(segs)
    tokens = core.split()
    while tokens:
        tok = tokens[-1]
        low = re.sub(r"[^\w./]", "", tok).lower()
        if tok == "-" or low in _SWEED_FORM_WORDS or _SIZE_TOKEN_RE.match(low):
            tokens.pop()
            continue
        break
    strain = " ".join(tokens).strip(" -")
    return brand, "", strain, None


_GRAMMARS = {
    "igadi": parse_igadi,
    "lightshade": parse_lightshade,
    "magnolia": parse_magnolia,
    "reefer": parse_reefer,
    "dispense": parse_dispense,
    "weedmaps": parse_weedmaps,
    "sweed": parse_sweed,
}


def parse_name(store_key, raw_name):
    """(brand, form, strain, lineage_claim) for a raw product name, dispatched
    on STORES[store_key]['grammar']."""
    store = STORES.get(store_key)
    if not store:
        raise ValueError(f"unknown store key '{store_key}'")
    fn = _GRAMMARS[store["grammar"]]
    return fn(raw_name)


# ── Size / potency helpers ───────────────────────────────────────────────────

_OZ_FRACTIONS = {0.125: 3.5, 0.25: 7.0, 0.5: 14.0, 1.0: 28.0}


def parse_size_g(label):
    """'1g'->1.0  '2g'->2.0  '1/8oz'->3.5  '.4g'->0.4  '3.5g'->3.5. None if unparseable."""
    if not label:
        return None
    s = str(label).strip().lower().replace(" ", "")
    m = re.match(r"^(\d+)/(\d+)oz$", s)
    if m:
        frac = int(m.group(1)) / int(m.group(2))
        return _OZ_FRACTIONS.get(frac, round(frac * 28.3495, 2))
    m = re.match(r"^(\d*\.\d+|\d+\.?\d*)g$", s)
    if m and m.group(1):
        try:
            return float(m.group(1))
        except ValueError:
            return None
    m = re.match(r"^(\d*\.\d+|\d+\.?\d*)oz$", s)
    if m and m.group(1):
        try:
            return round(float(m.group(1)) * 28.3495, 2)
        except ValueError:
            return None
    return None


def potency_flag(value, unit):
    """True when potency < 5 or > 95 or the unit isn't '%'/'PERCENTAGE', or
    when the value is missing entirely (unknown potency is flagged too)."""
    if value is None:
        return True
    if (unit or "").upper() not in ("%", "PERCENTAGE"):
        return True
    return value < 5 or value > 95


def _now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _mk_row(store_key, brand, strain, form, size_label, price, special_price, qty,
            potency, potency_unit, raw_name, lineage_claim, subcategory=""):
    store = STORES[store_key]
    return {
        "store": store_key,
        "store_name": store["name"],
        "platform": store["platform"],
        "brand": brand or "",
        "strain": strain or "",
        "form": form or "",
        "size_g": parse_size_g(size_label),
        "size_label": size_label or "",
        "price": price,
        "special_price": special_price,
        "qty": qty,
        "potency": potency,
        "potency_unit": potency_unit or "",
        "potency_flag": potency_flag(potency, potency_unit),
        "raw_name": raw_name,
        "lineage_claim": lineage_claim,
        "match_tier": "",
        "match_slug": "",
        "fetched_at": _now_iso(),
        "subcategory": subcategory or "",
    }


# ── Adapter: dutchie-wp (IgadI) ──────────────────────────────────────────────

_MENU_QUERY = """
query MenuQuery($retailerId: ID!, $offset: Int!, $limit: Int!, $filter: MenuFilter) {
  menu(retailerId: $retailerId, pagination: {offset: $offset, limit: $limit}, filter: $filter) {
    productsCount
    products {
      id
      name
      slug
      category
      subcategory
      strainType
      brand { name }
      potencyThc { formatted }
      terpenes { name value unitSymbol }
      variants { option priceRec specialPriceRec quantity }
    }
  }
}
"""


def _gql(proxy, referer, variables):
    headers = dict(UA, **{"Content-Type": "application/json", "Accept": "application/json", "Referer": referer})
    body = json.dumps({"query": _MENU_QUERY, "variables": variables}).encode()
    req = urllib.request.Request(proxy, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    if "errors" in data:
        raise RuntimeError(f"GraphQL errors: {json.dumps(data['errors'])[:400]}")
    return data["data"]["menu"]


def _fetch_igadi(store_key):
    store = STORES[store_key]
    ids = store["ids"]
    products, offset, limit = [], 0, 100
    while True:
        menu = _gql(ids["proxy"], ids["referer"],
                    {"retailerId": ids["retailer_id"], "offset": offset, "limit": limit,
                     "filter": {"category": "CONCENTRATES"}})
        products.extend(menu["products"])
        offset += limit
        if offset >= (menu.get("productsCount") or 0) or not menu["products"]:
            break
    rows = []
    for p in products:
        brand_seg, form, strain, lineage = parse_igadi(p["name"])
        brand = (p.get("brand") or {}).get("name") or brand_seg
        thc_raw = (p.get("potencyThc") or {}).get("formatted") or ""
        potency, unit = None, ""
        m = re.match(r"^([\d.]+)\s*(%?)", thc_raw)
        if m and m.group(1):
            try:
                potency = float(m.group(1))
                unit = "%"
            except ValueError:
                pass
        for v in p.get("variants") or []:
            rows.append(_mk_row(
                store_key, brand, strain, form, v.get("option") or "",
                v.get("priceRec"), v.get("specialPriceRec"), v.get("quantity"),
                potency, unit, p["name"], lineage, subcategory=p.get("subcategory") or "",
            ))
    return rows


def discover(site_url):
    html = urllib.request.urlopen(urllib.request.Request(site_url, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    pairs = set(re.findall(r'data-retailer-id="([^"]+)"[^>]*data-retailer-name="([^"]+)"', html))
    plugin = re.search(r"/plugins/cp-dutchie/", html)
    return sorted(pairs, key=lambda p: p[1]), bool(plugin)


# ── Adapter: dispense (The Dab Broomfield) ───────────────────────────────────

def _find_dispense_api_key(page_url):
    html = urllib.request.urlopen(urllib.request.Request(page_url, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    srcs = re.findall(r'<script[^>]+src="([^"]+)"', html)
    srcs = [s if s.startswith("http") else ("https:" + s if s.startswith("//") else s) for s in srcs]
    srcs = [s for s in srcs if "_next" in s or s.endswith(".js")]
    key_re = re.compile(r'apiKey["\']?\s*:\s*"([0-9a-fA-F-]{36})"')
    for src in srcs[:60]:
        try:
            js = urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=20).read().decode("utf-8", "ignore")
        except Exception:
            continue
        m = key_re.search(js)
        if m and "apiUrl" in js and "dispenseapp.com" in js:
            return m.group(1)
    raise RuntimeError(
        "could not locate the Dispense API key in thedab.com's script bundle -- "
        "the site's build may have changed. Inspect the Next.js chunk sources by "
        "hand (search for apiKey next to apiUrl:\"https://api.dispenseapp.com\")."
    )


def _fetch_dispense(store_key):
    store = STORES[store_key]
    ids = store["ids"]
    api_key = _find_dispense_api_key(ids["page_url"])
    headers = dict(UA, **{"api-key": api_key})
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
    rows = []
    for p in products:
        brand_seg, form, strain, lineage = parse_dispense(p.get("name") or "")
        brand = (p.get("brand") or {}).get("name") or brand_seg
        labs = p.get("labs") or {}
        potency = labs.get("thc")
        unit = labs.get("thcContentUnit") or ""
        price = p.get("price")
        special = p.get("priceWithDiscounts")
        if special == price:
            special = None
        rows.append(_mk_row(
            store_key, brand, strain, form, p.get("weightFormatted") or "",
            price, special, p.get("quantity"),
            potency, unit, p.get("name") or "", lineage, subcategory=p.get("subType") or "",
        ))
    return rows


# ── Adapter: weedmaps (Maikoh) ───────────────────────────────────────────────

_WM_EXCLUDE_RE = re.compile(
    r"(?i)gummies?|chocolate|cartridge|\bpen\b|\broll\b|joint|tincture|drops?\b|pills?\b|"
    r"chew|dissolv|\bsystem\b|\baio\b"
)


def _fetch_weedmaps(store_key):
    store = STORES[store_key]
    slug = store["ids"]["slug"]
    items, page = [], 1
    while True:
        url = (f"https://api-g.weedmaps.com/discovery/v1/listings/dispensaries/{slug}/menu_items"
               f"?filter%5Bcategory_slug%5D=concentrates&page={page}&page_size=100")
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
        # NOTE: filter[category_slug]=concentrates is accepted but not honored
        # server-side (verified live Sept 2, 2026 -- a flower item came back
        # first) -- the meta block also sits at the top level, not under
        # 'data' as the persisted query's own field naming would suggest.
        # Category is filtered client-side below instead.
        batch = (data.get("data") or {}).get("menu_items") or []
        items.extend(batch)
        total = (data.get("meta") or {}).get("total_menu_items") or 0
        if not batch or page * 100 >= total:
            break
        page += 1
    rows = []
    for it in items:
        if ((it.get("category") or {}).get("name") or "").lower() != "concentrate":
            continue
        name = it.get("name") or ""
        if _WM_EXCLUDE_RE.search(name):
            continue
        brand, form, strain, lineage = parse_weedmaps(name)
        agg = (it.get("metrics") or {}).get("aggregates") or {}
        potency = agg.get("thc")
        unit = agg.get("thc_unit") or ""
        price_obj = it.get("price") or {}
        size_label = price_obj.get("label") or ""
        if price_obj.get("on_sale"):
            price = price_obj.get("original_price")
            special = price_obj.get("price")
        else:
            price = price_obj.get("price")
            special = None
        rows.append(_mk_row(
            store_key, brand, strain, form, size_label, price, special, None,
            potency, unit, name, lineage, subcategory=(it.get("edge_category") or {}).get("name") or "",
        ))
    return rows


# ── Adapter: sweed (Krystaleaves) ────────────────────────────────────────────

def _fetch_sweed(store_key):
    store = STORES[store_key]
    ids = store["ids"]
    headers = dict(UA, **{"StoreId": ids["store_id"], "Content-Type": "application/json"})
    products, page = [], 1
    while True:
        body = json.dumps({
            "filters": {"category": ids["category_ids"]},
            "page": page, "pageSize": 100, "sortingMethodId": 3,
            "searchTerm": "", "platformOs": "web", "sourcePage": 0,
        }).encode()
        req = urllib.request.Request(f"{ids['api_base']}/_api/Products/GetProductList",
                                      data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
        batch = data.get("list") or []
        products.extend(batch)
        total = data.get("total") or 0
        if not batch or page * 100 >= total:
            break
        page += 1
    rows = []
    for p in products:
        name = p.get("name") or ""
        brand_seg, form, strain, lineage = parse_sweed(name)
        brand = (p.get("brand") or {}).get("name") or brand_seg
        for v in p.get("variants") or []:
            labs = (v.get("labTests") or {}).get("thc") or {}
            vals = labs.get("value") or []
            potency = vals[0] if vals else None
            unit = labs.get("unitAbbr") or ""
            price = v.get("price")
            special = v.get("promoPrice")
            qty = v.get("availableQty")
            qty = int(qty) if qty is not None else None
            rows.append(_mk_row(
                store_key, brand, strain, form, v.get("name") or "", price, special, qty,
                potency, unit, name, lineage,
            ))
    return rows


# ── Adapter: dutchie-embed (browser-fetched JSON dumps) ─────────────────────

def snippet(store_key):
    """Browser JS (paste into the console on the store's embedded-menu page)
    that pulls every concentrate-adjacent product for `store_key` across all
    subcategories and returns a JSON array shaped like shopping/rows/dutchie_*_raw.json
    (fields: Name, brandName, subcategory, Options, recPrices, recSpecialPrices,
    children[{option,quantityAvailable}], THCContent{unit,range}).

    Output is not persisted by this script -- save the printed array (browser
    devtools "copy object", or JSON.stringify+download) to shopping/rows/, then
    run `python menu_fetch.py join --json <path>:<store_key>`.
    """
    store = STORES.get(store_key)
    if not store or store["platform"] != "dutchie-embed":
        raise ValueError(f"'{store_key}' is not a dutchie-embed store (see `list`)")
    dispensary_id = store["ids"]["dispensary_id"]
    return f"""// menu_fetch.py snippet for {store_key} ({store["name"]})
// Run on https://dutchie.com/embedded-menu/{dispensary_id}/products/concentrates
// then save the resulting JSON array to shopping/rows/dutchie_{store_key}_raw.json
(async () => {{
  const dispensaryId = "{dispensary_id}";
  const hash = "3307e40a53bfb0b59896e267e3a46c2e99da18d3b376567d23267b6483bc3a76";
  const out = [];
  let page = 0;
  while (true) {{
    const variables = {{
      includeEnterpriseSpecials: false,
      productsFilter: {{
        productIds: [], dispensaryId, pricingType: "rec", strainTypes: [], subcategories: [],
        Status: "Active", types: ["Concentrate"], useCache: false, isDefaultSort: true,
        sortDirection: 1, bypassOnlineThresholds: false, ignoreQuantityThresholds: false,
        isKioskMenu: false, removeProductsBelowOptionThresholds: true,
        platformType: "ONLINE_MENU", preOrderType: null,
      }},
      page, perPage: 100,
    }};
    const extensions = {{persistedQuery: {{version: 1, sha256Hash: hash}}}};
    const url = "https://dutchie.com/api-0/graphql?operationName=FilteredProducts"
      + "&variables=" + encodeURIComponent(JSON.stringify(variables))
      + "&extensions=" + encodeURIComponent(JSON.stringify(extensions));
    const resp = await fetch(url, {{headers: {{"content-type": "application/json"}}}});
    const json = await resp.json();
    const products = json.data.filteredProducts.products;
    const total = json.data.filteredProducts.queryInfo.totalCount;
    for (const p of products) {{
      out.push({{
        Name: p.Name, brandName: p.brandName, subcategory: p.subcategory,
        Options: p.Options, recPrices: p.recPrices, recSpecialPrices: p.recSpecialPrices,
        children: (p.POSMetaData && p.POSMetaData.children) || [],
        THCContent: p.THCContent,
      }});
    }}
    if (products.length === 0 || page * 100 >= total) break;
    page += 1;
  }}
  console.log(JSON.stringify(out));
  return out;
}})();
"""


def load_rows_json(path, store_key):
    """Normalize a saved dutchie-embed dump (shape: see `snippet`) into Rows."""
    if store_key not in STORES:
        raise ValueError(f"unknown store key '{store_key}'")
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = []
    for p in data:
        name = p.get("Name") or ""
        brand_seg, form, strain, lineage = parse_name(store_key, name)
        brand = p.get("brandName") or brand_seg
        thc = p.get("THCContent") or {}
        potency_range = thc.get("range") or []
        potency = potency_range[0] if potency_range else None
        unit = thc.get("unit") or ""
        options = p.get("Options") or []
        rec_prices = p.get("recPrices") or []
        rec_special = p.get("recSpecialPrices") or []
        children = {c.get("option"): c.get("quantityAvailable") for c in (p.get("children") or [])}
        for i, opt in enumerate(options):
            price = rec_prices[i] if i < len(rec_prices) else None
            special = rec_special[i] if i < len(rec_special) else None
            qty = children.get(opt)
            rows.append(_mk_row(
                store_key, brand, strain, form, opt, price, special, qty,
                potency, unit, name, lineage, subcategory=p.get("subcategory") or "",
            ))
    return rows


# ── fetch_store dispatch ─────────────────────────────────────────────────────

def fetch_store(key):
    """list[Row] for a script-retrieval store. Raises for a browser-only store
    (dutchie-embed) with a message pointing at `snippet` + `join`."""
    store = STORES.get(key)
    if not store:
        raise ValueError(f"unknown store key '{key}' (see `list`)")
    if store["retrieval"] != "script":
        raise RuntimeError(
            f"'{key}' ({store['name']}) is browser-only (Cloudflare-walled to scripts). "
            f"Run `python menu_fetch.py snippet {key}` in the browser pane on its "
            f"embedded-menu page, save the resulting JSON to shopping/rows/, then "
            f"`python menu_fetch.py join --json <path>:{key}`."
        )
    platform = store["platform"]
    if platform == "dutchie-wp":
        return _fetch_igadi(key)
    if platform == "dispense":
        return _fetch_dispense(key)
    if platform == "weedmaps":
        return _fetch_weedmaps(key)
    if platform == "sweed":
        return _fetch_sweed(key)
    raise RuntimeError(f"no script fetcher for platform '{platform}'")


# ── Catalog join ──────────────────────────────────────────────────────────────

def norm_key(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9#+× ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _strip_hash_suffix(k):
    return re.sub(r"\s*#\d+$", "", k)


def _load_research_catalog():
    entries = {}
    for p in STRAINS_DIR.glob("*.md"):
        for ln in p.read_text(encoding="utf-8").splitlines():
            if ln.startswith("# "):
                entries[norm_key(ln[2:])] = p.stem
                break
    nodes = set()
    if NODES_FILE.exists():
        for m in re.finditer(r"^- \*\*([^*]+?)\*\*", NODES_FILE.read_text(encoding="utf-8"), flags=re.M):
            name = re.sub(r"\s*\(.*?\)\s*", " ", m.group(1)).strip()
            nodes.add(norm_key(name))
    return entries, nodes


def _load_classics():
    if not CLASSICS_FILE.exists():
        return set()
    text = CLASSICS_FILE.read_text(encoding="utf-8")
    paragraphs = text.split("\n\n")
    block = next((p for p in paragraphs if "·" in p), "")
    block = block.replace("\n", " ")
    names = set()
    for raw_entry in block.split("·"):
        raw_entry = raw_entry.strip()
        if not raw_entry:
            continue
        if "/" in raw_entry:
            alts = [a.strip() for a in raw_entry.split("/")]
            base_words = None
            for a in alts:
                if re.match(r"^\d+$", a) and base_words:
                    prefix = " ".join(base_words[:-1])
                    names.add(norm_key(f"{prefix} {a}".strip()))
                else:
                    names.add(norm_key(a))
                    base_words = a.split()
        else:
            names.add(norm_key(raw_entry))
    return names


def _load_jar_names():
    import jar_manifest
    _, statuses = jar_manifest.load_all_jars()
    return {norm_key(s.name): s.slug for s in statuses}


def build_catalog():
    """{'jar': {norm_key: slug}, 'entries': {norm_key: slug}, 'nodes': {norm_key},
    'classics': {norm_key}} -- built once and passed into join_row."""
    entries, nodes = _load_research_catalog()
    return {
        "jar": _load_jar_names(),
        "entries": entries,
        "nodes": nodes,
        "classics": _load_classics(),
    }


def join_row(row, catalog):
    """(tier, slug) with tier in 'jar'|'entry'|'node'|'classic'|''. Matches on
    the strain name only, jar/entry also tried with a trailing '#N' stripped."""
    k = norm_key(row.get("strain") or "")
    if not k:
        return "", ""
    k2 = _strip_hash_suffix(k)
    for key in (k, k2):
        if key in catalog["jar"]:
            return "jar", catalog["jar"][key]
    for key in (k, k2):
        if key in catalog["entries"]:
            return "entry", catalog["entries"][key]
    if k in catalog["nodes"] or k2 in catalog["nodes"]:
        return "node", ""
    if k in catalog["classics"] or k2 in catalog["classics"]:
        return "classic", ""
    return "", ""


# ── Output ────────────────────────────────────────────────────────────────────

def money(x):
    return "" if x is None else f"${x:.2f}"


_MATCH_LABEL = {"jar": "jar", "entry": "entry", "node": "lineage node", "classic": "classic", "": "unknown"}


def _match_label(row):
    tier = row.get("match_tier", "")
    slug = row.get("match_slug", "")
    label = _MATCH_LABEL.get(tier, "unknown")
    return f"{label}: {slug}" if slug else label


def _potency_label(row):
    if row.get("potency") is None:
        s = "?"
    else:
        s = f"{row['potency']:g}{row.get('potency_unit') or ''}"
        if row.get("potency_flag"):
            s += "?"
    return s


def rundown_table(rows):
    head = "| Store | Brand | Strain | Form | Size | Price | Special | Qty | Potency | Match |\n|---|---|---|---|---|---|---|---|---|---|"
    lines = [head]
    for r in rows:
        lines.append(
            f"| {r['store_name']} | {r['brand']} | {r['strain']} | {r['form']} | {r['size_label']} | "
            f"{money(r['price'])} | {money(r['special_price'])} | {r['qty'] if r['qty'] is not None else ''} | "
            f"{_potency_label(r)} | {_match_label(r)} |"
        )
    return "\n".join(lines)


def _apply_filters(rows, subs, brands):
    if subs:
        # Store subcategory vocab varies wildly (Dutchie: 'rosin'; Dispense
        # subType: 'Live Rosin Gram (3)'; Weedmaps edge_category: 'Rosin') --
        # substring match on the uppercased field, not exact equality.
        rows = [r for r in rows if any(s in (r.get("subcategory") or "").upper() for s in subs)]
    if brands:
        rows = [r for r in rows if any(b in (r["brand"] or "").lower() for b in brands)]
    return rows


def _join_and_sort(rows):
    catalog = build_catalog()
    for r in rows:
        r["match_tier"], r["match_slug"] = join_row(r, catalog)
    rows.sort(key=lambda r: (r["match_tier"] != "jar", r["match_tier"] != "entry",
                              (r["brand"] or "").lower(), (r["strain"] or "").lower(), r["store"]))
    return rows


def _print_result(rows, json_out):
    print(rundown_table(rows))
    unmatched = sorted({r["strain"] for r in rows if not r["match_tier"]})
    if unmatched:
        print(f"\nNot in catalog ({len(unmatched)}): " + ", ".join(unmatched))
    tiers = {}
    for r in rows:
        tiers.setdefault(r["store"], {}).setdefault(r["match_tier"] or "none", 0)
        tiers[r["store"]][r["match_tier"] or "none"] += 1
    if json_out:
        Path(json_out).write_text(json.dumps(rows, indent=1), encoding="utf-8")
        print(f"\nwrote {json_out}")
    return tiers


# ── Fixtures ──────────────────────────────────────────────────────────────────

_FIXTURE_STORES = {
    "lightshade_fh": "names_lightshade_fh.txt",
    "magnolia_broomfield": "names_magnolia_broomfield.txt",
    "reefer_nd": "names_reefer_nd.txt",
    "thedab_broomfield": "names_thedab_broomfield.txt",
    "maikoh_boulder": "names_maikoh_boulder.txt",
    "krystaleaves_denver": "names_krystaleaves_denver.txt",
    "igadi": "names_igadi.txt",  # shared grammar across all igadi_* keys
}


def run_fixtures():
    failures = []
    total = 0
    for store_key, fname in _FIXTURE_STORES.items():
        path = FIXTURES_DIR / fname
        if not path.exists():
            failures.append(f"missing fixture file: {path}")
            continue
        grammar_store = "igadi_golden" if store_key == "igadi" else store_key
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                failures.append(f"{fname}:{lineno}: expected 3 tab-separated fields, got {len(parts)}: {line!r}")
                continue
            raw, expect_strain, expect_brand = parts
            total += 1
            brand, form, strain, lineage = parse_name(grammar_store, raw)
            if strain != expect_strain:
                failures.append(f"{fname}:{lineno}: strain mismatch for {raw!r}: got {strain!r}, want {expect_strain!r}")
            if expect_brand and brand != expect_brand:
                failures.append(f"{fname}:{lineno}: brand mismatch for {raw!r}: got {brand!r}, want {expect_brand!r}")
    if failures:
        print(f"FIXTURE FAILURES ({len(failures)} of {total} cases):")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    print(f"fixtures OK: {total} cases across {len(_FIXTURE_STORES)} grammars")


# ── CLI ───────────────────────────────────────────────────────────────────────

def _parse_filter_opts(subs_arg, brands_arg):
    subs = {s.strip().upper() for s in subs_arg.split(",")} if subs_arg else None
    brands = [b.strip().lower() for b in brands_arg.split(",")] if brands_arg else None
    return subs, brands


def main(argv):
    parser = argparse.ArgumentParser(prog="menu_fetch.py", add_help=True)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list")

    p_discover = sub.add_parser("discover")
    p_discover.add_argument("url")

    p_fetch = sub.add_parser("fetch")
    p_fetch.add_argument("keys")
    p_fetch.add_argument("--sub")
    p_fetch.add_argument("--brands")
    p_fetch.add_argument("--json")

    p_join = sub.add_parser("join")
    p_join.add_argument("--json", dest="json_in", action="append", required=True)
    p_join.add_argument("--sub")
    p_join.add_argument("--brands")
    p_join.add_argument("--out")

    p_snippet = sub.add_parser("snippet")
    p_snippet.add_argument("store_key")

    sub.add_parser("fixtures")

    try:
        args = parser.parse_args(argv)
    except SystemExit:
        raise

    if args.cmd is None:
        print(__doc__)
        return

    if args.cmd == "list":
        for key, store in STORES.items():
            print(f"{key}  ({store['name']}, {store['platform']}, {store['retrieval']})")
        return

    if args.cmd == "discover":
        try:
            pairs, has_proxy = discover(args.url)
        except Exception as e:
            sys.exit(f"discover failed: {e}")
        print(f"cp-dutchie plugin present (proxy at <site>/wp-json/cannaplanners/v1/graphql/): {has_proxy}")
        for rid, name in pairs:
            print(f"  {name}: {rid}")
        return

    if args.cmd == "fetch":
        if args.keys == "all-script":
            keys = [k for k, s in STORES.items() if s["retrieval"] == "script"]
        else:
            keys = [k.strip() for k in args.keys.split(",") if k.strip()]
            for k in keys:
                if k not in STORES:
                    sys.exit(f"unknown store key '{k}' (see `list`)")
        subs, brands = _parse_filter_opts(args.sub, args.brands)
        rows = []
        for k in keys:
            try:
                rows.extend(fetch_store(k))
            except Exception as e:
                print(f"! {k} failed: {e}", file=sys.stderr)
        rows = _apply_filters(rows, subs, brands)
        rows = _join_and_sort(rows)
        tiers = _print_result(rows, args.json)
        for store, counts in tiers.items():
            print(f"  {store} match tiers: {counts}", file=sys.stderr)
        return

    if args.cmd == "join":
        subs, brands = _parse_filter_opts(args.sub, args.brands)
        rows = []
        for spec in args.json_in:
            if ":" not in spec:
                sys.exit(f"join --json expects <path>:<store_key>, got '{spec}'")
            path, store_key = spec.rsplit(":", 1)
            if store_key not in STORES:
                sys.exit(f"unknown store key '{store_key}' in '{spec}' (see `list`)")
            if not Path(path).exists():
                sys.exit(f"file not found: {path}")
            rows.extend(load_rows_json(path, store_key))
        rows = _apply_filters(rows, subs, brands)
        rows = _join_and_sort(rows)
        tiers = _print_result(rows, args.out)
        for store, counts in tiers.items():
            print(f"  {store} match tiers: {counts}", file=sys.stderr)
        return

    if args.cmd == "snippet":
        if args.store_key not in STORES:
            sys.exit(f"unknown store key '{args.store_key}' (see `list`)")
        try:
            print(snippet(args.store_key))
        except Exception as e:
            sys.exit(str(e))
        return

    if args.cmd == "fixtures":
        run_fixtures()
        return

    sys.exit(f"unknown command '{args.cmd}'")


if __name__ == "__main__":
    main(sys.argv[1:])
