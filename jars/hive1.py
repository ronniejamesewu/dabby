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
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 6, 19),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 19, 22, 42, 22, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_6,
        endpoint_note='<strong>Endpoint:</strong> 420°F — 8s ramp; repeat of Run 6 curve',
        swab='Beige — clean.',
        session_char='Clean throughout, no harshness, full 60s. Proactive water sip mid-session. Vapor wispy in last 2. Medium intensity.',
        dab_notes='Cold nose has a floral note on jar today. Super clean run. No harshness with a sip of water in the middle — just a proactive sip. Finished whole 60 seconds, saw vapor wispiness in last 2.',
        analysis='Run 7 on Rig 6 at 420°F — clean throughout, full 60s, no harshness. Beige swab consistent with Run 6 and this jar\'s history. Water sip was proactive, not reactive — the clean outcome stands on its own without water as an intervention. Vapor wispy in the last 2 (seconds or draws — reported ambiguously) is consistent with depletion near session end, parallel to Run 6\'s ~50s depletion signal. Two runs at 420°F on Rig 6 now give opposite harshness outcomes: Run 6 had harshness at ~43s (first dab, very intense); Run 7 was clean to 60s (second dab, medium intensity). Session order goes the wrong direction to explain it — second dab should accumulate more airway exposure, not less. The intensity gap is the live confound: medium vs. very intense suggests Run 7 may have been a lighter load, and lower vapor density may have kept the harshness threshold uncrossed throughout. Pre-session cold nose note (floral) logged; different character from prior spice-forward descriptions, consistent with the jar continuing to develop in the fridge.',
    ),
    CompletedRun(
        strain='The Hive #1',
        run_date=date(2026, 6, 19),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 6, 20, 2, 1, 5, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_6,
        endpoint_note='<strong>Endpoint:</strong> 420°F — 8s ramp; third run on Rig 6',
        swab='Beige — clean.',
        session_char='Very nice. Harshness at ~23s (~37s remaining, timing approximate). Reactive water sip; harshness returned; stopped cycle early. Load present at end of cycle. High intensity initially; duration short.',
        dab_notes='Not the planned experiment — same 420 curve. Very nice. Swabs beige. Harshness around 37 seconds left — might have the time wrong. Had a sip of water and kept going. Load wasn\'t depleted at end of cycle but harshness was back and I was done. High intensity for a little bit, duration doesn\'t seem to stick.',
        analysis='Run 8 on Rig 6 at 420°F — beige swab consistent with the jar\'s history. Harshness entered at approximately 23s (~37s remaining, timing flagged as uncertain). Water sip mid-session (reactive this time, unlike Run 7\'s proactive sip) didn\'t hold — harshness returned and the user stopped the cycle. Load was present at the end, so depletion doesn\'t explain it. Third dab of the day. Three runs at 420°F on Rig 6 now span a range: Run 6 (first dab, harshness ~43s), Run 7 (second dab, clean to 60s), Run 8 (third dab, harshness ~23s approximate). The pattern isn\'t monotone — cleanest run was the second dab, not the first — which cuts against a simple session-order story and keeps load size as a live confound. Run 7\'s medium intensity vs. Run 6 and 8\'s higher intensity is consistent with a lighter load in Run 7 explaining the clean result as much as session order. "High intensity for a little bit, duration doesn\'t stick" noted; three dabs into the day, tolerance is the most parsimonious read on the short duration.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='The Hive #1',
    profile_anchor='#hive1-profile',
    next_text='Run 9: repeat 420°F on Rig 6, first dab of day, deliberate larger load',
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
    next_dab_notes='Repeat 420°F on Rig 6, first dab of day, deliberate larger load — test whether the clean range at this endpoint holds at higher material weight.',
    next_ai_analysis='Three runs at 420°F on Rig 6, all from the same day, now show: Run 6 (first dab, harshness ~43s), Run 7 (second dab, clean to 60s), Run 8 (third dab, harshness ~23s approximate). Non-monotone pattern keeps load size and session order entangled — the planned experiment (first dab, deliberate larger load) still hasn\'t happened. Run 9: first dab, deliberate larger load. That\'s the one that actually tests whether 420°F on Rig 6 is clean at this material weight.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
