# Dabby — Conversation Handoff Notes
## Last updated: May 11, 2026 — Session 19

This document provides full context for a new AI assistant picking up this project. Read alongside Dabby_Methodology.md and the live log at `index.html` in the repo working directory.

---

## Project Goal

A running log of sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig." All material is hash rosin (ice water extracted, solventless) using cold start technique. The log records what happened, swab results, and current thinking on what to try next — not a formal calibration program. The methodology document captures the physical reasoning behind curve design.

---

## Infrastructure

**Live log:** https://ronniejamesewu.github.io/dabby
**Repo:** ronniejamesewu/dabby (branch: main)
**Files in repo:** `index.html` (the rendered log), `Dabby_Log_Generator.py` (Python generator), `CLAUDE.md` (session instructions), `Dabby_Handoff_Notes.md` (this file), `Dabby_Methodology.md` (thermal model and session process reasoning), `.github/workflows/deploy.yml` (auto-deploys main to gh-pages on push), `.github/workflows/preview.yml` (posts preview URL on every PR, cleans up on close)

**Environment:** Claude Code. Files are in the repo working directory. Read them directly — do not fetch from raw.githubusercontent.com or copy files to a separate path.

**Publishing workflow:**
1. Edit `Dabby_Log_Generator.py`
2. Run `python3 Dabby_Log_Generator.py` to produce `index.html`
3. Commit both files to a feature branch
4. Push the branch and open a PR
5. GitHub automatically posts a preview URL as a PR comment
6. User confirms in conversation — say "merge it" and Claude merges the PR directly via GitHub MCP tools. If the user wants to review the preview first, they do so, then confirm. Either way, Claude handles the merge — user does not need to go to GitHub.
7. `deploy.yml` automatically publishes to gh-pages — live site updates

**PR merge:** Claude can merge PRs directly using `mcp__github__merge_pull_request`. Always merge the PR as soon as the user confirms — do not leave it for the user to merge manually. If the handoff notes are updated after the PR is opened, push them to the same branch before merging, or open a follow-up PR immediately and merge that too.

**CRITICAL — never use `push_files` for `index.html` or routine commits.** `push_files` passes full file content as string literals and has caused silent content loss in past sessions (stripped charts, lost sections). Git is the correct path for all routine work. `push_files` is acceptable only for temporary files on non-main branches (e.g., mockups on gh-pages) when git checkout of that branch is impractical — and only when the file is not `index.html`.

**CRITICAL — push index.html correctly:** The `index.html` committed to the repo must be the literal output of running `python3 Dabby_Log_Generator.py`. Never write `index.html` content manually or from memory. The correct sequence is always: edit generator → run generator → commit both files.

**Generator notes:** Python, not Node.js. Produces HTML. Charts rendered via Chart.js from CDN — requires internet to render. Each curve section has a chart auto-generated from the same waypoint data that feeds the waypoint table. Chart IDs are auto-incremented. The `curve_chart_html()` helper accepts a waypoints list and returns self-contained HTML+JS. Adding a new strain requires: data constants, `STRAIN_STATUS` entry, `COMPLETED_RUNS` entries, and section build code. No TOC entries — the dashboard browser is the navigation. Footer auto-timestamps on each run. `COMPLETED_RUNS` tuples take the form `(strain, run_date, sessions_prior_today, utc_logged_at, waypoints)` — `run_date` is a `date` object or `None` if not confirmed; `sessions_prior_today` is an int (sessions run before this one on the same day) or `None` if unknown; `utc_logged_at` is a `datetime` object with UTC timezone (e.g. `datetime(2026, 5, 12, 3, 15, tzinfo=timezone.utc)`) or `None` for entries predating this field. `STRAIN_STATUS` is a 5-tuple `(name, profile_anchor, next_text, accent, slug)` — `accent` is `None` for auto-assignment or a hex string override; `slug` drives the last-run anchor (`#{slug}-run{n}`). Accent colors are resolved at module load time into `_ACCENT_RESOLVED` dict by distributing hues evenly across the non-green hue space (0–89° and 166–359°). There is no `ACCENT_PALETTE` — do not add one back. `TERPENE_REFERENCE` is an 8-tuple `(name, alias, bp_f, bp_c, band, aroma, qualities, found_in)`. `what_to_try_next_html()` helper generates the What to Try Next block; signature: `(section_id, dab_notes, ai_analysis, proposed_waypoints=None, accent=None)` — pass `accent` to apply the strain's color to the section header. `accent_header(title, accent)` returns a colored section header div for use on profile sections. `session_order_note(sessions_prior)` returns a "Nth session of the day — N prior" meta note string when sessions_prior > 0, empty string otherwise.

---

## Session Logging Protocol

When the user reports a completed run, parse the natural language description into log fields and confirm the interpretation before touching the generator. If the date is missing, ask. If swab result is missing, ask — do not log without it.

Runs are logged with exact date (not month only) when known.

**Swab protocol clarification:** A swab is always taken — it is the standard insert-cleaning step after every session, not an optional measurement. "Not recorded" means the color wasn't noted, not that no swab was taken. Always ask for swab color if not reported.

**Duration typo:** If the user reports a session time of 69 seconds, assume it is a typo for 60 seconds, log it as 60, and note the assumption in your output — tell the user to complain if you assumed wrong. Do not stop to ask for confirmation.

