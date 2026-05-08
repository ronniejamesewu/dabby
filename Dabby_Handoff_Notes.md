# Dabby — Conversation Handoff Notes
## Last updated: May 8, 2026 — Session 6

This document provides full context for a new AI assistant picking up this project. Read alongside Dabby_Methodology.md and the live log fetched from GitHub.

---

## Project Goal

Empirical temperature curve calibration for live rosin sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig." All material is hash rosin (ice water extracted, solventless) using cold start technique. The log documents strain-specific calibration runs, swab results, and curve adjustments. The methodology document captures the physical reasoning behind curve design decisions.

---

## Infrastructure

**Live log:** https://ronniejamesewu.github.io/dabby
**Repo:** ronniejamesewu/dabby (branch: main)
**Files in repo:** `index.html` (the rendered log), `Dabby_Log_Generator.py` (Python generator), `CLAUDE.md` (session instructions), `Dabby_Handoff_Notes.md` (this file), `Dabby_Methodology.md` (thermal model and calibration reasoning)

**Session start protocol:** Fetch `index.html` and `Dabby_Log_Generator.py` from raw.githubusercontent.com. Read `Dabby_Methodology.md` from project files. Copy generator to `/home/claude/Dabby_Log_Generator.py` before editing.

**Publishing:** After regenerating the log, push both `index.html` and `Dabby_Log_Generator.py` to the repo using `push_files`. Never use `create_or_update_file` — it requires SHA lookup. `push_files` does not.

**CRITICAL — push index.html correctly:** The `index.html` pushed to the repo must be the literal output of running `python3 Dabby_Log_Generator.py`. Never write `index.html` content manually or from memory — this will silently strip charts and other content. The correct sequence is always: edit generator → run generator → push both output files. Do not attempt to recover from a failed push by writing HTML manually.

**Generator notes:** Python, not Node.js. Produces HTML. Charts rendered via Chart.js from CDN — requires internet to render. Each curve section has a chart auto-generated from the same waypoint data that feeds the waypoint table. Chart IDs are auto-incremented. The `curve_chart_html()` helper accepts a waypoints list and returns self-contained HTML+JS. Adding a new strain requires: data constants, TOC entries, and section build code. Footer auto-timestamps on each run.

**Environment note:** The user has raised the question of whether Claude Code would be a better environment for this project, given that every log update requires editing the generator and pushing both files. The main friction in the current setup is the push step — passing full file content as string literals in tool calls is error-prone at scale. Claude Code would allow direct file editing and native git operations. This is a considered option, not yet a decision.

---

## Session Logging Protocol

When the user reports a completed run, parse the natural language description into log fields and confirm the interpretation before touching the generator. If the date is missing, ask. If swab result is missing, ask — or note "not recorded" if the user confirms none was taken. Do not prompt with a structured form unless the user gives no information at all.

Runs are logged with exact date (not month only) when known.

**Swab protocol clarification:** A swab is always taken — it is the standard insert-cleaning step after every session, not an optional measurement. "Not recorded" means the color wasn't noted, not that no swab was taken. Always ask for swab color if not reported; do not log "not recorded" without confirming.

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

---

## Harm Reduction Context

Established from ACS Omega 2017 peer-reviewed study: benzene and methacrolein are documented degradation products of terpene thermolysis. Benzene formation begins in small amounts around 400°F and increases significantly with temperature. Studies showing alarming toxicant levels used 500–550°C (932–1022°F) — far above typical practice. At conservative setpoints (375–440°F) benzene formation is at the low end of the documented range. Benzene is a Group 1 carcinogen (IARC) linked to aplastic anemia and acute myeloid leukemia. Lower temperatures are meaningfully safer as well as more flavorful. This is a genuine harm reduction argument, not just a flavor argument.

**Open harm reduction question:** The user wants a future discussion on the specific harm reduction implications of 440°F vs 460°F endpoints — i.e., whether the difference is meaningful given what the ACS Omega study shows about benzene formation in that range. Flag this at the start of the next session if not yet addressed.

---

## Current Strain Status

**WW Z** (Quasi Farms, Michigan) — Dialed. Run 1 complete. Profile locked. Baseline curve confirmed appropriate.

**Caramel Apple Gelato** (Quasi Farms, Michigan) — In calibration. Run 1 too hot (450°F endpoint, swab amber toward brown). Run 2 pending: endpoint reduced to 430°F, hold shortened to 55 seconds.

