from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-rendering-labels',
    kind='decision',
    claim="Rendering labels for new run-section fields settled: \"Equipment:\" inline in "
          "Curve block; \"Notes on this dab:\" for `dab_notes`; \"AI Run Analysis:\" for "
          "`analysis`",
    guidance="\"AI Run Analysis:\" distinguishes the frozen per-run synthesis from \"AI "
             "Analysis:\" used in What to Try Next (revisable guidance). \"Notes on this "
             "dab:\" is user-voice and distinct from AI fields.",
    positions=[
        Position(
            stated='Session 49',
            text="\"AI Run Analysis:\" distinguishes the frozen per-run synthesis from "
                 "\"AI Analysis:\" used in What to Try Next (revisable guidance). \"Notes "
                 "on this dab:\" is user-voice and distinct from AI fields. Equipment "
                 "line derives human-readable text from the nested EquipmentConfig "
                 "fields via `_fmt_equipment_display()` — never echo the Python "
                 "identifier (`RIG_3` etc.) to the user; always use the display name "
                 "(Rig 3).",
        ),
    ],
    updated='Session 49',
)
