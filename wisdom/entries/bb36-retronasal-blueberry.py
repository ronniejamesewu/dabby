from wisdom_core import *

ENTRY = WisdomEntry(
    key='bb36-retronasal-blueberry',
    kind='pattern',
    claim="BB36 family retronasal blueberry — delayed post-session olfaction from the "
          "throat, minutes after the dab.",
    guidance="Not actionable for curve design. Watch for recurrence on subsequent BB36 "
             "runs and on unrelated strains.",
    grade='observation',
    grade_basis="Two jars, same seed pop — bb362 now twice (R1, R7), bb364 once; "
                "within-lineage pattern only.",
    evidence=[
        Citation(
            source='bb362 R1',
            role='confirms',
            provenance='user-verbatim',
            gist="Retronasal blueberry \"much much after taking the dab — it seems to "
                 "come up my throat too\".",
            confounds="Same seed pop as the other confirming jar — within-lineage only; "
                      "single run.",
        ),
        Citation(
            source='bb364 R1',
            role='confirms',
            provenance='ai-authored',
            gist="Retronasal blueberry ~10 minutes post-session from throat — first "
                 "run, baseline on Rig 6.",
            confounds="Same seed pop; single run.",
        ),
        Citation(
            source='bb362 R7',
            role='confirms',
            provenance='user-verbatim',
            gist="July 23, 2026 — the jar's last dab, purple 430°F descent on Rig 7 — "
                 "\"a clear blueberry note, coughing it up my throat many minutes "
                 "after\"; identical throat-route presentation to R1, so the pattern "
                 "now repeats within a single pheno, not just across the two siblings.",
            confounds="Same jar as the R1 instance — within-pheno recurrence, not a new "
                      "lineage member.",
        ),
    ],
    positions=[
        Position(
            stated='Session 121',
            text="Both are phenotypes from Matt's 4-seed pop. Within-lineage pattern "
                 "only until it appears on an unrelated strain.",
        ),
        Position(
            stated='July 23, 2026 (bb362 R7)',
            text="bb362 R7 is a second within-pheno instance (identical to R1's "
                 "throat-route presentation), so the pattern repeats within a single "
                 "jar, not only across the sibling phenos. Still within-lineage — the "
                 "open question is recurrence on a strain outside Matt's seed pop. Held "
                 "at observation.",
        ),
    ],
    watch_for="Recurrence on a strain outside the seed pop — that would make this a "
              "general phenomenon, not a lineage quirk. Within-lineage recurrence is "
              "now seen both across the siblings and within bb362 (R1, R7).",
    updated='Session 121; bb362 R7 July 23, 2026',
)
