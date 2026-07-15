from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-equipment-schema',
    kind='decision',
    claim="Equipment schema: nested `Insert`/`CarbCap`/`Pearl` dataclasses; sequenced "
          "`RIG_N` constants; `pearls: list[Pearl]` sorted for stable equality; "
          "`airflow` front-loaded on `CarbCap`; `glass_top` flat string; Terp Tools "
          "row deleted",
    guidance="Insert, pearl, cap, and glass-top variation are all real or "
             "confirmed-coming. Schema captures the four independent variables. "
             "Sequenced naming eliminates rename churn when new variables appear. "
             "Pearl/insert/cap normalized as nested dataclasses; glass top deferred "
             "to flat string.",
    positions=[
        Position(
            stated='Session 65',
            text="Insert, pearl, cap, and glass-top variation are all real or "
                 "confirmed-coming. Schema captures the four independent variables. "
                 "Sequenced naming eliminates rename churn when new variables appear. "
                 "Pearl/insert/cap normalized as nested dataclasses; glass top "
                 "deferred to flat string until sub-dimensions appear. Audited by "
                 "Plan agent before execution.",
        ),
    ],
    updated='Session 65',
)
