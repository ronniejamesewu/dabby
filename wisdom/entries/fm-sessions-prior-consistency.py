from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-sessions-prior-consistency',
    kind='failure-mode',
    claim="sessions_prior_today computed correctly but written inconsistently across "
          "outputs",
    guidance="When logging runs, compute sessions_prior_today once and use the same "
             "value consistently in the readback display, the stored field, and the "
             "analysis text.",
    evidence=[],
    positions=[
        Position(
            stated='Structure',
            text="The stored field is validator-cross-checked; prose consistency is still "
                 "manual: compute once, use identically in the readback, the field, and "
                 "the `analysis` text.",
        ),
    ],
    updated='',
    resolution="sessions_prior_today computed correctly but written inconsistently across "
               "outputs",
)
