# Pickup Prompt — Handoff Notes Split

*Paste this to the session that picks up the notes-split work (symptom-triggered or
idle). It is written to be run by an Opus-class orchestrator or better. The archived
design is `wisdom/design/NOTES_SPLIT.md`; this prompt exists because that design was
written BEFORE the problem's symptoms appeared, by a session with an entire adjacent
migration loaded in context — twice over a candidate for anchoring. Your job is to
make it re-earn its place before executing it.*

---

You are picking up a pre-designed re-architecture for this project's
`Dabby_Handoff_Notes.md`. An archived design exists at `wisdom/design/NOTES_SPLIT.md`.
**Do not read it yet.** The sequencing below is the point of this prompt — the
archived design was authored pre-symptom by an anchored session, and its value can
only be tested by comparison against work it did not influence.

## Step 1 — Observe the problem fresh (before reading any design)

Your normal session-open reads (`WISDOM_BRIEF.md`, `Dabby_Handoff_Notes.md`) are the
problem material itself — fine. Beyond those: measure the notes file (chars, and
tokens against the Read tool's single-pass cap); pull its growth history from git
(`git log --follow -p --stat Dabby_Handoff_Notes.md`, sampled) to get a real accrual
rate; inventory its current sections and which ones accrete; check where its content
overlaps other homes (the wisdom layer's decision/failure-mode entries, the skills'
protocol text); and note what triggered this pickup — a paged Read, a boundary
hesitation, an idle session, or something the design never predicted. That last item
matters most: **the symptom that actually fired is evidence the pre-symptom design
never had.**

## Step 2 — Write a neutral problem statement

Author a problem statement from your Step 1 observations only: what the file is, what
is failing (with your measurements, not July 2026's), the growth mechanisms you can
document, the consumers and read moments, the requirements, and the house precedent
(the jar and wisdom layers — describable as proven mechanism). Use
`wisdom/design/problem-statement.md` as the template for register and scope
discipline. Two hard rules: every sentence must survive the test "could this have
been written if NOTES_SPLIT.md never existed?"; and the statement must contain no
disposition of any section (no "X should move to Y") — requirements and facts only.

## Step 3 — Clean-context design

Dispatch a frontier-class agent that has NOT read `Dabby_Handoff_Notes.md` in full,
NOT read `NOTES_SPLIT.md`, and is explicitly instructed to ignore the repository
CLAUDE.md's mandatory-read gate (obeying it would destroy the exercise). Give it:
your neutral problem statement, a few verbatim content samples spanning the notes'
section shapes (a voice paragraph, a protocol rule, a decision, a short and a long
failure-mode entry), and read access to the house architecture code
(`wisdom_core.py`, `wisdom/manifest.py`, a couple of entry files, the generator). Ask
for a complete design: disposition per content type, what bounds each destination,
enforcement, migration mechanics, touched surfaces. This mirrors the protocol that
produced the wisdom layer — the record of that exercise is in this directory if you
want the worked example (`problem-statement.md` → `accepted-proposal.md`), but read
those only after your designer is dispatched.

## Step 4 — Now read the archived design and run the three-way comparison

Read `NOTES_SPLIT.md`. You now hold three things: the problem as observed (Step 1),
a design produced by an unanchored frontier model from a neutral statement (Step 3),
and a design produced pre-symptom by an anchored session (the archive). Compare:

1. **Problem vs. predicted problem.** Does the archive's "problem being pre-empted"
   section match your measurements and the symptom that actually fired? Quantify the
   drift (size, accrual rate, which sections grew, any content type that appeared
   after July 2026 and has no disposition in the archive).
2. **Fresh design vs. archived design.** Per component: convergent, divergent, or
   the archive covers something the fresh design missed / vice versa. For each
   divergence, classify it: (a) the problem changed → the archive is stale on that
   point, prefer fresh reasoning and record why; (b) same problem, different
   judgment → neither design wins by age or recency; carry both options to the user
   with the specific tradeoff. Convergence between an anchored pre-symptom design
   and an unanchored post-symptom design is strong validation — where they agree,
   execute without further debate.
3. **The archive's flagged open calls** (its final section) — resolve each against
   current facts; several were left open precisely because they depended on
   measurements that didn't exist yet.

## Step 5 — Verdict, user triage, then execution

Produce a short verdict document: convergences (execute as archived), drift-driven
revisions (with the measurement that drove each), judgment-level divergences (as
options for the user), and the resolved open calls. Get user triage on the
divergences and the archive's known sizing problem (the brief-budget fit — do NOT
resolve it by silently raising the brief cap). Then execute using the factory in
this directory (`TRANSPOSITION.md` contract unchanged: verbatim moves, gap-marking —
`none noted` / `undated in source` — provenance defaults, tiered workers, mechanical
reference check, adversarial per-entry review, PR with preview). Append the verdict
document to `wisdom/design/` and record any architecture calls with reasoning, per
standing instruction.

Budget note: this whole exercise is Opus-orchestrated with Sonnet/Haiku workers; the
judgment was deliberately front-loaded into the archive and into this protocol so
that no Fable-class session is required. If you are a Fable-class session reading
this, the polite thing to do is wonder why, and then check the price of your tokens.
