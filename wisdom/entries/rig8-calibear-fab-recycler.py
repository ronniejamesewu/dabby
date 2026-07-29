from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig8-calibear-fab-recycler',
    kind='equipment',
    claim="Rig 8 (Rig 6/7 base + Calibear Fab Recycler wet top): two runs, one strain, "
          "one curve — heavier pull and better flavor than the RBR on the user's read, "
          "no harshness on either, nothing matched. Flowback defect is a "
          "hardware-safety condition.",
    guidance="Two runs, both lhbh on one 440°F bounded hold. Do not credit the recycler "
             "with the flavor or the clean harshness read — the RBR runs are other "
             "strains and curves, and their taste read splits. Three tops, no matched "
             "pair. OPERATIONAL: flowback risks thermal shock to the insert — handle "
             "deliberately when hot.",
    grade='observation',
    grade_basis="Two runs (lhbh R9, R10), one strain, one curve. R9 a rig debut on a "
                "new curve and large-ish load; R10 held curve and rig but moved load "
                "and session order together. Neither isolates the top.",
    evidence=[
        Citation(
            source='lhbh R9',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — Rig 8 debut, 440°F 15s bounded hold descending "
                 "through 430°F at 35s to a 400°F floor, first dab, slightly larger "
                 "than normal load, three cycles. Pull \"very clearly heavier than "
                 "the rbr\"; flavor \"seemed better than rbr\"; no harshness at all, "
                 "throat or chest, during or after (both windows asked explicitly). "
                 "Beige to light golden swab, minimal residue after three trips to "
                 "440°F. Big effect. User's open question, recorded unresolved: why "
                 "a piece holding more water would read better on both flavor and "
                 "draw weight, against the expectation that water costs terpenes and "
                 "adds drag.",
            confounds="Rig debut with no matched comparison — this jar has never run "
                      "on the RBR, so the RBR contrast crosses strain, curve, and "
                      "session order as well as top. Curve was also new to the jar "
                      "(first 440°F run) and the load ran slightly large, so the "
                      "clean harshness read is not attributable to the top. Recycler "
                      "and bell differ in airpath geometry, not only water volume, "
                      "so \"more water\" may not be the operative variable.",
        ),
        Citation(
            source='lhbh R10',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — same curve and rig as R9, second dab, moderate load, "
                 "single cycle stopped on depletion with ~12s left. No harshness at "
                 "all, throat or chest, asked in both windows. Beige swab, next to no "
                 "reclaim. Intensity a creeping medium. User's read on the top "
                 "strengthened but stayed hedged: \"I hate to say it because this is "
                 "cheap lazy glass but the function might be my favorite so far. Too "
                 "early to say without trying other strains.\"",
            confounds="Still no matched comparison — both Rig 8 runs are this strain on "
                      "this curve, and this jar has never run on the RBR. Load and "
                      "session order both moved from R9, so the pair isolates nothing "
                      "about the top; the milder session (one cycle, less material) "
                      "also makes its clean harshness read less surprising than R9's. "
                      "Light swab off a single cycle is expected independent of the "
                      "top, and minimal reclaim on an observed-depleted load is close "
                      "to tautological.",
        ),
    ],
    positions=[
        Position(
            stated='July 28, 2026 (lhbh R9)',
            text="Rig 8 debut. Acquired deliberately as a cheap read on recycler / "
                 "multi-path straight-flow function against the RBR's bell design, "
                 "with a better piece to follow if the function is worth it — an "
                 "obsolete design still in stock. The run came back the jar's "
                 "cleanest in nine (second no-harshness run ever, first since Run 1) "
                 "with a light minimal swab after three cycles, but the rig debut "
                 "sits on top of a new curve and a slightly large load, and the RBR "
                 "comparison is cross-strain and cross-curve. Nothing here isolates "
                 "the top. The one thing the run does establish independent of the "
                 "flavor question: this is the first hot-open run on a top that is "
                 "neither the stock bubbler nor the RBR — a third airpath and "
                 "posture condition — and it threw no chest signal in either window. "
                 "Held at observation on one run.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R10)',
            text="The rerun the debut asked for came back clean again and the user's "
                 "read on the top strengthened, but it did not deliver the match it "
                 "was set up for: load and session order both moved, so R9 and R10 "
                 "isolate nothing between them. What the second run does buy is "
                 "narrower than it looks — it removes the new-glass objection (the top "
                 "is no longer novel) and it shows the clean harshness result was not "
                 "a one-off. It buys nothing at all on the flavor and draw-weight "
                 "claims, which are the whole reason the top was acquired, because "
                 "both remain single-strain single-curve impressions with no RBR run "
                 "on this jar to sit beside them. Two runs is not two data points on "
                 "the top. Held at observation.",
        ),
    ],
    counter_reading="Everything attributed to the top is equally explained by the curve "
                    "(this jar's only 440°F bounded hold), the load, or session order — "
                    "and the RBR baseline it is compared against is itself two unmatched "
                    "runs on other strains whose taste read already splits. R10 does not "
                    "answer this: it repeats the same strain on the same curve, so it "
                    "confirms the pairing is reproducible without showing the top caused "
                    "any of it. A skeptic reads both Rig 8 runs as good runs on a good "
                    "curve, with the glass contributing nothing demonstrable — a reading "
                    "the user's own hedge (\"too early to say without trying other "
                    "strains\") anticipates.",
    watch_for="The matched comparison, still owed: same strain and curve on the RBR "
              "(Rig 7) — lhbh R11 is set up for it. Whether the heavier pull reproduces "
              "off new glass. Any flowback reaching the insert.",
    updated='lhbh R9 (July 28, 2026) — Rig 8 debut; lhbh R10 (July 28, 2026) — second run, no matched comparison yet.',
)
