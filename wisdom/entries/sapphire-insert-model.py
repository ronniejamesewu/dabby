from wisdom_core import *

ENTRY = WisdomEntry(
    key='sapphire-insert-model',
    kind='theory',
    claim="Sapphire insert theory: higher volumetric heat capacity (stabler at cold "
          "contact) and ~20x higher bulk conductivity (better surface uniformity) vs "
          "quartz — consistent with Reddit's 10–20°F lower-setpoint consensus.",
    guidance="Do not scale sapphire setpoints from quartz curves — calibrate empirically from scratch (done for Rig 3: 415-417°F band mapped; see rig3-sapphire). Treat the 10-20°F Reddit consensus as consistent-with-the-model, not a target.",
    grade='observation',
    grade_basis="Section written pre-acquisition (material-properties reasoning + Reddit consensus). Sapphire has since been in use on Rigs 3-6; empirical calibration lives in the rig entries.",
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
        Position(
            stated='July 15, 2026 (migration correction)',
            text="This section predates the sapphire acquisition — it was written as "
                 "pre-purchase reasoning ('When acquired: fresh empirical calibration "
                 "from scratch'). Sapphire inserts have since been in continuous use "
                 "(Rigs 3-6, May 22, 2026 onward) and the calibration it called for "
                 "happened: Rig 3 mapped the 415-417°F operating band (see "
                 "rig3-sapphire). Retained as the background thermal model; both "
                 "mechanisms remain the working explanation for sapphire's "
                 "lower-setpoint behavior. Correction source: the external migration "
                 "review caught the stale framing being presented as current.",
        ),
    ],
    updated='July 1, 2026 (thermal model doc)',
)
