# Wisdom-Layer Audit — Proposed Changes (for user triage)

All 144 runs across 20 jars re-derived from primary jar-file prose via
verbatim-quoted extraction (verified: spot-checks passed on all 20 jars).
Every proposed change below was made only after reading the cited runs'
actual prose. Each change carries its counter-reading. Ranked by consequence.

Verdict up front: the wisdom layer is in good shape. Of ~10 cross-strain
rows, ~5 equipment rows, and the methodology sections, most hold as written.
The audit found TWO confirmed evidence errors in row citations, TWO
overclaims in row prose relative to primary records, one stale note, and a
recurring provenance weakness (load sizes sourced from AI-authored fields).
No confidence promotions are proposed. Nothing found warrants demotion of a
High row; two rows get scope qualifiers.

**Revision note:** this document was reviewed by a clean-context adversarial
reviewer (fresh Fable session, no shared context) before reaching you, per
the Session 146 rule. The reviewer confirmed every headline discovery against
primary and found no fabricated quotes — and caught the first draft
committing milder versions of the failure class it audits: two citation
errors inside P1, an asymmetric provenance standard (strict on confirming
evidence, loose on countering evidence and on P3's kept row), a Row B
instance list that dropped documented confounds and silently reopened a
Do-Not-Re-Litigate decision, and a false "holds" checkmark on the Rig 1-vs-2
row (now P8). All reviewer findings are incorporated below.

---

## P1 — Load-size row: the "strongest" FW106 comparison is partly unsupported (CONFIRMED)

**The row says:** "Strongest, session-order-matched: FW106 R26 (first dab,
larger load, harshness ~50s) vs R28 (first dab, maybe-too-large load,
harshness ~32s)... FW106 R27 (2nd dab, larger load, harshness ~16s) vs R29
(2nd dab, moderate load, harshness ~30s)... The two session-order-matched
FW106 comparisons (first-dab and 2nd-dab axes) both moved harshness ~14–18s
earlier on the heavier load."

**Primary record says:**
- R27: NO load statement exists in its own record (dab_notes, session_char,
  endpoint_note, analysis — checked directly in jars/fw106.py:463-477). Its
  own frozen analysis attributes the early harshness to SESSION ORDER:
  "Session order is the primary candidate." The "larger load" label for R27
  exists only in R28's and R29's analyses (fw106.py:491, :506) — it
  originates inside the very comparison prose it is being used to support.
- R26 "larger load" is in its `analysis` field (fw106.py:461); R29 "moderate
  load" is in its `endpoint_note` (fw106.py:501). Both AI-authored — not in
  the user's words. (First draft of this proposal placed both in
  endpoint_note; corrected by the adversarial reviewer.)
- R28 "Larger load, maybe too large" is user-verbatim (fw106.py:490). ✓

**Proposed edit:** Strike the R27-vs-R29 leg as a load comparison. Rationale
for striking this leg while keeping R26's AI-sourced label with a note: R26's
label is a same-run, logging-time record (plausibly echoing what the user
said that session); R27's label first appears in a *sibling run's* comparison
synthesis — a claim with no independent record that exists only inside the
comparison it supports is circular, not merely secondary. The pair remains
valid as a session-order data point. Keep the R26-vs-R28 leg with a
provenance note (R26's load class is AI-recorded; both loads were
"larger"-class, so the heavier/lighter ordering within the pair is itself
soft). Replace "the two session-order-matched FW106 comparisons both moved
harshness ~14–18s earlier on the heavier load" with the single supportable
statement. Soften "the strongest load-effect isolations in the log to date"
for FW106. bp4rw13 R6-vs-R7 becomes the best remaining pair on load
provenance (both loads user-verbatim, same curve, same rig) — but state its
own weaknesses in the row: R6 was a 2nd dab and R7 a next-day 1st dab
(order asymmetric), harshness timing barely differs between them, and the
intensity contrast (medium vs medium-high) carries R6's tolerance confound.
No pair in the log is clean; the row should say so rather than crown one.
Confidence stays Low; direction stays split.

