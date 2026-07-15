# CLAUDE.md

> **MANDATORY — COMPLETE BEFORE ANY RESPONSE**
>
> At the start of every session, before producing any reply:
> 1. `git checkout main && git pull origin main` — the working directory may be on a stale branch.
> 2. Read both: `WISDOM_BRIEF.md`, `Dabby_Handoff_Notes.md` — every session, any type.
> 3. If the opening message shows dab intent or names a strain — or the moment any run, jar, or strain-state work starts mid-session — also read `HANDOFF_STATE.md`. (The dab and log-run skills mandate this read in their own sequences; this gate is the backstop.)
> 4. If the opening message names a strain, also read that strain's jar file in `jars/` (filename = the strain's slug — `Glob jars/*.py` to discover, or check `jar_manifest.py`).
>
> These are not optional. Do not respond first and read later. Do not answer from memory or summaries. Instance-level wisdom claims (run details, confounds, provenance) may only be written from `wisdom/entries/<key>.py` or a jar file — never from the brief alone.
>
> Sole exception: party-mode capture (the dab skill). There, the timestamp capture and a one-line confirmation come before the reads — nothing is answered from project state and nothing is written to the repo — and this gate runs in full at reconciliation, before anything is logged.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Dabby — Session Instructions

## Session-Start Reads

Unconditional (every session, any type):
- `WISDOM_BRIEF.md` — GENERATED summary of the wisdom layer: every entry's claim, confidence grade, guidance, and evidence counts, plus settled decisions, compressed one-liners, and the session-close checklist. Never edit by hand — the generator rewrites it. Anything deeper than what's on the page (instance evidence, confounds, provenance, position history) lives in `wisdom/entries/<key>.py`.
- `Dabby_Handoff_Notes.md` — operational notes, session protocol, decisions made, known failure modes.

Conditional on the session touching runs/jars/strain state (dab intent, a named strain, or run work starting mid-session):
- `HANDOFF_STATE.md` — generated per-strain status: run counts, last dates, current equipment, current What to Try Next per strain. This is the working surface for run logging; a session that never touches a run never needs it.

## Conditional Reads

Read these files when the session topic requires them:
- `wisdom/entries/<key>.py` — one file per wisdom entry (keys visible in the brief): full evidence with per-citation role/provenance/confounds, dated positions, counter-readings, supersession history. Read before finalizing any analysis that cites, compares against, or would change that entry, and before any session-close edit to it. Tier lists and loader: `wisdom/manifest.py`; schema and validators: `wisdom_core.py`; design rationale: `wisdom/design/DECISIONS.md`.
- `jars/<slug>.py` — one file per jar, holding that jar's runs (`RUNS`), status (`STATUS`), and local waypoint constants. This is the per-strain run data, status, waypoints. If the opening message names a strain, read its jar file before responding — not as a follow-up if questions get complex, but before the first reply. A Claude that hasn't read the jar file will answer confidently from `HANDOFF_STATE.md` summaries and hallucinate the run history behind them. Users won't catch it until something is wrong. Discover the slug via `Glob jars/*.py` or `jar_manifest.py`. Closed jars are jar files too (in the `CLOSED` tier) — not a separate archive file.
- `Dabby_Core.py` — dataclasses, `RIG_N` constants, `BASELINE_*` curves, `GLOBAL_INFO`, `TERPENE_REFERENCE`, color resolution, `validate()`. Read for schema/equipment/baseline questions. If the named jar has `RUNS = []`, read this file at session start — use the CONTENTS index at the top to jump directly to `CompletedRun` and `StrainStatus`.
- `jar_manifest.py` — the `ACTIVE` / `CLOSED` tier lists and the load function that assembles all jars. Read for lifecycle work.
- `BACKLOG.md` — open and completed backlog items. Read for session-close Q6, infrastructure work, or skill authoring.
- `Dabby_Log_Generator.py` — for generator/rendering work.
- `Dabby_Methodology.md` — for curve design or methodology questions.
- `Dabby_UI_Principles.md` — for UI/layout changes.

This project logs sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig."
All material is hash rosin (ice water extracted, solventless) unless explicitly 
stated otherwise. The log records what happened, swab results, and current thinking 
on what to try next — not a formal calibration program.

