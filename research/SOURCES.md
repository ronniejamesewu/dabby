# Source Atlas

Which surfaces hold lineage info, by tier. **Append rule:** every research
pass that discovers a new productive surface adds it here with a dated note.
Retrieval rule for all web reads: raw page text (browser tools), never
WebFetch — it summarizes pages through a small model and misses JS-rendered
content while reporting the page as read (validated by A/B test, Aug 28 2026).

## Anchor-controlled surfaces (the party's own words)

| Surface | What it holds | Notes |
|---|---|---|
| Producer IG drop menus | Lineage lines under strain names; blend/pheno notation; terp %s in captions | Login-gated — main-session read via user's Chrome only. Often the ONLY source for blends, pheno selections, and fresh drops. Erva: @ervacolorado; In House: @inhousemelts, @capndevdev posts their menus |
| Brand storefronts (Weedmaps/Jane brand pages) | Brand-controlled SKU listings; In House's carry "=" lineage formulas (~250 SKUs, 6 pages: weedmaps.com/brands/in-house-llc/products) | Generalizes: ANY brand's own storefront listing is anchor-controlled. Discovered Aug 29 2026 |
| Breeder catalogs | Full cultivar lists, sometimes multi-generation trees | bloomseed.co/cultivars (356 names, 4 tiers; product pages have lineage-tree widgets); threesgeneticreserve.com (~30 SKUs, JS-heavy — use /search or /collections/all); archiveseedbank.com (pheno-numbered precision); dnagenetics.com; skunktek.com |
| Deep brand libraries | Per-strain genetics pages from brands with long catalogs | 710labs.com genetics pages (e.g. Papaya: "Mystery / Clone Only") |
| fruitfullseeds.com/genetics | Fruitfull Seeds' own catalog with dated releases and full pheno-numbered formulas (e.g. Rainbow Juice = Garlic Juice #2 × Grape Rainbow Pie #17) | Discovered Aug 31 2026; Erva-roster breeder, KY hashmaker Mr. Autogrow |
| Dispensary product pages | Product existence + spelling; igadiltd.com carries NO lineage text (generic boilerplate; menus load via JS embeds) | Existence confirmation only |

**Menu-post index (anchor reads, chronological):** Erva×InHouse collab
announcement 7/18 (instagram.com/p/Da8N1onuO8U/); collab drop 8.7.26
(instagram.com/p/Dbql2m3jsQA/ — carries Erva's breeder-roster credit
comment); In House 8.15.26 (instagram.com/p/Db8kFLyNntD/); Erva 8.25.26
(instagram.com/p/DcbpZF1EUi_/); In House peach drop 8.29.26
(instagram.com/p/Dci4mpoNj2a/); In House 7.3.26
(instagram.com/p/DaQEmPgtGld/); In House 7.31.26
(instagram.com/p/DbZbm59gG67/); In House 6.5.26 menu (URL not captured).
Drop-post comment sections carry breeder credits and demand chatter —
credits are anchor when posted by the producer's own account; demand
chatter is a timing signal only, never a quality input.

## Non-anchor surfaces (leads and corroboration only)

| Surface | Use |
|---|---|
| SeedFinder | Best broad genealogy index; middle-tier lead generation; flags "probably"/algorithmic trees — treat those as low confidence |
| Leafly / AllBud / Strainpedia | Corroboration votes; frequently repeat each other — check independence before counting convergence |
| Seed retailers (Terpy Seeds, DC Seed Exchange, etc.) | Sometimes the only listing tying a breeder to a cultivar |
| Forums (THCFarmer, Rollitup) | Occasionally the real story (Death Star); always attribute |

## Open datasets and APIs (assessed Aug 31, 2026)