**Also fold in (same row, one edit):**
- bp4rw13 R5 "big load" is analysis-sourced (R6, R7 are user-verbatim) —
  annotate the three-point gradient accordingly.
- WW Z R8/R9 load classes are analysis-sourced ("one of three roughly equal
  chunks," "the final chunk") — annotate; R8's analysis already admits the
  simultaneous equipment change.
- BB36 #2 counter-pair (R4 vs R5): session order differed (first dab vs
  second dab) — unflagged asymmetry in a row that treats order as live
  confound elsewhere. Annotate.
- WW Z R5-vs-R6 (cited via frozen analyses): R6 was both bigger-load AND
  second-dab — same asymmetry. Annotate.
- Hive #1 R6-vs-R8 (a COUNTERING pair): same provenance weakness as the
  confirming legs — neither run's dab_notes states a load; R8's "larger
  load" lives in endpoint_note/analysis (hive1.py:144, :148) and R6's
  "uncertain/smaller" is inferred in R8's analysis. Annotate identically.
  (Added by the adversarial reviewer — the first draft flagged only the
  confirming side, which would have silently tilted a direction-split row
  toward the counters.)

**Counter-reading (why not to make this edit):** `endpoint_note` labels are
written at logging time from the live conversation — they plausibly record
real user statements that never made it into dab_notes verbatim, so treating
them as unreliable may be pedantry. **Why it fails:** plausible for R26/R29,
but R27 carries no load label in its own record — its label traces only to
sibling-run comparison prose — and the row's quantified claim ("~14–18s
earlier on the heavier load") inherits precision the sourcing can't carry. The project's own rule is that evidence
cites inline observations; an AI field label is an interpretation, not an
observation, and the row should say which is which.

**Process implication (backlog candidate, not a row edit):** load size — the
log's most confound-cited variable — repeatedly lives only in AI-authored
fields (5 runs across 3 jars found this way). Cheap fix at the source: the
log-run skill's Beat 1 readback could always echo the load class into the
dab_notes verbatim record.

---

## P2 — Chest-harshness row: restructure into two rows (one confirmed overclaim, one misclassification)

**Confirmed overclaim:** the row states "Both confirming instances (papzp22
R7, bp4rw13 R8) ... persisted past when the heating cycle ended." papzp22
R7's full primary record (jars/papzp22.py:130-145) contains chest location
("It felt lower in my chest than my normal throat") and late onset — but NO
persistence statement. Its analysis even says "Two separable signals" (late
onset + chest location); persistence never appears. The post-session event
in R7's record is a productive HIT on the still-hot insert — material, not
harshness. bp4rw13 R8's persistence IS user-verbatim ("Late and after.").

**Misclassification:** Hive #1 R13/R14 are described as "throat-and-chest
that persists — matching neither cluster cleanly." Primary: R13's in-session
harshness "seemed to resolve by the end and wasn't bothering me at all";
R14's "kind of lingered and seemed to resolve by the end." What persisted was
a POST-SESSION-ONSET discomfort: "Afterwards a little bit in my chest and
throat, it feels like heartburn." That is a different phenomenon — in-session
harshness resolved, discomfort appeared after — and it matches the
methodology section's existing "post-session soreness thread" (WM R1, R9),
not the chest-harshness cluster.

**Proposed restructure — replace the one row with two:**

**Row A — In-session chest-located harshness (hot-open curves, Rig 6).**
Confirming: papzp22 R7 (chest, verbatim), bp4rw13 R8 (chest + lingered,
verbatim), LunarZ R1 (chest + lingered, verbatim). Mixed/countering:
bp4rw13 R9, R11 (throat-and-chest; no persistence *reported* — same
absence-of-statement standard applied as for papzp22 R7), Hive #1 R10
(throat-and-chest, resolved by draw 3). Confidence Low. The chest+lingers
conjunction now has exactly two documented instances (bp4rw13 R8, LunarZ R1)
— stated as an intersection to watch, not a syndrome.

