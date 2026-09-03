# Research Layer — Display & Shopping Plan

Design record for how the `research/` catalog gets consumed. Derived from
two shopping scenarios walked through Aug 31, 2026 (planned desktop trip;
unplanned in-store/offered-jar). Companion to `research/README.md`
(conventions) and the research-strain skill (research workflow).

## Principles carried in

- Mechanize the floor: retrieval is code, inference is on demand. Menu
  scraping and price comparison never spend frontier tokens.
- Durable vs ephemeral: lineage and provenance persist in the catalog;
  stock, prices, and trip lists live in conversation or disposable
  deliverables and never enter the repo.
- Public register: anything rendered or committed reads like a database.
  Reputation and opinion never touch the repo.
- Social latency is a design constraint: in-store use is a ten-second
  glance while a person waits.

## Build 1 — `research.html` (reference layer)

- Standalone `Dabby_Research_Renderer.py`; the log generator stays
  jars-only. Reads `research/`, writes `research.html`, committed and
  regenerated in CI like `index.html` (one line each in `deploy.yml` and
  `preview.yml`). Markdown body via the `markdown` package (pip step in
  workflows) — no hand-rolled parser.
- **Cards:** one per strain, extracted from the conventional bullets
  (`**Grower:**`, `**Processor:**`, `**Type:**`, `**Cross:**`) — name,
  axes, type badge (cross / blend / pheno wash), cross line, status mark
  (terminated vs open questions). Card expands to the full entry.
- Below cards: ancestry nodes, brand facts, source atlas — collapsible.
- **Validator for free:** renderer fails on any entry missing required
  fields; catalog conventions become a mechanical check.
- Mobile-first via existing `style.css`; client-side filter box (strain
  browser pattern); zero CDN dependencies (must work on bad signal).
  Single page, anchors. Nav link from the main log (one generator line —
  flagged).
- Not rendered: reputation/watchlist (private layer), menu images
  (archive question unresolved).

## Build 2 — brands split (no build; convention)