**Timestamp and date confirmation:** When logging a run, always capture `utc_logged_at = datetime.now(timezone.utc)` and derive local time using the user's timezone (US/Mountain, America/Denver — MDT in summer UTC-6, MST in winter UTC-7). Confirm with the user before writing: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off." Only surface the UTC/local date discrepancy in the message if the dates differ (i.e. it's late evening local time and UTC has rolled over). `run_date` should reflect the confirmed local date.

**sessions_prior_today:** When logging a run on the same day it was run, compute `sessions_prior_today` automatically from `COMPLETED_RUNS` (count entries with the same `run_date`) and tell the user what you filled in — no confirmation needed, they can correct if wrong. If logging post-date, ask casually: "Do you happen to know how many dabs you had before this one on [DATE]?" — use `None` if they don't know.

**Optional field register:** When prompting for optional or hard-to-recall fields (sessions prior today when post-date, load size, anything that may not be fresh in memory), use a casual register: "Do you happen to remember X?" This signals that the field is genuinely optional without making it feel like a required checkbox.

**Intensity:** When logging a run, ask for effect intensity if not reported: "How hard did it hit?" — anchor options are light / moderate / strong, freeform notes welcome. Keep in mind that effects unfold over hours and logging usually happens minutes post-dab, so this captures the immediate read only.

**AI Analysis:** The "AI Analysis" field in each strain's What to Try Next section is not a summary of what happened — that belongs in the run results. It should state a concrete recommendation with the reasoning behind it. Before writing AI Analysis, draw on all four artifacts: the handoff (cross-strain patterns, methodology constraints), the methodology doc, the full run history for the strain, and the user's Dab Notes just added. Cross-strain patterns are often the most valuable input — flag them when relevant. Name confounders where they affect the recommendation. Flag clearly when a recommendation is based on a single data point.

---

## Thermal Model — Current Understanding

This was substantially revised. The old estimate of a 15–35°F titanium-to-insert offset has been walked back. Current understanding:

- The quartz insert wall is ~1mm thick. At ~1.4 W/m·K conductivity the bulk thermal time constant is under one second — the insert equilibrates internally almost instantly.
- Physical contact points between titanium and quartz transfer heat efficiently. The air gap is not the dominant resistance when contact geometry is intact.
- The offset is probably small under most operating conditions. Dominant remaining uncertainties are vaporization cooling (phase change draws heat locally during active vaporization) and dynamic lag during steep ascent (titanium is always ahead of insert during fast climbs).
- Setpoints are reasonable proxies for material contact temperature.

**Do not rebuild the 1D thermal resistance model.** A substantial amount of work went into building and then partially dismantling it. The interface efficiency parameter (η) concept was developed but abandoned — the two dominant parameters were partially redundant and the underlying geometry is unknowable. Swab result is the ground truth.

**Sapphire advantage** (for when sapphire insert is acquired): not primarily closing a large interface resistance. Two mechanisms: (1) higher volumetric heat capacity — absorbs cold material contact perturbation more stably at session open; (2) better surface temperature uniformity during vaporization — ~20x higher bulk conductivity replenishes heat faster when local vaporization creates cold spots. Reddit consensus of 10–20°F lower setpoints for equivalent results is consistent with this model. Sapphire requires fresh empirical calibration from scratch — do not scale quartz curves.

---

## Curve Design — Key Insights

**Ascent rate and offset:** During steep ascent, titanium is ahead of insert temperature; during flat or slow phases the system approaches equilibrium. However, because the insert equilibrates in under a second, even a short flat tail (10 seconds) is sufficient for the insert to reach the setpoint. Do not flag short flat tails as inadequate for offset closure — the equilibration time is too fast for this to be a meaningful concern at any reasonable tail length.

Steeper mid-climbs move through terpene zones faster. The shape of the climb matters for when vaporization begins, not for offset concerns.

**Curve shape vs. single setpoint:** Multiple strains now have ramp vs. flat hold data. Emerging pattern: ramp produces better session character (more distinct staged flavors, tastier) than flat hold at equivalent endpoints — most clearly demonstrated in OC Run 6 (ramp) vs Run 7 (flat hold) at 430°F, and consistent with Hive #1 Run 5 (ramp, distinct staged flavors). Endpoint temperature appears to be the larger variable for harshness — both ramp and flat hold show tail harshness at 430°F+ across multiple strains. Swab is not a sensitive enough signal to distinguish between curve shapes within the normal operating range — subjective session character is the primary readout.

**Temperature and effect strength:** Higher temperatures vaporize a larger fraction of material in a shorter window, producing a larger bolus inhaled and a faster peak blood concentration. This is the most parsimonious explanation for the stronger effects observed at higher endpoints (OC Run 5, 460°F). CBN hypothesis rejected: CBN has ~1/10th CB1 binding affinity of THC, in-session CBN formation is limited by oxygen availability, and a higher CBN fraction would dilute rather than amplify the effect. Rate of delivery matters, not just total dose — the same material at lower temps over a longer curve could deliver similar total cannabinoids but with a slower, smoother absorption profile.