**Row B — Post-session airway discomfort (onset or persistence after session
end), consolidated — WITH each instance's documented confound carried
inline** (the first draft listed these bare; the adversarial reviewer
correctly flagged that as confound-stripping):
- WM R1 ("afterward it was pronounced for a long time" — 380-open ramp,
  Rig 4). Confound, user's own attribution: "I totally did more draws than I
  should have" — the draw-count reading is the recorded primary explanation.
- WM R2 (mild, "Afterward I can feel some harshness in my throat" —
  380-open, Rig 5, 2nd dab).
- WM R9 ("Significant throat soreness after" — 460 descent open, Rig 5).
  Confounds per the existing thread: load finished early (depletion not
  separable), 2nd dab (partial session-order confound).
- FW106 R4 ("It's lingering now a few minutes later" — exhale-path, 380-open
  fast ramp, Rig 5, 2nd dab). NOTE: Session 82 Do-Not-Re-Litigate decision
  attributes R4's harshness to session order (R6 same-setup first dab came
  back clean). Listed here as a *post-session persistence* observation only;
  the in-session attribution stays settled. If you prefer, exclude R4
  entirely — the row loses little.
- FW106 R11/R12 ("Definitely hot in that afterward" / "hot in throat
  afterward" — programmed-460, Rig 5). Both were deliberate above-ceiling
  runs (`too_hot=True`); expected-hot territory, weight accordingly.
- Hive #1 R13/R14 (heartburn-like, chest and throat, post-session onset —
  440 gentle descent, Rig 6; 1st and 2nd dab of the same day).
- LunarZ R1 ("it lingered" — bounded hold, Rig 6; 3rd dab,
  slightly-larger load — both uncontrolled).
- bb362 R2 ("My throat is burning a bit still" — BASELINE_416 ramp, Rig 5).
Counters: WM R10 ("No post-session throat soreness" — user-verbatim), Hive
#1 R15 (no heartburn — session_char record; user's words were "I feel pretty
good"; same curve as R13/R14, first dab, large load). Confidence Low;
mechanism open; the confound column is the point — this row exists to stop
each new instance being read against a memory of the others.

