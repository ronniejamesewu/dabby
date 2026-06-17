"""Banana Punch #4 + Randy Watzon #13 — jar file (slug: bp4rw13)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

BP4RW13_425 = [
    Waypoint(time_s=0,  temp_f=380, note='Session open'),
    Waypoint(time_s=4,  temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8,  temp_f=425, note='Endpoint — up 5°F from baseline'),
    Waypoint(time_s=60, temp_f=425, note='Hold'),
]

BP4RW13_430 = [
    Waypoint(time_s=0,  temp_f=380, note='Session open'),
    Waypoint(time_s=4,  temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8,  temp_f=430, note='Endpoint — up 5°F from Run 2'),
    Waypoint(time_s=60, temp_f=430, note='Hold'),
]

BP4RW13_435 = [
    Waypoint(time_s=0,  temp_f=380, note='Session open'),
    Waypoint(time_s=4,  temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8,  temp_f=435, note='Endpoint — up 5°F from Run 3'),
    Waypoint(time_s=60, temp_f=435, note='Hold'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──

RUNS = [
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 16),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 16, 18, 38, 34, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 420°F — baseline curve, inaugural run',
        swab='golden',
        session_char='Tasty but not overly; dense vapor through two cycles; mild to mid harshness; very smooth overall; high intensity',
        intensity='high',
        dab_notes='Tasty but not overly. Ran for two cycles, still very dense with mild to mid harshness. Very smooth overall. Golden swabs, lots of reclaim — fits with too big a load. High intensity. Hint of harshness at end of first cycle, present throughout second.',
        analysis='Run 1, baseline curve, Rig 5, larger-than-normal load. Golden swab and heavy reclaim are consistent with the oversized load — material was not depleted; reclaim is excess reaching the glass. Dense vapor through both cycles confirms it. Harshness pattern — hint at the tail of the first cycle (~60s), present throughout the second from the first draw — is consistent with airway sensitization carrying over between cycles: cycle 1 primed the airways enough that cycle 2 started already past the threshold. Depletion is ruled out by material remaining. Vapor density is a live candidate given the large load, but the immediate-onset harshness in cycle 2 points more directly at accumulated airway state than density per se. "Very smooth overall" with mild-to-mid harshness reads as threshold-crossing but not acute. High intensity expected on the larger load; confounded first read. Tasty but not overly on a new jar is neutral — character may open as the jar continues to cure. Single data point; load size is the dominant confound.',
    ),
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 16),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 16, 21, 30, 0, tzinfo=timezone.utc),
        waypoints=BP4RW13_425,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 425°F — up 5°F from Run 1',
        swab='golden',
        session_char='Very tasty; very dense vapor; harshness in last 20 seconds; medium-high intensity',
        intensity='medium-high',
        dab_notes='Very tasty, very dense. Harshness in last 20 seconds. Lots of golden reclaim, I think this maybe needs even higher temp. Intensity was medium high.',
        analysis='Normal load, single cycle, 425°F — up 5°F from Run 1. Vapor character improved clearly: "very tasty" and "very dense" vs Run 1\'s "tasty but not overly." Harshness landed in the last 20 seconds of a 60s cycle — later and more contained than Run 1, where it tracked throughout the second cycle. Golden swab with lots of reclaim at normal load rules out depletion as the harshness driver — material was still present at session end. Accumulated heat exposure / airway sensitization is the more parsimonious framing: 40s of 425°F vapor without a depletion signal, threshold crossed somewhere in the tail. Second-dab-of-the-day is a mild confound but one prior session isn\'t dramatic. The "needs higher temp" read is directionally consistent with the shorter-and-higher working theory: higher endpoint vaporizes more completely, potentially exhausting the load before the harshness threshold is crossed. Two-data-point read; load-size isolation from Run 1 landed cleaner session character, as expected.',
    ),
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 16),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 6, 17, 2, 47, 20, tzinfo=timezone.utc),
        waypoints=BP4RW13_430,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 430°F — up 5°F from Run 2',
        swab='golden',
        session_char='Tasty; harshness only in last 10 seconds, not acute; single cycle; medium intensity',
        intensity='medium',
        dab_notes='Super nice run. Tasty, harshness in last 10 second but not bad. I wanted to run a second cycle but didn\'t. Swabs were golden, maybe still a lot more reclaim and that seemed like a normal load. But this jar is runnier than the other thumbprint jars. Hard to control load size — been trying, thought I had it much smaller.',
        analysis='Run 3, 430°F, single cycle, third dab of the day. Harshness pushed back another 10 seconds from Run 2 — last 20s at 425°F, last 10s at 430°F. The trend across three single-cycle runs is clean and directional: each 5°F bump has bought roughly 10 more seconds of clean session. "Not bad" matters — this is threshold-crossing at the very tail, not the acute carry-over harshness from Run 1\'s second cycle. Golden swab with heavy reclaim again; user has been trying to keep loads small but the runniness makes portion control genuinely difficult — actual load size across all three runs is uncertain, and some of the persistent reclaim likely reflects consistency-driven pooling rather than purely unconsumed material. Depletion-ruled-out framing stands but is softened. Intensity landed medium as third dab of the day — tolerance accumulation is the dominant read; not diagnostic for the temperature-intensity relationship.',
    ),
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 16),
        sessions_prior_today=3,
        utc_logged_at=datetime(2026, 6, 17, 6, 20, 11, tzinfo=timezone.utc),
        waypoints=BP4RW13_435,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 435°F — up 5°F from Run 3',
        swab='golden',
        session_char='Lots of vapor; harshness in last 17 seconds; tasty; high intensity',
        intensity='high',
        dab_notes='Golden swab, less reclaim than prior runs. Lots of vapor, harshness with about 17 seconds left. Tasty. Hit hard, high intensity.',
        analysis='Run 4, 435°F, 8s ramp, 60s single cycle, fourth dab of the day. Harshness entered at ~17s left — a step backward from Run 3\'s last 10s, against the predicted direction. Less reclaim than prior runs is the most plausible confound: smaller actual load means less material buffering the session, earlier heat-exposure onset once the load thins. Fourth dab of the day adds a mild airway-sensitization confound — threshold may be lower than a fresh-start run would show. "Lots of vapor" and high intensity confirm material was present well into the session, so outright depletion isn\'t the obvious driver, but a smaller load that ran thin around 43s is consistent with both the vapor density reading and the harshness onset timing. The 10s-per-5°F trend from Runs 1–3 didn\'t hold at 435°F — two reads: the trend was fragile and the load confound finally showed through, or 435°F has a different relationship with harshness than the lower endpoints did. With four uncontrolled loads across this jar\'s history, the load read is more parsimonious. "Tasty" and high intensity at 435°F are clean positives.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Banana Punch #4 + Randy Watzon #13',
    profile_anchor='#bp4rw13-profile',
    next_text='Run 5: repeat 435°F, first dab of day, deliberate larger load — confirm whether the Run 4 reversal was confound-driven',
    accent=None,
    slug='bp4rw13',
    info=[
        ('Strains', 'Banana Punch #4 (Banana OG × Purple Punch) + Randy Watzon #13 (Runtz × Wedding Crasher — Runtz: Zkittlez × Gelato; Wedding Crasher: Wedding Cake × Purple Punch)'),
        ('Format', 'Close Friends Persy Thumbprint — outer ring cold cure badder (Banana Punch #4), center jam (Randy Watzon #13) layered on top of the same badder. 90μ persy-tier. Outer ring load is pure BP#4; center load blends both. Load zone not distinguishable by eye.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Banana Punch #4 brings ripe banana and grape. Randy Watzon #13 adds Runtz-forward sweetness, Z, and musky gas on the backend. Fruit up front, gas underneath.'),
        ('Nose', 'Fruity, hint of chem/gas (Run 1)'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Myrcene inferred from Banana Punch #4 (Banana OG × Purple Punch — banana/sweet indica character); limonene and linalool inferred from Randy Watzon #13 (Runtz × Wedding Crasher — Runtz: Zkittlez × Gelato; Wedding Crasher: Wedding Cake × Purple Punch). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='The 10s-per-5°F trend didn\'t hold at Run 4 — harshness landed at ~17s instead of the predicted ~5s or gone. Less reclaim suggests a smaller load, which is the most plausible explanation: smaller load means less material buffering the session, triggering heat-exposure harshness sooner. Fourth dab of the day adds an airway-sensitization confound. Before stepping to 440°F, repeat 435°F as first dab of day with a deliberate larger load. If harshness pushes back to 5–10s, the trend is intact and 440°F is the next step. If it still lands at ~17s, the 435°F ceiling is real and 440°F or a session-length cut (stop at ~45s at 430°F) is the direction.',
    next_waypoints=BP4RW13_435,
    jar_index='',
)
