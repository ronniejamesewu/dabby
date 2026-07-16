from wisdom_core import *

ENTRY = WisdomEntry(
    key='harshness-threshold-crossing',
    kind='pattern',
    claim="Harshness onset is threshold-crossing, not temperature-pinned — harshness "
          "builds continuously through the ramp and is noticed when it crosses a "
          "perceivable level, not at a fixed temperature.",
    guidance="\"Tail harshness\" may describe when harshness became noteworthy, not an "
             "endpoint-specific signal. Needs cross-strain confirmation. All onset "
             "temperatures here are app-display readings — the Session 132 decision "
             "limits the readout below 1°F precision, so the shifts are directional, "
             "not measured.",
    grade='observation',
    grade_basis="Low — 2 runs one strain, plus an OC supporting pair.",
    evidence=[
        Citation(
            source='wwz R3',
            role='confirms',
            provenance='user-verbatim',
            gist="Same curve (430°F endpoint ramp) as R4; harshness appeared at 414°F. (user-verbatim per the tail-harshness row, line 28 — corrected at migration review)",
            confounds="none noted",
        ),
        Citation(
            source='wwz R4',
            role='confirms',
            provenance='user-verbatim',
            gist="Same curve (430°F endpoint ramp) as R3; harshness appeared at 420°F. (user-verbatim per the tail-harshness row, line 28 — corrected at migration review)",
            confounds="none noted",
        ),
        Citation(
            source='oc R11',
            role='confirms',
            provenance='ai-authored',
            gist="Harshness \"exactly when temp hit 417\" — arrival. (Provenance "
                 "untagged in source.)",
            confounds="2nd-vs-3rd-dab order asymmetry cuts against the direction, and "
                      "OC R11's load class is analysis-sourced.",
        ),
        Citation(
            source='oc R12',
            role='confirms',
            provenance='ai-authored',
            gist="416°F — onset 15s into hold, mild. (Provenance untagged in source.)",
            confounds="2nd-vs-3rd-dab order asymmetry cuts against the direction, and "
                      "OC R11's load class is analysis-sourced.",
        ),
    ],
    positions=[
        Position(
            stated='Session 57',
            text="WW Z R3–4: same curve (430°F endpoint ramp), harshness "
                 "appeared at 414°F (R3) and 420°F (R4) — 6°F shift "
                 "on identical curve.",
        ),
        Position(
            stated='Session 57',
            text="Harshness builds continuously through the ramp and is noticed when "
                 "it crosses a perceivable level, not at a fixed temperature. \"Tail "
                 "harshness\" may describe when harshness became noteworthy, not an "
                 "endpoint-specific signal. Needs cross-strain confirmation. All onset "
                 "temperatures here are app-display readings — the Session 132 "
                 "decision limits the readout below 1°F precision, so the shifts "
                 "are directional, not measured.",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="Supporting (added July 11, 2026 audit): OC R11 (harshness \"exactly "
                 "when temp hit 417\" — arrival) vs R12 (416°F — onset "
                 "15s into hold, mild): a 1°F endpoint change moved onset from "
                 "arrival to mid-hold; 2nd-vs-3rd-dab order asymmetry cuts against the "
                 "direction, and OC R11's load class is analysis-sourced.",
        ),
    ],
    watch_for="Needs cross-strain confirmation.",
    updated='Session 57; OC supporting pair added July 11, 2026 audit',
)
