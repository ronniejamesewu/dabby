from wisdom_core import *

ENTRY = WisdomEntry(
    key='sapphire-insert-model',
    kind='theory',
    claim="Sapphire insert theory: higher volumetric heat capacity (stabler at cold "
          "contact) and ~20x higher bulk conductivity (better surface uniformity) vs "
          "quartz — consistent with Reddit's 10–20°F lower-setpoint consensus.",
    guidance="Do not scale sapphire setpoints from quartz curves. When a sapphire "
             "insert is acquired, calibrate empirically from scratch, treating the "
             "10-20°F Reddit consensus as a consistent-with-the-model prior, not a "
             "target to hit.",
    grade='observation',
    grade_basis="No sapphire runs logged yet — theoretical reasoning from material "
                "properties (heat capacity, conductivity) plus an external Reddit "
                "consensus anecdote, pending acquisition.",
    evidence=[],
    positions=[
        Position(
            stated='July 1, 2026 (thermal model doc)',
            text="When acquired: fresh empirical calibration from scratch. Do not "
                 "scale from quartz curves. Two mechanisms that differentiate "
                 "sapphire from quartz: (1) higher volumetric heat capacity — "
                 "absorbs cold-material contact perturbation more stably at "
                 "session open; (2) better surface temperature uniformity during "
                 "vaporization — ~20x higher bulk conductivity replenishes heat "
                 "faster when local vaporization creates cold spots. Reddit "
                 "consensus of 10–20°F lower setpoints for equivalent results is "
                 "consistent with this model.",
        ),
    ],
    updated='July 1, 2026 (thermal model doc)',
)
