from wisdom_core import *

ENTRY = WisdomEntry(
    key='bitter-citrus-note',
    kind='pattern',
    claim="Bitter citrus / citrus rind note recurs across strains.",
    guidance="Not worth weighting in per-run analysis until a mechanism or genetic "
             "correlation is established.",
    grade='observation',
    grade_basis="Six strains, different producers, different genetics; note recurs "
                "across multiple sessions.",
    evidence=[
        Citation(
            source='mb9zst R1',
            role='confirms',
            provenance='ai-authored',
            gist="Tangerine/bitter citrus. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='mbd R4',
            role='confirms',
            provenance='ai-authored',
            gist="Citrus rind. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='oc R12',
            role='confirms',
            provenance='user-verbatim',
            gist="Bitter citrus — user: \"increasingly familiar\".",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R2',
            role='confirms',
            provenance='ai-authored',
            gist="Bitter citrus throughout. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R7',
            role='confirms',
            provenance='ai-authored',
            gist="Citrus bitter, draw 1. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R11',
            role='confirms',
            provenance='ai-authored',
            gist="Bitter citrus with a creamier undertone. Provenance untagged in "
                 "source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 39, 47, 70, 73, 138, 146',
            text="OC, FW106, and bp4rw13 (Randy Watzon side — limonene inferred from "
                 "Runtz/Wedding Crasher lineage) all have citrus-associated genetics, "
                 "making the note less diagnostic for those three. Origin unknown. "
                 "Limonene is inferred in most of these strains' terpene profiles — "
                 "could be limonene expression at these temperature ranges, or an "
                 "unrelated coincidence. MB9ZST, MBD, and now Hive1 (Honey Banana × "
                 "Papaya — myrcene/terpinolene inferred, no citrus association) are "
                 "the more surprising occurrences.",
        ),
    ],
    watch_for="Watch for recurrence.",
    updated='Sessions 39, 47, 70, 73, 138, 146',
)