**Swab as floor indicator:** Swab color is a floor indicator within the normal operating range, not a fine-grained calibration metric. Dark or burnt residue (amber-toward-brown or darker) is a reliable signal to reduce temperature. Within the light-golden-to-amber range, swab has too many uncontrolled variables — load size, material starting color, oxidation state, swab timing, pressure — to reliably distinguish between curve shapes or small endpoint differences. Do not over-interpret swab color within the clean range.

**Baseline philosophy:** Single baseline curve for all hash rosin with cold start. Strain-specific adjustment happens empirically via swab results, not terpene-profile reasoning. Do not design different starting curves based on strain name, consistency, or inferred terpene profile without empirical justification.

**Mode:** Custom Ascent preferred over Valley. Valley's initial dip is redundant with cold start — material is already at its lowest temperature at session open.

**Opening setpoint exploration:** OC Run 5 tested a 350°F open — darker swab, stronger effect, not a clean calibration signal. Runs 6 and 7 reverted to 380°F baseline open. Lower opening setpoints are not under active exploration at this time.

---

## Chart Styling — Current State

Current spec:

- **Curve:** `#1DB954` (vivid green), 2px, solid filled dots at 2.7px radius, `clip:false` to prevent edge clipping
- **Terpene BP lines:** `#4A7D9A` (steel blue), 1px dashed, full opacity
- **Terpene labels:** `#555555`, 11px DM Mono 400, vertically centered on line (`yp + 4`)
- **Terpene label format:** `Name 311°F` (name + number + unit)
- **Terpene line length:** stops at `ca.right - 110`, label starts at `ca.right - 108`
- **THC band:** `rgba(210,90,80,0.09)` fill, pill label at 11px DM Mono 400
- **Tooltip:** dark (`#111` background), green body text, DM Mono
- **Font:** DM Mono loaded from Google Fonts CDN (300/400/500 weights)
- **Chart background:** white (`#fff`), `1px solid #CCCCCC` border
- **No area fill** under curve (removed — was visual noise)
- **Layout padding:** `{left:4, right:4, top:4, bottom:0}` to prevent edge dot clipping

**Visual overhaul pending:** The user has flagged the overall forest green styling of the log as feeling heavyweight. A visual identity review is on the open items list for a future session. Do not make styling changes without raising this first.

---

## Harm Reduction Context

Established from ACS Omega 2017 peer-reviewed study: benzene and methacrolein are documented degradation products of terpene thermolysis. Benzene formation begins in small amounts around 400°F and increases significantly with temperature. Studies showing alarming toxicant levels used 500–550°C (932–1022°F) — far above typical practice. At conservative setpoints (375–440°F) benzene formation is at the low end of the documented range. Benzene is a Group 1 carcinogen (IARC) linked to aplastic anemia and acute myeloid leukemia. Lower temperatures are meaningfully safer as well as more flavorful. This is a genuine harm reduction argument, not just a flavor argument.

**Resolved:** The 440°F vs 460°F question has been reviewed and determined to fall well below the temperature range where the research documents meaningful risk. No further discussion needed.

---

## Current Strain Status

**WW Z** (Quasi Farms, Michigan) — Run 1 complete (May 2, 2026). Baseline curve confirmed appropriate. Nothing specific to try next.

**Caramel Apple Gelato** (Quasi Farms, Michigan) — Run 1 logged (450°F endpoint, swab amber toward brown — too hot). Run 2 pending: endpoint reduced to 430°F, hold shortened to 55 seconds.

**Orange Candy** (Nikka T, 90 micron full melt) — Runs 1–2 too flat. Run 3 redesigned with steeper mid-climb and flatter tail — clean swab, strong result, wispy opening draws. Run 4 (380°F open, 440°F endpoint) run twice on May 5, 2026 — both light golden swabs. Run 5 (May 6, 2026): 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint — darker swab, last portion harsh, notably stronger effect (one data point, not confirmed). Run 6 (May 9, 2026): 380→390→410→430°F ramp — light golden swab, very nice. Run 7 (May 9, 2026): 430°F steady flat hold, 60s — plain amber swab, pleasant but not as tasty as ramp, harsh in last 20s. Ramp (Run 6) outperforming flat hold at same endpoint. Next: repeat Run 6 ramp to confirm, or try 420°F flat hold.

**The Hive #1** (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron) — Runs 1–2 (May 7, 2026): 380→390→410→440°F ramp, 65s — both clean. Run 3 (May 8, 2026): 430°F steady flat hold, 45s — clean swab, similar session character, vapor still producing at cutoff. Run 4 (May 8, 2026): same 430°F hold, 60s — clean swab, consistent. Run 5 (May 8, 2026): ramp to 430°F — light golden swab, distinct staged flavors, harsh in last ~10 seconds. Consistent tail harshness suggests 430°F slightly high on ramp. Run 6 pending: try 420–425°F endpoint, keep ramp shape.

**Fembot #3** (Riptide, CO — Fuzzy Melon × Rambutan, cold cure, 169–73 micron) — Run 1 (May 9, 2026): ramp to 430°F — light golden swab, tasty, slight tail harshness. Run 2 (May 9, 2026): 430°F steady flat hold, 60s — light golden swab, very tasty, great effects, harshness in last third. Consistent tail harshness at 430°F across both curve shapes. Run 3 pending: 420°F steady flat hold, 60 seconds.

