"""
menu_fetch.py — planned-trip menu pull (Build 3 of research/design/SHOPPING_PLAN.md).

Pulls a dispensary's in-stock concentrate list through a Dutchie Plus GraphQL
proxy, normalizes it, joins product names against the research/ catalog, and
prints a paste-ready rundown table. Retrieval is code; nothing here is
persisted to the repo — stock and prices are ephemeral by design.

Adapter: "dutchie-wp" — dispensary sites running the cp-dutchie WordPress
plugin expose Dutchie's GraphQL at <site>/wp-json/cannaplanners/v1/graphql/,
which is not behind the Cloudflare wall that blocks scripts at dutchie.com.
Retailer ids per location sit in the site's shop page as data-retailer-id
attributes (`discover` reads them).

Usage
  python menu_fetch.py list
  python menu_fetch.py discover https://<cp-dutchie site>/shop/
  python menu_fetch.py fetch igadi:lafayette[,igadi:golden,...] [--sub ROSIN,HASH]
                       [--brands "In House,Erva"] [--all] [--json out.json]

`fetch` defaults to the CONCENTRATES category and every subcategory; --sub
narrows (Dutchie values seen: ROSIN, HASH, WAX, LIVE_RESIN, SHATTER, ...).
--brands is a case-insensitive substring match on the Dutchie brand name or
the name's first "|" segment. Location key `igadi:all` expands every location.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STRAINS = ROOT / "research" / "strains"
NODES = ROOT / "research" / "lineage_nodes.md"

UA = {"User-Agent": "Mozilla/5.0"}

# ── Sources ───────────────────────────────────────────────────────────────────
# Public platform facts only (proxy URL, location → retailer id). Which
# locations a trip covers is a conversation-level choice, never recorded here.

SOURCES = {
    "igadi": {
        "name": "IgadI",
        "adapter": "dutchie-wp",
        "proxy": "https://igadiltd.com/wp-json/cannaplanners/v1/graphql/",
        "referer": "https://igadiltd.com/shop/concentrates/",
        "locations": {  # discovered Sept 2, 2026 via `discover https://igadiltd.com/shop/concentrates/`
            "golden":        "c60092e6-b16c-49c3-8b3b-5749174a2255",
            "granby":        "6c586832-ec38-46b0-bb5b-b52f1170ff2a",
            "idaho-springs": "44933038-77c5-41d6-8a63-d6eba138eb38",
            "lafayette":     "27195e36-fd0b-439b-a8b2-88490db01bd1",
            "louisville":    "2d9ed0f8-6ff5-4e9c-9ec4-ee6cde2fb334",
            "lyons":         "1a7bffee-86c0-48f9-ad07-bf4c7964c53a",
            "nederland":     "d46c121c-9bca-4612-9677-042a5e6482bf",
            "northglenn":    "7e907883-d4d3-414d-9f4e-d44ac38da047",
        },
    },
}

# Dutchie Plus menu query — the field set the cp-dutchie plugin itself sends,
# trimmed to what the rundown needs.
MENU_QUERY = """
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


# ── Adapter: dutchie-wp ───────────────────────────────────────────────────────