**Orange Candy** (Nikka T, 90 micron full melt) — In calibration. Runs 1–2 too flat. Run 3 redesigned with steeper mid-climb and flatter tail — clean swab, strong result, wispy opening draws. Run 4 (380°F open, 440°F endpoint) run twice on May 5, 2026 — both light golden swabs, not noticeably different from Run 3. Run 5 (May 6, 2026): 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint. Darker swab, last portion harsh. Effect notably stronger than prior runs — user's hypothesis is that higher temperature produced stronger effect; logged as one data point, not a confirmed finding, confounders acknowledged. Curve to be repeated as Run 6 before drawing conclusions.

**The Hive #1** (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron) — In calibration. Run 1 complete (May 8, 2026): 380°F open curve (380→390→410→440°F, 65s hold), light golden swab, nice flavors on the way up, heavy indica effect. Repeat as Run 2 to confirm before locking.

**Blueberry 36** — Three jars in collection, phenotypes #1, #2, #4 from a trusted grower's pheno hunt. Producer-specific designation, not a documented cultivar. Base genetics: DJ Short's Blueberry — myrcene dominant, caryophyllene and pinene as secondaries. No curves designed. Recommended approach: nose all three jars before first sessions to establish relative comparison across phenotypes, then start all three from baseline curve and log each separately. Meaningful differences will emerge from session character and swab, not from nose or jar appearance.

---

## Open Questions

- The Hive #1 Run 2 pending — repeat Run 1 curve to confirm before locking.
- Blueberry 36 first sessions not yet run.
- Orange Candy Run 6 pending — repeat of Run 5 curve (350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint) to see if results replicate before drawing conclusions.
- Caramel Apple Gelato Run 2 not yet completed.
- Sapphire insert not yet acquired. When acquired, requires fresh calibration from scratch — do not scale from quartz curves.
- Whether fresh press consistency justifies a different baseline curve remains an open question. Not settled.
- Harm reduction question: what do the documented benzene formation data say specifically about the 440°F vs 460°F range? User wants this discussed in a future session.

**Potential log enhancements — not yet implemented, user interested:**
- **Session date precision.** Existing run entries dated to month only. New runs should be logged with exact date. Full backfill of existing entries not yet done.
- **Nose notes field.** ~~Resolved~~ — Nose is already a row on each strain profile. No per-run nose field needed.
- **Summary dashboard.** A table at the top of the log showing all strains, current status, and current curve endpoint at a glance.
- **Terpene boiling point reference section.** A clean standalone table in the log with all terpenes, BPs, and character notes — readable without hovering over chart annotations.

---

## Decisions Made — Do Not Re-Litigate

- 1D thermal resistance model is a dead end. Do not rebuild.
- The 15–35°F offset estimate is retired. Current position: offset probably small.
- Swab is the calibration ground truth, not terpene profile reasoning.
- Quartz-to-sapphire curve scaling does not work.
- Valley mode is not appropriate for cold start sessions.
- Consistency type alone does not justify a different baseline curve.
- All MD files (`CLAUDE.md`, `Dabby_Handoff_Notes.md`, `Dabby_Methodology.md`) are now in the repo. This was reversed in Session 5 to enable full context in mobile and cloud sessions. Push all five files when relevant changes are made.
- The user's hypothesis that higher temperature (460°F endpoint) produced a notably stronger effect in OC Run 5 is logged as stated — one data point, not a confirmed finding. Do not dismiss it or over-assert it.

---

## Known Claude Failure Modes — This Project

Specific errors made in past sessions that a new instance should avoid:

