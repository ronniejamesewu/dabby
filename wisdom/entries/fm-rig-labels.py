from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-rig-labels',
    kind='failure-mode',
    claim="New `RIG_N` constant without a `_RIG_LABELS` entry.",
    guidance="No action required — `_RIG_LABELS` auto-discovers `RIG_N` constants by "
             "introspecting `dir(Dabby_Core)`. This failure can no longer occur.",
    evidence=[],
    positions=[
        Position(
            stated='Structurally resolved',
            text="Auto-discovery via introspection eliminated the manual-entry step; "
                 "the failure mode is no longer possible.",
        ),
    ],
    updated='Structurally resolved (code-caught, skill-caught)',
    resolution="New `RIG_N` constant without a `_RIG_LABELS` entry — auto-discovered by "
               "introspection; this failure can no longer occur.",
)
