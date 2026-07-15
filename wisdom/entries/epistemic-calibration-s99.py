from wisdom_core import *

ENTRY = WisdomEntry(
    key='epistemic-calibration-s99',
    kind='decision',
    claim="Draw count was treated as a causal variable (\"2-draw ceiling,\" \"draw count "
          "as the primary harshness driver\") across ~38 analysis fields; Session 99 "
          "audited and reframed it as a correlate — the underlying mechanism remains "
          "unresolved. (provenance untagged in source)",
    guidance="Do not treat draw count as the causal or boundary variable in analysis. "
             "\"Harshness entered on draw 3\" is data; \"the 2-draw ceiling\" promotes a "
             "correlate to a boundary variable. General epistemic calibration rules "
             "were added to CLAUDE.md Epistemic Flags (general section).",
    evidence=[
        Citation(
            source='session:99',
            role='context',
            provenance='ai-authored',
            gist="Draw count was treated as a causal variable (\"2-draw ceiling,\" "
                 "\"draw count as the primary harshness driver\") across ~38 analysis "
                 "fields in COMPLETED_RUNS and STRAIN_STATUS. Session 99 audited all "
                 "analyses and reframed: draw count correlates with harshness timing "
                 "but the underlying mechanism (depletion, cumulative heat exposure, "
                 "airway sensitization) is unresolved. \"Harshness entered on draw 3\" "
                 "is data; \"the 2-draw ceiling\" promotes a correlate to a boundary "
                 "variable. General epistemic calibration rules added to CLAUDE.md "
                 "Epistemic Flags (general section).",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 99',
            text="Draw count was treated as a causal variable (\"2-draw ceiling,\" "
                 "\"draw count as the primary harshness driver\") across ~38 analysis "
                 "fields in COMPLETED_RUNS and STRAIN_STATUS. Session 99 audited all "
                 "analyses and reframed: draw count correlates with harshness timing "
                 "but the underlying mechanism (depletion, cumulative heat exposure, "
                 "airway sensitization) is unresolved. \"Harshness entered on draw 3\" "
                 "is data; \"the 2-draw ceiling\" promotes a correlate to a boundary "
                 "variable. General epistemic calibration rules added to CLAUDE.md "
                 "Epistemic Flags (general section).",
        ),
    ],
    updated='Session 99',
    resolution="Session 99 audited ~38 analysis fields treating draw count as causal; "
               "reframed as a correlate with unresolved mechanism. General epistemic "
               "calibration rules added to CLAUDE.md Epistemic Flags.",
)
