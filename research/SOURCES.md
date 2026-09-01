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
| Dutchie embed | Wrapper pages are consent-gated iframes; the store id is in the `dutchie.com/api/v2/embedded-menu/<id>.js` script tag; read `dutchie.com/embedded-menu/<id>/products/<category>` directly — plain text. Multi-location wrappers carry one id per location |
| Dutchie via WordPress (IgadI `cp-dutchie` plugin) | Server-rendered product pages; readable, but descriptions are boilerplate |
| Weedmaps brand/dispensary pages | Readable; category filters are client-side (URL params ignored) |
| Jane / iheartjane | Client-side search over an alphabetically paginated full list — load all, then filter |

## Known hazards

- **"In House Genetics" (WA seed breeder, Branden Bond)** ≠ In House /
  In House Melts (CO processor). Pollutes nearly every "In House" search.
  BUT: legitimately appears inside some lineages (Black Cherry Punch,
  Divine Banana) — collision and genuine ancestry interleave; keep straight.
- Private IG accounts (@jlsmonster, @terpfountaingenetics as of Aug 30
  2026) — bios readable, grids need a follow (user's call, user's account).
- Cloudflare walls: strainly.io. Age-gate JS: maikohholistics.com.
- Content farms (JointCommerce) — AI-generated strain pages; never a
  corroboration vote on their own.
