---
name: analysis-toolkit
description: Named analysis recipes for drafting per-run `analysis` and `next_ai_analysis` in this Dabby project. Use at log-run step 5 — before drafting, scan these recipes and select the ones whose trigger conditions match the run being logged. Each recipe states the confidence language it licenses and the failure mode it guards against. This skill constrains synthesis; it does not generate conclusions — the jar's run history and the wisdom layer are still the primary inputs. Trigger when drafting analysis for a completed run, or when reviewing an existing analysis for epistemic hygiene.
---

# Analysis Toolkit

Named analysis moves for per-run synthesis. Each recipe is a repeating
pattern in this project's analytical work — extracted from the wisdom layer,
the failure-mode lists, and 140+ runs of frozen analyses.

## How to use

At log-run step 5, before drafting `analysis` and `next_ai_analysis`:

1. Read the trigger conditions below.
2. Select every recipe whose trigger matches the current run's data.
3. Apply the steps and use only the licensed confidence language.
4. If a recipe's worked example resembles the current situation, read the
   cited runs' frozen analyses in the jar file — the example is a pointer,
   not a substitute for the source.

Multiple recipes fire on most runs. The confidence ladder (Recipe 8) fires
on every run — it is always applicable.

## When NOT to use

- **Not a substitute for reading the jar.** The recipes constrain how you
  write, not what you write. The run history, `HANDOFF_WISDOM.md`, and
  `Dabby_Methodology.md` are still the primary inputs.
- **Recipes license confidence language — they don't generate conclusions.**
  A recipe that fires does not mean you should write about that topic. It
  means *if* you write about that topic, use the licensed language.
- **Do not cite recipe numbers in user-facing text.** These are internal
  assembly instructions; the user sees analysis prose, not recipe labels.
- **Do not copy recipe text into `analysis`.** Synthesize from the run data
  and the jar history; recipes shape the epistemic framing, not the words.

---

## Recipes

### 1. Session-order-matched comparison

**Trigger:** Comparing two or more runs to isolate a variable (load size,
endpoint, curve shape) where session order (first dab, second dab, etc.)
differs between the compared runs.

**Steps:**
1. Check `sessions_prior_today` on both runs.
2. If session order differs, flag it as a confound before drawing any
   conclusion about the intended variable.
3. The strongest comparisons match session order *and* vary only one other
   input. Cite the match explicitly when it holds.

**Licensed confidence language:**
- Session order matched: "session-order-matched comparison; [variable] is
  the differing input"
- Session order unmatched: "[variable] changed, but session order also
  differs — can't isolate"
- Never assert a variable is "the driver" from an unmatched comparison.

**Guarded failure mode:** Treating any cross-run comparison as clean
isolation when session order differs. Session order is the most frequent
uncontrolled confound in this log.

**Worked example:** FW106 R26/R28 (both first dab of day, same curve —
load sizes differ: R26 larger → harshness ~50s, R28 maybe-too-large →
harshness ~32s) and R27/R29 (both second dab, same curve — R27 larger →
harshness ~16s, R29 moderate → harshness ~30s). Two session-order-matched
pairs, each showing ~14–18s harshness shift from load. The cross-pairing
(R28 first dab/too-large at ~32s vs. R29 second dab/moderate at ~30s)
shows session order and load roughly offsetting — directional for both
having similar-magnitude effects. See `jars/fw106.py` R26–R29.

---

### 2. Equipment-confound check

**Trigger:** Any cross-run comparison, before writing. Fires on every
analysis that references a prior run.

**Steps:**
1. Compare the `equipment` field (the `EquipmentConfig` / `RIG_N`
   constant) on both runs.
2. If equipment differs: state "equipment is an unresolved confound"
   and do not attribute differences to the intended variable alone.
3. If equipment matches: the comparison is clean on that axis — say so.

**Licensed confidence language:**
- Equipment matched: "same rig; equipment is controlled"
- Equipment differs: "equipment changed simultaneously — [rig A] vs.
  [rig B]; can't attribute to [intended variable] alone"
- Never omit the equipment check. Per `Dabby_Handoff_Notes.md`, abandoning
  established equipment framing for an improvised mechanism is a documented
  failure mode.