**Methodology edit that follows:** the "Opening temperature / post-session
soreness thread" currently says "Opening temperature tracks most clearly with
the soreness signal across the three data points." The consolidated instance
list breaks that: WM R1, WM R2, FW106 R4, and bb362 R2 all occurred on
ordinary 380°F opens. Rewrite the thread to point at Row B and drop the
opening-temperature framing to one candidate among several (it still fits
WM R9, FW106 R11/12, Hive R13/14 — hot curves — but no longer "tracks most
clearly").

**Counter-reading:** the original row's conjunction (chest AND persists)
might be the real signal, and splitting could destroy it — papzp22 R7's
persistence may simply have gone unrecorded; absence of statement isn't
absence of phenomenon. **Why it fails:** a row's confidence rests on what is
documented, and the documented conjunction exists in two of five claimed
instances. The split preserves the conjunction explicitly (Row A's closing
note) while letting each axis accumulate evidence instead of forcing every
new run into "matches neither cluster."

---

## P3 — Tail-harshness ≥430°F row (High): add a rig-era scope qualifier

**The row:** 8 strains, "it is the temperature, not the shape." It stays
High — but state the provenance honestly: of the cited runs, only WW Z R3/R4
and FW106 R5 have user-verbatim (`dab_notes`) harshness records. MBD R4,
RF R2, Fembot3 R1/R2, MB9ZST R1/R2, Hive1 R5, and OC R7 are pre-dab_notes-era
runs whose harshness lives in contemporaneous AI-authored `session_char`
(per the Session 49 decision, no user-verbatim record exists for that era).
Contemporaneous session_char is decent evidence — it was written at logging
time from the user's report — but the row should not be certified on a
"user-verbatim" basis the records can't support. First-dab instances are
well represented (no systematic session-order confound). Additional citation
rot found by the reviewer: the row cites "Hive1 R2-5," but R2 has no
harshness record at all, R3 says "never harsh or burnt, just less distinct,"
and R4 defers to R3 — only R5 supports; narrow the citation to Hive1 R5.
Also note within cited strains: RF R1 (430°F baseline) recorded "No
harshness" — a clean 430°F run the row's evidence column doesn't mention.

**But:** every citation is Rig 1/2-era except FW106 R5 (Rig 5). Since the
row was written, Rig 6 has produced two 430°F runs without the signature:
papzp22 R6 (zero harshness through a full 60s first cycle at 430°F —
preemptive water confound; second cycle did show harshness) and Sour Tangie
R2 (430°F fast ramp, full 60s, no tail harshness reported for the user's
portion — occasional-user and load confounds). Neither is clean, but a High
row silently extended to a rig it predates is how future analyses go wrong.

**Proposed edit:** Notes addition only: "Evidence is Rig 1–5 era. On Rig 6
two 430°F runs lack the signature (papzp22 R6, Sour Tangie R2 — both
confounded); the Rig 6 ceiling above 425°F is unmapped. Do not extrapolate
this row to Rig 6 without a deliberate test." Two small citation tightenings
in the same edit: (a) MBD evidence: R4 is verbatim support; R1/R2's
harshness-absence at 430°F traces only to R2's analysis field, and R3 showed
mild harshness at 420°F — cite as "MBD R4 (R1–R2 uncorroborated in user
record)"; (b) BB36 #1 R1's "Hard in the tail" is ambiguous phrasing
(harshness vs intensity — its jar-mates use explicit harshness language, R1
doesn't) — either drop the citation or mark it ambiguous; the row loses
nothing either way.

**Counter-reading:** papzp22 R6's own second cycle showed medium harshness,
and Sour Tangie R2 is confounded to the point of unusability — maybe Rig 6
isn't eroding anything and the qualifier invites doubt where none is earned.
**Why it fails:** the qualifier claims only that Rig 6 is UNMAPPED, which is
true either way; the cost of the note is one sentence, the cost of silent
extrapolation is a wrong ceiling on the current daily-driver rig.

---

## P4 — Stale note: LHBH R6 "remains open" (mechanical fix)

Rig 6 equipment row Notes: "The pending first-dab 420°F test for LHBH (LHBH
R6) remains open." R6 ran June 23 (first dab, 420°F, Rig 6): "Harshness in
last 20 seconds, growing to medium by end" (lhbh.py:104). Replace with the
result, and pair it with Hive #1 R6 (first dab, 420°F, harshness ~43s) — two
strains now show first-dab 420°F Rig 6 harshness onset at ~40s, with the
load qualifier attached: Hive #1 R8 (first dab, LARGER load, same curve/rig)
was nearly clean, and load is the variable the Rig 6 row itself credits for
separating R6 from R8 — so the ~40s pairing holds for normal-load first dabs
only. No counter-reading needed; this is bookkeeping.

---

## P5 — Ramp-vs-flat row (Moderate): scope to flavor, annotate order structure

