# Wisdom Layer — Architecture Decisions

*Written July 15, 2026, during the build. Audience: a future Claude trying to understand
why this layer is shaped the way it is. Companion files: `problem-statement.md` (the
requirements this design answers), `accepted-proposal.md` (the clean-context design it
started from), `external-review-brief.md` (the migration-audit brief for an outside model).
The proposal was produced by a designer that had NOT read HANDOFF_WISDOM.md — deliberate
anti-anchoring — then revised against the full content by the orchestrating session.
This file records the deltas and the calls made during implementation, with reasoning.*

## The core architecture (from the accepted proposal — read that file for the full case)

Wisdom entries are typed Python data: one file per entry under `wisdom/entries/<key>.py`,
tier lists (`LIVE` / `COMPRESSED`) in `wisdom/manifest.py`, dataclasses + validators +
brief renderer in `wisdom_core.py`, and a **generated** `WISDOM_BRIEF.md` as the bounded
mandatory session-open read. The generator writes the brief on every run; validators fail
the build on structural mistakes. This is the jar architecture applied a second time:
bounded generated summary, keyed on-demand detail, mechanical enforcement. The alternative
(split markdown documents) was rejected because hand-maintained summary/detail pairs drift,
and discipline-only rules have a documented failure record in this project.

## Field policy: "git preserves; it does not inform"

The single rule behind every schema-size call. Sessions read files; git gets opened for
deliberate archaeology, rarely — the project's own record shows git history functioning as
a write-only archive (see the changelog-removal decision in Dabby_Handoff_Notes.md).
Therefore:

- **Typed field** — only when a validator guards a documented failure mode through it.
- **Prose in the entry file** — anything a future session needs to *weigh* the entry
  (strike reasons, audit dates, lineage notes: "struck July 11 audit because X" changes
  how you read the evidence, so it lives in `gist`/`positions` text, not in git).
- **Git only** — purely forensic detail (who edited what when, exact retired wordings
  after they stop mattering).

This is why the schema is ~half the size of the accepted proposal's: `added`,
`first_observed`, `provenance_note`, `struck`/`struck_note`, `split_from`, and `strains`
were cut as fields. Their *content* was not cut — it moves into prose (or, for `strains`,
is derived from citation keys at render time). Storing what you can derive is how
summary/detail drift re-enters; informing from git is how information dies.

## Schema calls (deltas from the accepted proposal)

1. **`Citation` is five fields** — `source`, `role`, `provenance`, `gist`, `confounds`.
   Each typed field backs a validator: `source` → citation-integrity check against jar
   files (hallucinated evidence is unwritable); `role` → promotion-gate counting;
   `provenance` → the July 11 audit's user-verbatim/ai-authored tagging, required so it
   can never be silently omitted again; `confounds` → required non-empty ("none noted"
   must be explicit) because confound-dropping is this project's single most documented
   drift failure (Session 146: four dropped confound clauses). Everything else is prose
   in `gist`. The proposal's richer Citation atomized evidence essays too far — the
   comparative weave (R26-vs-R28 pairs, gradients) is the intelligence, and it lives in
   prose (`positions` for cross-run narrative, `gist` for per-instance facts).

2. **`struck` is a `role`, not a flag.** A struck citation is one whose evidentiary role
   is "struck" — reason and date in `gist`. One enum value instead of two fields.

3. **`Citation.source` takes three forms** — a run key (`"fw106 R26"`, validated against
   the jar manifest and that jar's run count), `"session:<ref>"` (e.g. the Session 106
   empty-insert control — real evidence that exists in no jar), or
   `"conversation:<ref>"` (e.g. the cold-cure fridge-nose reports — user remarks that
   were never run-logged). The strict jar cross-check applies only to run keys. Without
   this, the validator would force mis-citation of genuine non-run evidence — found by
   checking the design against the full corpus, which the clean-context designer
   couldn't do.

4. **Grade ladder uses the house epistemic lexicon** — `speculative` / `observation` /
   `directional` / `tested` — not the proposal's `low`→`established`. "Established" is on
   the project's banned-words list (Epistemic Flags; analysis-toolkit Recipe 8's closed
   ladder is observation = 1 run, directional = 2 consistent, survives-disconfirmation =
   multi-strain; `tested` is that last rung's enum-friendly name). An enum value leaks
   into prose eventually; it must be a word the prose is allowed to say. Migration
   mapping from the old file: Low → `observation`, Moderate → `directional`,
   High → `tested`, with per-entry judgment allowed where the old label and its evidence
   visibly disagree (flag such cases to review rather than silently regrading).

