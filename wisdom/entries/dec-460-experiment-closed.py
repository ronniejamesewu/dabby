from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-460-experiment-closed',
    kind='decision',
    claim="Ramp-to-460°F experiment on Rig 5 is closed",
    guidance="No further 460°F experiments on Rig 5 without a longer session or a "
             "different insert.",
    evidence=[
        Citation(
            source='fw106 R11',
            role='confirms',
            provenance='ai-authored',
            gist="Curve programmed to arrive at 460°F at the 40s terminus (no hold) — "
                 "sapphire thermal lag put actual temperature at terminus in the high "
                 "440s. Showed above-ceiling session character (toasty taste, harsh "
                 "2nd draw). Provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='fw106 R12',
            role='confirms',
            provenance='ai-authored',
            gist="Same programmed 460°F-at-40s-terminus curve as R11 (no hold) — same "
                 "sapphire thermal lag putting actual terminus temperature in the high "
                 "440s. Showed above-ceiling session character (toasty taste, harsh "
                 "2nd draw). Provenance untagged in source.",
            confounds="None noted.",
        ),
    ],
    positions=[
        Position(
            stated='Session 93',
            text="FW106 R11-12 (June 5, 2026): curve programmed to arrive at 460°F at "
                 "the 40s terminus (no hold) — sapphire thermal lag put actual "
                 "temperature at terminus in the high 440s. Both runs showed "
                 "above-ceiling session character (toasty taste, harsh 2nd draw). Two "
                 "findings: (1) Rig 5 cannot reach the programmed 460°F at the 40s "
                 "terminus; (2) the high 440s it does reach is above FW106's clean "
                 "zone. No further 460°F experiments on Rig 5 without a longer session "
                 "or a different insert.",
        ),
    ],
    updated='Session 93',
)
