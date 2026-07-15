from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-wm-dark-gold-second-cycle',
    kind='decision',
    claim="WM dark gold swab was second-cycle driven, not material — do not re-litigate",
    guidance="WM R15 (June 11, 2026): single cycle, 60s hold → beige swab, breaking the "
             "streak of four consecutive dark gold 2x2 runs. The second cycle (reheat) "
             "was driving the dark gold, not the material itself or the 420°F endpoint.",
    evidence=[
        Citation(
            source='watermellos R15',
            role='confirms',
            provenance='ai-authored',
            gist="Single cycle, 60s hold → beige swab, breaking the streak of four "
                 "consecutive dark gold 2x2 runs. The second cycle (reheat) was driving "
                 "the dark gold, not the material itself or the 420°F endpoint.",
            confounds="none noted",
        ),
    ],
    updated='Session 103',
)