**Mango Starburst #23** (Terps Over Yields, CO — Starburst 36 #217 × Starburst 36 #1, cold cure, jar 14 of 23) — SB36 base genetics (Starburst OG × '97 KC36), sativa-dominant, limonene/terpinolene-forward inferred. Cold nose: diesel note pronounced, sweetness underneath. Run 1 (May 9, 2026): baseline curve (380→390→410→430°F) — very clean swab, pine-forward character (more pinene than lineage inference anticipated), heady effects, no harshness. Tasty but not to user's preference. Run 2 pending: repeat to confirm.

**Maple Bacon Donut** (Quasi Farms, Michigan, cold cure, micron unknown) — Genetics not documented. Run 1 (May 10, 2026): 380→390→410→430°F ramp — darker golden swab (between target and amber, nothing burnt, flagged to watch), tasty first half, faded to generic second half, milder effect (tolerance confound — 5 sessions prior day). Run 2 (May 10, 2026): same curve — lighter swab (closer to target), distinct bacon character on first half, effects came on noticeably. Swab trending cleaner. Run 3 pending: repeat same curve to confirm trend.

**Rain Fruit** (Quasi Farms, Michigan, cold cure, micron unknown) — Run 1 (May 10, 2026): baseline ramp — notably clean swab, clear fruit notes, strong effects, no harshness. Run 2 (May 11, 2026): 375→385→410→430°F (lower open than baseline) — light golden swab, tasty, tail heat in last 10 seconds, mild effects. Consistent with cross-strain 430°F tail pattern. Run 3 pending: 420°F endpoint with 10-second hold.

**Blueberry 36** — Three jars in collection, phenotypes #1, #2, #4 from a trusted grower's pheno hunt. Producer-specific designation, not a documented cultivar. Base genetics: DJ Short's Blueberry — myrcene dominant, caryophyllene and pinene as secondaries. No curves designed. Recommended approach: nose all three jars before first sessions to establish relative comparison across phenotypes, then start all three from baseline curve and log each separately. Each phenotype is logged separately. Meaningful differences will emerge from session character and swab, not from nose or jar appearance.

---

## Open Questions

- Sapphire insert not yet acquired. When acquired, requires fresh calibration from scratch — do not scale from quartz curves.
- Whether fresh press consistency justifies a different baseline curve remains an open question. Not settled.
- **Visual overhaul of the log** — user flagged the forest green styling as feeling heavyweight. Raise this as an agenda item at start of a future session.
- **Session date backfill** — `run_date` is now a field in each `COMPLETED_RUNS` tuple. Most runs from Session 6 onward have confirmed dates. CAG Run 1 and OC Runs 1–3 are still `None` — if the user can recall the exact dates, update those tuples and re-run the generator.

**Open ideas (not yet built):**
- **Bring some excitement to first dab of the day** — user flagged a desire for this; no specific mechanism discussed yet. Could be curve, ritual, or strain choice.
- **THC boil-off vs. harshness trade-off** — higher endpoints complete more THC vaporization but produce tail harshness. Raised in Rain Fruit Run 2 context. Worth thinking through whether there's a way to characterize the trade-off empirically across strains, or whether it just becomes a preference call.
- **Quantify "rice grain" load descriptor** — weigh a few loads to establish a mg range (e.g. 0.05–0.15g). One-time calibration; update the global constants with the range.
- **Control water temperature and change frequency as variables** — standardize practice and log it. Revisit when calibration work matures.

---

## Dashboard — Implemented

The dashboard is live in the generator and deployed. It sits above the strain profiles. There is no separate Contents or TOC section — the strain browser serves as navigation.

**Structure:**
- Six stat cards in two rows of three, computed at generator runtime
  - Row 1 (volume/frequency): total runs over N days / most dabs in a day / unique strains
  - Row 2 (temperature): avg open / avg endpoint / most time spent (linear interpolation across all runs, 5°F buckets)
- Grid: `repeat(3, 1fr)` desktop, `repeat(2, 1fr)` mobile
- Searchable strain browser below the stat cards — replaces the old strain table and the old Contents section
  - Fixed-height scrollable container with sticky search input; live JS filter on `data-strain` attribute
  - Each row: colored left accent bar (per-strain hex from `_ACCENT_RESOLVED`), strain name linking to profile (🥇 if leader), → Next pill linking to What to Try Next section, → Last pill linking to most recent run, session count, last date

**Design decisions locked:**
- No calibration badges, no status column, no calibration language anywhere in the log or dashboard
- No separate Contents section — the strain browser is navigation
- Medal emoji preserved: appended to strain name in the browser row
- → Next pill always present; links to `#<anchor>-next` within each strain's What to Try Next block

**Implementation notes:**
- `COMPLETED_RUNS` list drives all stat computation — add an entry here whenever a run is logged. Tuple form: `(strain, run_date, sessions_prior_today, utc_logged_at, waypoints)`. Use `None` for `run_date` if not confirmed; `None` for `sessions_prior_today` if unknown; `None` for `utc_logged_at` for pre-existing entries. New entries should always populate `utc_logged_at` using `datetime.now(timezone.utc)` at logging time.
- `STRAIN_STATUS` drives the browser rows — 5-tuple `(name, profile_anchor, next_text, accent, slug)`. Set `accent` to `None` for auto-assignment or a hex string to override. `slug` drives the last-run anchor. Colors are resolved from `_ACCENT_RESOLVED` — there is no `ACCENT_PALETTE`.
- `FIRST_RUN_DATE` is hardcoded to `date(2026, 5, 2)` — do not change unless the first-ever run date changes.
- "Most dabs in a day" excludes runs with `run_date = None`; the stat grows more accurate as dates are confirmed.
- What to Try Next sections: each strain has a `what_to_try_next_html()` block at the bottom of its section. Helper signature: `(section_id, dab_notes, ai_analysis, proposed_waypoints=None, accent=None)`. "Dab Notes" is the user's raw observation; "AI Analysis" is Claude's concrete recommendation. If a proposed curve exists, pass waypoints and the helper will render both chart and table. Pass `accent` to apply the strain's color to the section header.

