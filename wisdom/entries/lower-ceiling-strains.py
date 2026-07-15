from wisdom_core import *

ENTRY = WisdomEntry(
    key='lower-ceiling-strains',
    kind='pattern',
    claim="MB9ZST and BB36#1: tail harshness persisting below 430°F — may need a lower "
          "ceiling.",
    guidance="For MB9ZST and BB36#1, tail harshness persists at 420°F and 415°F; these two "
             "strains appear to require a lower ceiling (~410°F or below). Do not generalize "
             "the lower-ceiling need beyond them — strain-specific vs equipment-related is "
             "unresolved (both Gemlock-era).",
    grade='directional',
    grade_basis="2 strains, multiple confirming runs each.",
    evidence=[
        Citation(
            source='mb9zst R3',
            role='confirms',
            provenance='ai-authored',
            gist="420°F harsh. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='mb9zst R4',
            role='confirms',
            provenance='ai-authored',
            gist="415°F still present. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bb361 R2',
            role='confirms',
            provenance='ai-authored',
            gist="415°F harsh (BB36#1 R2-3). Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bb361 R3',
            role='confirms',
            provenance='ai-authored',
            gist="415°F harsh (BB36#1 R2-3). Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 39–44',
            text="Rain Fruit resolved cleanly at 420°F; these two strains appear to require "
                 "a lower ceiling (~410°F or below). Insufficient data to confirm whether "
                 "this is strain-specific or equipment-related (both are Gemlock-era).",
        ),
    ],
    counter_reading="Both strains ran only on Gemlock-era equipment, so the sub-430°F "
                    "harshness may be an equipment artifact rather than a strain-specific "
                    "lower-ceiling requirement — the source flags strain-specific vs "
                    "equipment-related as unresolved.",
    updated='Sessions 39–44',
)
