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
    Waypoint(time_s=4, temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8, temp_f=425, note='Endpoint — up 5°F from baseline'),
    Waypoint(time_s=60, temp_f=425, note='Hold'),
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
        run_date=date(2026, 6, 20),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 20, 23, 1, 34, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_6,
        endpoint_note='<strong>Endpoint:</strong> 420°F — 8s ramp; second cycle (1 draw); first dab of day, larger load',
        swab='Golden — second cycle (one draw) attributed as driver; beige expected without it.',
        session_char='Very little harshness late in draw 2 (~30s remaining), never escalated. Heavy terpene-load coughing throughout. Mildew, fruitiness, and savory/cheese notes in early draws. Second cycle: one draw. Medium-high intensity, still building post-session.',
        dab_notes='Swabs golden but I did run 1 draws worth of a second cycle so darker makes some sense. Very little harshness, which showed up late in the second draw, maybe 30 seconds left. I didn\'t have water handy but through the rest of the draws it never really increased. Flavor in first couple draws had that mildew quality, also some fruitiness, and maybe something savory? Cheese? It produced a lot of coughing which is interesting to get that effect but not a lot of harshness. Maybe it\'s because first dab of the day. Intensity medium high and building.',
        analysis='Run 8 on Rig 6 at 420°F — first dab of day, deliberate larger load. Functionally clean: very little harshness, appeared late in draw 2 (~30s remaining), never escalated. Swab golden — user attributes to the second cycle (one draw), consistent with the established cycle-count swab pattern (second cycles drive darker swabs regardless of material or endpoint; beige is the likely baseline without it). Coughing throughout with little harshness is consistent with terpene-load cough at dense vapor delivery — FW106 R1 on Rig 4 documented the same signature (terpene-load cough without harshness at 416°F); a larger load through Rig 6\'s efficient joystick delivery produces denser early vapor that can trigger a cough reflex before the harshness threshold is crossed.\n\nThree runs at 420°F on Rig 6 now: R6 (first dab, uncertain/smaller load, harsh at ~43s); R7 (second dab, lighter suspected load, clean); R8 (first dab, larger load, very little non-escalating harshness). R8 matches R6\'s session-order condition and gives a meaningfully cleaner result — load size is the most parsimonious explanation for R6\'s divergence. Smaller load in R6 likely brought material to depletion or the harshness threshold earlier; R6 depleted at ~50s with harshness entering 7s prior, which is consistent with either hot-insert exposure or density crossing at the load\'s margin. R8\'s second cycle confirms material was still present well into the session.\n\nFlavor notes — mildew, fruitiness, savory/cheese — are new for this jar. Prior runs noted spice (R1–5) and a floral cold nose (R7). Worth tracking whether this profile stabilizes on R9 or reflects the jar\'s current fridge state.\n\n420°F is the working point on Rig 6 for this jar with adequate load. R6 is now the outlier, explained by load, not a ceiling signal.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='The Hive #1',
    profile_anchor='#hive1-profile',
    next_text='Run 9: push to 425°F — first dab of day, larger load',
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
    next_dab_notes='425°F, 8s ramp, 60s hold. First dab of day, larger load. Watch: harshness onset timing vs. R8\'s ~30s; flavor character (mildew/fruitiness/savory — does it persist?).',
    next_ai_analysis='Three runs at 420°F on Rig 6 — R8 (first dab, larger load) was functionally clean, resolving the R6 vs. R7 ambiguity: load was the live variable, not session order. 420°F is established. Run 9: push to 425°F, same first-dab condition, same load discipline. If clean or comparable to R8, 420°F is well below the ceiling and 425°F is the new working point. If harshness escalates meaningfully earlier than R8\'s ~30s, 420°F is the operating point.',
    next_waypoints=HIVE1_NEXT,
    jar_index='',
)
