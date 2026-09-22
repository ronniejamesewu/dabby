---
name: wisdom-audit
description: Re-audit the accumulated wisdom layer — the typed entries under wisdom/entries/ surfaced in the generated WISDOM_BRIEF.md — against primary run data across all jars, an orchestrator/worker sweep that re-derives cross-strain patterns from verbatim jar prose, proposes evidence-grounded entry changes each with a counter-reading, and passes the proposal through a clean-context adversarial review before the user triages. Trigger when the user asks to audit, re-verify, or stress-test the wisdom layer, when a wisdom entry's confidence is questioned, or when enough new runs have accumulated that the pattern library deserves a fresh pass. This is a rare, high-impact operation — most sessions never need it. It proposes changes for user approval; it never edits wisdom entries unprompted, and it never touches frozen run data (that is correct-frozen-data). Also carries a self-improvement step — the audit critiques and proposes improvements to its own process.
---

# Wisdom-Layer Audit

Re-derives the cross-strain patterns, equipment observations, and working
theories in the wisdom layer — the typed entry files under `wisdom/entries/`,
surfaced through the generated `WISDOM_BRIEF.md` — from primary jar prose,
proposes changes for user triage, and self-critiques the audit process.
Origin: the July 11, 2026 audit (`audit/matrix-2026-07-11/`), which ran against
the pre-migration `HANDOFF_WISDOM.md` (single markdown file, since replaced by
the typed layer) and found one confirmed evidence error, two prose overclaims,
a false control claim, and a recurring provenance weakness — and whose own
first-draft proposal was caught committing milder versions of the same failure
class by a clean-context reviewer.

This is the rare-but-high-impact tier, alongside `change-baseline`. It is not
part of the run-logging loop. It is user-initiated only.

## Terms

| Term | Meaning |
|---|---|
| Wisdom layer | The typed wisdom entries (`wisdom/entries/<key>.py`), their tier lists in `wisdom/manifest.py`, and the generated always-read `WISDOM_BRIEF.md` that renders them. The audit edits entry files and tier lists; the brief is regenerated, never hand-edited |
| Entry | One `wisdom/entries/<key>.py` file — the audit unit. Carries `claim`, `grade`, `guidance`, `watch_for`, typed `Citation` evidence (`source`/`role`/`provenance`/`gist`/`confounds`), dated `Position` history, and `counter_reading`. Kinds: pattern / equipment / failure-mode / decision / theory |
| Re-derivation | Per-entry structured extraction: a worker re-reads the entry's cited runs and re-derives whether the claim and grade still hold — verbatim quotes + line anchors + source-field tags. Frozen under `audit/<date>/`; the direct descendant of the pre-migration per-jar evidence matrix |
| Provenance / source tag | Whether a citation is user-verbatim (`dab_notes`) or AI-authored (`analysis`, `session_char`, `endpoint_note`) — the audit's central discriminator. Now the typed `Citation.provenance` field; the validator guarantees it is present, the audit judges whether it is *right* |
| Counter-reading | The strongest good-faith argument *against* a proposed change, written before the change; a change whose counter-reading you can't rebut is flagged for the user, not made. Now the typed `counter_reading` field — the validator requires it for any grade above `observation` |
| Adversarial review | A fresh-context agent that attacks the proposal against primary data before the user sees it — catches drift that self-review misses at any model scale (Session 146 rule) |

**Two registers.** Never surface to the user: field names (`dab_notes`,
`session_char`, `next_ai_analysis`), slugs, entry keys (`tail-harshness-430`),
`RIG_N`, the words "matrix" or "citation" as tooling artifacts, phase/step
labels. The user sees: strain names, rig display names, run numbers, plain-English
findings.

## Hard rules

- **This skill proposes; the user disposes.** No wisdom entry is edited until
  the user approves it, section by section. Present the proposal and wait.