---

## Decisions Made — Do Not Re-Litigate

- 1D thermal resistance model is a dead end. Do not rebuild.
- The 15–35°F offset estimate is retired. Current position: offset probably small.
- Quartz-to-sapphire curve scaling does not work.
- Valley mode is not appropriate for cold start sessions.
- Consistency type alone does not justify a different baseline curve.
- All MD files (`CLAUDE.md`, `Dabby_Handoff_Notes.md`, `Dabby_Methodology.md`) are in the repo. Push them when relevant changes are made.
- The user's hypothesis that higher temperature (460°F endpoint) produced a notably stronger effect in OC Run 5 is logged as stated — one data point, not a confirmed finding. Do not dismiss it or over-assert it.
- Claude Code is the active environment. The old cloud/API session protocol (fetch from raw.githubusercontent.com, push_files for publishing) is retired.
- PR preview workflow is established and active. Changes go to a feature branch → PR → preview URL → merge → auto-deploy.
- Blueberry 36 phenotypes are logged as separate strains, not grouped.
- Dashboard is implemented. Do not redesign from scratch — iterate from the current generator code.
- Calibration framing retired. This is a session log, not a calibration program. Do not re-introduce "dialed," "in calibration," status badges, or status columns anywhere in the log or dashboard.
- Contents/TOC section removed. The searchable strain browser on the dashboard serves as navigation. Do not re-add a separate Contents section.
- Strain browser with live search implemented. Fixed-height scrollable container, sticky search input, JS filter on `data-strain` attribute, per-strain accent color left bars, → Next pills linking to What to Try Next sections.
- `STRAIN_STATUS` is now a 5-tuple `(name, profile_anchor, next_text, accent, slug)`. The accent field uses `None` for auto-assignment or a hex string to override. The slug field drives last-run anchors. The old calibration badge fields (badge_class, badge_text) are gone — do not add them back.
- Reference sections (Device Constants, Swab Color Reference, Baseline Curve, Terpene Reference) are collapsible blocks on the main index page. Do not move them to a separate page.
- Accent colors are auto-assigned from a hue distribution across the non-green hue space. `ACCENT_PALETTE` has been removed. To override a strain's color, set the accent field in `STRAIN_STATUS` to a hex string. `validate_accent_colors()` checks only manual overrides — auto-assigned colors are valid by construction.
- Band badge colors for terpene reference are cool-to-warm: Low = `#D6EAF8`/`#1A4A6B` (blue), Mid = `#FFF0CC`/`#8A6000` (amber), High = `#FFE5CC`/`#7A3000` (orange). Do not change.
- Reference section headers: steel blue (`#4A7D9A`), not the generic grey of run sections.
- Visual hierarchy on the page: accent color = strain profile headers + What to Try Next headers; green = run section headers; steel blue = reference section headers.
- Sessions_prior_today is surfaced in run sections via `session_order_note()` as "Nth session of the day — N prior." Runs with sessions_prior = 0 or None show nothing.

---

## Known Claude Failure Modes — This Project

Specific errors made in past sessions that a new instance should avoid:

- **Over-asserting the thermal offset.** Earlier sessions built a 1D resistance model and landed on 15–35°F as a confident estimate. This was walked back. Do not re-assert a large fixed offset without empirical justification.
- **Re-applying offset reasoning to short flat tails.** The insert equilibrates in under a second. Do not flag a 10-second (or any reasonable) flat tail as "too short to close the offset." The methodology is explicit on this. The error is applying correct physics to a timescale where it doesn't matter.
- **Chart glow pass thickening the curve.** An `afterDatasetsDraw` plugin that restroked the curve with a wide low-opacity line made the curve look significantly thicker than intended. Do not use secondary draw passes on the curve line.
- **`globalAlpha` for terpene line opacity not rendering correctly.** Using `ctx.globalAlpha` to lighten the terpene BP lines produced inconsistent results. Use baked hex colors instead.
- **Dressing up the generic cannabis terpene palette as strain-specific knowledge.** The same five or six terpenes appear across nearly all strains. Do not present inferred profiles as if they reflect meaningful strain differentiation.
- **Proposing changes without showing them first.** For chart styling and methodology edits, always propose the change with before/after context before executing. Do not edit and present without the proposal step.
- **Using `push_files` for routine file updates.** `push_files` passes full file content as string literals and has caused silent content loss (stripped charts, lost sections) in past sessions. In Claude Code, use git for all routine commits. `push_files` is acceptable only for temporary files on non-main branches when git checkout is impractical, and never for `index.html`.
- **Using ambiguous abbreviations in branch names.** "fb" reads as "Facebook" in some UIs. Use full strain abbreviations — "fembot", "hive1", "ms23", etc.
- **Narrating instead of proposing.** Presenting an interpretation or plan and then immediately executing is not confirmation — it is narration with extra steps. This applies to all actions: editing files, running the generator, committing, updating methodology or collaboration notes. The correct behavior is always: present the plan, ask for approval or corrections, wait for a response, then act.

