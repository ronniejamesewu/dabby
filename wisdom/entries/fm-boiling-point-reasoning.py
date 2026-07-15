from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-boiling-point-reasoning',
    kind='failure-mode',
    claim="Fractional-distillation or selective-boiling reasoning when all compounds "
          "are above boiling point — a structural impossibility.",
    guidance="Verify that not all compounds exceed boiling point before reasoning about "
             "selective-delivery mechanisms. analysis-toolkit Recipe 7 (boiling-point / "
             "mass-conservation check) validates this prerequisite automatically.",
    evidence=[
        Citation(
            source='fw106 R24',
            role='context',
            provenance='ai-authored',
            gist="Session 130 worked example where boiling-point / mass-conservation check "
                 "fires before any selective-delivery mechanism attribution.",
            confounds="none noted",
        ),
    ],
    updated='Session 130',
    resolution="Fractional-distillation / selective-boiling reasoning when all compounds "
               "are above boiling point",
)
