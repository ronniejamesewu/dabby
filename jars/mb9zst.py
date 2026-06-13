"""Mango Banana #9 + Z + Sour Tangie — jar file (slug: mb9zst)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
MB9ZST_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
MB9ZST_RUN3 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=420, note='Endpoint'),
    Waypoint(time_s=65, temp_f=420, note='Hold at 420°F'),
]
MB9ZST_RUN4 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=415, note='Endpoint — down 5°F from Run 3'),
    Waypoint(time_s=65, temp_f=415, note='Hold at 415°F'),
]
MB9ZST_RUN5 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=415, note='Endpoint — same as Run 4'),
    Waypoint(time_s=65, temp_f=415, note='Hold at 415°F'),
]
MB9ZST_RUN6 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=15, temp_f=400, note='Faster mid climb'),
    Waypoint(time_s=30, temp_f=420, note='Endpoint — faster ramp, up 5°F from proposed'),
    Waypoint(time_s=60, temp_f=420, note='Hold — extended 10s via push button'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 13),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 13, 23, 27, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN1,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 430°F — baseline ramp &nbsp;|&nbsp; <strong>Equipment:</strong> First session with Gemlock joystick, no pearl',
        swab='Very light golden.',
        session_char='Pronounced flavors up front. Bitter citrus note with a distinct tangerine quality — consistent with Sour Tangie lineage (limonene-forward). Slight harshness at the end. Also appeared as a bitter/citrus rind note in Maple Bacon Donut Run 4 (May 12) — cross-strain parallel, genetics connection unclear, worth watching.',
        intensity='Strong — face tingling.',
        extra_rows=[
            ('Equipment note:', 'First run with Gemlock joystick, no pearl. Swab lighter than typical for a first run. Hypothesis: joystick may be more efficient — cleaner swab and/or more material vaporized in the same window. Single data point; something to watch.'),
        ],
    ),
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 13),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 5, 14, 4, 55, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN1,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 430°F — baseline ramp repeated',
        swab='Light golden — same as Run 1.',
        session_char='Big flavors up front. Visible vapor at lower temps than expected. Slight harshness at the end.',
        intensity='Strong — not too cloudy mentally, noticeably lazy physically.',
    ),
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 14),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 15, 2, 0, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN3,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 420°F with 20-second hold — ramp 375→400→420°F',
        swab='Light golden — "lightly toasted marshmallow." Clean.',
        session_char='Nice. Climb rate felt right, hold felt right. Still a bit harsh at the end.',
        intensity='High',
    ),
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 14),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 5, 15, 4, 34, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN4,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 415°F with 20-second hold — down 5°F from Run 3',
        swab='Golden — slightly darker than Run 3. Still in the clean range.',
        session_char='Less harsh at the tail than prior runs — still present but attenuating. More material in swabs at the end.',
        intensity='Decent — second dab of the evening, tolerance factor in play.',
    ),
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 17),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 18, 1, 9, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN5,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 415°F with 20-second hold — same as Run 4',
        swab='Super light golden — clean. Lighter than Run 4.',
        session_char='Tiny bit of harshness in the throat. Tiny bit of burnt taste at the very last draw.',
        intensity='Pretty hard hit.',
        dab_notes='Ran the same curve as last time, the 415 hold. Only one dab left in the jar. A tiny bit of harshness in the throat and a tiny bit of burnt taste at the very last draw. Swabs were their typical super light golden, so clean. Pretty hard hit.',
        analysis="Harshness at 415°F is now consistent across two runs (Runs 4 and 5) — the same two-run pattern that triggered the step-down recommendation for BB36#1 at the same endpoint. The burnt taste at the very last draw is a new and more specific observation: it points at the final seconds of the 20-second hold as the problem zone, not the ascent. Swab came back super light golden — lighter than Run 4, which runs counter to the hypothesis that lower endpoints leave more material behind. One data point, swab noise is real. Intensity landed hard with no same-day tolerance confound, consistent with the strain's potency pattern.",
    ),
    CompletedRun(
        strain='Mango Banana #9 + Z + Sour Tangie',
        run_date=date(2026, 5, 17),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 5, 18, 5, 1, tzinfo=timezone.utc),
        waypoints=MB9ZST_RUN6,
        equipment=RIG_2,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 420°F — faster ramp (30s), 60s total (planned 50s + push-button extension)',
        swab='Super light golden — clean.',
        session_char='Super tasty first half. Faster to 420°F hit harder than prior ramps. Last few draws harsh in the push-button extension.',
        intensity='Very stoned.',
        dab_notes="Using the proposed next curve but 420 for the hold instead of 415. Swabs were the regular clean light golden. Faster to 420 definitely seems to hit harder, and the first half was super tasty, I didn't miss the lingering lower longer. The shorter duration didn't finish the material loaded, I added 10 more seconds via the push button on Dabby. Very stoned. The last few draws were expectedly harsh.",
        analysis="Fastest ramp in the MB9ZST dataset — 420°F in 30s vs. 45s in Run 3. The harder hit and front-loaded flavor are consistent with that: same temperature, more vaporization concentrated in the early window. 'Didn't miss the lingering lower longer' is the clearest preference signal in the strain's history — the compressed front end works better than the drawn-out one. The push-button extension to 60s added 10s of hold at 420°F beyond the plan, and the harshness arrived there — consistent with the full MB9ZST/420°F pattern. Swab came back light golden throughout, same as every other Gemlock run on this strain. Jar done at 6 runs.",
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Mango Banana #9 + Z + Sour Tangie',
    profile_anchor='#mb9zst-profile',
    next_text='Jar finished — 6 runs, May 13–17, 2026',
    accent=None,
    slug='mb9zst',
    info=[
        ('Strain', 'Mango Banana #9 + Z + Sour Tangie'),
        ('Product', 'Persy Neapolitan — three-strain cold-cure blend, 2g jar'),
        ('Consistency', 'Cold cure'),
        ('Producer', '710 Labs'),
        ('Extraction', '90μ full-melt bubble hash, hand-pressed'),
        ('Blend', 'Mango Banana #9 (SB 36 × Forbidden Banana) · Z (Zkittlez lineage) · Sour Tangie (Sour Diesel × Tangie)'),
        ('Character', 'Sativa-leaning hybrid — uplifting from Sour Tangie, tropical melon from Mango Banana, sweet/gas balance from Z. Neapolitan format means three separate layers in one jar; actual session character driven by which portion you pull from.'),
        ('Nose', 'Not yet recorded'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred prominent from Sour Tangie (Sour Diesel × Tangie) and Mango Banana lineages; myrcene from Mango Banana (SB36 × Forbidden Banana); terpinolene from Z and Sour Tangie character. This is the generic cannabis palette applied to a three-component blend — the Neapolitan format means each layer may have a different terpene balance. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='Run 6 at 420°F (faster ramp to 30s, planned 50s extended to 60s via push button): super light golden swab, very tasty first half, faster to 420 hit harder than the slower ramp. Extension into harsh territory. Jar done.',
    next_ai_analysis="Jar finished. Six runs over five days, May 13–17, 2026. This was also the Gemlock joystick's debut jar — every data point in this strain's history was collected on the new rig, so the baseline cross-strain confound never resolved. Harshness appeared in the tail on all six runs across three endpoint temperatures (430°F, 420°F, 415°F) and two curve shapes. A clean tail was never achieved. The fastest ramp (Run 6) produced the best first-half character and the hardest hit — the right shape arrived on the last dab of the jar.",
    next_waypoints=None,
    jar_index="<div style='text-align:center;margin-top:1em;'><strong>Number of runs on a 2g jar:</strong> 6<br><strong>Days from first dab to last:</strong> 5<br><strong>Endpoint temperatures tried in search of a clean tail:</strong> 3<br><strong>Runs that ended with a clean tail:</strong> 0<br><strong>Swabs described as “lightly toasted marshmallow”:</strong> 1<br><strong>Named strains in the Neapolitan ever individually identified:</strong> 0 of 3<br><strong>Equipment changes mid-jar:</strong> 0 <em>(though this jar was the equipment change)</em><br><strong>Seconds added to the final run by push button:</strong> 10<br><strong>Remaining dabs:</strong> 0</div>",
)