- **Pushing a manually written `index.html` instead of the generator output.** When recovering from a failed or incorrect push, the correct fix is always to run the generator and commit its output. Writing `index.html` by hand will silently strip charts, simplify sections, and produce a degraded log. This happened in Session 4. Always run the generator first.
- **Not checking main before rebasing.** In Session 7, a feature branch conflicted with main because Hive #1 Runs 1–2 had already been committed to main separately. Always run `git log origin/main` after fetching to understand what's on main before rebasing.
- **Using UTC date when logging runs.** Cloud environments run in UTC. A session run at 8pm US time is already the next calendar day in UTC. When logging a run, always capture `utc_logged_at = datetime.now(timezone.utc)`, derive local time (subtract 6 hours MDT / 7 hours MST), and confirm with the user: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off." Use the confirmed local date as `run_date`. OC Runs 6 and 7 were incorrectly logged as May 10 when they were run on May 9 local time; Hive #1 Runs 4–5 similarly logged a day late.
- **Force pushes are blocked in this environment.** `git push --force-with-lease` returns HTTP 403. Do not attempt it — it wastes time. Do not amend already-pushed commits either (same problem). When a branch needs correction after being pushed, cut a fresh branch from `origin/main`, apply the fix there, and push that as a new branch.
- **Not reading handoff and methodology at session start.** CLAUDE.md explicitly requires reading `Dabby_Handoff_Notes.md`, `Dabby_Methodology.md`, and `Dabby_Log_Generator.py` before taking any action. This was skipped in Session 15, leading to suggestions made without full context. Read all three files before responding to any request, every session.
- **Re-introducing calibration framing.** The project has been reframed as a session log. Do not use "dialed," "in calibration," status badges, or status columns anywhere in the log or dashboard. `STRAIN_STATUS` no longer contains badge fields.
- **Re-adding a Contents/TOC section.** The Contents section was deliberately removed. The searchable strain browser on the dashboard provides navigation. Do not add a separate Contents or TOC section.
- **PR preview going stale after the first commit.** If the preview comment stops updating on subsequent pushes, check whether the PR has merge conflicts (`mergeable_state: dirty`). A dirty PR blocks the `synchronize` workflow trigger — GitHub can't compute the merge commit. Fix by merging main into the feature branch, resolving conflicts, and pushing. The preview workflow will fire again on the next push.
- **Putting color and design decisions in CLAUDE.md.** Color rules (no greens, minimum hue separation, no miami-vice saturation) belong as validation code in the generator, not as prose in CLAUDE.md. CLAUDE.md is for session-to-session behavioral instructions. When a rule is mechanical and checkable, write it as code.

---

## Unresolved Issues

- **Linalool line rendering lighter than other terpene lines.** The top terpene BP line (Linalool, 388°F) appears visually lighter/thinner than the lines below it in the rendered log. Cause not diagnosed. Noted for future investigation.

---

## What a Good Session Looks Like

- Propose before executing — for any substantive action (file edits, curve changes, methodology updates, log restructuring), state what you are about to do and wait for explicit user confirmation before proceeding. Stating the plan and immediately acting is narrating, not proposing. Stop and wait. Mechanical steps that follow from an already-approved decision — running the generator, committing, pushing, opening PRs — do not need a separate confirmation.
- Show before coding — render chart changes in mockup before touching the generator
- Audit before presenting — check output against the current conversation before presenting files
- Flag epistemic uncertainty explicitly — especially on terpene profile inferences
- Update the handoff at session end when meaningful changes were made
- Use git for all commits and pushes — not push_files
- Fetch and check main before rebasing to avoid surprise conflicts

---

## Changelog

