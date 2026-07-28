from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig8-calibear-fab-recycler',
    kind='equipment',
    claim="Rig 8 (Rig 6/7 base + Calibear Fab Recycler wet top): one run — heavier "
          "pull, better flavor than the RBR, no harshness at all, nothing matched. "
          "Carries a water-flowback defect that is a hardware-safety condition.",
    guidance="One run. Do not credit the recycler with the flavor or the clean "
             "harshness read — the RBR runs are other strains, other curves. Three "
             "tops now in rotation, no matched comparison between any pair. "
             "OPERATIONAL: the flowback defect risks thermal shock to the insert — "
             "handle deliberately whenever running hot.",
    grade='observation',
    grade_basis="One run (lhbh R9), one strain, one curve, on a rig debut — load ran "
                "slightly larger than normal and the curve was new to the jar, so "
                "nothing about the top is isolated from anything else.",
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
    ],
    counter_reading="Everything attributed to the top here is equally explained by the "
                    "curve (the jar's first 440°F bounded hold), the load, or first-dab "
                    "session order — and the RBR baseline it is being compared against "
                    "is itself two unmatched runs on other strains whose taste read "
                    "already splits. A skeptic reads Run 9 as a good run that happened "
                    "to be the first on new glass, with the top contributing nothing "
                    "demonstrable.",
    watch_for="A matched-load matched-curve rerun on this top (lhbh R10); whether "
              "the heavier-pull read reproduces off new glass; any flowback reaching "
              "the insert.",
    updated='lhbh R9 (July 28, 2026) — Rig 8 debut.',
)
