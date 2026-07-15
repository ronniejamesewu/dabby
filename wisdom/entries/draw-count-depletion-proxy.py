from wisdom_core import *

ENTRY = WisdomEntry(
    key='draw-count-depletion-proxy',
    kind='pattern',
    claim="Draw count is a proxy for material depletion — harshness enters when the "
          "load is spent.",
    guidance="Load size discipline matters alongside session length discipline. Higher "
             "endpoint accelerates depletion; the complement is a shorter session — stop "
             "when vapor drops rather than lowering temperature to extend it.",
    grade='directional',
    grade_basis="Two strains, multiple sessions; R8 refines draw-count to "
                "material-depletion framing.",
    evidence=[
        Citation(
            source='fw106 R7',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, 3 draws large load — draws 1–2 clean, draw 3 harsh. Provenance "
                 "untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R8',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, 2 draws smaller load — very little reclaim, harshness "
                 "mid-draw-2, material spent before session end. Provenance untagged in "
                 "source.",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R4',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, 3 draws — draws 1–2 clean, harshness entered on draw 3 at 14s "
                 "remaining. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R6',
            role='context',
            provenance='ai-authored',
            gist="One of two 2-draw, larger-load runs with no harshness (\"FW106 R6 and "
                 "R10 ... no harshness first and last dab of day\") — supports the clean "
                 "profile when load is sufficient. Source does not pin which of R6/R10 "
                 "was the first vs last dab. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R10',
            role='context',
            provenance='ai-authored',
            gist="One of two 2-draw, larger-load runs with no harshness (\"FW106 R6 and "
                 "R10 ... no harshness first and last dab of day\") — supports the clean "
                 "profile when load is sufficient. Source does not pin which of R6/R10 "
                 "was the first vs last dab. Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 91',
            text="Harshness has consistently appeared later in the session (often around "
                 "draw 3) when load is large enough to last; small loads can exhaust "
                 "before draw 2 ends, triggering harshness regardless of draw count — "
                 "draw count is a correlate, not necessarily the causal variable. Load "
                 "size discipline matters alongside session length discipline. FW106 R6 "
                 "and R10 (both 2 draws, larger load, no harshness first and last dab of "
                 "day) support the clean profile when load is sufficient. Implication of "
                 "the depletion framing: higher endpoint accelerates depletion; the "
                 "complement is a shorter session — stop when vapor drops rather than "
                 "lowering temperature to extend it.",
        ),
    ],
    counter_reading="Draw count is a correlate, not necessarily the causal variable — "
                    "small loads can exhaust before draw 2 ends, triggering harshness "
                    "regardless of draw count. Harshness has only consistently appeared "
                    "around draw 3 when load was large enough to last, so draw count and "
                    "depletion are confounded across these runs; the boundary may be "
                    "depletion, cumulative heat exposure, or something else rather than "
                    "draw number.",
    updated='Sessions 82, 91',
)