## Commands

- **Generate the log:** `python3 Dabby_Log_Generator.py` (Windows: `python
  Dabby_Log_Generator.py`) — assembles the jar files via `jar_manifest.py` and the
  wisdom entries via `wisdom/manifest.py`, writes `index.html`, `HANDOFF_STATE.md`,
  and `WISDOM_BRIEF.md`.
- `validate()` and `validate_accent_colors()` run automatically at the top of
  `build_html()`. A data error prints `VALIDATION ERRORS:` and exits 1 — a bad
  edit fails the generate step instead of producing a broken page.
- **No test suite, linter, or build system.** The logged runs are the de-facto
  regression suite; correctness is verified by eyeballing rendered `index.html`
  (locally or via the PR preview URL).
- **Deploy is automatic:** push to `main` → `deploy.yml` regenerates and
  publishes to GitHub Pages. Each PR auto-gets a preview URL via `preview.yml`.
  Both share a `gh-pages` concurrency group to avoid a merge race.
- **`pending_dab.py`** — mechanical timestamp capture and display-form facts
  for run logging. Subcommands: `start` (capture now), `brief` (session-open
  facts), `list` (show pending), `consume` (paste-ready fields for the oldest
  entry), `discard N` (remove an entry that won't become a run). Storage is
  `.pending_dabs.json` (gitignored, session-local). The generator refuses to
  run while unmatched pending entries exist.

## Skills

Skills in `.claude/skills/` are the primary workflow mechanism for run logging
and lifecycle operations. See `.claude/skills/README.md` for the full catalog,
handoff graph, and authoring rules.

The dab and log-run skills orchestrate the run-logging workflow end to end —
from timestamp capture through analysis drafting to PR creation. Other skills
handle lifecycle operations (new-jar, close-jar), equipment changes (new-rig),
frozen-data corrections (correct-frozen-data), baseline changes
(change-baseline), and per-run analysis discipline (analysis-toolkit).

Skills sequence the mechanical steps; they don't replace judgment. The design
principle: mechanize the floor so inference is freed for analysis.

## Architecture

- **Wisdom-as-data (July 15, 2026).** The wisdom layer mirrors the jar architecture:
  `wisdom_core.py` = schema (`WisdomEntry`/`Citation`/`Position`), validators (citation
  integrity against jar files, promotion gate, field caps, brief budget), and the brief
  renderer; `wisdom/entries/<key>.py` = one file per entry; `wisdom/manifest.py` =
  `LIVE`/`COMPRESSED` tiers + loader. `WISDOM_BRIEF.md` is generated on every generator
  run — never hand-edited — and is the mandatory session-open read. Compressing a
  settled entry = move its key to `COMPRESSED` and set its `resolution` one-liner; the
  entry file is untouched. Entry keys are stable identity — never renamed; splits
  create new keys with lineage noted in prose. Design record: `wisdom/design/DECISIONS.md`.
- **Per-jar architecture (Session 108).** Three layers: (1) `Dabby_Core.py` =
  shared stable layer (dataclasses, `RIG_N` constants, `BASELINE_*` curves,
  `GLOBAL_INFO`, `TERPENE_REFERENCE`, color resolution, validators — see the
  CONTENTS index at the top of the file for the full inventory with line numbers).
  (2) `jars/<slug>.py` = one file per
  jar, each exporting `RUNS` (list of `CompletedRun`) and `STATUS` (a single
  `StrainStatus`), plus that jar's local waypoint constants; each imports only
  `datetime` and `from Dabby_Core import *`. (3) `jar_manifest.py` = `ACTIVE` /
  `CLOSED` slug lists + `load_all_jars()`, which assembles them (closed first,
  then active) into the combined `COMPLETED_RUNS` / `STRAIN_STATUS`.
  `Dabby_Log_Generator.py` = rendering only; imports `from Dabby_Core import *`,
  `from Dabby_Core import _resolve_accent_colors`, and
  `from jar_manifest import load_all_jars`, then
  `COMPLETED_RUNS, STRAIN_STATUS = load_all_jars()` and re-runs accent resolution
  over the combined list. CSS is external in `style.css` (Session 36).
- **Jar isolation invariant.** Jar files never import from other jar files. If two
  jars need the same curve, the waypoint values are duplicated locally (e.g.
  Watermellos carries its own copies of the FW106 curves it borrowed). Shared
  constants (`BASELINE_*`, `RIG_N`) come from `Dabby_Core`, never duplicated.
- **Adding a run is data-only.** Edit the jar file in `jars/`: add the local
  waypoint constant, add a `CompletedRun` to `RUNS`, update the jar's `STATUS`
  `next_*` fields. The generator loop picks it up automatically — no generator
  edits for run logging. A new strain = a new `jars/<slug>.py` (from the
  boilerplate pattern) + its slug added to `ACTIVE` in `jar_manifest.py` with an
  inline name comment (`'slug',  # Full Strain Name`); `validate()` and the manifest
  preflight catch a missed half.
- **Lifecycle.** Two tiers: `ACTIVE` (material remaining) and `CLOSED` (jar
  done). Closing a jar = move its slug from `ACTIVE` to `CLOSED` in
  `jar_manifest.py`. The jar file itself is never touched by the move. The
  rendered log shows each jar's last-run date, which is sufficient to surface
  idle jars without a separate dormancy check.
- **Equipment is per-run.** `EquipmentConfig` with nested `Insert`/`CarbCap`/`Pearl`
  dataclasses; sequenced `RIG_N` constants; Rig Reference block on the rendered log
  documents each rig. `validate()` rejects `equipment=None` — no field defaults by design.
- **Charts:** Chart.js from CDN, one per curve via `curve_chart_html()`, fed by
  the same waypoint list as the table; needs internet to render.
- **Infra hazards:** never use GitHub MCP `push_files` for `index.html` or
  routine commits (caused silent content loss — use git); `push_files` is
  acceptable only for temporary files on non-main branches when git checkout
  of that branch is impractical, and never for `index.html`. Never hand-write
  `index.html`.

## Updating the Log

The dab and log-run skills orchestrate the full workflow — from timestamp capture
through file edits, generation, and PR creation. The underlying file changes are
data-only: edit the strain's `jars/<slug>.py` — add the local waypoint constant, add
a `CompletedRun` to `RUNS` with all content fields, and update the jar's `STATUS`
`next_*` fields. Then run `python3 Dabby_Log_Generator.py` to regenerate
`index.html`. Commit the jar file and the regenerated output to a feature branch,
then open a PR. `Dabby_Log_Generator.py` requires no edits for run logging.

Never write `index.html` by hand — always run the generator and commit its output.

Closed jars are jar files like any other (in the `CLOSED` tier of
`jar_manifest.py`) — historical record, never edited. When writing `analysis` or
`next_ai_analysis`, check `WISDOM_BRIEF.md` (already read at session open) for
relevant entry keys, then Read `wisdom/entries/<key>.py` for every entry the draft
cites, compares against, or would change — instance-level claims come from entry
files or jar files, never from the brief alone. Read a closed jar's `jars/<slug>.py`
only when: (a) a wisdom citation points to its runs and the entry's account feels
thin for the analysis at hand, (b) a pattern is flagged as needing cross-strain
confirmation and you want to search for it, or (c) a wisdom entry is vague and you
need the underlying run prose.

## Date and Time Logging

User timezone: **America/Denver (MDT/MST, UTC-6/UTC-7)**

`pending_dab.py` is the mechanical timestamp layer. The dab skill runs `start`
at announcement time to capture `utc_logged_at`; `brief` and `consume` print
all date, time, and dab-of-the-day facts in display form — no hand math. The
log-run skill's fallback path covers runs that were never captured.

Two rules that aren't fully mechanized:
- **Handoff date:** The `## Last updated:` header in `Dabby_Handoff_Notes.md`
  must be the **local date derived from `utc_logged_at` of the last run logged
  this session** (Denver time) — not the UTC date, and not `run_date` (which
  reflects when the dab happened, not when logging occurred). For sessions with
  no new runs, apply the Denver offset to the current time.
- **Post-date runs:** `utc_logged_at` can't be derived from `datetime.now()` —
  ask casually: "Do you have a sense of what time it was?" Use `None` if they
  don't know.

## Confirm Before Acting

Before taking any substantive action — editing files, updating methodology, 
proposing curve changes, restructuring the log — present what you are about to 
do and wait for explicit confirmation. Do not proceed until the user approves. 
Stating the plan and immediately executing is not proposing — it is narrating. 
Stop and wait.

Mechanical steps that follow from an already-approved decision do not need a 
separate confirmation: running the generator after changes are agreed, committing, 
pushing, and opening PRs can all be done without asking.

## PR Workflow

Changes go to a feature branch, then a PR to merge into `main`. Never commit data directly to main — always use a feature branch and PR. Every PR automatically gets a preview URL posted as a comment so the rendered log can be reviewed before merging.

PR descriptions should be plain English, not code diffs. Example format:

> Logged The Hive #1 Run 2 (May 8, 2026). Same curve as Run 1 — very light swab,  
> really nice session. Added note to try a lower endpoint (420–425°F) on Run 3.

One sentence per meaningful change. No technical details unless they affect 
interpretation of the results.

If work continues on an open PR across multiple commits or sessions, update the PR 
description to reflect what's actually in it. Use the GitHub MCP tool to read the 
current description first, then rewrite it to cover all changes to date.

When the user asks for the handoff to be updated, treat it as a session-close signal. Run the checklist in `WISDOM_BRIEF.md`'s footer — each "yes" edits the relevant `wisdom/entries/<key>.py` file (Read it first; append a Citation or dated Position, or update claim/guidance/grade — promotions above 'observation' require a counter_reading or the build fails) or `BACKLOG.md` for Q6. Mark gaps, never fill them: when the record is silent, write `none noted` / `undated in source` — never a plausible date, session, or explanation. Then update `Dabby_Handoff_Notes.md` (header date) and run the generator — it validates everything and regenerates `HANDOFF_STATE.md` and `WISDOM_BRIEF.md`. Before writing, scan for known issues and inconsistencies between what was done and what the docs say. Propose these alongside the update so they can be bundled into the same PR.

`HANDOFF_STATE.md` is always regenerated by running `python3 Dabby_Log_Generator.py` — never edit it by hand.

If there is already an open PR when the handoff update is written, push the handoff changes to that same branch — do not open a separate PR for the handoff alone.

## Reference Sections

The five reference sections (Device & Session Constants, Swab Color Reference, Baseline
Curve, Terpene Reference, Rig Reference) live on the main index page as collapsible blocks.
Do not move them to a separate page — they collapse when not needed and are rarely accessed.

## Reasoning Standard

For methodology, design, and schema decisions, apply first-principles reasoning: decompose every undefined term to its atomic meaning before proceeding.

## Epistemic Flags

General:
- Match confidence to evidence weight. One run is an observation. Two 
  consistent runs are directional. Do not write "confirmed," "established," 
  or "resolved" until the evidence would be surprising if it reversed.
- Do not promote correlates to causal variables. If the mechanism is 
  unresolved, describe what happened and flag the mechanism as open. 
  Example: "harshness entered on draw 3" is data; "the 2-draw ceiling" 
  treats draw count as the boundary variable when it may be a proxy for 
  depletion, cumulative heat exposure, or something else.

Domain-specific:
- Terpene profiles are inferred from genetics, not measured. The same generic 
  cannabis terpene palette appears across most strains. Do not present inferences 
  as specifications or dress up the generic palette as strain-specific knowledge.
- Swab color is a within-strain directional signal only. Do not compare across strains.
- Nose is a weak secondary signal. User has a non-discerning palate. Use genetics 
  as primary source.
- Do not assume a large titanium-to-insert offset. Setpoints are reasonable proxies 
  for material contact temperature.
- Do not reason about cold-material thermal shock. Cold start means material and 
  insert co-heat from ambient together.
- Do not import flower rosin assumptions. Hash rosin vaporizes more cleanly at lower 
  temperatures — efficiency argument, not heat sensitivity.
- Baseline curve is the starting point for all strains. Do not design different 
  starting curves from strain name, terpene profile, or consistency alone. Empirical 
  swab results drive adjustment.
