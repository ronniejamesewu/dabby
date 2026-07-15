from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-read-maps-to-analysis',
    kind='decision',
    claim="`read` content maps to `analysis`, not `dab_notes`",
    guidance="Do not backfill `dab_notes` with `read` content.",
    positions=[
        Position(
            stated='Session 49',
            text="Both `read` and `verdict` were AI-authored — terpene reasoning, "
                 "cross-strain pattern references, floor indicator framing. `dab_notes` "
                 "is the user's verbatim words; pre-Step-3 runs have no user-verbatim "
                 "record because the field didn't exist yet. Do not backfill `dab_notes` "
                 "with `read` content.",
        ),
    ],
    updated='Session 49',
)
