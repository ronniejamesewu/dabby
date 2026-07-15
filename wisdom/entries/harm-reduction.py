from wisdom_core import *

ENTRY = WisdomEntry(
    key='harm-reduction',
    kind='theory',
    claim="Degradation byproducts (benzene, methacrolein) from terpene thermolysis occur "
          "at low ppb at conservative setpoints (375-440°F) — far below EPA allowable "
          "levels. Not a meaningful harm-reduction lever at practiced temperatures.",
    guidance="Do not invoke degradation byproducts as a harm reduction argument for "
             "temperature choices within 375–460°F. The thermal injury mechanism has the "
             "stronger evidence base.",
    grade='directional',
    grade_basis="Source: ACS Omega 2017 peer-reviewed study. Session 57 correction "
                "(user-reported, paper not re-read) downgraded the initial framing.",
    evidence=[
        Citation(
            source='session:57',
            role='context',
            provenance='ai-authored',
            gist="Benzene and methacrolein are documented degradation products of "
                 "terpene thermolysis. Benzene formation begins in small amounts around "
                 "400°F and increases significantly with temperature. Alarming toxicant "
                 "levels in published studies used 500–550°C (932–1022°F) — far above "
                 "typical practice. At conservative setpoints (375–440°F) benzene "
                 "formation is at the low end of the documented range.",
            confounds="none noted",
        ),
        Citation(
            source='session:57',
            role='counters',
            provenance='mixed',
            gist="Session 57 correction (user-reported, paper not re-read): Measured "
                 "byproduct quantities were in low ppb even at the high study "
                 "temperatures — far below EPA allowable levels in hundreds of ppm. The "
                 "\"meaningfully safer\" framing overstates what the evidence supports at "
                 "our operating range. Do not invoke degradation byproducts as a harm "
                 "reduction argument for temperature choices within 375–460°F. The "
                 "thermal injury mechanism (see below) has the stronger evidence base.",
            confounds="Paper not re-read to verify the correction directly — the "
                      "byproduct figures are user-reported, not re-confirmed against the "
                      "study.",
        ),
    ],
    positions=[
        Position(
            stated='Session 57',
            text="Resolved: The 440°F vs. 460°F question falls well below the "
                 "temperature range where the research documents meaningful risk. No "
                 "further discussion needed.",
        ),
    ],
    counter_reading="The Session 57 correction is itself unverified — the paper was not "
                    "re-read, so the low-ppb figures are a secondhand recollection, not a "
                    "re-check of the source. If the recalled figures understate the "
                    "study's actual byproduct levels, or if repeated high-frequency use "
                    "accumulates exposure across sessions in a way single-session ppb "
                    "figures don't capture, degradation byproducts could remain a live "
                    "harm-reduction consideration within 375–460°F rather than a closed "
                    "question.",
    updated='Session 57',
)
