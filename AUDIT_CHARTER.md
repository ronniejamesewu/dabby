# Project Audit Charter
*Written July 3, 2026 (Session 144, Fable-class) — the charter for a one-time,
whole-project audit. Execute in a FRESH session: full context window, and an
auditor that did not write the July 3 changes. When the audit ships, this file
is deleted in the audit PR (its scope decisions get one paragraph in
`AUDIT.md`'s preamble — same disposal pattern as `DABBY_ARCHITECTURE.md`,
Session 109).*

To execute: open a fresh session and say "run AUDIT_CHARTER.md".

---

## Mission

A retiring-senior-fellow audit of the entire project, producing `AUDIT.md`
with two ranked findings lists:

1. **Mechanization opportunities** — every place a fact or rule is still held
   in prose and recalled at use time, where code could compute, print, or
   validate it instead. The project's trajectory is prose → code (validators,
   generated facts, printed display blocks, sequenced skill steps); this scope
   systematizes the hunt.
2. **Stale, contradictory, or confusing prose** — every doc claim that no
   longer matches the code, contradicts another doc, or would mislead a fresh
   Sonnet-class session.

The audit **reports; it does not fix.** Findings become backlog items or PRs
only after user review. The only writes permitted: `AUDIT.md`, the citation
checker script (step 1), and deleting this charter.

## Model and independence

- **Frontier-class session (Fable/Opus) required for steps 3–5.** The
  judgment calls — is this a contradiction or a deliberate tension, what's the
  mechanization ROI — are the work. Steps 1–2 are Sonnet-safe.
- **Audit the July 3 changes with extra suspicion, not less.** PRs #214/#215
  and this charter were authored by one session (Fable); PRs #216–#217, the
  Session 145 close, and the register-leak diagnostic files by another
  (Sonnet). Authors under-flag their own work (Session 71 lesson) — a fresh
  auditor is the point of this charter existing.

## Corpus

**In scope:** `Dabby_Core.py`, `Dabby_Log_Generator.py`, `pending_dab.py`,
`jar_manifest.py`; all of `.claude/skills/` (dab, log-run, new-jar +
references); `CLAUDE.md`, `Dabby_Handoff_Notes.md`, `HANDOFF_WISDOM.md`
(**both pages** — it exceeds one Read call; a page-1-only read invalidates the
audit), `Dabby_Methodology.md`, `Dabby_UI_Principles.md`, `DESIGN_BRIEF.md`,
`jar_return_check.md`, `switch2_thermal_model.md`,
`register_leak_diagnostic_exercise.md`; `.github/workflows/*.yml`;
`style.css` (light pass — scope 2 only).

**Out of scope:** `index.html` and `HANDOFF_STATE.md` (generated — audit the
generator, not its output); full prose read of `jars/*.py` (frozen history;
spot-check only where the citation checker or a wisdom claim demands it); git
history (targeted lookups only); **`register_leak_diagnostic_answer.md` — do
not open it.** It is gated behind a blinded exercise designed for a future
session; the incident is already summarized in the failure-mode entry and its
backlog item, which is sufficient for audit purposes. Reading the answer burns
the exercise.

## Method — in this order

**0. Session open per `CLAUDE.md`** (mandatory reads; this is a session like
any other).

**1. Build the citation checker first** — a small script (committed in the
audit PR, e.g. `citecheck.py`; it is also the tool pass 3's guardrail 2
needs). Deterministic checks only, no LLM:
- Every run citation in `HANDOFF_WISDOM.md` / `Dabby_Handoff_Notes.md` /
  `Dabby_Methodology.md` (patterns like `FW106 R26`, `WM R16–18`, `Run 9`
  with a strain in context) resolves to a real run: build a short-form → slug
  alias table (FW106→fw106, WM→watermellos, …) from `jar_manifest.py`'s
  inline comments, then check the cited run number ≤ that jar's `len(RUNS)`.
- Every filename mentioned in the docs exists on disk.
- Every code identifier the docs name (`RIG_N`, `BASELINE_*`, function names)
  greps to a definition.
Checker hits are **triage input, not auto-fail**: historical failure-mode rows
deliberately reference retired artifacts (e.g. `Dabby_Data.py`); the auditor
dispositions every hit rather than bulk-flagging.

**2. Full fresh read of the in-scope corpus.** No skimming, no trusting
summaries, no "already know this file."

**3. Scope 2 — prose vs. reality.** For every protocol claim: does the code
still do this? For every pair of docs covering the same ground
(CLAUDE.md ↔ skills ↔ handoff notes ↔ wisdom): do they agree? Distinguish
three severities in the finding itself: **contradiction** (two sources
disagree), **stale** (describes a world that no longer exists), **confusing**
(true but structured to mislead a fresh session). Every finding quotes both
ends with `file:line`.

**4. Scope 1 — mechanization sweep.** Sources: the Live failure-mode list
(each entry is a candidate by definition — the section header says "no
mechanical guard exists"; the audit asks whether that's still true), the
protocol prose in `Dabby_Handoff_Notes.md`/`CLAUDE.md`, and the skills. Each
finding states: the failure it prevents (has it actually occurred?), the
mechanism (validator / generated fact / printed display block / skill step /
preflight), the precedent pattern in this repo, and a build-cost grade
(S/M/L). Apply the project's own bar: if the justification is aesthetic or
hypothetical, say so explicitly (Session 112 lesson).

**5. Write `AUDIT.md`:** preamble (method actually followed, deviations from
this charter, citation-checker summary); Scope 2 findings ranked; Scope 1
findings ranked; **known-items disposition table** (below — confirmed /
amended / obsolete, so pre-known work is validated, not rediscovered); a
**Leave It Alone** section for things that look like findings but are settled
(check both Decisions — Do Not Re-Litigate tables *before* flagging anything;
also settled by design: jar-isolation waypoint duplication, machine-side
vocabulary inside skill files, wisdom short-form run citations, frozen jar
prose). `AUDIT.md` must fit one Read call (<25k tokens).

**6. Ship:** fresh branch (e.g. `project-audit`), the three permitted writes
only, PR with a plain-English description. Merging waits for the user.

**7. Optional, user decides at PR time (+30–50% cost): adversarial
verification.** Clean-context agent, brief: "try to break each finding
against the source; demote or drop any that don't survive." Recommended —
the report becomes load-bearing the moment it merges.

## Known items — validate and rank, don't rediscover

From the backlog (confirm each is still real, then rank it among the new
findings): CLAUDE.md integration pass (prose and mechanical layer describe
different worlds — skill-library item 6); wisdom file exceeds the Read cap
(pass 3 is fully specified — the audit checks *correctness* of what pass 3
will compress, it does not compress); skills README; BASELINE_CURVE-in-RUNS
preflight ban; workflow simplification; User Configuration block; the three
Session 145 items — `fmt_curve_table()` mobile overflow, model-check at
dab-skill start, and the pre-send check's semantic blind spot ("the swab
field" leaked in plain English past syntactic triggers — the open question is
whether a semantic check can be mechanical at all). Also validate the
Session 145 failure-mode entry on proactively surfacing the session-close
checklist mid-session.

## Sequencing and budget

This audit precedes the wisdom consolidation (correctness before compression
— compressing unaudited claims launders errors into more authoritative text)
and the analysis-toolkit skill (which mines the consolidated file). Budget:
one heavy session — roughly 2–3 hours, ~500–800k tokens. If the window runs
short: scope 2 findings ship first (live confusion cost), scope 1 ranking can
land in a follow-up.
