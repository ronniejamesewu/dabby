from wisdom_core import *

ENTRY = WisdomEntry(
    key='bb36-retronasal-blueberry',
    kind='pattern',
    claim="BB36 family retronasal blueberry — delayed post-session olfaction from the "
          "throat, minutes after the dab.",
    guidance="Not actionable for curve design. Watch for recurrence on subsequent BB36 "
             "runs and on unrelated strains.",
    grade='observation',
    grade_basis="Two jars, same seed pop, one run each; within-lineage pattern only.",
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
            confounds="Same seed pop; single run; different rig than the bb362 "
                      "instance.",
        ),
    ],
    positions=[
        Position(
            stated='Session 121',
            text="Both are phenotypes from Matt's 4-seed pop. Within-lineage pattern "
                 "only until it appears on an unrelated strain.",
        ),
    ],
    watch_for="Recurrence on later BB36 runs, or on any strain outside the seed pop — "
              "the latter would make this a general phenomenon, not a lineage quirk.",
    updated='Session 121',
)
