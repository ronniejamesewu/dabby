# Dabby — Conversation Handoff Notes
## Last updated: May 8, 2026 — Session 7

This document provides full context for a new AI assistant picking up this project. Read alongside Dabby_Methodology.md and the live log fetched from GitHub.

---

## Project Goal

Empirical temperature curve calibration for live rosin sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig." All material is hash rosin (ice water extracted, solventless) using cold start technique. The log documents strain-specific calibration runs, swab results, and curve adjustments. The methodology document captures the physical reasoning behind curve design decisions.

---

## Infrastructure

**Live log:** https://ronniejamesewu.github.io/dabby
**Repo:** ronniejamesewu/dabby (branch: main)
**Files in repo:** `index.html` (the rendered log), `Dabby_Log_Generator.py` (Python generator), `CLAUDE.md` (session instructions), `Dabby_Handoff_Notes.md` (this file), `Dabby_Methodology.md` (thermal model and calibration reasoning), `.github/workflows/deploy.yml` (auto-deploys main to gh-pages on push), `.github/workflows/preview.yml` (posts preview URL on every PR, cleans up on close)

**Environment:** Claude Code. Files are in the repo working directory. Read them directly — do not fetch from raw.githubusercontent.com or copy files to a separate path.

**Publishing workflow:**
1. Edit `Dabby_Log_Generator.py`
2. Run `python3 Dabby_Log_Generator.py` to produce `index.html`
3. Commit both files to a feature branch
4. Push the branch and open a PR
5. GitHub automatically posts a preview URL as a PR comment
6. User reviews the preview, merges the PR
7. `deploy.yml` automatically publishes to gh-pages — live site updates

**CRITICAL — never use `push_files` for `index.html` or routine commits.** `push_files` passes full file content as string literals and has caused silent content loss in past sessions (stripped charts, lost sections). Git is the correct path for all routine work. `push_files` is acceptable only for temporary files on non-main branches (e.g., mockups on gh-pages) when git checkout of that branch is impractical — and only when the file is not `index.html`.

**CRITICAL — push index.html correctly:** The `index.html` committed to the repo must be the literal output of running `python3 Dabby_Log_Generator.py`. Never write `index.html` content manually or from memory. The correct sequence is always: edit generator → run generator → commit both files.

**Generator notes:** Python, not Node.js. Produces HTML. Charts rendered via Chart.js from CDN — requires internet to render. Each curve section has a chart auto-generated from the same waypoint data that feeds the waypoint table. Chart IDs are auto-incremented. The `curve_chart_html()` helper accepts a waypoints list and returns self-contained HTML+JS. Adding a new strain requires: data constants, TOC entries, STRAIN_STATUS entry, COMPLETED_RUNS entries, and section build code. Footer auto-timestamps on each run.

---

## Session Logging Protocol

When the user reports a completed run, parse the natural language description into log fields and confirm the interpretation before touching the generator. If the date is missing, ask. If swab result is missing, ask — do not log without it.

Runs are logged with exact date (not month only) when known.

**Swab protocol clarification:** A swab is always taken — it is the standard insert-cleaning step after every session, not an optional measurement. "Not recorded" means the color wasn't noted, not that no swab was taken. Always ask for swab color if not reported.

---

## Thermal Model — Current Understanding

This was substantially revised. The old estimate of a 15–35°F titanium-to-insert offset has been walked back. Current understanding:

- The quartz insert wall is ~1mm thick. At ~1.4 W/m·K conductivity the bulk thermal time constant is under one second — the insert equilibrates internally almost instantly.
- Physical contact points between titanium and quartz transfer heat efficiently. The air gap is not the dominant resistance when contact geometry is intact.
- The offset is probably small under most operating conditions. Dominant remaining uncertainties are vaporization cooling (phase change draws heat locally during active vaporization) and dynamic lag during steep ascent (titanium is always ahead of insert during fast climbs).
- Setpoints are reasonable proxies for material contact temperature.

**Do not rebuild the 1D thermal resistance model.** A substantial amount of work went into building and then partially dismantling it. The interface efficiency parameter (η) concept was developed but abandoned — the two dominant parameters were partially redundant and the underlying geometry is unknowable. The swab is the calibration ground truth.

**Sapphire advantage** (for when sapphire insert is acquired): not primarily closing a large interface resistance. Two mechanisms: (1) higher volumetric heat capacity — absorbs cold material contact perturbation more stably at session open; (2) better surface temperature uniformity during vaporization — ~20x higher bulk conductivity replenishes heat faster when local vaporization creates cold spots. Reddit consensus of 10–20°F lower setpoints for equivalent results is consistent with this model. Sapphire requires fresh empirical calibration from scratch — do not scale quartz curves.

