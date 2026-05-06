# Dabby — Conversation Handoff Notes
## Last updated: May 6, 2026 — Session 2

This document provides full context for a new AI assistant picking up this project. Read alongside Dabby_Methodology.md and the live log fetched from GitHub.

---

## Project Goal

Empirical temperature curve calibration for live rosin sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig." All material is hash rosin (ice water extracted, solventless) using cold start technique. The log documents strain-specific calibration runs, swab results, and curve adjustments. The methodology document captures the physical reasoning behind curve design decisions.

---

## Infrastructure

**Live log:** https://ronniejamesewu.github.io/dabby
**Repo:** ronniejamesewu/dabby (branch: main)
**Files in repo:** `index.html` (the rendered log), `Dabby_Log_Generator.py` (Python generator)
**Project files:** `Dabby_Methodology.md` (thermal model and calibration reasoning), `Dabby_Handoff_Notes.md` (this file)

**Session start protocol:** Fetch `index.html` and `Dabby_Log_Generator.py` from raw.githubusercontent.com. Read `Dabby_Methodology.md` from project files. Copy generator to `/home/claude/Dabby_Log_Generator.py` before editing.

**Publishing:** After regenerating the log, push both `index.html` and `Dabby_Log_Generator.py` to the repo using `push_files`. Never use `create_or_update_file` — it requires SHA lookup. `push_files` does not.

**Generator notes:** Python, not Node.js. Produces HTML. Charts rendered via Chart.js from CDN — requires internet to render. Each curve section has a chart auto-generated from the same waypoint data that feeds the waypoint table. Chart IDs are auto-incremented. The `curve_chart_html()` helper accepts a waypoints list and returns self-contained HTML+JS. Adding a new strain requires: data constants, TOC entries, and section build code. Footer auto-timestamps on each run.

---

## Thermal Model — Current Understanding

This was substantially revised. The old estimate of a 15–35°F titanium-to-insert offset has been walked back. Current understanding:

- The quartz insert wall is ~1mm thick. At ~1.4 W/m·K conductivity the bulk thermal time constant is under one second — the insert equilibrates internally almost instantly.
- Physical contact points between titanium and quartz transfer heat efficiently. The air gap is not the dominant resistance when contact geometry is intact.
- The offset is probably small under most operating conditions. Dominant remaining uncertainties are vaporization cooling (phase change draws heat locally during active vaporization) and dynamic lag during steep ascent (titanium is always ahead of insert during fast climbs).
- At flat or slowly-ascending phases the system approaches equilibrium and the offset approaches its minimum.
- Setpoints are reasonable proxies for material contact temperature.

**Do not rebuild the 1D thermal resistance model.** A substantial amount of work went into building and then partially dismantling it. The interface efficiency parameter (η) concept was developed but abandoned — the two dominant parameters were partially redundant and the underlying geometry is unknowable. The swab is the calibration ground truth.

**Sapphire advantage** (for when sapphire insert is acquired): not primarily closing a large interface resistance. Two mechanisms: (1) higher volumetric heat capacity — absorbs cold material contact perturbation more stably at session open; (2) better surface temperature uniformity during vaporization — ~20x higher bulk conductivity replenishes heat faster when local vaporization creates cold spots. Reddit consensus of 10–20°F lower setpoints for equivalent results is consistent with this model. Sapphire requires fresh empirical calibration from scratch — do not scale quartz curves.

---

## Curve Design — Key Insights

**Ascent rate and offset:** The slower the ascent rate, the smaller the offset between titanium setpoint and material contact temperature. Flat phases deliver the most accurate temperature to the material relative to setpoint. Steep mid-session climbs move the titanium through terpene zones faster than the material actually experiences them — the material catches up during subsequent flat or slower phases. A slowly-arrived-at lower endpoint delivers more heat to the material than a steeply-arrived-at higher endpoint, because the flat tail allows offset to close. This drove the Orange Candy Run 3 redesign: steeper mid-climb, flatter tail, lower endpoint.

