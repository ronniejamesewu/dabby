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
]

# ── Status ──
STATUS = StrainStatus(
    name='Banana Punch #4 + Randy Watzon #13',
    profile_anchor='#bp4rw13-profile',
    next_text='Run 3: try 430°F with normal load, single cycle',
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
    next_ai_analysis='Run 3: try 430°F, same 8s ramp, 60s single cycle. Harshness in the last 20s with material confirmed remaining at 425°F points at accumulated heat exposure / airway sensitization, not depletion — depletion won\'t fix it. The user\'s instinct toward higher temp aligns with the curve working theory: faster, more complete vaporization means the load is spent before the harshness window. The golden reclaim at 425°F also confirms there\'s room to push. If harshness shifts earlier at 430°F, pull back to 427–428°F; if it stays in the tail or disappears, 430°F is the operating point.',
    next_waypoints=BP4RW13_430,
    jar_index='',
)