Both cited legs re-read. OC leg: R6 (ramp, 4th session of day) vs R7 (flat,
5TH session of the day) — the flat leg's worse showing is fully consistent
with session order alone; asymmetry favors the row's conclusion and is
unflagged. Hive1 leg: flat ran 1st/2nd dab, ramp ran 3rd — the ramp still won
on flavor AGAINST the order gradient ("nice distinct flavors through the
first two-thirds" on the 3rd dab vs "faded to generic" on the 1st), so the
flavor claim survives; the harshness picture doesn't favor ramp on either leg
(Hive R5 ramp: "harsh in the last ~10 seconds" vs R3 flat: "never harsh").

**Proposed edit:** keep Moderate but scope the claim to flavor staging /
session character explicitly; add the order structures to Notes; note all
evidence is Rig 1 era (retired equipment). Alternative if you prefer strict:
Moderate → Low. My recommendation is scope-plus-annotate — two strains
pointing the same direction with opposite order structures is real, if thin.

**Counter-reading (to the demotion option):** opposite order structures
across the two legs partially cancel the confound — that's modest
cross-validation, which argues for keeping Moderate. That's why the
recommendation is scoping, not demotion.

---

## P6 — Threshold-crossing row: app-precision caveat + optional second strain

WW Z R3/R4's 414°F vs 420°F onsets are app-display readings; the Session 132
decision says the app readout can't carry 1°F precision. Add that caveat to
the row Notes. Optionally add OC R11/R12 as second-strain support (harshness
"exactly when temp hit 417" on arrival vs 416 mid-hold onset — 1°F endpoint
change moved onset materially; same app caveat applies; note OC R11's load
class is analysis-sourced). Row stays Low; it gains a strain and loses false
precision.

---

## P7 — Swab floor-indicator row: add cycle-count as a documented color driver

bp4rw13's within-jar gradient (3 cycles → brown, 1 → golden, 2 →
amber-to-brown, 1 → amber; already cited in the Rig 6 row) plus the WM R15
decision (second cycle drove dark gold) and FW106 R27 ("Ran a second cycle...
maybe that's the brown?") make cycle count a documented within-strain color
driver. One Notes line in the swab row: "Before reading a warm swab as a
floor signal, check cycle count — second cycles darken swabs independent of
endpoint (bp4rw13 R5–R8 gradient, WM R15, FW106 R27)." Cheap, operational,
prevents a documented misread.

---

## P8 — Rig 1-vs-2 row: false control claim (caught by the adversarial reviewer)

The row's Notes state: "WW Z R8–9 (small load, spinner) both produced
harshness; WW Z R5 (small load, Gemlock) was clean — same curve, same
endpoint, same load class." Primary: R5 ran WWZ_RUN3 (430°F endpoint,
wwz.py:19-22); R8/R9 ran WWZ_RUN7 (420°F fast ramp, wwz.py:25-28) —
**different curve AND different endpoint**. The "same curve, same endpoint"
control claim is false (inherited from R9's frozen analysis, which says
"clean on the same endpoint"). On top of that, "same load class" rests on
the analysis-sourced load labels flagged in P1. The first draft of this
proposal passed this row with a checkmark — the reviewer caught it.

**Proposed edit:** correct the Notes sentence to state the actual
comparison (R5 at 430°F Gemlock clean vs R8/R9 at 420°F spinner harsh —
endpoint moved DOWN 10°F and harshness still appeared on the spinner, which
if anything is more suggestive, but it is not a controlled comparison and
cannot be described as one). Drop "same curve, same endpoint"; annotate the
load provenance. Row confidence is already Low and stays Low. Whether the
underlying frozen error in R9's analysis warrants a correct-frozen-data pass
is your call — the wisdom row fix doesn't require it.

**Counter-reading:** the endpoint difference cuts in the direction that
strengthens the spinner-as-contributor reading, so the row's conclusion may
survive the correction — true, and the proposed text says so; but a wisdom
row asserting a control that doesn't exist is exactly what this audit is
for, whichever way the correction cuts.

---

## Checked and holding (no edit proposed)

- MB9ZST/BB36#1 lower-ceiling row — verbatim-anchored, correctly hedged, ✓
- Draw-count-as-depletion-proxy row ✓ (FW106 R7/R8, WM R4 all verbatim)
- Water-reset row ✓ (all five instances verbatim; Rig 6-only caveat already
  present and correct)
- Descent/limiting-factor row ✓ (dbrb/Sour Tangie/LunarZ additions already
  correctly hedged "directional, not a pattern")