`research/brands.md` holds facts only (roles, licenses, surfaces, stated
partnerships). Reputation, watchlist status (trusted / curious / avoid /
unresearched), and dated opinion positions ("X thinks mids — last tried
2025, updates only on a jar in hand") live in the private memory layer.
Rep is a time series: every line dated and attributed, never a bare
adjective.

## Build 3 — menu adapters (planned-trip workflow)

**First adapter (dutchie-wp) built Sept 2, 2026.** Same date: a seven-store
survey (all tested live) extended coverage to five platforms and produced
the join and pricing design in Build 4.

- `menu_fetch.py` (`list` / `discover` / `fetch` / `join` / `snippet` /
  `fixtures`). First adapter is `dutchie-wp`: dutchie.com blocks scripts
  outright (Cloudflare 403), but sites on the cp-dutchie WordPress plugin
  proxy Dutchie's GraphQL unauthenticated — the script sends the plugin's
  own menu query, paginates, normalizes variants to rows (location, brand,
  strain, form, subcategory, size, price, special, qty, THC), joins the
  strain segment of the product name against the catalog, and prints the
  rundown table. Filters: subcategory, brand substring, in-stock only by
  default. IgadI's eight locations are registered; `discover <shop url>`
  reads retailer ids off any cp-dutchie site.
- **Five platforms, seven stores (Sept 2, 2026 survey):** dutchie-wp
  (IgadI, script, proxy as above); dutchie-embed (Lightshade Federal
  Heights, Magnolia Road Broomfield, Reefer Madness ND/SB — dutchie.com
  itself Cloudflare-walls scripts (403 "Just a moment"), so these four
  stores are retrieved only via the browser pane running persisted-query
  GETs against `dutchie.com/api-0/graphql` from an
  `embedded-menu/<storeId>` page); dispense (The Dab Broomfield, script,
  public menu key extracted at run time from the site's Next.js bundle,
  never committed); weedmaps (Maikoh Boulder + Denver, script,
  `discovery/v1/listings/dispensaries/<slug>/menu_items`); sweed
  (Krystaleaves Denver, script, `_api/Products/GetProductList` with a
  `StoreId` header).
- **Retrieval split is a platform property, not a preference:** script
  covers dutchie-wp, dispense, weedmaps, sweed; only dutchie-embed
  requires the browser pane. `menu_fetch.py snippet <store_key>` prints
  the browser JS for a dutchie-embed store; the pane runs it and the
  result feeds `join --json`.
- **Per-store name grammar.** Every platform prints "brand / form / size /
  strain" in its own order, and three separate grammars appear inside a
  single store (Reefer Madness: `REC - Brand - Strain / Form`, one
  unprefixed product with no leading `REC -`, and `*...*` drop-date notes
  to strip; Dispense: brand/form/size all pipe-delimited before a `- `
  strain marker, with tier words and trailing type codes to drop; Maikoh:
  brand-form-strain with lineage in `{A x B}` braces, strain-only rows
  with no brand, and a four-field `Lazercat | Strain | Form | size` row).
  `parse_name(store_key, raw_name)` holds one grammar function per store
  key rather than one generalized parser, because the seven grammars do
  not reduce to a shared pattern.
- **Join tiers, checked in order:** `jar` (an active/closed jar's
  `STATUS.name`) → `entry` (a `research/strains/` catalog title) → `node`
  (a `lineage_nodes.md` name) → `classic` (the classics stop-list) →
  unmatched (`''`). **POS strain taxonomy fields are never used for
  joining** — Sweed's own `strain{name}` field collapses "Papaya Cake" to
  "Papaya," a name-collision trap; the join always works from the parsed
  product name, never the platform's internal strain record.
- **Potency is recorded as-listed** (value + unit as the platform prints
  it) with a `potency_flag` below 5% — not corrected, not re-derived.
  Three failure modes drove the flag, not one: IgadI's dutchie-wp
  `potencyThc.formatted` and Reefer Madness's dutchie-embed rows both read
  ~7% on rosin (a POS sync artifact, not measured THC); dutchie-embed
  potency units flip per product (`PERCENTAGE` vs `MILLIGRAMS` holding a
  percent-looking number); Dispense carries a decimal-fraction bug on some
  brands (Mighty Melts rows read 0.4–1.5 instead of 40–150).
- **No COA column.** The lab-result link fields (Dutchie
  `canonicalLabResultUrl`, Dispense `labs`, Sweed `labTests`) carried zero
  links across roughly 1,400 rows fetched in the survey; the column is
  dropped from `Row` rather than kept empty.
- **Stock is variant-level or absent, per store.** Dispense never returns
  qty 0 (out-of-stock variants are omitted from the response); Dutchie
  stores return zero-quantity variants alongside in-stock ones (the
  product still lists, one option shows 0); Sweed carries a per-variant
  `availableQty`; Weedmaps carries no stock count at all, only
  `is_online_orderable`.
- **Specials present at 6 of 7 stores** (all but Maikoh, whose own
  `/discovery/v1/deals` endpoint ignores its `listing_slug` filter and
  returns unusable results; Maikoh's storefront instead prints promo
  codes with no schedule).
- **Deals model — two authorities, not one.** The feed is authoritative
  for a specific product's sale price *today* (IgadI specials, Dispense
  per-product discounts, Sweed promotions, Dutchie-embed
  `filteredSpecials`). Store-published text is authoritative for
  *recurring* day-of-week deals — the Reefer Madness feed carried 9 of
  the 13 deals posted on reefermadnessdenver.com, 3 of those 9 with wrong
  end dates and 1 with the wrong percent. Both layers are kept; neither
  substitutes for the other. Exclusions are name predicates applied to
  the whole deal object, not a percent adjustment — Lightshade's Monday
  710 Labs deal excludes the Persy and Close Friends lines entirely (they
  get no discount tier, not a smaller one).
- **Tax basis and stacking rule are per-store facts, sourced and dated**
  (see Build 4 for the full table); where a store gives no answer the
  field is `unknown`, printed alongside the as-listed price rather than
  assumed.
- Cross-shop (same jar across dispensaries + promos) stays parked as its
  own feature; near-free once adapters exist for a location, decision
  deferred.
- Trip sheet: email-to-self (ranked shortlist, substitution branch for
  website-vs-shelf divergence, pass list, deal notes). Artifacts rejected
  — hard to retrieve on mobile. Bookmark page (`trip.html`) only if the
  inbox hop proves annoying.

## Build 4 — price and forecast

**Built Sept 2, 2026** on the seven-store survey, alongside Build 3's
grammar and join work.

- **`menu_price.py`** (`price` / `forecast` / `deals fetch`), importing
  `menu_fetch`. `price "<query>" [--json rows.json ...] [--day
  YYYY-MM-DD]` matches a query case-insensitively on strain (then
  optional `--brand`) and prints the as-listed price, any feed special,
  and the applicable posted deal for that day. `forecast "<query> --days
  7 [--json ...]` prints a store × day table ranked by per-gram
  out-the-door price, with qty and a confidence note per row.
- **Deals schema**, one file per store at `shopping/deals/<store_key>.json`:
  `{store, captured (ISO date), source (url/text), deals: [{id, name,
  source: 'feed'|'posted', kind: 'percent'|'target_price'|'bogo'|
  'bundle', value, brand, scope, category, days, start, end, hours,
  excludes, includes, menu_type, stack, notes}]}`. `excludes` are regex
  strings checked against the raw product name **before** any tier is
  applied — the Lightshade 710 Labs Monday deal is written with
  `excludes: ["(?i)persy", "(?i)close friends"]` for exactly that reason.
  `menu_price.py deals fetch <store_key>` writes the script-fetchable
  feed layer (IgadI specials, Dispense discounts, Sweed promotions) to
  `shopping/deals/<store>_feed.json`; the posted (store-published,
  recurring) layer has no auto-parser — `deals from-text` is documented
  but not implemented, and the posted-deal files for Lightshade Federal
  Heights and both Reefer Madness locations were hand-written from the
  facts below, captured 2026-09-02.
