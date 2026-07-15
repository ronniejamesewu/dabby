from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-bamboo-swab-artifact',
    kind='failure-mode',
    claim="Bamboo swab sticks produce false amber color through the cotton tip — reads "
          "warmer/darker than the actual material color; paper-stick swabs don't have "
          "this artifact.",
    guidance="With bamboo-stick swabs, discount amber spots and treat golden+amber as "
             "golden. Paper-stick swabs remain the reference. Note in any run logged "
             "with bamboo sticks that color reads may be slightly warmer than actual.",
    evidence=[
        Citation(
            source='fw106 R21',
            role='confirms',
            provenance='mixed',
            gist="Swab logged as \"golden with amber spots\" — confirmed as bamboo "
                 "artifact when compared against Run 22 and a dry test.",
            confounds="None noted — the dry test (no material) reproducing the amber "
                      "is what isolates the stick as the source.",
        ),
    ],
    updated='FW106 R21 era (June 2026)',
)