- **No entry edit on re-derivation output alone.** Before proposing any
  promotion, demotion, or reframe, read the cited runs' actual prose in
  `jars/<slug>.py`. Workers navigate; they don't testify. The re-derivation
  tells you where to look.
- **Every proposed change carries its counter-reading.** If you can't write a
  counter-reading you believe, flag the change for user/frontier review
  instead of making it (checklist Q1 in the brief's session-close footer). A
  grade promotion above `observation` also *requires* a written
  `counter_reading` on the entry — the validator rejects it otherwise.
- **Never edit frozen run data here.** If the audit finds genuinely wrong
  frozen data (a bad swab, wrong rig, an error inside a run's `analysis`),
  route it through `correct-frozen-data` as a separate flagged item. This skill
  edits wisdom entry files (`wisdom/entries/<key>.py`), tier lists in
  `wisdom/manifest.py`, and `STATUS` `next_*` fields only. It never hand-edits
  `WISDOM_BRIEF.md` — that surface is generated.
- **Validators pre-catch the mechanical errors; workers hunt the semantic ones.**
  Every `python3 Dabby_Log_Generator.py` runs citation integrity (each run-key
  `source` resolves to a real run in a real jar), the promotion gate (grades
  above `observation` carry a `counter_reading`; patterns need ≥2 confirming
  citations, `tested` needs confirming runs from ≥2 jars), and the field caps.
  So audit workers do not re-litigate those facts — a hallucinated citation is
  already unwritable. Their job is semantic fidelity: does the entry's claim and
  grade still match what the jar prose actually supports, is each provenance tag
  correct, does each confound still belong.
- **Provenance is the discriminator.** Apply the user-verbatim vs. AI-authored
  standard *symmetrically* — to confirming and countering evidence alike, and
  to entries you keep as strictly as entries you change. The July 11 audit's own
  failure was applying it strictly where it struck a claim and loosely where it
  kept a claim. The validator guarantees a provenance tag exists on every
  citation; it cannot tell you the tag is honest — that is the audit's read.
- **The confound must survive the edit.** When condensing or consolidating
  evidence prose, carry each citation's documented confound with it. `confounds`
  is a required non-empty field, so the validator catches a *dropped* confound
  (empty string). It cannot catch a *weakened* one — a real confound overwritten
  with "none noted." That silent erosion is the Session 146 failure class:
  direction-agnostic, narrative-seeking, invisible to self-review and to the
  validator alike.
- **Respect Do-Not-Re-Litigate.** Before reopening any attribution, check the
  `decision`-kind entries (rendered as the brief's "Decisions — Do Not
  Re-Litigate" one-liners; rationale in each entry file) and the Decisions
  section of `Dabby_Handoff_Notes.md`. A settled attribution (e.g.
  `dec-fw106-r4-session-order`, Session 82) may be cited in a new context but
  not silently reopened.
- **Researcher-participant rule binds the experiment portfolio.** No proposed
  next-run design withholds a protective behavior (water, draw discipline,
  early stop) for a cleaner read. Where a tension exists, state it; the session
  goal wins.

## When NOT to use

- **A single run's analysis needs drafting** — that's the `log-run` skill
  (step 5) and `analysis-toolkit`, not a full audit.
- **A specific frozen field is wrong** — that's `correct-frozen-data`.
- **The baseline curve should change** — that's `change-baseline`.
- **You just want to read what an entry says** — read `WISDOM_BRIEF.md`, or the
  entry file for instance detail, directly; don't spin up a fan-out.

## Workflow

**1. Session-start gate first.** If this is a fresh session, complete the
CLAUDE.md gate (git sync; read `WISDOM_BRIEF.md` + `Dabby_Handoff_Notes.md`,
and `HANDOFF_STATE.md` once run/jar/state work begins) before anything.

**2. Enumerate the audit units and write the re-derivation contract.** The
audit unit is a wisdom entry. Read `wisdom/manifest.py` for the `LIVE` and
`COMPRESSED` key lists — every key is one file at `wisdom/entries/<key>.py`. For
each entry, list its cited jars: each `Citation.source` is a run key
(`fw106 R26`), a `session:<ref>`, or a `conversation:<ref>`; the run-key slugs
are the jars that entry's worker will read. `Glob jars/*.py` and read
`jar_manifest.py` (ACTIVE/CLOSED tiers) to resolve slugs to files. Reuse or
refine the extraction contract from the most recent `audit/<date>/SCHEMA.md`
(see step 8). The contract is where judgment enters delegated work: one that
omits a facet (e.g. harshness *location*) reproduces lossy summarization
mechanically. Current contract fields: date, timestamp, session order,
equipment, curve/waypoints, load, draws/cycles, stopping condition, harshness
(onset / location / persistence / escalation — kept separate), swab, reclaim,
intensity, water use, flavor, anomalies. Every cell: verbatim quote + source
tag + `jars/<slug>.py:<line>` anchor; `not stated` explicit; no interpretation.

**3. Fan out re-derivation workers — one per entry key, parallel.**
`subagent_type: general-purpose`, `model: sonnet` (prose-dense re-derivation;
the fidelity inversion — the audience for the wisdom layer is a cheaper session,
so a cheaper worker is the right test rig, not the orchestrator role-playing
one). Each worker prompt is self-contained: the entry file path, the paths of
*its cited jars only*, the contract, the output path. The worker re-reads the
cited runs verbatim and re-derives, against the jar prose: does the `claim` still
hold; does the `grade` still match the evidence weight; is each citation's
`provenance` tag honest; does each `confounds` clause still belong; does any
cited run fail to support the `role` it's filed under. It returns a proposed
entry-file diff — or "holds up" — with a counter-reading on every proposed
change. Diff types the worker may propose: citation edits (add, strike via
`role='struck'`, re-tag provenance, correct `gist`/`confounds`, add a
`counters`), `Position` additions (append a dated one; supersede in place with a
`superseded_note`, never delete), `claim`/`guidance` reframes within caps, and
`grade` changes (a promotion must ship with its `counter_reading`). Workers
write to `audit/<date>/<key>.md`. Batch all entries in one message.

**4. Spot-check before trusting.** For each returned re-derivation, follow at
least two anchors to the live jar and confirm the quote. A worker that fails one
spot-check gets its entry re-derived by the orchestrator directly. Worker interim
messages are status, not findings — only final reports enter synthesis, and
nothing enters an entry-change proposal unverified.

**5. Synthesize — orchestrator only, no delegation.** Assemble the per-entry
proposals into one ranked change set. Because each worker saw only its entry's
*cited* jars, cross-corpus coverage is the orchestrator's job: when an entry's
grade leans on cross-strain breadth (a `tested` pattern, whose validator floor
is confirming runs from ≥2 jars), read the uncited jars that could confirm or
counter it before trusting the grade. Walk each entry: is the evidence
verbatim or AI-authored? Are the cited runs' attributes (rig era, session order,
curve, endpoint) what the claim asserts? Does a direction-split dissolve under a
mediating variable? Named high-value targets recur — load-size provenance, the
≥430°F ceiling's rig scope, chest/persistence conflation, ramp-vs-flat order
structure — but hunt the whole tier. Draft each change with its counter-reading
*before* writing it. Hard cap ~10 proposed changes ranked by consequence, plus a
one-line "checked, holds up" list for every entry examined and left alone. An
audit that confirms most entries is a good outcome.

**6. Clean-context adversarial review.** Spawn a fresh agent (`model: fable`
while available, else `opus`) with the proposal, the re-derivation artifacts, and
read access to `jars/` and `wisdom/entries/`. Brief: attack every headline claim
against primary; hunt dropped or weakened confounds, strawman counter-readings,
citation errors in the proposal itself, asymmetric provenance standards, and
unflagged entries in the "holds up" list. Self-review plus a checklist is
demonstrably insufficient at any model scale — this step is the mechanization of
that lesson, not a courtesy. Reconcile every finding into the proposal before the
user sees it; mark what changed.

**7. Present for triage; on approval, ship.** Show the proposal ranked, each
change with counter-reading and review status, plus the holds-up list and any
experiment-portfolio updates. User approves per section. Then: apply approved
edits to the entry files (`wisdom/entries/<key>.py`), any tier moves in
`wisdom/manifest.py` (LIVE↔COMPRESSED — a compressed key needs its `resolution`
one-liner), and any `STATUS` `next_*` fields. Do **not** touch
`WISDOM_BRIEF.md` — run `python3 Dabby_Log_Generator.py`, which re-validates
(citation integrity, promotion gate, caps) and regenerates `WISDOM_BRIEF.md`
alongside `HANDOFF_STATE.md` + `index.html`. A validation failure here means an
entry edit is malformed — fix the entry, never the generated brief. Feature
branch; PR with a plain-English description. Commit the re-derivation artifacts
as a dated frozen artifact under `audit/<date>/` with the freeze banner (see the
July 11 README; `dec-matrix-snapshots-frozen`). The session-close checklist will
fire (Q1 promotions, Q4 methodology) — offer it proactively.

**8. Self-improvement pass (do this every run).** Before closing, critique the
audit process itself and propose improvements. Questions to answer in the PR or a
short note: Did the contract miss a facet that would have surfaced a finding? Did
any worker systematically mis-tag (a contract-clarity signal)? Did the
adversarial reviewer catch a class of error the orchestrator should have caught
earlier (a step-5 discipline signal)? Did a coverage gap show up because a worker
saw only its entry's cited jars (a step-5 cross-corpus signal)? Is any part of
the re-derivation mechanically derivable, or already covered by a validator (→
propose a script or a validator, not a re-run)? Record concrete proposals as
backlog items and, if warranted, edit this skill's contract or step list
directly. The audit that doesn't improve its own method will keep finding the
same class of thing the slow way.

## Recovery paths (don't improvise these)

- **A worker returns paraphrase instead of verbatim quotes** — reject its entry;
  re-read the cited jars directly. Do not synthesize from a paraphrased
  re-derivation; that reintroduces the compression drift the whole structure
  exists to prevent.
- **The adversarial reviewer finds a citation error in the proposal** — correct
  it in place, mark the correction, and re-check whether the same error class
  appears elsewhere in the proposal (errors travel in families).
- **A proposed change has no believable counter-reading** — do not make it. Flag
  it for the user or a frontier-class session per checklist Q1.
- **The generator fails validation after an edit** — the error names the entry
  and the rule (citation integrity, promotion gate, cap). Fix the entry file;
  never edit `WISDOM_BRIEF.md` to make the number go away (it is overwritten on
  the next generate anyway).

## Provenance and maintenance

Created July 11, 2026, from the first wisdom-layer audit
(`audit/matrix-2026-07-11/`), and retargeted to the typed wisdom layer in the
Phase 4 migration (July 15, 2026). Verify these still hold if this skill starts
giving results that don't match reality:

```
# wisdom entries enumerable and manifest tiers intact:
python3 -c "from wisdom.manifest import LIVE, COMPRESSED; print(len(LIVE), len(COMPRESSED))"

# jars enumerable and manifest tiers intact:
python3 -c "from jar_manifest import ACTIVE, CLOSED; print(len(ACTIVE), len(CLOSED))"

# generator still validates entries + regenerates WISDOM_BRIEF.md and HANDOFF_STATE.md:
python3 Dabby_Log_Generator.py

# most recent prior audit (contract to reuse / diff against):
ls audit/
```

Dogfood-test status: **Partially exercised** — the July 11, 2026 audit ran the
pre-migration procedure (per-jar matrix, single wisdom file) end to end before
the skill was written from it. The retargeted per-entry procedure is not yet
independently dogfood-tested on a fresh session.