- **Over-asserting the thermal offset.** Earlier sessions built a 1D resistance model and landed on 15–35°F as a confident estimate. This was walked back. Do not re-assert a large fixed offset without empirical justification.
- **Re-applying offset reasoning to short flat tails.** The insert equilibrates in under a second. Do not flag a 10-second (or any reasonable) flat tail as "too short to close the offset." The methodology is explicit on this. The error is applying correct physics to a timescale where it doesn't matter.
- **Chart glow pass thickening the curve.** An `afterDatasetsDraw` plugin that restroked the curve with a wide low-opacity line made the curve look significantly thicker than intended. Do not use secondary draw passes on the curve line.
- **`globalAlpha` for terpene line opacity not rendering correctly.** Using `ctx.globalAlpha` to lighten the terpene BP lines produced inconsistent results. Use baked hex colors instead.
- **Dressing up the generic cannabis terpene palette as strain-specific knowledge.** The same five or six terpenes appear across nearly all strains. Do not present inferred profiles as if they reflect meaningful strain differentiation.
- **Proposing changes without showing them first.** For chart styling and methodology edits, always propose the change with before/after context before executing. Do not edit and present without the proposal step.
- **Pushing the handoff to the repo — no longer a failure mode.** This was reversed in Session 5. All MD files are now tracked in the repo. Push them when relevant changes are made.
- **Passing placeholder content to `push_files`.** The `push_files` tool requires full file content passed directly as string parameters in the tool call. Do not use placeholder strings, shell variable references, or stub content. Read the file content and pass it literally.
- **Pushing a manually written `index.html` instead of the generator output.** When recovering from a failed or incorrect push, the correct fix is always to run the generator and push its output. Writing `index.html` content by hand will silently strip charts, simplify sections, and produce a degraded log. This happened in Session 4. Always run the generator first.

---

## Unresolved Issues

- **Linalool line rendering lighter than other terpene lines.** The top terpene BP line (Linalool, 388°F) appears visually lighter/thinner than the lines below it in the rendered log. Cause not diagnosed. Noted for future investigation.

---

## What a Good Session Looks Like

- Propose before executing — especially for edits to methodology, curve data, or chart styling
- Show before coding — render chart changes in the widget before touching the generator
- Audit before presenting — check output against the current conversation before presenting files
- Flag epistemic uncertainty explicitly — especially on terpene profile inferences
- Update the handoff at session end when meaningful changes were made

---

## Changelog

- **May 8, 2026 — Session 6:** The Hive #1 Run 1 logged (May 8, 2026 — 380°F open curve, light golden swab, nice flavors, heavy indica effect; repeat as Run 2 before locking). Strain status updated from Pending to In Calibration. Swab protocol clarified in Session Logging Protocol: swab is always taken as part of insert cleaning; "not recorded" means color not noted, not that no swab was taken.
- **May 6, 2026 — Session 1:** Initial structured handoff created. Thermal model revised (offset estimate walked back). Methodology doc updated. Chart styling overhauled (DM Mono, vivid green curve, steel blue terpene lines, THC pill label). Generator moved from project files to GitHub repo. Known failure modes, unresolved issues, and behavioral notes added.
- **May 6, 2026 — Session 2:** Producer updated to Quasi Farms (Michigan) for WW Z and Caramel Apple Gelato in generator and log. Enhancements list: nose notes marked resolved (already on strain profiles); confidence rating (4) and load consistency note (5) removed at user request. New failure modes added: pushing handoff to repo; passing placeholder content to push_files.
- **May 6, 2026 — Session 3:** OC Run 4 status updated (run twice May 5, light golden swabs, close to dialed). Curve design section corrected — flat tail rationale clarified, offset-closure framing removed as it overstates the timescale concern. Session logging protocol added. New failure mode added: re-applying offset reasoning to short flat tails. Opening setpoint exploration noted as active direction for OC.
- **May 7, 2026 — Session 5:** The Hive #1 added (Myxed Up, Honey Banana × Papaya, Bloom Seed Co, cold cure, 159–73 micron). Nose noted (very fragrant, spice consistent with caryophyllene). WW Z and CAG producer corrected to Quasi Farms (Michigan) — lost in a prior botched push recovery. All MD files pushed to repo to enable full context in mobile/cloud sessions. Prior decision against pushing handoff reversed. Output path in generator fixed from cloud path to `index.html`. Claude Code confirmed as active environment.
- **May 7, 2026 — Session 4:** OC Run 5 logged (May 6, 350°F open, 410°F at 30s, 440°F at 50s, 460°F endpoint; darker swab; harsh tail; notably stronger effect; user's hypothesis logged; curve to repeat as Run 6). OC strain status updated. Open Questions updated — stale OC curve candidate removed, Run 6 and 440°F vs 460°F harm reduction question added. Infrastructure section: critical note added on always pushing generator output, never hand-written HTML. Environment note added re Claude Code as a considered option. New failure mode added: pushing manually written index.html that stripped charts. Decisions Made: user's effect hypothesis noted as logged-not-confirmed. Harm reduction section: 440°F vs 460°F open question flagged.