- **Tax basis, by store (all verified Sept 2, 2026):** Lightshade Federal
  Heights — pre-tax, 25.85% rec flat (Dutchie `taxConfig`; corroborated by
  a Reddit post). Magnolia Road Broomfield — pre-tax, 8.15% sales +
  24.25% cannabis (Dutchie `taxConfig` states compound, but menu prices ×
  1.324 land on round dollars, consistent with cumulative in practice;
  both readings recorded). IgadI (dutchie-wp) — pre-tax (stated in the
  specials text); rate unknown. The Dab (Dispense) — out-the-door
  (inferred: venue `salesTax`/`cannabisTax` both read 0, and the site
  states "Listed Prices Include Tax"). Reefer Madness (ND/SB),
  Krystaleaves, Maikoh — unknown; no tax field found on any surface
  checked. Where the basis is unknown, the engine prints the as-listed
  price plus an `otd_if_pretax` line at a default 0.30 CO rate, labeled
  as an assumption.
- **Stacking rule, by store:** IgadI — none (stated in the specials
  text). Lightshade, Magnolia — best-single discount (Dutchie dispensary
  `specialsSettings` reads `discountStacking: false`, `favorCustomer`). The
  Dab — `NO_DOUBLE_STACKING` (Dispense venue field). Reefer Madness —
  conflicting sources: the dispensary-level `specialsSettings` reads
  `discountStacking: true` (compounding) while each individual special
  reads `non-stacking`/`favorCustomer`; recorded as unknown, both
  readings printed. Krystaleaves, Maikoh — unknown; no stacking field
  found.
- **7-day forecast and confidence decay.** Weekly promos are posted a
  week at a time (Lightshade's r/LightshadeDispensary and r/COents
  threads, Reefer Madness's site) — a forecast whose posted-deal layer is
  older than 7 days is marked `stale`; a deal end-dated beyond the
  forecast window is marked `ok`. Feed end dates on recurring deals are
  unreliable in both directions — the Dutchie feed returns recurrences
  past their own end date as current, and end-dates deals the store's
  site says are ongoing (Build 3's Reefer Madness count) — so the posted
  layer, not the feed's dates, decides whether a recurring deal is live.
- **Interfaces (fixed, shared with Build 3):** `menu_fetch.py` — `STORES`
  registry, `Row` dict, `fetch_store` / `load_rows_json` / `parse_name` /
  `join_row`. `menu_price.py` — `load_deals`, `applicable(deal, row,
  when)`, `price_on(row, deals, when, store)`. `shopping/deals/*.json` is
  committed (public facts, dated); `shopping/rows/` (fetched rows,
  browser dumps) is gitignored; the Dispense API key is never committed.

## Unplanned-trip workflow (no build; skill behavior)

- Two speeds: glance (research.html on phone) and conversation (jar
  photo → catalog diff → tensions).
- Catalog hit is a **diff**, not an answer: the offer (label, batch,
  pheno #, verbatim claims) is a new claimant; output what's new, what
  agrees, what conflicts.
- Live research aims at provenance triage and brand trust — never live
  lineage under social pressure. Strain research is homework from the
  captured photo.
- Every jar encounter is a capture event: label photo + COA QR. COAs
  carry measured cannabinoid/terpene panels — the `measured` evidence
  word outranks `stated`, and for owned jars lets inference be checked
  against measurement.

## Parked candidates

- Goddard cannabis-intelligence-database CSV as a local name-collision
  index (peek at columns first; retail-copy provenance, lead tier).
- demarily strains API as variant index + source router (lineage fields
  hollow as of Aug 31 2026 — re-probe ~Oct 2026).
- Menu-image archiving to a gitignored local directory.

## Order

1. Bookkeeping (this doc, atlas, skill amendments) — done Aug 31, 2026.
2. Build 1 renderer, own PR.
3. Build 2 memory file — done alongside bookkeeping.
4. Build 3 adapters — first adapter (dutchie-wp) built Sept 2, 2026 ahead
   of a trip; the same date's seven-store survey added dutchie-embed
   (browser pane), dispense, weedmaps, and sweed adapters, plus the join
   and grammar design above. Jane still waits for real friction.
5. Build 4 pricing/forecast layer (`menu_price.py`, deals schema, tax and
   stacking facts) — built Sept 2, 2026 on the same survey.
