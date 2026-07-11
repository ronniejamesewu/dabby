---
name: wisdom-audit
description: Re-audit the accumulated wisdom layer (HANDOFF_WISDOM.md) against primary run data across all jars — an orchestrator/worker sweep that re-derives cross-strain patterns from verbatim jar prose, proposes evidence-grounded row changes each with a counter-reading, and passes the proposal through a clean-context adversarial review before the user triages. Trigger when the user asks to audit, re-verify, or stress-test the wisdom layer, when a wisdom row's confidence is questioned, or when enough new runs have accumulated that the pattern library deserves a fresh pass. This is a rare, high-impact operation — most sessions never need it. It proposes changes for user approval; it never edits wisdom rows unprompted, and it never touches frozen run data (that is correct-frozen-data). Also carries a self-improvement step — the audit critiques and proposes improvements to its own process.
---

# Wisdom-Layer Audit

Re-derives the cross-strain patterns and equipment observations in
`HANDOFF_WISDOM.md` from primary jar prose, proposes changes for user triage,
and self-critiques the audit process. Origin: the July 11, 2026 audit
(`audit/matrix-2026-07-11/`), which found one confirmed evidence error, two
prose overclaims, a false control claim, and a recurring provenance weakness —
and whose own first-draft proposal was caught committing milder versions of
the same failure class by a clean-context reviewer.

This is the rare-but-high-impact tier, alongside `change-baseline`. It is not
part of the run-logging loop. It is user-initiated only.

## Terms

| Term | Meaning |
|---|---|
| Wisdom layer | `HANDOFF_WISDOM.md` — the Cross-Strain Patterns and Equipment Observations tables plus the Methodology sections |
| Evidence matrix | Per-run structured extraction of every jar (verbatim quotes + line anchors + source-field tags); see `audit/matrix-<date>/` |
| Provenance / source tag | Whether a claim is user-verbatim (`dab_notes`) or AI-authored (`analysis`, `session_char`, `endpoint_note`) — the audit's central discriminator |
| Counter-reading | The strongest good-faith argument *against* a proposed change, written before the change; a change whose counter-reading you can't rebut is flagged for the user, not made |
| Adversarial review | A fresh-context agent that attacks the proposal against primary data before the user sees it — catches drift that self-review misses at any model scale (Session 146 rule) |

**Two registers.** Never surface to the user: field names (`dab_notes`,
`session_char`, `next_ai_analysis`), slugs, `RIG_N`, the word "matrix" as a
tooling artifact, phase/step labels. The user sees: strain names, rig display
names, run numbers, plain-English findings.

## Hard rules

- **This skill proposes; the user disposes.** No wisdom row is edited until
  the user approves it, section by section. Present the proposal and wait.
- **No row edit on matrix data alone.** Before proposing any promotion,
  demotion, or reframe, read the cited runs' actual prose in `jars/<slug>.py`.
  Workers navigate; they don't testify. The matrix tells you where to look.
- **Every proposed change carries its counter-reading.** If you can't write a
  counter-reading you believe, flag the change for user/frontier review
  instead of making it (checklist Q1 in `HANDOFF_WISDOM.md`).
