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

BP4RW13_DESCENT_GENTLE = [
    Waypoint(time_s=0,  temp_f=440, note='Session open — hot open, descent start'),
    Waypoint(time_s=30, temp_f=420, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
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
        utc_logged_at=datetime(2026, 6, 17, 5, 28, 50, tzinfo=timezone.utc),
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
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 30),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 1, 1, 0, 2, tzinfo=timezone.utc),
        waypoints=BP4RW13_DESCENT_GENTLE,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — first descent curve for this jar',
        swab='brown',
        session_char='No harshness cycle 1; massive terpene-load cough; flavor throughout; harshness moderate cycle 2 dropping to mild after water; three total cycles; intensity overwhelming — big and buzzy',
        intensity='high',
        dab_notes='Cycle 1: 14 second hit and then maybe an 8 second hit from that cycle but it was so terpy I felt like I was choking to death. No harshness but coughing and flavor for days. Cycle 2: got a rip, same character, massive terp load, some harshness appearing — put it down to exhale, coughed a lot on exhale. When I recovered I didn\'t remember I had done the rip so I hit the button to start what I thought was the second cycle but was actually the third cycle, then I realized that I had short stopped the previous cycle and then I restarted it and did another cycle and then did one big rip from that and that\'s when I couldn\'t do any more. God I can\'t hang with it. Harshness moderate, dropped to mild after water. Intensity is fucking big and kind of buzzy. Swabs plentifully showing brown reclaim.',
        analysis='Run 5, first descent curve on this jar, 440°F open → 400°F floor, Rig 5, big load (roughly equal proportions of both rosins), first dab of the day. 14 days and six-plus other jars since Run 4.\n\nThe most striking result: the session ended because intensity overwhelmed, not because harshness crossed a threshold. All four prior runs ended at the tail-harshness ceiling. This run had no harshness on cycle 1 at all — terpene-load cough, no airway harshness, flavor throughout. Harshness appeared on cycle 2 (moderate, dropped to mild after water) but wasn\'t the stopping condition. Intensity was. That\'s a categorically different session profile from any prior run on this jar.\n\nThe descent curve is the most plausible driver. FW106 R23 (Rig 6, 440→350°F descent, first dab, normal load) and WM R16 (Rig 5, same shape, first dab, larger load) both produced clean first cycles with no harshness despite the hot open. This replicates that pattern on a third strain. Opening at 440°F and moving away from it immediately delivers a heavy terpene bolus up front without the sustained high-temperature exposure that drove tail harshness on the ramp runs.\n\nBrown swab is the first departure from golden on this jar. Three cycles from the same load is the most parsimonious driver — same mechanism documented on FW106 where 60s duration runs returned dark golden while 40s runs were beige. 440°F open is an unresolved confound but less likely given that prior descent runs on other strains didn\'t produce notably darker swabs.\n\nThe memory gap after cycle 2 is a data point about intensity, not noise. "Fucking big, buzzy" — Randy Watzon\'s Runtz lineage (Zkittlez × Gelato) is directionally consistent with the cerebral character noted.\n\nUser\'s working hypothesis going in: jar-to-jar variation in optimal curve is small; the descent shape should generalize. One run, large load, long jar gap — the hypothesis earns a supportive data point, not confirmation.',
    ),
    CompletedRun(
        strain='Banana Punch #4 + Randy Watzon #13',
        run_date=date(2026, 6, 30),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 1, 4, 24, 25, tzinfo=timezone.utc),
        waypoints=BP4RW13_DESCENT_GENTLE,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — same descent curve as Run 5, lighter load',
        swab='golden',
        session_char='Lighter load; single cycle; depletion right near session end; harshness slight in the last third; medium intensity',
        intensity='medium',
        dab_notes='It was lighter load, golden swabs, depletion right near the end, harshness slight in the last third. Medium effect.',
        analysis='Run 6, same descent curve as Run 5 (440°F open → 420°F @30s → 400°F floor @60s), Rig 5, lighter load, single cycle, second dab of the day. This directly answers the question Run 5 left open: is intensity load-driven or curve-driven? Medium effect on a lighter load with an identical curve — down sharply from Run 5\'s overwhelming, memory-gap intensity — points at load as the primary lever, not the curve itself. Golden swab returns after Run 5\'s one-off brown, consistent with the swab-darkening pattern being duration/cycle-count driven rather than descent-curve-specific (documented cross-strain on FW106). Harshness stayed mild, appearing in the last third with depletion arriving right near session end — consistent with the harshness-preceding-depletion pattern seen on LHBH R3 (Rig 6), not a pure empty-insert signal. Fourth data point (with FW106 R23, WM R16, and this jar\'s own R5) supporting the descent shape\'s core finding: opening hot and moving immediately away from peak temperature front-loads the terpene bolus without sustained high-temp exposure. With load now controlled down, the curve itself reads as comfortably within range — Run 5\'s ceiling problem was the load, not the shape. Single comparison point; "lighter load → medium" isn\'t a mapped relationship yet, just one data point against Run 5\'s much bigger load.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Banana Punch #4 + Randy Watzon #13',
    profile_anchor='#bp4rw13-profile',
    next_text='Run 7: repeat same descent curve and similar lighter load — confirm reproducibility now that load size resolved Run 5\'s overwhelm',
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
    next_ai_analysis='Repeat the same curve and a similar lighter load on Run 7 to confirm reproducibility before calling this the jar\'s working point — one clean comparison against Run 5\'s overwhelm isn\'t enough, especially given this thumbprint\'s documented run-to-run load variability (Runs 1–4 all fought portion control on the runny material). If Run 7 replicates clean and medium, this curve/load combination is the baseline going forward. If intensity swings again despite a deliberately controlled load, load control on this specific jar is as unreliable as it\'s looked all along, and the fix becomes weighing or eyeballing more carefully before starting rather than trusting the "lighter" instruction alone.',
    next_waypoints=BP4RW13_DESCENT_GENTLE,
    jar_index='',
)