**Baseline philosophy:** Single baseline curve for all hash rosin with cold start. Strain-specific calibration happens empirically via swab results, not terpene-profile reasoning. Do not design different starting curves based on strain name, consistency, or inferred terpene profile without empirical justification.

**Mode:** Custom Ascent preferred over Valley. Valley's initial dip is redundant with cold start — material is already at its lowest temperature at session open.

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

---

## Current Strain Status

**WW Z** (Quasi Farms, Michigan) — Dialed. Run 1 complete. Profile locked. Baseline curve confirmed appropriate.

**Caramel Apple Gelato** (Quasi Farms, Michigan) — In calibration. Run 1 too hot (450°F endpoint, swab amber toward brown). Run 2 pending: endpoint reduced to 430°F, hold shortened to 55 seconds.

**Orange Candy** (Nikka T, 90 micron full melt) — In calibration. Runs 1–2 too flat (low vapor density in opening phase). Run 3 redesigned with steeper mid-climb and flatter tail — clean swab, strong result, wispy opening draws. Run 4 pending: opening raised 5°F to 380°F to address wispy vapor density at session start.

**Blueberry 36** — Three jars in collection, phenotypes #1, #2, #4 from a trusted grower's pheno hunt. Producer-specific designation, not a documented cultivar. Base genetics: DJ Short's Blueberry — myrcene dominant, caryophyllene and pinene as secondaries. No curves designed. Recommended approach: nose all three jars before first sessions to establish relative comparison across phenotypes, then start all three from baseline curve and log each separately. Meaningful differences will emerge from session character and swab, not from nose or jar appearance.

---

## Open Questions

- Blueberry 36 first sessions not yet run.
- Orange Candy Run 4 not yet completed.
- Caramel Apple Gelato Run 2 not yet completed.
- Sapphire insert not yet acquired. When acquired, requires fresh calibration from scratch — do not scale from quartz curves.
- Whether fresh press consistency justifies a different baseline curve remains an open question. Not settled.

**Potential log enhancements — not yet implemented, user interested:**
- **Session date precision.** Runs currently dated to month only. Add exact date to each run entry for longitudinal tracking.
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

---

## Known Claude Failure Modes — This Project

Specific errors made in past sessions that a new instance should avoid:

- **Over-asserting the thermal offset.** Earlier sessions built a 1D resistance model and landed on 15–35°F as a confident estimate. This was walked back. Do not re-assert a large fixed offset without empirical justification.
- **Chart glow pass thickening the curve.** An `afterDatasetsDraw` plugin that restroked the curve with a wide low-opacity line made the curve look significantly thicker than intended. Do not use secondary draw passes on the curve line.
- **`globalAlpha` for terpene line opacity not rendering correctly.** Using `ctx.globalAlpha` to lighten the terpene BP lines produced inconsistent results. Use baked hex colors instead.
- **Dressing up the generic cannabis terpene palette as strain-specific knowledge.** The same five or six terpenes appear across nearly all strains. Do not present inferred profiles as if they reflect meaningful strain differentiation.
- **Proposing changes without showing them first.** For chart styling and methodology edits, always propose the change with before/after context before executing. Do not edit and present without the proposal step.

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

- **May 6, 2026 — Session 1:** Initial structured handoff created. Thermal model revised (offset estimate walked back). Methodology doc updated. Chart styling overhauled (DM Mono, vivid green curve, steel blue terpene lines, THC pill label). Generator moved from project files to GitHub repo. Known failure modes, unresolved issues, and behavioral notes added.
- **May 6, 2026 — Session 2:** Producer updated to Quasi Farms (Michigan) for WW Z and Caramel Apple Gelato. Nose notes resolved — field already present on strain profiles, no per-run addition needed. Enhancements list: confidence rating (4) and load consistency note (5) removed at user request.