- **Never edit frozen run data here.** If the audit finds genuinely wrong
  frozen data (a bad swab, wrong rig, an error inside a run's `analysis`),
  route it through `correct-frozen-data` as a separate flagged item. This
  skill touches `HANDOFF_WISDOM.md` and `STATUS` `next_*` fields only.
- **Provenance is the discriminator.** Apply the user-verbatim vs. AI-authored
  standard *symmetrically* — to confirming and countering evidence alike, and
  to rows you keep as strictly as rows you change. The July 11 audit's own
  failure was applying it strictly where it struck a claim and loosely where
  it kept a row.
- **The confound must survive the edit.** When condensing or consolidating
  evidence prose, carry each instance's documented confound with it. Dropped
  confound clauses are the Session 146 failure class — direction-agnostic,
  narrative-seeking, invisible to self-review.
- **Respect Do-Not-Re-Litigate.** Before reopening any attribution, check the
  Decisions tables in `HANDOFF_WISDOM.md` and `Dabby_Handoff_Notes.md`. A
  settled attribution (e.g. FW106 R4 = session-order, Session 82) may be cited
  in a new context but not silently reopened.
- **Researcher-participant rule binds the experiment portfolio.** No proposed
  next-run design withholds a protective behavior (water, draw discipline,
  early stop) for a cleaner read. Where a tension exists, state it; the
  session goal wins.

## When NOT to use

- **A single run's analysis needs drafting** — that's the `log-run` skill
  (step 5) and `analysis-toolkit`, not a full audit.
- **A specific frozen field is wrong** — that's `correct-frozen-data`.
- **The baseline curve should change** — that's `change-baseline`.
- **You just want to read what a row says** — read `HANDOFF_WISDOM.md`
  directly; don't spin up a fan-out.

## Workflow

**1. Session-start gate first.** If this is a fresh session, complete the
CLAUDE.md gate (git sync, read the three handoff files) before anything.

**2. Enumerate jars and write the extraction schema.** `Glob jars/*.py`;
read `jar_manifest.py` for the ACTIVE/CLOSED tiers. Copy the extraction
contract from the most recent `audit/matrix-*/SCHEMA.md` — or refine it (see
step 8). The schema is where judgment enters delegated work: a schema that
omits a facet (e.g. harshness *location*) reproduces lossy summarization
mechanically. Current schema fields: date, timestamp, session order,
equipment, curve/waypoints, load, draws/cycles, stopping condition, harshness
(onset / location / persistence / escalation — kept separate), swab, reclaim,
intensity, water use, flavor, anomalies. Every cell: verbatim quote + source
tag + `jars/<slug>.py:<line>` anchor; `not stated` explicit; no interpretation.

**3. Fan out extraction workers — one per jar, parallel.** `subagent_type:
general-purpose`, `model: sonnet` (prose-dense extraction; the fidelity
inversion — the audience for the matrix is a cheaper session, so a
cheaper worker is the right test rig, not the orchestrator role-playing one).
Each worker prompt is self-contained: full schema path, full jar path, the
contract, the output path. Workers write to `audit/matrix-<date>/<slug>.md`
(or scratchpad first, promoted on user approval to commit). Batch all jars in
one message.

**4. Spot-check before trusting.** For each returned table, follow at least
two anchors to the live jar and confirm the quote. A worker that fails one
spot-check gets its whole jar re-read by the orchestrator directly. Worker
interim messages are status, not findings — only final reports enter the
matrix, and nothing enters a wisdom-row proposal unverified.

**5. Synthesize — orchestrator only, no delegation.** Walk the wisdom rows
against the matrix. For each: is the evidence verbatim or AI-authored? Are the
cited runs' attributes (rig era, session order, curve, endpoint) what the row
claims? Does a direction-split dissolve under a mediating variable? Named
high-value targets recur — load-size provenance, the ≥430°F ceiling's rig
scope, chest/persistence conflation, ramp-vs-flat order structure — but hunt
the whole table. Draft each change with its counter-reading *before* writing
it. Hard cap ~10 proposed changes ranked by consequence, plus a one-line
"checked, holds up" list for every row examined and left alone. An audit that
confirms most rows is a good outcome.

**6. Clean-context adversarial review.** Spawn a fresh agent (`model: fable`
while available, else `opus`) with the proposal, the matrix, and read access
to `jars/`. Brief: attack every headline claim against primary; hunt dropped
confounds, strawman counter-readings, citation errors in the proposal itself,
asymmetric provenance standards, and unflagged rows in the "holds up" list.
Self-review plus a checklist is demonstrably insufficient at any model scale —
this step is the mechanization of that lesson, not a courtesy. Reconcile every
finding into the proposal before the user sees it; mark what changed.

**7. Present for triage; on approval, ship.** Show the proposal ranked, each
change with counter-reading and review status, plus the holds-up list and any
experiment-portfolio updates. User approves per section. Then: apply approved
edits to `HANDOFF_WISDOM.md` and any `STATUS` `next_*` fields; `python
Dabby_Log_Generator.py` (regenerates `HANDOFF_STATE.md` + `index.html`);
feature branch; PR with a plain-English description. Commit the matrix as a
dated frozen artifact under `audit/matrix-<date>/` with the freeze banner (see
the July 11 README). The session-close checklist will fire (Q1 promotions, Q4
methodology) — offer it proactively.

**8. Self-improvement pass (do this every run).** Before closing, critique the
audit process itself and propose improvements. Questions to answer in the PR
or a short note: Did the schema miss a facet that would have surfaced a
finding? Did any worker systematically mis-tag (a schema-clarity signal)? Did
the adversarial reviewer catch a class of error the orchestrator should have
caught earlier (a step-5 discipline signal)? Is any part of the matrix's value
mechanically derivable (→ propose a script, not a re-run)? Record concrete
proposals as backlog items and, if warranted, edit this skill's schema or step
list directly. The audit that doesn't improve its own method will keep finding
the same class of thing the slow way.

## Recovery paths (don't improvise these)

- **A worker returns paraphrase instead of verbatim quotes** — reject its
  jar; re-read that jar directly. Do not synthesize from a paraphrased table;
  that reintroduces the compression drift the whole structure exists to
  prevent.
- **The adversarial reviewer finds a citation error in the proposal** —
  correct it in place, mark the correction, and re-check whether the same
  error class appears elsewhere in the proposal (errors travel in families).
- **A proposed change has no believable counter-reading** — do not make it.
  Flag it for the user or a frontier-class session per checklist Q1.

## Provenance and maintenance

Created July 11, 2026, from the first wisdom-layer audit
(`audit/matrix-2026-07-11/`). Verify these still hold if this skill starts
giving results that don't match reality:

```
# jars enumerable and manifest tiers intact:
python -c "from jar_manifest import ACTIVE, CLOSED; print(len(ACTIVE), len(CLOSED))"

# generator still validates + regenerates HANDOFF_STATE.md:
python Dabby_Log_Generator.py

# most recent prior matrix (schema to reuse / diff against):
ls audit/
```

Dogfood-test status: **Partially exercised** — the July 11, 2026 audit ran
this procedure end to end before the skill was written from it; the skill
text itself is not yet independently dogfood-tested on a fresh session.
