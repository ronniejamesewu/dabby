from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig1-vs-rig2-gemlock',
    kind='equipment',
    claim="Rig 1 (spinner+pearl) vs Rig 2 (Gemlock, no pearl): lighter swabs on Gemlock, visible vapor at lower temps. Spinner-as-harshness-contributor is directional only — the 'same endpoint, same load' framing was struck July 11, 2026.",
    guidance="Treat as a persistent confound when comparing Gemlock runs against "
             "spinner-era data; do not assume equivalence between configs in "
             "analysis.",
    grade='observation',
    grade_basis="Low — cross-strain and cross-variable confounds persist",
    evidence=[
        Citation(
            source='mb9zst R1',
            role='confirms',
            provenance='ai-authored',
            gist="MB9ZST R1-2 — first Gemlock-era runs",
            confounds="none noted",
        ),
        Citation(
            source='mb9zst R2',
            role='confirms',
            provenance='ai-authored',
            gist="MB9ZST R1-2 — first Gemlock-era runs",
            confounds="none noted",
        ),
        Citation(
            source='wwz R1',
            role='context',
            provenance='ai-authored',
            gist="WW Z R1 (spinner) vs R2 (Gemlock) — first same-strain cross-config "
                 "swab comparison: golden/amber on spinner, wheat-clean on Gemlock; "
                 "endpoint also dropped 20°F (partial confound)",
            confounds="endpoint also dropped 20°F (partial confound)",
        ),
        Citation(
            source='wwz R2',
            role='confirms',
            provenance='ai-authored',
            gist="WW Z R1 (spinner) vs R2 (Gemlock) — first same-strain cross-config "
                 "swab comparison: golden/amber on spinner, wheat-clean on Gemlock; "
                 "endpoint also dropped 20°F (partial confound)",
            confounds="endpoint also dropped 20°F (partial confound)",
        ),
    ],
    positions=[
        Position(
            stated='undated in source',
            text="Lighter swabs *may* indicate less material remaining at end of "
                 "cycle, which *may* indicate the joystick vaporizes more efficiently "
                 "than the spinner + pearl setup — both steps are inferences, "
                 "neither is settled. Treat as a persistent confound when comparing "
                 "Gemlock runs against spinner-era data; do not assume equivalence "
                 "between configs in analysis. WW Z R8–9 (spinner) both produced "
                 "harshness; WW Z R5 (Gemlock) was clean — two directional data "
                 "points pointing at spinner config as a harshness contributor for "
                 "this strain, still within-strain only.",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="the prior wording here — \"same curve, same endpoint, same load "
                 "class\" — was false and inherited from R9's frozen analysis. R5 "
                 "ran WWZ_RUN3 (430°F endpoint); R8/R9 ran WWZ_RUN7 (420°F fast "
                 "ramp) — different curve AND endpoint (down 10°F). Nor is \"same "
                 "load class\" supportable: all three load classes are AI-recorded, "
                 "not user-verbatim. This is not a controlled comparison; harshness "
                 "appearing on the spinner even at the *lower* endpoint is "
                 "directionally consistent with the spinner-contributor read but "
                 "cannot be described as a control. (The underlying error still "
                 "sits in R9's frozen analysis — a correct-frozen-data pass is "
                 "optional; this row no longer relies on it.)",
        ),
        Position(
            stated='May 21-22, 2026',
            text="Gemlock era ended May 21, 2026 — joystick broke mid-session; back "
                 "on Cloud Vortex 21.0 + 6mm pearl as of WW Z Run 8. Rig 3 (sapphire "
                 "insert, Cloud Vortex 21.0 + 6mm pearl) in use as of May 22, 2026.",
        ),
    ],
    updated='May 21-22, 2026 (Gemlock era ended); July 11, 2026 audit (correction)',
)