def gql(proxy, referer, variables):
    headers = dict(UA, **{"Content-Type": "application/json", "Accept": "application/json", "Referer": referer})
    body = json.dumps({"query": MENU_QUERY, "variables": variables}).encode()
    req = urllib.request.Request(proxy, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    if "errors" in data:
        raise RuntimeError(f"GraphQL errors: {json.dumps(data['errors'])[:400]}")
    return data["data"]["menu"]


def fetch_menu(source, loc_key, category="CONCENTRATES"):
    src = SOURCES[source]
    rid = src["locations"][loc_key]
    products, offset, limit = [], 0, 100
    while True:
        menu = gql(src["proxy"], src["referer"], {"retailerId": rid, "offset": offset, "limit": limit,
                                                   "filter": {"category": category}})
        products.extend(menu["products"])
        offset += limit
        if offset >= (menu.get("productsCount") or 0) or not menu["products"]:
            break
    return products


def discover(site_url):
    html = urllib.request.urlopen(urllib.request.Request(site_url, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    pairs = set(re.findall(r'data-retailer-id="([^"]+)"[^>]*data-retailer-name="([^"]+)"', html))
    # The proxy URL lives in the plugin bundle, not the page — the plugin's presence is the tell.
    plugin = re.search(r'/plugins/cp-dutchie/', html)
    return sorted(pairs, key=lambda p: p[1]), bool(plugin)


# ── Normalization ─────────────────────────────────────────────────────────────

def split_name(name):
    """'Erva | 90u Live Rosin | Cherry Plantains' → ('Erva', '90u Live Rosin', 'Cherry Plantains').
    Names without pipes return ('', '', name). A trailing '(Indica)' style tag is dropped."""
    parts = [p.strip() for p in name.split("|")]
    if len(parts) >= 3:
        brand, form, strain = parts[0], " | ".join(parts[1:-1]), parts[-1]
    elif len(parts) == 2:
        brand, form, strain = parts[0], "", parts[1]
    else:
        brand, form, strain = "", "", parts[0]
    # Drop trailing '(Indica)' style tags and '(2g)' size tags; collapse doubled spaces.
    strain = re.sub(r"\s*\((?:indica|sativa|hybrid|\d+(?:\.\d+)?\s*(?:g|mg|oz))[^)]*\)\s*$", "", strain, flags=re.I)
    return brand, form, re.sub(r"\s+", " ", strain).strip()


def normalize(product, source, loc_key):
    brand_seg, form, strain = split_name(product["name"])
    rows = []
    for v in product.get("variants") or []:
        rows.append({
            "source": source,
            "location": loc_key,
            "brand": (product.get("brand") or {}).get("name") or brand_seg,
            "brand_seg": brand_seg,
            "form": form,
            "strain": strain,
            "product": product["name"],
            "subcategory": product.get("subcategory") or "",
            "strain_type": product.get("strainType") or "",
            "size": v.get("option") or "",
            "price": v.get("priceRec"),
            "special": v.get("specialPriceRec"),
            "qty": v.get("quantity"),
            "thc": (product.get("potencyThc") or {}).get("formatted") or "",
            "terpenes": [(t["name"], t["value"], t.get("unitSymbol") or "") for t in (product.get("terpenes") or [])],
            "slug": product.get("slug") or "",
        })
    return rows


# ── Catalog join ──────────────────────────────────────────────────────────────

def norm_key(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9#+× ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_catalog():
    entries = {}
    for p in STRAINS.glob("*.md"):
        for ln in p.read_text(encoding="utf-8").splitlines():
            if ln.startswith("# "):
                entries[norm_key(ln[2:])] = p.stem
                break
    nodes = set()
    if NODES.exists():
        for m in re.finditer(r"^- \*\*([^*]+?)\*\*", NODES.read_text(encoding="utf-8"), flags=re.M):
            name = re.sub(r"\s*\(.*?\)\s*", " ", m.group(1)).strip()
            nodes.add(norm_key(name))
    return entries, nodes


def catalog_match(strain, entries, nodes):
    k = norm_key(strain)
    if k in entries:
        return "entry", entries[k]
    k2 = re.sub(r"\s*#\d+$", "", k)  # 'guava push pop #82' → 'guava push pop'
    if k2 in entries:
        return "entry", entries[k2]
    if k in nodes or k2 in nodes:
        return "node", ""
    return "", ""


# ── Output ────────────────────────────────────────────────────────────────────

def money(x):
    return "" if x is None else f"${x:.2f}"


def rundown_table(rows):
    head = "| Location | Brand | Strain | Form | Sub | Size | Price | Special | Qty | THC | Catalog |\n|---|---|---|---|---|---|---|---|---|---|---|"
    lines = [head]
    for r in rows:
        cat = {"entry": f"entry: {r['match_slug']}", "node": "lineage node", "": "unknown"}[r["match"]]
        lines.append(f"| {r['location']} | {r['brand']} | {r['strain']} | {r['form']} | {r['subcategory']} | {r['size']} | "
                     f"{money(r['price'])} | {money(r['special'])} | {r['qty']} | {r['thc']} | {cat} |")
    return "\n".join(lines)


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_targets(spec):
    targets = []
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if ":" not in item:
            sys.exit(f"target '{item}' must be <source>:<location> (see `list`)")
        src, loc = item.split(":", 1)
        if src not in SOURCES:
            sys.exit(f"unknown source '{src}' (see `list`)")
        if loc == "all":
            targets.extend((src, l) for l in SOURCES[src]["locations"])
        elif loc not in SOURCES[src]["locations"]:
            sys.exit(f"unknown location '{loc}' for {src} (see `list`)")
        else:
            targets.append((src, loc))
    return targets


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = argv[0]

    if cmd == "list":
        for key, src in SOURCES.items():
            print(f"{key}  ({src['name']}, {src['adapter']})")
            for loc in src["locations"]:
                print(f"  {key}:{loc}")
        return

    if cmd == "discover":
        pairs, has_proxy = discover(argv[1])
        print(f"cp-dutchie plugin present (proxy at <site>/wp-json/cannaplanners/v1/graphql/): {has_proxy}")
        for rid, name in pairs:
            print(f"  {name}: {rid}")
        return

    if cmd == "fetch":
        targets = parse_targets(argv[1])
        opts = argv[2:]
        subs = brands = None
        json_out = None
        show_all = "--all" in opts
        for i, o in enumerate(opts):
            if o == "--sub":
                subs = {s.strip().upper() for s in opts[i + 1].split(",")}
            if o == "--brands":
                brands = [b.strip().lower() for b in opts[i + 1].split(",")]
            if o == "--json":
                json_out = opts[i + 1]

        entries, nodes = load_catalog()
        rows = []
        for src, loc in targets:
            try:
                products = fetch_menu(src, loc)
            except Exception as e:
                print(f"! {src}:{loc} failed: {e}", file=sys.stderr)
                continue
            for p in products:
                rows.extend(normalize(p, src, loc))

        if subs:
            rows = [r for r in rows if r["subcategory"].upper() in subs]
        if brands:
            rows = [r for r in rows if any(b in r["brand"].lower() or b in r["brand_seg"].lower() for b in brands)]
        if not show_all:
            rows = [r for r in rows if (r["qty"] or 0) > 0]
        for r in rows:
            r["match"], r["match_slug"] = catalog_match(r["strain"], entries, nodes)
        rows.sort(key=lambda r: (r["match"] != "entry", r["brand"].lower(), r["strain"].lower(), r["location"]))

        print(rundown_table(rows))
        unknown = sorted({r["strain"] for r in rows if not r["match"]})
        if unknown:
            print(f"\nNot in catalog ({len(unknown)}): " + ", ".join(unknown))
        if json_out:
            Path(json_out).write_text(json.dumps(rows, indent=1), encoding="utf-8")
            print(f"\nwrote {json_out}")
        return

    sys.exit(f"unknown command '{cmd}'\n{__doc__}")


if __name__ == "__main__":
    main(sys.argv[1:])