---

## Curve Design — Key Insights

**Ascent rate and offset:** During steep ascent, titanium is ahead of insert temperature; during flat or slow phases the system approaches equilibrium. However, because the insert equilibrates in under a second, even a short flat tail (10 seconds) is sufficient for the insert to reach the setpoint. Do not flag short flat tails as inadequate for offset closure — the equilibration time is too fast for this to be a meaningful concern at any reasonable tail length.

The rationale for a flat tail at endpoint is simply spending time at the target temperature, not closing a significant offset. Steeper mid-climbs move through terpene zones faster. The shape of the climb matters for when vaporization begins, not for offset concerns.

**Curve shape vs. single setpoint:** Whether a multi-stage ramp provides meaningfully better results than a single sustained setpoint is an open empirical question. The Hive #1 Run 3 (steady 430°F flat hold) is the first direct test of this. The main theoretical justification for a ramp is staging volatile terpene fractions — lower opening temps may preserve more terpene vapor before degradation. The counterargument is that the window between terpene vaporization and degradation is narrow enough that the ramp may not accomplish much in practice. Swab is not a sensitive enough signal to distinguish between curve shapes within the normal operating range — subjective session character is the primary readout for this experiment.

**Temperature and effect strength:** Higher temperatures vaporize a larger fraction of material in a shorter window, producing a larger bolus inhaled and a faster peak blood concentration. This is the most parsimonious explanation for the stronger effects observed at higher endpoints (OC Run 5, 460°F). CBN hypothesis rejected: CBN has ~1/10th CB1 binding affinity of THC, in-session CBN formation is limited by oxygen availability, and a higher CBN fraction would dilute rather than amplify the effect. Rate of delivery matters, not just total dose — the same material at lower temps over a longer curve could deliver similar total cannabinoids but with a slower, smoother absorption profile.

**Swab as floor indicator:** Swab color is a floor indicator within the normal operating range, not a fine-grained calibration metric. Dark or burnt residue (amber-toward-brown or darker) is a reliable signal to reduce temperature. Within the light-golden-to-amber range, swab has too many uncontrolled variables — load size, material starting color, oxidation state, swab timing, pressure — to reliably distinguish between curve shapes or small endpoint differences. Do not over-interpret swab color within the clean range.

**Baseline philosophy:** Single baseline curve for all hash rosin with cold start. Strain-specific calibration happens empirically via swab results, not terpene-profile reasoning. Do not design different starting curves based on strain name, consistency, or inferred terpene profile without empirical justification.

**Mode:** Custom Ascent preferred over Valley. Valley's initial dip is redundant with cold start — material is already at its lowest temperature at session open.

**Opening setpoint exploration:** Lower opening setpoints (below the baseline 375°F) are under active exploration for OC. Run 5 tested 350°F open — see Current Strain Status.

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

**WW Z** (Quasi Farms, Michigan) — Dialed. Run 1 complete (May 2, 2026). Profile locked. Baseline curve confirmed appropriate.

**Caramel Apple Gelato** (Quasi Farms, Michigan) — In calibration. Run 1 too hot (450°F endpoint, swab amber toward brown). Run 2 pending: endpoint reduced to 430°F, hold shortened to 55 seconds.

**Orange Candy** (Nikka T, 90 micron full melt) — In calibration. Runs 1–2 too flat. Run 3 redesigned with steeper mid-climb and flatter tail — clean swab, strong result, wispy opening draws. Run 4 (380°F open, 440°F endpoint) run twice on May 5, 2026 — both light golden swabs, not noticeably different from Run 3. Run 5 (May 6, 2026): 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint. Darker swab, last portion harsh. Effect notably stronger than prior runs — user's hypothesis is that higher temperature produced stronger effect; logged as one data point, not a confirmed finding, confounders acknowledged. Curve to be repeated as Run 6 before drawing conclusions.

**The Hive #1** (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron) — In calibration. Runs 1–2 complete (both May 8, 2026): 380°F open curve (380→390→410→440°F, 65s hold). Run 1: light golden swab, nice flavors, heavy indica effect. Run 2: very light swab, really nice, consistent. Both runs clean — endpoint may be higher than needed. Run 3 pending: steady 430°F flat hold (no ramp) — testing whether curve shape meaningfully affects result vs. a single sustained setpoint.

**Blueberry 36** — Three jars in collection, phenotypes #1, #2, #4 from a trusted grower's pheno hunt. Producer-specific designation, not a documented cultivar. Base genetics: DJ Short's Blueberry — myrcene dominant, caryophyllene and pinene as secondaries. No curves designed. Recommended approach: nose all three jars before first sessions to establish relative comparison across phenotypes, then start all three from baseline curve and log each separately. Each phenotype is logged separately. Meaningful differences will emerge from session character and swab, not from nose or jar appearance.

