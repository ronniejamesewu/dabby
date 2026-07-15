from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-insert-display',
    kind='decision',
    claim="Insert display: show material only when `model == \"stock\"` "
          "(`\"{brand} stock {material}\"`); named models use `\"{brand} {model}\"` only",
    guidance="Material is redundant when the model name is self-describing. If a "
             "future named insert needs material surfaced, add it at that point. "
             "Applies in both `_fmt_equipment_display()` and the Rig Reference table.",
    positions=[
        Position(
            stated='Session 65',
            text="Material is redundant when the model name is self-describing. If "
                 "a future named insert needs material surfaced, add it at that "
                 "point. Applies in both `_fmt_equipment_display()` and the Rig "
                 "Reference table.",
        ),
    ],
    updated='Session 65',
)
