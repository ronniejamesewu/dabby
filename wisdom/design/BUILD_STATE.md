# Wisdom Migration — Build State Checkpoint

*Written July 15, 2026, session hitting its usage limit mid-Phase-3. Audience: the
session (or a fresh one) resuming this build on branch
`claude/handoff-wisdom-length-vr0sa5`. Read `DECISIONS.md` first for the architecture;
`INVENTORY.md` for the entry map; `TRANSPOSITION.md` for the migration contract.*

## Done and pushed

- **Phase 0–1:** `wisdom_core.py` (schema, validators, brief renderer),
  `wisdom/manifest.py` (tiers, preflight, loader), generator hook (validates + writes
  `WISDOM_BRIEF.md` on every run; all outputs computed before any is written).
  Validators proven against seven deliberately broken entries + an orphan file.
- **Phase 2:** all 59 entries transposed (57 by tiered workers — Haiku/Sonnet/Opus —
  plus 2 hand-built exemplars), registered in the manifest, generator green. Brief
  renders 33.3k chars ≈ 12.5k tokens, one Read. Budget recalibrated once pre-ship
  against measured blocks (DECISIONS.md #9): hard 40k / warn 36k; counter_reading and
  per-entry pointers removed from the render. Standing advisory: `curve-design-theory`
  entry file is 26k chars (>20k warn) — split-or-compact is a triage decision.
- **Mechanical migration check: PASS.** All 94 old-file run references present in the
  new tree (202 citations; provenance u-v=16 / ai=176 / mixed=10; roles 141/21/32/8;
  1 superseded position). Script + results were delivered to the user; two initial
  "missing" refs were scanner bugs (Python string-seam, missing 'rainfruit' alias),
  not migration misses.

## In flight at checkpoint

- **Phase 3 internal review:** 59-agent workflow (`review-workflow.js` in this
  directory — copied verbatim from the run) — per-entry adversarial two-direction
  drift review, Opus×31 (authored-text entries) + Sonnet×28, with the 14 transposition
  worker FLAG items embedded for adjudication. Run ID `wf_4d6ee1a9-5b2` in session
  container (cache dies with the container; if lost, re-run the script via the
  Workflow tool — it is self-contained).
- **External review (user-side):** 9 ChatGPT-sized packets covering the 31
  authored-text entries were delivered to the user (priority order: 2, 3, 7, then
  1 and 9). Findings come back through the user. The external-reviewer brief is
  `external-review-brief.md` here.
- **14 worker FLAG items** await triage (verbatim in the transposition workflow
  result; the substantive ones are embedded in `review-workflow.js` FLAGS map —
  struck-vs-counters on tail-harshness-430, counters-vs-context on water-sip-reset,
  provenance judgment calls, the rig5 citation-collapse check).

## Remaining phases

- **Phase 3 close:** triage internal findings + external findings with the user;
  fixes to entry files on this branch; re-run generator.
- **Phase 4 — surface rewire** (touched-surfaces list: accepted-proposal.md §6):
  CLAUDE.md gate — retarget mandatory read #2 to `WISDOM_BRIEF.md` AND implement the
  two-tier purpose-keyed read policy (DECISIONS.md #13: HANDOFF_STATE.md becomes
  conditional on dab-intent/strain-named/run-work); dab skill step 3; log-run +
  analysis-toolkit skills (brief-then-entry-file rule); wisdom-audit skill (per-entry
  fan-out); session-close checklist references (now lives in wisdom_core.py, rendered
  in the brief footer); jar_manifest.py error strings (lines ~97, ~108 say "see
  HANDOFF_WISDOM.md"); Dabby_Handoff_Notes.md cross-references; Dabby_Methodology.md
  pointers; BACKLOG.md (the length item this build resolves); .claude/skills/README.md;
  deploy.yml + preview.yml (add `git diff --exit-code WISDOM_BRIEF.md` stale-brief
  guard). Sweep by meaning, not just filename grep (documented failure mode).
- **Phase 4 end:** delete `HANDOFF_WISDOM.md` (3-line tombstone pointing at
  WISDOM_BRIEF.md + wisdom/entries/, one release cycle).
- **Phase 5:** PR (plain-English description), preview check, user merge. Wisdom-edit
  freeze lifts on merge.

## Standing constraints

- Wisdom-edit freeze while this branch is open (run logging unaffected — jars only).
- Architecture calls get recorded in DECISIONS.md with reasoning (user instruction).
- Model-budget discipline: orchestrator judgment at top tier; workers tiered
  Haiku/Sonnet/Opus; Fable subagents only with user approval.
- Do not hand-edit WISDOM_BRIEF.md; never commit data to main; PR previews are the
  verification surface.
