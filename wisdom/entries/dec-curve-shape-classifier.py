from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-curve-shape-classifier',
    kind='decision',
    claim="Curve shape classifier lives in the generator as a rendering utility "
          "function, not as a `@property` on `CompletedRun` (supersedes Session 46 "
          "decision)",
    guidance="The label is not queryable: if shape-based querying is needed in "
             "future, either query waypoints directly (e.g. "
             "`run.waypoints[-1].temp_f`, monotonicity checks) or add structured "
             "boolean/int properties to `CompletedRun` at that point. Do not add "
             "properties speculatively before a real query exists.",
    positions=[
        Position(
            stated='Session 47',
            text="A string label is display logic — it belongs in the rendering "
                 "layer, not the data model. The label is not queryable: if "
                 "shape-based querying is needed in future, either query "
                 "waypoints directly (e.g. `run.waypoints[-1].temp_f`, "
                 "monotonicity checks) or add structured boolean/int properties "
                 "to `CompletedRun` at that point. Do not add properties "
                 "speculatively before a real query exists",
        ),
    ],
    updated='Session 47',
)
