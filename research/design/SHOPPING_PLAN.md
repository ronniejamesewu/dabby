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

**Built Sept 2, 2026** as `menu_fetch.py` (`list` / `discover` / `fetch`).
First adapter is `dutchie-wp`: dutchie.com blocks scripts outright
(Cloudflare 403), but sites on the cp-dutchie WordPress plugin proxy
Dutchie's GraphQL unauthenticated — the script sends the plugin's own
menu query, paginates, normalizes variants to rows (location, brand,
strain, form, subcategory, size, price, special, qty, THC), joins the
strain segment of the product name against catalog entry titles and
lineage-node names, and prints the rundown table. Filters: subcategory,
brand substring, in-stock only by default. IgadI's eight locations are
registered; `discover <shop url>` reads retailer ids off any cp-dutchie
site. Watchlist filtering stays in conversation (private layer).

- `menu_fetch` script with per-platform adapters producing a normalized
  in-stock concentrate list (brand, product, size, price, promo).
  Platforms seen: Dutchie (direct
  `dutchie.com/embedded-menu/<store-id>/products/<category>` is raw-
  readable; store id sits in the dispensary page's embed-script tag;
  wrappers are consent-gated), Dutchie-via-WordPress (IgadI's
  `cp-dutchie` plugin proxies GraphQL — see above), Weedmaps brand/dispensary
  pages (readable), Jane (client-side search, load-all-then-filter).
- Workflow: name dispensaries → script pulls stock → filter to watchlist
  brands → join against catalog (known → card; unknown → research-strain
  pass) → rundown table in conversation → pick.
- Cross-shop (same jar across dispensaries + promos) is parked as its
  own feature; near-free once adapters exist, decision deferred.
- Trip sheet: email-to-self (ranked shortlist, substitution branch for
  website-vs-shelf divergence, pass list, deal notes). Artifacts rejected
  — hard to retrieve on mobile. Bookmark page (`trip.html`) only if the
  inbox hop proves annoying.

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
   of a trip; further adapters (Weedmaps, Jane, direct Dutchie via browser)
   wait for real friction.
