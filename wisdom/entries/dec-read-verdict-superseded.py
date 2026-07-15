from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-read-verdict-superseded',
    kind='decision',
    claim="`read` and `verdict` on `CompletedRun` are superseded by `analysis` — "
          "migration complete",
    guidance="Do not populate `read` or `verdict` on new runs.",
    evidence=[
        Citation(
            source='hive1 R3',
            role='context',
            provenance='ai-authored',
            gist="The one run with both `read` and `verdict` populated — combined "
                 "read-first when migrated into `analysis`. (provenance untagged in "
                 "source)",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 48–49',
            text="Both fields predate the formal `analysis` field and hold AI-authored "
                 "interpretive text that `analysis` was designed to replace. Migration "
                 "completed Session 49: all 13 pre-Step-3 runs with non-empty "
                 "`read`/`verdict` had content moved verbatim into `analysis` (Hive1 R3, "
                 "the one run with both, was combined read-first). `extra_rows` is not "
                 "affected. Do not populate `read` or `verdict` on new runs.",
        ),
    ],
    updated='Sessions 48–49',
)