**Guarded failure mode:** The Session 140 seven-run equipment mislog.
bp4rw13 R5–R8 and WM R16–R18 were all logged as Rig 5 due to stale
jar-local defaults after 14–15-day gaps; corrected to Rig 6 on July 2,
2026. Cross-rig comparisons masqueraded as within-rig data. See the
`HANDOFF_WISDOM.md` failure-mode row "Equipment default taken from
`COMPLETED_RUNS` list position" and `Dabby_Handoff_Notes.md` Decisions.

**Worked example:** WM R16 (originally logged Rig 5, descent curve, clean
first cycle) was cited as the first descent-curve data point on Rig 5.
After correction to Rig 6, the "descent curves viable on Rig 5" claim
collapsed — descent remains empirically untested on Rig 5. Seven runs,
five strains, all had downstream analytical claims revised.

---

### 3. Load-size reasoning under the unresolved direction split

**Trigger:** When load size varies between compared runs and harshness
onset timing or intensity differs.

**Steps:**
1. Check the cross-strain load-size row in `HANDOFF_WISDOM.md` (read it
   live — the evidence and direction count update with the log).
2. Note the direction split: as of July 3, 2026, four strains show larger
   load → earlier/more harshness or intensity (WW Z, LHBH, FW106,
   bp4rw13); two show no change or less (BB36 #2, Hive #1).
3. Frame load as a modulator, not a driver. Within-strain consistency
   may be strong (FW106's paired comparisons are the cleanest in the
   log); cross-strain generalization is unsettled.

**Licensed confidence language:**
- Within-strain: "load modulated harshness timing by ~Ns on this strain"
- Cross-strain: "directional for load as a contributor; cross-strain
  direction is unresolved (N strains for, M against)"
- Never: "load drove the harshness", "load is the primary factor"

**Guarded failure mode:** Treating load size as a settled cross-strain
harshness driver when the evidence splits.

**Worked example — the strongest case and the strongest counter:**
FW106 R26/R28 + R27/R29 (two session-order-matched pairs, both
showing ~14–18s shift from load) vs. BB36 #2 R4/R5 (larger-than-normal
vs. minimal load on the same curve, Rig 5 — identical outcomes:
dark golden swab, slight draw-2 harshness, wispy vapor, medium-high
intensity; "felt exactly the same" in the user's words). See
`jars/fw106.py` R26–R29 and `jars/bb362.py` R4–R5.

---

### 4. Draw count as depletion proxy

**Trigger:** When harshness is attributed to a specific draw number, or
when draw count is cited as a variable.

**Steps:**
1. Check whether reclaim data or vapor character indicates depletion at
   harshness onset. "Very little reclaim" or "vapor ended" at the moment
   of harshness points to depletion; "dense vapor still present" points
   away from it.
2. Frame draw count as a proxy for cumulative exposure or depletion — not
   a boundary variable. "Harshness entered on draw 3" is data; "the
   3-draw ceiling" promotes a correlate to a causal variable.
3. Cross-reference the `HANDOFF_WISDOM.md` "Draw count is a proxy for
   material depletion" row for the current evidence state.

**Licensed confidence language:**
- "Harshness entered on draw N" (data)
- "Consistent with material depletion — [reclaim/vapor evidence]"
- "Draw count is a proxy; the underlying mechanism is unresolved"
- Never: "N-draw ceiling", "draw count is the harshness driver",
  "draw count as the primary variable"

**Guarded failure mode:** Session 99 epistemic audit — 38 analysis fields
promoted draw count from a correlate to a boundary variable ("2-draw
ceiling", "draw count as the primary harshness driver"). See
`HANDOFF_WISDOM.md` Epistemic Calibration.

**Worked example:** FW106 R7 (3 draws, large load — harsh on draw 3;
golden swab, normal reclaim) vs. FW106 R8 (2 draws, smaller load — very
little reclaim, harshness midway through draw 2, material spent before
session end). R8 is the refinement: harshness tracked depletion, not
draw count — material exhausted mid-draw-2, harshness followed regardless
of the draw number. See `jars/fw106.py` R7–R8.

---

### 5. Swab as floor indicator

**Trigger:** When referencing swab color in analysis — always, on every
run.

**Steps:**
1. Dark/burnt residue (amber-toward-brown or darker): reliable floor
   signal — state "floor signal, reduce endpoint."
2. Within the light-golden-to-amber range: too many uncontrolled
   variables (load size, material starting color, oxidation, timing,
   pressure) to reliably distinguish curve shapes or small endpoint
   differences. Do not over-interpret.
3. Never compare swab color across strains — within-strain only.
4. A clean swab does not rule out harshness or thermal degradation.
   Session character is the operative signal for everything above the
   floor.

**Licensed confidence language:**
- Dark swab: "reliable floor signal"
- Clean swab + harshness: "clean swab, but session character indicates
  [harshness/degradation] — swab is not a fine-grained calibration metric"
- Clean swab, no issues: "within the clean range" or "no floor signal"
- Never: "lighter swab confirms better vaporization" (within the clean
  range), or "swab shows the curve is dialed"

**Guarded failure mode:** Using a clean swab to assert fine-grained
calibration success, or dismissing session-character harshness because the
swab looked clean.

**Worked example — three independent demonstrations:**
(a) OC R7 (430°F flat hold): plain amber clean swab, but "harsh in last
20 seconds" — clean swab did not predict harshness absence.
(b) WW Z R5 vs. R6 (same curve, same equipment, same light golden swab):
R5 no harshness/mild; R6 tail harshness/hard hit — load size moved
session character without moving swab.
(c) FW106 R11–R12 (Rig 5, high 440s): light gold swab + toasty taste +
hot aftermath — clean swab while material degraded above the ceiling.
Session character, not swab, was the operative signal.
See `jars/oc.py` R7, `jars/wwz.py` R5–R6, `jars/fw106.py` R11–R12.

---

### 6. Threshold-crossing vs. temperature-pinned harshness

**Trigger:** When harshness onset is reported with a specific temperature
reading from the app display, or when attributing harshness to "arriving
at" a particular temperature.

**Steps:**
1. Check whether the same curve produced harshness at different display
   temperatures across runs. If yes, harshness built continuously and was
   *noticed* at a threshold, not *caused* at a temperature.
2. App temperature readouts are subject to Bluetooth lag, display refresh,
   and controller-model interpolation — do not trust to 1°F precision.
   See `Dabby_Handoff_Notes.md` Decisions (app readout limitation).
3. Frame onset as "harshness entered at [time or draw]" (data) rather than
   "harshness at [temp]°F" (implies temperature causation).

**Licensed confidence language:**
- "Harshness entered at [time remaining / draw N]" (data)
- "Harshness appeared at [temp]°F on the display" (observation, not
  mechanism)
- "Consistent with threshold-crossing — harshness builds through the ramp
  and registers when it crosses a perceivable level"
- Never: "harshness caused by arriving at [temp]°F" when the evidence is
  a single display reading

**Guarded failure mode:** Pinning harshness to a fixed temperature when
the evidence supports continuous buildup.

**Worked example:** WW Z R3 (ramp to 430°F — harshness at 414°F on
display, mid-ramp) vs. WW Z R4 (identical curve — harshness at 420°F on
display, mid-ramp). 6°F shift on the same curve. The user's own framing:
"harshness builds continuously and registers when it crosses a perceivable
level, not pinned to a specific temperature." See `jars/wwz.py` R3–R4.

---

### 7. Boiling-point / mass-conservation check

**Trigger:** Before writing any analysis that proposes selective delivery
of one compound class over another, fractional-distillation reasoning, or
"narrow delivery window" framing.

**Steps:**
1. Check whether all relevant compounds (terpenes and cannabinoids) are
   above their boiling points at the operating temperature. Boiling points
   are in `TERPENE_REFERENCE` in `Dabby_Core.py`; THC onset ~315°F,
   progressive to ~428°F (see `Dabby_Methodology.md` §4).
2. If all are above boiling point: no selective exclusion mechanism exists.
   Everything is simultaneously in the gas phase. Fractional distillation
   requires some components to remain below boiling point. Do not apply it.
3. Mass conservation: when material boils off, it goes to the inhaled
   bolus. Modest intensity alongside minimal reclaim is most
   parsimoniously explained by session order or load, not incomplete
   delivery.

**Licensed confidence language:**
- "All relevant volatiles are above boiling point at [temp]°F — no
  selective-delivery mechanism applies"
- "Modest intensity on a [Nth] dab is most parsimoniously session order"
- Never: "selectively delivers terpenes while limiting cannabinoids",
  "narrow delivery window", or any distillation-column framing when
  compounds are above boiling point

**Guarded failure mode:** FW106 R24 analysis (Session 130) — two draft
corrections required. Descent curve opened at 440°F; modest intensity on
the second dab of the day was incorrectly attributed to a "narrow delivery
window" and framed as selective terpene delivery excluding cannabinoids.
At 440°F, terpenes and cannabinoids are all above their boiling points
simultaneously. The honest read: session order (second dab). See
`HANDOFF_WISDOM.md` "Applying fractional-distillation / selective-boiling
reasoning" failure-mode row and `jars/fw106.py` R24.

---

### 8. Confidence ladder

**Trigger:** Every `analysis` and `next_ai_analysis` draft. Always fires.

**Steps:**
1. Count the supporting data points for every claim in the draft.
2. Match language to the evidence level:

| Evidence | Licensed language | Prohibited |
|---|---|---|
| One run | "single data point", "one run", "observation", "not a pattern" | "pattern", "consistent" (with itself) |
| Two consistent runs | "directional", "consistent with [hypothesis]", "two-run signal" | "confirmed", "established" |
| Multi-strain pattern | "pattern across N strains", "survives disconfirmation", "N independent strain contexts" | "proven", "the data shows" |
| Any level | "plausible", "consistent with", "directional support for" | "confirmed", "established", "resolved", "the data shows", "proves" |

3. When promoting a claim's confidence (even implicitly through wording),
   state the strongest counter-reading of the evidence and why it fails.
   If you can't produce a counter-reading you believe in, flag the
   promotion for user review rather than manufacturing a strawman.
4. Check for compression drift: if condensing or paraphrasing prior
   analysis, verify no confound clauses were dropped. Drift follows the
   author's working narrative — see `HANDOFF_WISDOM.md` "Strength drift
   during compression" failure mode.

**Licensed confidence language:** See the table above. The wisdom file's
lexicon is the closed set — do not introduce new certainty-language.

**Guarded failure mode:** Over-claiming certainty in analysis language.
Session 99 audit found 38 instances of "confirmed", "established", and
"the data shows" for patterns that were merely consistent with hypotheses.
See `HANDOFF_WISDOM.md` Epistemic Calibration and `CLAUDE.md` Epistemic
Flags.

**Worked example:** The cross-strain tail-harshness pattern at ≥430°F has
8 strains and High confidence in the wisdom table — yet even this is
framed "survives disconfirmation" (both ramp and flat-hold shapes show it;
it is the temperature, not the shape). It is never "proven" or "the
ceiling is 430°F." Each run updates priors; no run closes questions.

---

### 9. "Inputs hard to isolate" before mechanism invention

**Trigger:** When a run's observations don't fit prior patterns and the
impulse is to construct a physical or chemical causal chain to explain
the surprise.

**Steps:**
1. Count how many variables changed between the surprising run and its
   nearest comparators (load, endpoint, curve shape, rig, session order,
   draw count, material batch).
2. If more than one changed, or the run is simply noisy: lead with
   "the inputs are hard to isolate" or "this jar has broad run-to-run
   variability."
3. Do not fabricate a mechanism from uncontrolled observations. A causal
   chain must be physically correct and testable — not just plausible-
   sounding.
4. A hypothesis is fine. Label it as such ("one possible mechanism is...")
   and give it single-data-point weight.

**Licensed confidence language:**
- "The result is hard to interpret — [N variables] changed simultaneously"
- "This jar has documented run-to-run variability; inputs can't be cleanly
  isolated"
- "One possible mechanism is [X], but [confound Y] is equally consistent"
- Never: constructing a causal chain from a single uncontrolled observation
  and presenting it as explanation

**Guarded failure mode:** BB36 #2 R4 (Session 88) — wispy vapor and
minimal harshness despite a larger-than-normal load, counter to
predictions. Rather than accepting the observation as hard to interpret,
the draft fabricated a draw-timing mechanism: "first draw ended at 404°F
→ less vapor density → wispy + low harshness." Physically wrong — draw
timing affects what the user inhales per draw, not what the device
produces; "wispy" is a device output observation, not an inhale-duration
artifact. The user pushed back. The honest answer: "this jar has broad
run-to-run variability that's hard to trace to specific inputs." See
`jars/bb362.py` R4 and `Dabby_Handoff_Notes.md` "Constructing a physical
mechanism" failure mode.

---

### 10. Conversational hypothesis handling

**Trigger:** When the user floats a hypothesis casually during run
reporting — "maybe it's asking for more heat", "could be the equipment",
"I think the harshness is accumulating over days."

**Steps:**
1. Capture the hypothesis verbatim in `dab_notes`.
2. In `analysis`, attribute as "user suggested X" or "user's hypothesis:
   X" — never as a finding.
3. Give it single-data-point weight. Do not promote to a working
   position until subsequent runs test and support it.
4. When a subsequent run tests the hypothesis: cite the original
   suggestion and state whether the new data is consistent, inconsistent,
   or ambiguous.

**Licensed confidence language:**
- "User suggested [X]"; "user's hypothesis: [X]"
- After supporting run: "consistent with user's [X] hypothesis from
  Run N"
- After contradicting run: "[X] hypothesis weakened by Run N — [counter-
  evidence]"
- Never: promoting a single-session user hypothesis to "the mechanism is
  [X]" or treating it as a working position in analysis without
  confirming runs

**Guarded failure mode:** Promoting a conversational hypothesis into a
working analysis position. See `Dabby_Handoff_Notes.md` "Promoting a
conversational hypothesis" failure mode.

**Worked example:** FW106 R14 — user suggested that harshness is "heat
accumulation in the throat — building not just within a session but over a
longer timeframe." Captured at stated weight in R14's analysis ("user
suggests... maps to and extends the airway/thermal-dose hypothesis... mild
directional support"). R15 (identical conditions, next day, no rest day):
dramatically better result. If multi-day accumulation were the primary
driver, R15 should have been similar or worse. Demoted from directional
support to open speculation. See `jars/fw106.py` R14–R15 and
`HANDOFF_WISDOM.md` Tail Harshness Mechanism → Airway sensitization.

---

## Provenance and maintenance

Created 2026-07-04 in a frontier-class session (Opus 4.6). Recipe content
authored against `HANDOFF_WISDOM.md` (post-pass-3), `Dabby_Methodology.md`,
and the failure-mode lists in both `HANDOFF_WISDOM.md` and
`Dabby_Handoff_Notes.md`. Every run citation was verified against the jar
file before writing.

Verify these still hold if a recipe's worked example doesn't match reality:

```
# Recipe 1 — session-order-matched comparison (FW106 R26-R29):
grep -n "sessions_prior_today" jars/fw106.py | tail -8

# Recipe 2 — equipment-confound check (the 7-run correction):
grep -n "corrected.*Rig 6\|corrected July 2" jars/bp4rw13.py jars/wm.py

# Recipe 3 — load-size direction split (wisdom row):
grep -n "Load size influences" HANDOFF_WISDOM.md

# Recipe 4 — draw count as depletion proxy (wisdom row + epistemic audit):
grep -n "Draw count is a proxy\|Epistemic Calibration" HANDOFF_WISDOM.md

# Recipe 5 — swab as floor indicator (wisdom row):
grep -n "Swab is a floor indicator" HANDOFF_WISDOM.md

# Recipe 6 — threshold-crossing (WW Z R3-R4 analyses):
grep -n "414.*display\|420.*display" jars/wwz.py

# Recipe 7 — fractional-distillation failure (wisdom failure-mode row):
grep -n "fractional.distillation\|selective.boiling" HANDOFF_WISDOM.md

# Recipe 8 — confidence ladder (epistemic flags + wisdom lexicon):
grep -n "Epistemic Flags\|Match confidence to evidence" CLAUDE.md

# Recipe 9 — mechanism invention (BB36#2 R4 failure mode):
grep -n "Constructing a physical mechanism" Dabby_Handoff_Notes.md

# Recipe 10 — conversational hypothesis (failure mode):
grep -n "Promoting a conversational hypothesis" Dabby_Handoff_Notes.md
```

Dogfood-test protocol: give a fresh agent a historical run's inputs (the
user's report plus prior jar history, with the frozen analysis stripped).
Check: (a) which recipes it selects, (b) whether its draft's confidence
language stays within what the cited evidence licenses, (c) whether it
catches the failure mode each recipe guards against. Grade against the
actual frozen analysis. A passing result: the draft uses only licensed
language and doesn't trip any guarded failure mode. A failing result: the
draft over-claims, invents a mechanism, or misses an equipment confound —
identify which recipe should have fired and didn't.

Dogfood-test status: **passed** (Session 147, 2026-07-04). Two Sonnet
agents tested against FW106 R28 (frozen analysis stripped). Both selected
correct core recipes (1, 2, 3, 5, 8), stayed within confidence bounds
(no "confirmed" or "established" for the load signal), and caught all
guarded failure modes. Delta from frozen analysis was synthesis depth
(ceiling framing, specific cross-strain run citations) — expected and
acceptable for mechanized recipe application.
