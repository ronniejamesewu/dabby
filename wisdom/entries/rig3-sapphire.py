from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig3-sapphire',
    kind='equipment',
    claim="Rig 3 (sapphire insert — Dr. Dabber Sapphire Plus v2): 415°F is the clean "
          "operating point. Harshness onset appears to shift with each degree across "
          "415–417°F; ceiling appears to sit at 415–417°F.",
    guidance="Do not scale from quartz curves — empirical calibration from scratch. "
             "Operating point is 415°F; 416°F is workable if mild late harshness is "
             "acceptable. 417°F triggers harshness immediately at endpoint arrival.",
    grade='directional',
    grade_basis="Moderate — five runs, one strain; gradient mapped across 415–417°F.",
    evidence=[
        Citation(
            source='oc R8',
            role='confirms',
            provenance='ai-authored',
            gist="Run 8 (420°F): ultra-clean swab, very strong delayed effect, harshness "
                 "11s into the hold. [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='oc R9',
            role='confirms',
            provenance='ai-authored',
            gist="Run 9 (415°F, small load): clean first draw, wispy vapor, trace "
                 "harshness only as load ran out — load-size confound. [provenance "
                 "untagged in source]",
            confounds="Small load; load-size confound — trace harshness only as load ran "
                      "out.",
        ),
        Citation(
            source='oc R10',
            role='confirms',
            provenance='ai-authored',
            gist="Run 10 (415°F, ~25% larger load): no harshness across two full draws — "
                 "load-size confound resolved. [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='oc R11',
            role='confirms',
            provenance='ai-authored',
            gist="Run 11 (417°F, slightly larger load): harshness entered immediately at "
                 "endpoint arrival — not a hold-duration effect, the temperature itself "
                 "was the trigger. [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='oc R12',
            role='confirms',
            provenance='ai-authored',
            gist="Run 12 (416°F, third dab of day): harshness entered 15s into the hold "
                 "(~35s total), mild and never acute. [provenance untagged in source]",
            confounds="Tolerance confound on Run 12 (third dab of day) means intensity "
                      "comparison to 415°F is pending a first-dab repeat.",
        ),
    ],
    positions=[
        Position(
            stated='May 22–23, 2026',
            text="415°F clean on the sapphire across two runs. Slightly more reclaim at "
                 "415°F vs. 420°F; medium effect vs. Run 8's very intense, suggesting "
                 "415°F sits at the lower edge of the useful band. Ceiling appears to sit "
                 "at 415–417°F. 415°F is the operating point. Intensity trade-off across "
                 "2°F is directional — 415°F delivered medium, 417°F very hard (eyes "
                 "blurring, body feels like it's vibrating at 14 min post-session).",
        ),
        Position(
            stated='May 22–23, 2026',
            text="Empirical calibration from scratch. Do not scale from quartz curves. "
                 "Three adjacent endpoints now mapped: 415°F clean, 416°F mild harshness "
                 "mid-hold, 417°F immediate on arrival. The gradient is directionally "
                 "consistent — each degree in this band appears to shift harshness onset. "
                 "Operating point is 415°F; 416°F is workable if mild late harshness is "
                 "acceptable. Tolerance confound on Run 12 (third dab of day) means "
                 "intensity comparison to 415°F is pending a first-dab repeat.",
        ),
    ],
    counter_reading="All five runs are one strain (OC); load size varied across R9–R11 "
                    "and R12 was a third-dab (tolerance confound), so the per-degree "
                    "harshness-onset gradient could reflect load size and tolerance "
                    "rather than temperature alone — unconfirmed on any other strain.",
    watch_for="A first-dab repeat at 416°F to clear Run 12's tolerance confound; the "
              "415–417°F gradient reproducing on a second strain.",
    updated='May 22–23, 2026 (OC Runs 8–12)',
)