5. **`grade` is `None` for `decision` and `failure-mode` kinds.** A settled ruling and an
   operational hazard aren't confidence-graded claims; forcing a grade would produce
   noise that reads as signal. Validator enforces: patterns/equipment/theory must carry a
   grade, decisions/failure-modes must not.

6. **Decisions render as one-liners in the brief** (claim + key pointer), not full
   blocks. A settled ruling *is* its claim; rationale lives in the entry file. This is
   also the day-one budget fix: ~13 decision entries at full-block size (~400 chars)
   would have consumed ~a quarter of the brief for content nobody needs expanded at
   session open.

7. **Equipment entries are per-rig** (one entry per RIG_N-era configuration), not
   per-claim. Rig is the natural key — same reasoning as one-file-per-jar — and the
   multiple observations within a rig row are exactly what `positions` holds. Splitting
   per-claim would scatter one rig's story across files and multiply the entry count for
   no read-path benefit.

8. **The Tail Harshness Mechanism section stays one `theory` entry** (four candidate
   mechanisms + control observations as structured positions), because it is one open
   question with competing answers, not four questions. If it outgrows the per-file
   warning, the split move exists (new keys, lineage note in prose).

## Enforcement calls

9. **Brief budget: 40k chars hard error, 36k warn — recalibrated once, pre-ship, against
   measured blocks.** The accepted proposal guessed 20k assuming ~400-char entry blocks;
   the migration measured reality: workers write capped fields TO the caps, so full
   blocks average ~790 chars and the complete migrated corpus renders at ~33k chars
   (~12.5k tokens — a single Read at ~50% of the 25k-token tool cap, 2.6x cheaper at
   session open than the 84k-char file this replaced). The requirement was always
   one-Read-with-headroom + no-instance-growth, not a specific number; the number was
   repriced ONCE while the system was being built, with the measurement recorded here.
   Post-ship these caps only ratchet DOWN — raising a cap the day it fires is how
   tripwires die, and the July 2026 regrowth (63k → 84k in ten days, noticed only when
   a Read call paged) is what this cap exists to make impossible. Also from the same
   measurement: counter_reading is NOT brief-rendered (it is uncapped, and it matters
   when changing a grade — an edit, which already requires opening the entry file), and
   entries carry no per-entry file pointer (the header states the key→file rule once).

10. **The entry-count warning (>40) counts full-block-rendered LIVE entries only** —
    patterns, equipment, theory, live failure modes — not one-line decisions. The
    warning's job is to protect the brief's read cost; one-liners barely contribute.
    Day-one census: ~37 full-block LIVE, ~13 decision one-liners, ~10 compressed lines.

11. **Per-entry-file warning at 20k chars**, naming the two pressure valves: split the
    entry (new keys + lineage in prose) or compact fully-superseded positions to git
    with a pointer. Warning, not error — a heavy entry is legitimate; an unnoticed one
    is not.

12. **Validators run inside the existing generator invocation** (`load_all_entries()`
    preflight + `validate_wisdom()` alongside `validate()`), so enforcement inherits
    every existing trigger for free: every logging session, every handoff close, every
    CI run. No new commands to remember.

## Session-open read policy (purpose-keyed gate — lands with the Phase 4 CLAUDE.md edit)

13. **The mandatory session-start gate becomes two-tier.** Unconditional, every session,
    before first reply: `WISDOM_BRIEF.md` + `Dabby_Handoff_Notes.md` (behavioral rules,
    voice, live hazards, settled decisions — every-session material). Conditional:
    `HANDOFF_STATE.md` joins when the opening message shows dab intent or names a
    strain, or the moment any run/jar/state work starts mid-session. Reasoning: the
    problem statement's cost function is context spent per session, and HANDOFF_STATE's
    unique content (equipment default, next-run plans, per-strain status) is
    logging-context material — an infra/design session pays ~9k tokens for it and never
    uses it. The trigger is observable (message content, not inferred intent — the
    write-gate failure-mode lesson), and the drift case is already skill-covered: the
    dab and log-run skills mandate the state read in their own sequences, so the gate
    is the backstop, not the only wall. Accepted residual risk: a session that starts
    non-logging must notice the crossing into run work; exposure is small because the
    crossing points are skill-triggered, and the failure is loud (can't log without the
    equipment default) where the old failure (partial wisdom read) was silent.

## What future sessions must not do

- Hand-edit `WISDOM_BRIEF.md` (generated; the generator overwrites it).
- Add schema fields without a validator or a weigh-the-entry justification (see field
  policy above). The schema stays small on purpose.
- Rename entry keys (they are stable identity; splits create new keys, lineage in prose).
- Put instance-level evidence in capped brief-rendered fields — it belongs in
  `evidence`/`positions`, which the brief never renders.
