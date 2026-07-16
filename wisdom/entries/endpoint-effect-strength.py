from wisdom_core import *

ENTRY = WisdomEntry(
    key='endpoint-effect-strength',
    kind='pattern',
    claim="Higher endpoint → stronger effect (larger bolus, faster peak).",
    guidance="Low confidence — only 2 of 3 cited data points are unconfounded (OC R5 "
             "and papzp22 R6); the MB9ZST leg is equipment-confounded. Do not treat "
             "this as more than directional.",
    grade='observation',
    grade_basis="Low — 2 directional data points (OC R5 and papzp22 R6); others "
                "confounded.",
    evidence=[
        Citation(
            source='oc R5',
            role='confirms',
            provenance='ai-authored',
            gist="460°F — stronger effect noted. (provenance untagged in source)",
            confounds="none noted",
        ),
        Citation(
            source='mb9zst R1',
            role='context',
            provenance='ai-authored',
            gist="430°F Gemlock — strong effects noted but equipment confounded. "
                 "(provenance untagged in source)",
            confounds="Equipment confounded (Gemlock era).",
        ),
        Citation(
            source='mb9zst R2',
            role='context',
            provenance='ai-authored',
            gist="430°F Gemlock — strong effects noted but equipment confounded. "
                 "(provenance untagged in source)",
            confounds="Equipment confounded (Gemlock era).",
        ),
        Citation(
            source='papzp22 R6',
            role='confirms',
            provenance='mixed',
            gist="June 22, 2026 — 430°F on Rig 6, 'pretty fucking hard'; session order "
                 "matched to prior 425°F run with same rig; second independent "
                 "unconfounded data point.",
            confounds="Session order matched to prior 425°F run with same rig — "
                      "described in source as the second independent unconfounded "
                      "data point (i.e., no confound identified for this instance).",
        ),
    ],
    positions=[
        Position(
            stated='Session ~10',
            text="Rate-of-delivery hypothesis: same material at lower temps over a "
                 "longer curve delivers similar total cannabinoids but with a slower, "
                 "smoother absorption profile; CBN hypothesis rejected.",
        ),
    ],
    updated='Session ~10',
)
