from wisdom_core import *

ENTRY = WisdomEntry(
    key='thermal-model',
    kind='theory',
    claim="Titanium-to-insert thermal offset is probably small under most conditions "
          "— fast insert equilibration and efficient contact-point heat transfer "
          "retire the old 15-35°F estimate. Setpoints are reasonable proxies for "
          "material contact temp.",
    guidance="Do not flag short flat tails — even 10 seconds — as inadequate for "
             "offset closure. Do not rebuild the 1D thermal resistance model; the "
             "eta interface-efficiency concept was developed and abandoned. "
             "Setpoints are reasonable proxies for material contact temperature — "
             "swab result is the ground truth.",
    grade='directional',
    grade_basis="Physical/thermal reasoning (insert wall thickness ~1mm, ~1.4 W/m*K "
                "conductivity, contact geometry) plus retirement of the prior 15-35°F "
                "estimate — no per-run citations; not tested against logged runs.",
    evidence=[],
    positions=[
        Position(
            stated='undated in source (Methodology State)',
            text="The old 15-35°F titanium-to-insert offset estimate is retired. "
                 "Current position:\n\n"
                 "- Quartz insert wall is ~1mm thick at ~1.4 W/m·K conductivity — bulk "
                 "thermal time constant under one second. The insert equilibrates "
                 "internally almost instantly.\n"
                 "- Physical contact points between titanium and quartz transfer heat "
                 "efficiently; the air gap is not the dominant resistance when contact "
                 "geometry is intact.\n"
                 "- Offset is probably small under most operating conditions. Dominant "
                 "remaining uncertainties: vaporization cooling (phase change draws "
                 "heat locally during active vaporization) and dynamic lag during steep "
                 "ascent (titanium ahead of insert during fast climbs).\n"
                 "- Short flat tails — even 10 seconds — are sufficient for the insert "
                 "to reach the setpoint. Do not flag short flat tails as inadequate for "
                 "offset closure.\n"
                 "- Setpoints are reasonable proxies for material contact temperature.\n\n"
                 "**Do not rebuild the 1D thermal resistance model.** The interface "
                 "efficiency parameter (η) concept was developed and abandoned — the "
                 "two dominant parameters were partially redundant and the underlying "
                 "geometry is unknowable. Swab result is the ground truth.",
        ),
    ],
    counter_reading="The retirement rests on physical estimates (wall thickness, "
                    "conductivity) rather than a controlled measurement — no run has "
                    "isolated the offset by comparing setpoint against directly "
                    "measured insert/material temperature. If contact geometry "
                    "degrades (loose pearls, imperfect seating) the air-gap-resistance "
                    "argument weakens and offset could grow again; the model also "
                    "doesn't quantify vaporization cooling or ascent lag, so 'probably "
                    "small' could be wrong under heavy vaporization load or fast "
                    "ramps — precisely the uncertainties the model itself flags as open.",
    watch_for="Vaporization cooling during active vaporization, and dynamic lag "
              "during steep ascent (titanium ahead of insert) — the two dominant "
              "uncertainties that could reopen the offset question.",
    updated='undated in source',
)