- **May 11, 2026 — Session 19:** Log design overhaul (PR #32). Collapsible sections: all four reference blocks and all run sections now use native `<details>`/`<summary>`. Terpene Reference added as a fourth reference block — 36 entries in Low/Mid/High bands, cool-to-warm band badges, Found In botanical source column, three linked sources; Linalool added; `TERPENE_REFERENCE` is now an 8-tuple. Reference section headers changed from grey to steel blue (#4A7D9A). Per-strain accent colors on profile section headers and What to Try Next headers. `STRAIN_STATUS` extended to 5-tuple adding `slug` field. Sessions_prior_today surfaced in run sections. Dashboard gains Last pill; ref-row removed. OC Runs 1–2 split. `ACCENT_PALETTE` removed; colors auto-assigned via `_resolve_accent_colors()` / `_ACCENT_RESOLVED`. `_hsl_to_hex()` and `accent_header()` helpers added. Band badge colors locked. Rain Fruit Run 2 logged (May 11): 375→385→410→430°F lower-open test — light golden swab, tasty, tail heat last 10s, mild intensity. MBD Runs 1–2 and RF Run 1 date-corrected May 11 → May 10. RF What to Try Next updated with Run 3 direction (420°F endpoint).

- **May 11, 2026 — Session 18:** Generator: `COMPLETED_RUNS` extended to 5-tuple `(strain, run_date, sessions_prior_today, utc_logged_at, waypoints)` — `sessions_prior_today` is int or None; `utc_logged_at` is a UTC datetime or None for pre-existing entries. `what_to_try_next_html()` params renamed `your_read`→`dab_notes`, `my_read`→`ai_analysis`; rendered labels updated to "Dab Notes" and "AI Analysis." Intensity field added to four runs (OC Run 3, MBD Runs 1–2, Rain Fruit Run 1). Section header date corrections: Hive #1 Runs 1–2 moved from May 8 to May 7; Runs 4–5 from May 9 to May 8; OC Runs 6–7 from May 10 to May 9. Sessions_prior_today backfilled for all multi-run days. Session logging protocol updated: sessions_prior_today auto-computed when logging same-day; UTC timestamp confirmation protocol added; casual register guidance added for optional fields; AI Analysis guidance added (read all four artifacts, cross-strain patterns, concrete recommendation, not a summary). Open ideas section added to handoff. CLAUDE.md updated: session must start with `git checkout main && git pull origin main` before reading any files. Rain Fruit current status corrected (Run 1 was already logged).

- **May 11, 2026 — Session 17:** Maple Bacon Donut and Rain Fruit added (both Quasi Farms, Michigan, cold cure, micron unknown, genetics not documented). MBD Run 1 (May 10): darker golden swab, tasty first half, faded second half, milder effect (tolerance confound). MBD Run 2 (May 10): lighter swab, distinct bacon character first half, effects came on noticeably. Swab trending cleaner — repeat same curve on Run 3. Rain Fruit: profile only, no runs. Baseline curve updated to reflect effective operating baseline: 380→390→410→430°F (open raised from 375°F, endpoint locked at 430°F). Methodology construction parameters table updated to match.

- **May 11, 2026 — Session 16:** Reframed project from calibration log to session log. Removed all calibration badges, status columns, and calibration language throughout the generator. Cover subtitle changed to "Session Log." `STRAIN_STATUS` simplified from 5-tuple `(name, anchor, badge_class, badge_text, next_text)` to 4-tuple `(name, anchor, next_text, accent)`. `ACCENT_PALETTE` added — per-strain hex accent colors. Contents/TOC section removed entirely. Dashboard strain table replaced with searchable strain browser (fixed-height scrollable, sticky search, live JS filter, per-strain accent left bars, → Next pills). `what_to_try_next_html()` helper added — each strain now has a What to Try Next block at the bottom of its section with your read, my read, and optional proposed curve. CLAUDE.md, Handoff Notes, and Methodology updated to reflect new framing.

- **May 10, 2026 — Session 15:** Dashboard expanded from 4 to 6 stat cards. Added "most dabs in a day" (currently 5, on May 9 — Hive #1 Runs 4–5, Fembot #3 Runs 1–2, MS23 Run 1) and "unique strains" (currently 6). Cards reorganized into two rows of three: row 1 is volume/frequency (total runs, most dabs in a day, unique strains), row 2 is temperature (avg open, avg endpoint, most time spent). Grid changed from 4-column to 3-column desktop; mobile stays 2-column. `COMPLETED_RUNS` tuples extended to `(strain, run_date, waypoints)` — dates backfilled for all confirmed runs; CAG Run 1 and OC Runs 1–3 remain `None`. Fixed TOC mobile layout — removed `flex-direction:column` override that was stacking pills vertically on narrow screens. New failure mode added: skipping handoff and methodology read at session start.

- **May 10, 2026 — Session 14:** Orange Candy Run 7 logged (May 10, 2026). 430°F steady flat hold, 60s — plain amber swab, pleasant, not as tasty as ramp, harsh in last 20 seconds. Ramp (Run 6) outperforming flat hold at same 430°F endpoint — consistent with Fembot #3 pattern. Next: repeat Run 6 ramp to confirm, or try 420°F flat hold.

- **May 10, 2026 — Session 13:** Orange Candy Run 6 logged (May 10, 2026). 380→390→410→430°F ramp — light golden swab, very nice. First run at 430°F endpoint for OC; clean result. Next: repeat to confirm, or test 350°F open / 460°F curve. Handoff doc cleaned up: fixed stale "fetched from GitHub" reference, backfilled Fembot #3 Run 1 into Session 12 changelog, trimmed Open Questions to project-level items, removed redundant bullets from Decisions Made, tightened Curve Design paragraph, fixed Narrating failure mode list formatting.

- **May 9, 2026 — Session 12:** Fembot #3 Runs 1–2 logged (May 9, 2026). Run 1: ramp to 430°F endpoint — light golden swab, tasty, slight harshness at tail. Run 2: 430°F steady flat hold, 60s — light golden swab, very tasty, great effects, harshness in last third. Two data points at 430°F (Run 1 ramp, Run 2 flat hold) both showing tail harshness — consistent signal that 430°F is slightly above ideal regardless of curve shape. Run 3 pending: 420°F steady flat hold, 60 seconds.

- **May 9, 2026 — Session 11:** Fembot #3 and Mango Starburst #23 added to log. Fembot #3: Riptide (CO), Fuzzy Melon × Rambutan, cold cure, 169–73 micron, sativa-dominant character inferred, terpinolene-forward. Cold nose: subtle garlic note, strong fragrance, less distinct character. No runs. Mango Starburst #23: Terps Over Yields (CO), Starburst 36 #217 × Starburst 36 #1, cold cure, jar 14 of 23, SB36 line (Starburst OG × '97 KC36), sativa-dominant, limonene/terpinolene-forward inferred. Cold nose: diesel note pronounced, sweetness underneath. Run 1 logged (May 9, 2026): baseline curve — very clean swab, pine-forward character (more pinene than lineage inference anticipated), heady effects, no harshness. Leaderboard calculation confirmed correct — new strains excluded from dashboard until first run logged.

- **May 9, 2026 — Session 10:** The Hive #1 Run 5 logged (May 9, 2026). Ramp to 430°F endpoint (380→390→410→430°F). Light golden swab, distinct staged flavors through first two-thirds, harsh at tail (~last 10s), effects quite potent. Harshness is a directional signal that 430°F may be slightly high on the ramp. Run 6 direction: try 420–425°F endpoint.

- **May 9, 2026 — Session 9:** The Hive #1 Run 4 logged (May 9, 2026). Same 430°F steady flat hold as Run 3, extended to 60 seconds. Clean swab, session consistent with Run 3. Two flat-hold data points now complete. Run 5 planned: ramp to 430°F endpoint (380→390→410→430°F) for the curve-shape comparison.

- **May 8, 2026 — Session 8:** The Hive #1 Run 3 redesigned as steady 430°F flat hold (no ramp) — testing whether curve shape meaningfully affects result vs. single sustained setpoint. Swab floor indicator framing added to Decisions Made and Curve Design Key Insights: swab flags overheating reliably, but within the clean range it has too many uncontrolled variables to distinguish curve shapes. Temperature-effect bolus hypothesis added as working model: higher temps → larger bolus → faster peak blood concentration → stronger effect; CBN hypothesis rejected. Methodology and generator updated to reflect Run 3 curve change.

- **May 8, 2026 — Session 7:** Dashboard designed (mockup iterations 1–10 on gh-pages) and implemented in generator (PR #4, merged). Design decisions locked: no gold border, 🥇 medal emoji right of strain name, strain names as green profile links, compact badge-sm in table, Contents section as full section, "Contents" pill removed from Contents TOC. Stats computed at runtime. Hive #1 Run 3 endpoint set to 430°F (revised from 420°F during session). Terpene reference section still pending. New failure mode added: not checking main before rebase. dashboard_mockup.html on gh-pages is now a historical artifact.
- **May 8, 2026 — Session 6:** The Hive #1 Runs 1–2 logged (May 8, 2026). Run 1: light golden swab, nice flavors, heavy indica effect. Run 2: very light swab, really nice, consistent. Run 3 direction: try 430°F endpoint, keep opening and mid-climb unchanged. WW Z Run 1 date confirmed as May 2, 2026. PR preview workflow set up — `.github/workflows/deploy.yml` and `preview.yml` added; each PR now gets a live preview URL; merging to main auto-deploys. Harm reduction open question closed. Infrastructure section rewritten to reflect Claude Code as active environment and git as correct publish path. `push_files` for routine commits deprecated; failure mode added. Dashboard in active mockup iteration — design decisions captured. Visual overhaul of log flagged as future agenda item. Swab protocol clarified. Blueberry 36 phenotypes confirmed as separate log entries.
- **May 7, 2026 — Session 5:** The Hive #1 added (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron). Nose noted (very fragrant, spice consistent with caryophyllene). WW Z and CAG producer corrected to Quasi Farms (Michigan) — lost in a prior botched push recovery. All MD files pushed to repo to enable full context in mobile/cloud sessions. Prior decision against pushing handoff reversed. Output path in generator fixed from cloud path to `index.html`. Claude Code confirmed as active environment.
- **May 7, 2026 — Session 4:** OC Run 5 logged (May 6, 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint; darker swab; harsh tail; notably stronger effect; user's hypothesis logged; curve to repeat as Run 6). OC strain status updated. Infrastructure section: critical note added on always pushing generator output, never hand-written HTML. New failure mode added: pushing manually written index.html that stripped charts. Decisions Made: user's effect hypothesis noted as logged-not-confirmed. Harm reduction section: 440°F vs 460°F open question flagged.
- **May 6, 2026 — Session 3:** OC Run 4 status updated (run twice May 5, light golden swabs, close to dialed). Curve design section corrected — flat tail rationale clarified, offset-closure framing removed as it overstates the timescale concern. Session logging protocol added. New failure mode added: re-applying offset reasoning to short flat tails. Opening setpoint exploration noted as active direction for OC.
- **May 6, 2026 — Session 2:** Producer updated to Quasi Farms (Michigan) for WW Z and Caramel Apple Gelato in generator and log. Enhancements list: nose notes marked resolved (already on strain profiles); confidence rating (4) and load consistency note (5) removed at user request. New failure modes added: pushing handoff to repo; passing placeholder content to push_files.
- **May 6, 2026 — Session 1:** Initial structured handoff created. Thermal model revised (offset estimate walked back). Methodology doc updated. Chart styling overhauled (DM Mono, vivid green curve, steel blue terpene lines, THC pill label). Generator moved from project files to GitHub repo. Known failure modes, unresolved issues, and behavioral notes added.
