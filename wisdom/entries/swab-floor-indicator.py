from wisdom_core import *

ENTRY = WisdomEntry(
    key='swab-floor-indicator',
    kind='pattern',
    claim="Swab is a floor indicator, not a fine-grained calibration metric — "
          "dark/burnt residue reliably signals to reduce endpoint, but within the "
          "light-golden-to-amber range it cannot distinguish curve shapes or small "
          "endpoint differences.",
    guidance="Treat dark/burnt residue as a reliable signal to reduce endpoint. "
             "Within the light-golden-to-amber range, read session character, not "
             "swab, for small endpoint or curve-shape differences. Before reading a "
             "warm swab as a floor signal, check cycle count — second cycles darken "
             "swabs independent of endpoint.",
    grade='tested',
    grade_basis="Four independent strain contexts; FW106 R11-12 extends the pattern "
                "to include thermal degradation flavor, not just harshness.",
    evidence=[
        Citation(
            source='oc R7',
            role='confirms',
            provenance='ai-authored',
            gist="Plain amber clean swab + \"harsh in last 20s\" — clean swab, "
                 "harshness present. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='wwz R5',
            role='confirms',
            provenance='ai-authored',
            gist="Same curve, same equipment, same light golden swab as R6, but R5 "
                 "no harshness/mild. Provenance untagged in source. (See position for "
                 "the R5-vs-R6 comparison.)",
            confounds="Paired with R6; load size is the variable that moves session "
                      "character without moving swab.",
        ),
        Citation(
            source='wwz R6',
            role='confirms',
            provenance='user-verbatim',
            gist="Same curve, same equipment, same light golden swab as R5, but R6 "
                 "tail harshness/hard. Provenance untagged in source. (See position for "
                 "the R5-vs-R6 comparison.)",
            confounds="Paired with R5; load size is the variable that moves session "
                      "character without moving swab.",
        ),
        Citation(
            source='mb9zst R5',
            role='confirms',
            provenance='ai-authored',
            gist="Super light golden swab + harshness + burnt taste at last draw. "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R11',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, light gold swab + toasty taste + hot aftermath at ~high 440s "
                 "— clean swab while material degraded above the ceiling (FW106 R11-12). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R12',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, light gold swab + toasty taste + hot aftermath at ~high 440s "
                 "— clean swab while material degraded above the ceiling (FW106 R11-12). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R5',
            role='context',
            provenance='ai-authored',
            gist="Part of the bp4rw13 R5–R8 cycle/color gradient — second cycles "
                 "darken swabs independent of endpoint (added July 11, 2026 audit). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R6',
            role='context',
            provenance='ai-authored',
            gist="Part of the bp4rw13 R5–R8 cycle/color gradient — second cycles "
                 "darken swabs independent of endpoint (added July 11, 2026 audit). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R7',
            role='context',
            provenance='ai-authored',
            gist="Part of the bp4rw13 R5–R8 cycle/color gradient — second cycles "
                 "darken swabs independent of endpoint (added July 11, 2026 audit). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R8',
            role='context',
            provenance='ai-authored',
            gist="Part of the bp4rw13 R5–R8 cycle/color gradient — second cycles "
                 "darken swabs independent of endpoint (added July 11, 2026 audit). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R15',
            role='context',
            provenance='ai-authored',
            gist="WM R15 decision — second cycles darken swabs independent of endpoint "
                 "(added July 11, 2026 audit). Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R27',
            role='context',
            provenance='ai-authored',
            gist="FW106 R27 — second cycles darken swabs independent of endpoint "
                 "(added July 11, 2026 audit). Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Ongoing',
            text="Dark/burnt residue is a reliable signal to reduce endpoint; within "
                 "the light-golden-to-amber range, swab cannot reliably distinguish "
                 "curve shapes or small endpoint differences. FW106 R11-12 adds a "
                 "stronger case: even material degradation (toasty flavor) doesn't "
                 "necessarily produce a dark swab on Rig 5 at elevated temperatures — "
                 "session character is the operative signal.",
        ),
        Position(
            stated='Ongoing',
            text="WW Z R5 vs R6 (same curve, same equipment, same light golden swab, "
                 "but R5 no harshness/mild and R6 tail harshness/hard — load size moves "
                 "session character without moving swab).",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="Before reading a warm swab as a floor signal, check cycle count — "
                 "second cycles darken swabs independent of endpoint (bp4rw13 R5–R8 "
                 "cycle/color gradient, WM R15 decision, FW106 R27; added July 11, "
                 "2026 audit).",
        ),
    ],
    counter_reading="The floor-only reading leans on instances where swab stayed light "
                    "while harshness or degradation appeared, but most are AI-authored "
                    "session_char rather than user-verbatim, and the WW Z R5/R6 load "
                    "effect is a single-strain paired inference — swab may simply be "
                    "under-sampled at fine resolution rather than genuinely insensitive "
                    "to it.",
    updated='Ongoing; cycle-count caveat added July 11, 2026 audit.',
)