---

## Open Questions

- The Hive #1 Run 3 pending — steady 430°F flat hold (no ramp). Experiment: does curve shape affect the result, or does a single sustained setpoint achieve similar outcome?
- The Hive #1 Run 4 (or Run 3 follow-up) — repeat the Run 1–2 ramp (380→390→410°F) but with 430°F endpoint instead of 440°F. This is a separate variable from the steady-hold experiment and should also be run before drawing conclusions.
- Blueberry 36 first sessions not yet run.
- Orange Candy Run 6 pending — repeat of Run 5 curve (350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint) to see if results replicate before drawing conclusions.
- Caramel Apple Gelato Run 2 not yet completed.
- Sapphire insert not yet acquired. When acquired, requires fresh calibration from scratch — do not scale from quartz curves.
- Whether fresh press consistency justifies a different baseline curve remains an open question. Not settled.
- **Visual overhaul of the log** — user flagged the forest green styling as feeling heavyweight. Raise this as an agenda item at start of a future session.
- **Session date backfill** — most pre-Session 6 run entries are dated to month only. WW Z Run 1 is confirmed May 2, 2026. Other entries (CAG Run 1, OC Runs 1–5) still need exact dates if the user can recall them.

**Log enhancements pending:**
- **Terpene boiling point reference section** — standalone table in the log. Not yet implemented.

---

## Dashboard — Implemented

The dashboard is live in the generator and deployed. It sits between the cover and the Contents section.

**Structure:**
- Four stat cards computed at generator runtime: total runs / avg open / avg endpoint / most time spent (linear interpolation across all runs, 5°F buckets)
- Strain table sorted by run count desc; strains with zero runs excluded
- Leader row (most runs) gets 🥇 medal emoji to the right of the strain name
- Strain names are green links (`var(--green-dark)`, underline on hover) to their profile section

**Design decisions locked:**
- No gold border or gold stars — dropped after mockup iteration
- Medal emoji placed to the right of strain name, column left-justified
- Compact `.badge-sm` used in dashboard table (smaller than global `.badge` used in section headers)
- Contents section uses full `.section` treatment with `section_header()` — same as every other section in the log
- "Contents" pill removed from the Contents section (self-referential)

**Implementation notes:**
- `COMPLETED_RUNS` list drives all stat computation — add an entry here whenever a run is logged
- `STRAIN_STATUS` drives the table rows — add entry with `(name, profile_anchor, badge_class, badge_text, next_text)`
- `FIRST_RUN_DATE` is hardcoded to `date(2026, 5, 2)` — do not change unless the first-ever run date changes
- `dashboard_mockup.html` on gh-pages branch is a historical design artifact, now superseded by the generator

---

## Decisions Made — Do Not Re-Litigate

- 1D thermal resistance model is a dead end. Do not rebuild.
- The 15–35°F offset estimate is retired. Current position: offset probably small.
- Swab is the calibration ground truth in the sense that it flags overheating — dark/burnt residue means too hot. Within the light-golden-to-amber range, swab has too many uncontrolled variables to distinguish between curve shapes or small endpoint differences. Do not over-interpret clean swabs as fine-grained efficiency data.
- Quartz-to-sapphire curve scaling does not work.
- Valley mode is not appropriate for cold start sessions.
- Consistency type alone does not justify a different baseline curve.
- All MD files (`CLAUDE.md`, `Dabby_Handoff_Notes.md`, `Dabby_Methodology.md`) are in the repo. Push them when relevant changes are made.
- The user's hypothesis that higher temperature (460°F endpoint) produced a notably stronger effect in OC Run 5 is logged as stated — one data point, not a confirmed finding. Do not dismiss it or over-assert it.
- Claude Code is the active environment. The old cloud/API session protocol (fetch from raw.githubusercontent.com, push_files for publishing) is retired.
- PR preview workflow is established and active. Changes go to a feature branch → PR → preview URL → merge → auto-deploy.
- `push_files` is not to be used for `index.html` or routine commits. Git is the correct path.
- Blueberry 36 phenotypes are logged as separate strains, not grouped.
- Dashboard is implemented. Do not redesign from scratch — iterate from the current generator code.

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
- **Pushing a manually written `index.html` instead of the generator output.** When recovering from a failed or incorrect push, the correct fix is always to run the generator and commit its output. Writing `index.html` by hand will silently strip charts, simplify sections, and produce a degraded log. This happened in Session 4. Always run the generator first.
- **Not checking main before rebasing.** In Session 7, a feature branch conflicted with main because Hive #1 Runs 1–2 had already been committed to main separately. Always run `git log origin/main` after fetching to understand what's on main before rebasing.