- Bounded-hold deliver-vs-cook working theory ✓ (R31 correction already
  embedded; five-strain status accurately stated)
- Bitter-citrus row ✓ (optionally add bp4rw13 R11 "Bitter citrus in first
  rip, lemon pledge" and LHBH R6's bitter note — but the row already says
  don't weight it; skipping is fine per trim-to-strongest)
- Cold-cure fridge row, BB36 retronasal row ✓ (bb364 R1 verbatim match)
- Rig 3 sapphire band (415–417°F) ✓ (verbatim; OC R11 load provenance noted
  in P6)
- Rig 4 and Rig 5 rows ✓ (Rig 5's draw-3 pattern and 425°F density-fix
  qualifications check out against primary). Rig 1-vs-2 moved to P8.
- Harshness-mechanism section ✓ — honest about entanglement throughout. The
  audit hunted for unexploited discriminating pairs and found none the
  section doesn't already cite; the empty-insert control and FW106 R23-vs-R5
  remain the two strongest anchors. What's genuinely missing is not analysis
  but data: matched loads at deliberately different stop times (already
  named in the section as "what would move it").
- First-run potency caution ✓ working as designed (Sour Tangie R1: "Strong
  on a deliberately modest load validates the 710 first-run potency caution")

---

## Experiment portfolio (Phase 4 — proposed next_ai_analysis updates)

Current next_* plans are mostly right; the audit changes four of them and
adds branch conditions. Researcher-participant rule applied throughout — no
design withholds a protective behavior; one flags a tradeoff explicitly.

1. **LunarZ R2** (430°F bounded hold, first dab, modest load — plan on file,
   unchanged) — ADD branch: also record post-session discomfort explicitly
   (Row B tracking): "Expected: chest harshness lighter or gone at 430°F.
   Surprising: chest harshness at same intensity → curve shape or rig, not
   peak temp. Either way, note whether anything lingers or appears after
   session end — this jar is one of two documented chest+lingers instances."
2. **papzp22 R8** (415°F-floor descent — plan on file, unchanged) — the
   on-file next_ai_analysis already tracks chest-vs-throat location; the
   only addition is one clause asking whether anything appears or lingers
   AFTER session end (Row B's axis, which the on-file text doesn't cover).
3. **Sour Tangie R3** (baseline 420°F reference — plan on file, unchanged) —
   ADD: this doubles as a Rig 6 ceiling data point for P3 if R4 later probes
   430°F deliberately: propose R4 = 430°F fast ramp, first dab, modest load,
   water available as normal (NOT withheld — if the user happens to not need
   it, the read is cleaner, but session goal wins; stated per the
   researcher-participant rule).
4. **LHBH R8** (first-dab larger load at 420°F — plan on file, unchanged) —
   ADD: state the load class out loud at logging so it lands in dab_notes
   verbatim (P1's process fix, applied); this run is the log's next
   deliberate load-axis data point.
5. **All other active jars** — current next_* plans stand as written (FW106
   R32 user's-design hold-and-descend; WM R19 first-dab ceiling check; dbrb
   R2 replicate; bp4rw13 R13 signature-repeat; BB36 #4 R2 repeat; OC R15
   normal-load repeat; BB36 #2 R7 replicate; and the four idle Rig 1-era
   jars' plans are fine if those jars resurface).

Cross-rig items (water-reset on Rig 5, descent on Rig 5) require deliberately
re-rigging the pearls — equipment decisions, listed as options, not
prescriptions.

---

## Execution notes (post-approval)

Edits land in: `HANDOFF_WISDOM.md` (P1–P8), `jars/{lunarz,papzp22,sourtangie,lhbh}.py`
STATUS `next_ai_analysis` (portfolio items 1–4), regenerate, feature branch,
PR. The evidence matrix (scratchpad `matrix/*.md`, 20 files) can be committed
to the repo as a re-runnable audit artifact or left ephemeral — your call.
