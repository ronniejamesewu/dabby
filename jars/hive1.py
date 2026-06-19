"""The Hive #1 — jar file (slug: hive1)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
HIVE1_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=35, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=440, note='Endpoint'),
]
HIVE1_RUN2 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=35, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=440, note='Endpoint — repeated from Run 1'),
]
HIVE1_RUN3 = [
    Waypoint(time_s=0, temp_f=430, note='Steady hold — flat 430°F from session open'),
    Waypoint(time_s=45, temp_f=430, note='Endpoint'),
]
HIVE1_RUN4 = [
    Waypoint(time_s=0, temp_f=430, note='Steady hold — flat 430°F from session open'),
    Waypoint(time_s=60, temp_f=430, note="Endpoint — extended from Run 3's 45s"),
]
HIVE1_RUN5 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=35, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint — 430°F with ramp (down from 440°F in Runs 1–2)'),
]
HIVE1_NEXT = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=35, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=425, note='Endpoint — down 5°F from Run 5'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 5, 7),
        sessions_prior_today=0,
        utc_logged_at=None,
        waypoints=HIVE1_RUN1,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 440°F',
        swab='Light golden — clean. No darkening.',
        session_char='Nice flavors on the way up through the arc. Heavy indica effect.',
        analysis='Clean swab on first run — curve appears well-matched to this material. Repeated as Run 2 to confirm.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 5, 7),
        sessions_prior_today=1,
        utc_logged_at=None,
        waypoints=HIVE1_RUN2,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 440°F — identical to Run 1',
        swab='Very light — cleaner than Run 1.',
        session_char='Really nice. Consistent with Run 1.',
        analysis='Two clean runs, consistent character, swab lighter on repeat. 440°F endpoint may be higher than needed — material is fully expressing before the endpoint. Run 3: trying steady 430°F flat hold (no ramp) to test whether curve shape affects the result.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 5, 8),
        sessions_prior_today=0,
        utc_logged_at=None,
        waypoints=HIVE1_RUN3,
        equipment=RIG_1,
        duration_seconds=45,
        endpoint_note='<strong>Setpoint:</strong> 430°F steady (no ramp)',
        swab='Light golden — clean.',
        session_char='First half: lots of flavor, low throat irritation. Second half: irritation increased, flavor faded to generic dab vapor — never harsh or burnt, just less distinct. Effect notably strong.',
        analysis='At a flat 430°F from the open, all terpene fractions (pinene through linalool, all below 430°F) are available simultaneously — first hit may be the full palette combining at once rather than staged. The ramp climbs through each fraction sequentially, which may be what gives those runs more distinct flavor progression across the arc. 45 seconds was too short — vapor was still producing at session end. Not a temperature issue, just cut off early. One data point. Directionally supports the ramp producing more distinct staged flavor vs. the flat hold combining everything at once. If revisiting the flat hold, extend to 60 seconds. Next planned: repeat the Run 1–2 ramp (380→390→410°F) with 430°F endpoint to compare directly on the same endpoint.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 5, 8),
        sessions_prior_today=1,
        utc_logged_at=None,
        waypoints=HIVE1_RUN4,
        equipment=RIG_1,
        duration_seconds=60,
        endpoint_note="<strong>Setpoint:</strong> 430°F steady (no ramp) — extended from Run 3's 45s",
        swab='Light golden — clean. Consistent with Run 3.',
        session_char='Similar to Run 3. Extended hold confirmed vapor was still producing at 45s in Run 3 — 60s felt more complete.',
        analysis='Two flat-hold data points, both clean swabs, consistent character. Next: ramp to 430°F endpoint (380→390→410→430°F) — the original planned experiment — to compare curve shape on the same endpoint.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 5, 8),
        sessions_prior_today=2,
        utc_logged_at=None,
        waypoints=HIVE1_RUN5,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F (ramp — same shape as Runs 1–2, endpoint reduced from 440°F)',
        swab='Light golden — a tad lighter than the flat-hold 430°F runs (Runs 3–4). Clean.',
        session_char='Nice distinct flavors through the first two-thirds. Harsh in the last ~10 seconds. Effects quite potent.',
        extra_rows=[
            ('Next:', 'Try 420–425°F endpoint on Run 6. Keep ramp shape unchanged.'),
        ],
        analysis='Distinct staged flavor character is consistent with the ramp — each terpene fraction vaporizes as the curve climbs through it, rather than all at once as in the flat hold. Swab difference vs. Runs 3–4 is within noise (too many uncontrolled variables). Harshness at session tail is a directional signal that 430°F may still be slightly above ideal for this material on the ramp.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 6, 19),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 19, 19, 28, 13, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_6,
        endpoint_note='<strong>Endpoint:</strong> 420°F — 8s ramp; first run on Rig 6',
        swab='Beige — clean.',
        session_char='Dense vapor throughout to ~50s depletion. Harshness entered at ~43s with vapor still dense; water at 43s resolved it; next draw through active vapor clean; depletion signal (vapor drop visible through glass) at end of that draw; two post-depletion draws confirmed no harshness. Very intense. Chatty, creative, uplifting.',
        dab_notes='I was reminded what incredible quality this jar is. The rosin is so incredibly clean. Swabs were beige. Harshness showed up with 17 seconds left. A drink of water and it went away. Maybe a support for particulate accumulation? Very nice very intense high. Feels like the chatty creative and uplifting energy I wanted. Vapor was still dense when harshness showed up, but the material was depleted before the end of 60 seconds, I\'d guess around the 50 second mark. That may be why the harshness resolved, the material ran out so no more particles. Next draw had dense vapor and right at the end of draw showed depletion in drop in vapor observed through stock glass.',
        analysis='First run on Rig 6, first run on sapphire for this jar — all five prior runs were on Rig 1 quartz. Beige swab consistent with this strain\'s historical light-golden-to-very-light pattern and with Rig 6\'s documented efficient vaporization. Harshness entered at ~43s with dense vapor and material still present. User drank water; next draw through active dense vapor was clean — harshness did not return. Depletion signal (vapor drop visible through glass) appeared at end of that draw; two subsequent draws of hot air produced no harshness, consistent with Session 106 (hot air alone at 420°F does not cause harshness). Whatever water reset — particulate load, mucosal sensitization, or thermal sensitization — it held through the remaining material exposure. Mechanism remains open. User notes this as possible support for more percolating glass — more water contact in the vapor path could filter particles before they reach the airway, potentially delaying harshness onset. Tradeoff: more percolation also strips desirable compounds alongside particles. Effects — chatty, creative, uplifting, very intense — matched the occasion and the strain\'s terpene inference exactly.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='The Hive #1',
    profile_anchor='#hive1-profile',
    next_text='Try 420–425°F endpoint on Run 6',
    accent=None,
    slug='hive1',
    info=[
        ('Strain', 'The Hive #1 (Honey Banana × Papaya — Bloom Seed Co)'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Myxed Up (washed and pressed)'),
        ('Input', '159–73 micron ice water hash'),
        ('Nose', 'Very fragrant at cold nose. Spice noticeable (consistent with caryophyllene — weak secondary signal only).'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Myrcene and terpinolene inferred from tropical fruit character; Honey Banana × Papaya lineage (Bloom Seed Co). Terpene ratios not inferable from genetics — standard palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='Repeat 420°F on Rig 6. Stop at depletion signal (~50s) rather than riding to 60s.',
    next_ai_analysis='Repeat 420°F on Rig 6 before adjusting anything. Material depleted at ~50s on Run 6 — on Run 7, stop at the depletion signal rather than riding to 60s; that alone may eliminate the harshness tail without touching the endpoint. If Run 7 replicates the ~43s harshness onset and ~50s depletion, the pattern is established. Don\'t step to 425°F yet — Rig 6\'s efficiency advantage is still being mapped for this strain.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