---

## Unresolved Issues

- **Linalool line rendering lighter than other terpene lines.** The top terpene BP line (Linalool, 388°F) appears visually lighter/thinner than the lines below it in the rendered log. Cause not diagnosed. Noted for future investigation.

---

## What a Good Session Looks Like

- Propose before executing — especially for edits to methodology, curve data, or chart styling
- Show before coding — render chart changes in mockup before touching the generator
- Audit before presenting — check output against the current conversation before presenting files
- Flag epistemic uncertainty explicitly — especially on terpene profile inferences
- Update the handoff at session end when meaningful changes were made
- Use git for all commits and pushes — not push_files
- Fetch and check main before rebasing to avoid surprise conflicts

---

## Changelog

- **May 8, 2026 — Session 8:** The Hive #1 Run 3 redesigned as steady 430°F flat hold (no ramp) — testing whether curve shape meaningfully affects result vs. single sustained setpoint. Swab floor indicator framing added to Decisions Made and Curve Design Key Insights: swab flags overheating reliably, but within the clean range it has too many uncontrolled variables to distinguish curve shapes. Temperature-effect bolus hypothesis added as working model: higher temps → larger bolus → faster peak blood concentration → stronger effect; CBN hypothesis rejected. Methodology and generator updated to reflect Run 3 curve change.

- **May 8, 2026 — Session 7:** Dashboard designed (mockup iterations 1–10 on gh-pages) and implemented in generator (PR #4, merged). Design decisions locked: no gold border, 🥇 medal emoji right of strain name, strain names as green profile links, compact badge-sm in table, Contents section as full section, "Contents" pill removed from Contents TOC. Stats computed at runtime. Hive #1 Run 3 endpoint set to 430°F (revised from 420°F during session). Terpene reference section still pending. New failure mode added: not checking main before rebase. dashboard_mockup.html on gh-pages is now a historical artifact.
- **May 8, 2026 — Session 6:** The Hive #1 Runs 1–2 logged (May 8, 2026). Run 1: light golden swab, nice flavors, heavy indica effect. Run 2: very light swab, really nice, consistent. Run 3 direction: try 430°F endpoint, keep opening and mid-climb unchanged. WW Z Run 1 date confirmed as May 2, 2026. PR preview workflow set up — `.github/workflows/deploy.yml` and `preview.yml` added; each PR now gets a live preview URL; merging to main auto-deploys. Harm reduction open question closed. Infrastructure section rewritten to reflect Claude Code as active environment and git as correct publish path. `push_files` for routine commits deprecated; failure mode added. Dashboard in active mockup iteration — design decisions captured. Visual overhaul of log flagged as future agenda item. Swab protocol clarified. Blueberry 36 phenotypes confirmed as separate log entries.
- **May 7, 2026 — Session 5:** The Hive #1 added (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron). Nose noted (very fragrant, spice consistent with caryophyllene). WW Z and CAG producer corrected to Quasi Farms (Michigan) — lost in a prior botched push recovery. All MD files pushed to repo to enable full context in mobile/cloud sessions. Prior decision against pushing handoff reversed. Output path in generator fixed from cloud path to `index.html`. Claude Code confirmed as active environment.
- **May 7, 2026 — Session 4:** OC Run 5 logged (May 6, 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint; darker swab; harsh tail; notably stronger effect; user's hypothesis logged; curve to repeat as Run 6). OC strain status updated. Infrastructure section: critical note added on always pushing generator output, never hand-written HTML. New failure mode added: pushing manually written index.html that stripped charts. Decisions Made: user's effect hypothesis noted as logged-not-confirmed. Harm reduction section: 440°F vs 460°F open question flagged.
- **May 6, 2026 — Session 3:** OC Run 4 status updated (run twice May 5, light golden swabs, close to dialed). Curve design section corrected — flat tail rationale clarified, offset-closure framing removed as it overstates the timescale concern. Session logging protocol added. New failure mode added: re-applying offset reasoning to short flat tails. Opening setpoint exploration noted as active direction for OC.
- **May 6, 2026 — Session 2:** Producer updated to Quasi Farms (Michigan) for WW Z and Caramel Apple Gelato in generator and log. Enhancements list: nose notes marked resolved (already on strain profiles); confidence rating (4) and load consistency note (5) removed at user request. New failure modes added: pushing handoff to repo; passing placeholder content to push_files.
- **May 6, 2026 — Session 1:** Initial structured handoff created. Thermal model revised (offset estimate walked back). Methodology doc updated. Chart styling overhauled (DM Mono, vivid green curve, steel blue terpene lines, THC pill label). Generator moved from project files to GitHub repo. Known failure modes, unresolved issues, and behavioral notes added.