| Source | Verdict |
|---|---|
| demarily "Cannabis Strains API" (api.demarily.dev/bud; 43k names from Hytiva/Leafly/AllBud/SeedFinder/Weedmaps; free 100 req/day) | Lineage/breeder fields hollow on known-answer probes (Sherbanger, Rainbow Belts → "Unknown"). BUT: variant-preserving name index (pheno #s and crosses kept as separate records), per-record `source_url` router, and Dutchie-image records with menu THC = retail-circulation signal. Use as collision/variant index + discovery router. Re-probe lineage fields ~Oct 2026 |
| Goddard / Loyal9 cannabis-intelligence-database (GitHub; 15.7k strains CSV, MIT, Zenodo DOI) | Scraped seed-retailer product copy, regex-"AI" extracted; cultivation/retail fields, weak on parentage. Candidate local name-collision index only — check columns first |
| Loyal9 grow_data (2.8k strains, Wikileaf scrape, categorical THC/CBD) | No lineage. Skip |
| strain-database.com (claims 51.7k strains, "open-access") | GitHub org is an empty shell (profile README only); site Cloudflare-blocks automated access; never surfaced in any research pass. Treat as look-alike, not a source |
| Strain Diary (iOS beta, straindiary.com) | Personal jar-level journal, not a data source. Relevant for its capture UX: label / COA-QR scan auto-fills entries — the pattern the capture protocol borrows |

## Menu platforms (planned-trip adapters)

| Platform | Read pattern |
|---|---|
| Dutchie embed | dutchie.com itself returns 403 (Cloudflare) to scripts — read via browser only, or via a WordPress proxy (next row). Wrapper pages are consent-gated iframes; the store id is in the `dutchie.com/api/v2/embedded-menu/<id>.js` script tag; read `dutchie.com/embedded-menu/<id>/products/<category>` directly — plain text. Multi-location wrappers carry one id per location |
| Dutchie via WordPress (IgadI `cp-dutchie` plugin) | Listing is filled client-side, but the plugin proxies Dutchie's GraphQL at `<site>/wp-json/cannaplanners/v1/graphql/` — no Cloudflare wall, arbitrary Dutchie Plus queries accepted; per-location retailer ids sit in the shop page as `data-retailer-id`. This is the `menu_fetch.py` adapter (`dutchie-wp`, Sept 2 2026). Descriptions are boilerplate |
| Weedmaps brand/dispensary pages | Readable; category filters are client-side (URL params ignored) |
| Jane / iheartjane | Client-side search over an alphabetically paginated full list — load all, then filter |
| Dutchie embed persisted-query API (`dutchie.com/api-0/graphql`) | `menu_fetch.py`'s `dutchie-embed` adapter (Lightshade Federal Heights, Magnolia Road Broomfield, Reefer Madness ND/SB; Sept 2 2026): FilteredProducts/FilteredSpecials/ConsumerDispensaries persisted-query GETs, read from the browser pane only — dutchie.com Cloudflare-walls the same endpoint to scripts. `menu_fetch.py snippet <store_key>` prints the browser JS; the pane's result feeds `join --json` |
| Dispense v1 API (`api.dispenseapp.com`) | `thedab.com` (The Dab Broomfield), script-fetchable. Requires an `api-key` header carrying the site's public menu key, read from the Next.js bundle at run time (`menus-*.vercel.app/_next/static/chunks/*.js`, pattern `apiKey:"<uuid>"`) — never committed. Discovered Sept 2 2026 |
| Weedmaps discovery API (`api-g.weedmaps.com/discovery/v1/listings/dispensaries/<slug>/menu_items`) | Maikoh Boulder + Denver, script-fetchable. Static per-request menu, no stock counts; lineage claims appear in `{A x B}` braces on some product names — captured as `lineage_claim`, kept verbatim, not treated as an anchor lineage source on its own. Discovered Sept 2 2026 |
| Sweed `_api` (`shop.krystaleaves.com/_api`) | Krystaleaves Denver, script-fetchable; requires a `StoreId` header. Product records carry a POS `strain{name}` taxonomy field that must never be used for catalog joining (name-collision trap — see Known hazards). Discovered Sept 2 2026 |
| Store-published deal text | reefermadnessdenver.com is script-readable (day-of-week deals page). Lightshade's deals are published only on Reddit — r/LightshadeDispensary and the weekly r/COents thread — readable only through the user's Chrome, never the browser pane or a script. Both are the authoritative source for *recurring* day-of-week deals; feeds are authoritative for a specific product's price today (see `research/design/SHOPPING_PLAN.md` Build 3). Discovered Sept 2 2026 |

## Known hazards

- **"In House Genetics" (WA seed breeder, Branden Bond)** ≠ In House /
  In House Melts (CO processor). Pollutes nearly every "In House" search.
  BUT: legitimately appears inside some lineages (Black Cherry Punch,
  Divine Banana) — collision and genuine ancestry interleave; keep straight.
- Private IG accounts (@jlsmonster, @terpfountaingenetics as of Aug 30
  2026) — bios readable, grids need a follow (user's call, user's account).
- Cloudflare walls: strainly.io. Age-gate JS: maikohholistics.com.
- Dutchie's brand records are platform-wide and collide: the "ERVA" brand
  object on IgadI's menu carries a Massachusetts hemp company's description
  while the products are Erva Colorado's. Product names, not brand
  descriptions, identify the producer (Sept 2 2026).
- Content farms (JointCommerce) — AI-generated strain pages; never a
  corroboration vote on their own.
- Dutchie potency fields read ~7% on rosin at two unrelated stores
  (IgadI's dutchie-wp `potencyThc.formatted`, Reefer Madness's
  dutchie-embed rows) — a POS sync artifact, not measured THC. Dutchie-
  embed potency units also flip per product (`PERCENTAGE` vs
  `MILLIGRAMS` holding a percent-looking number). Record potency
  as-listed with its unit and a below-5% flag; never correct it
  (Sept 2 2026).
