"""Sour Tangie — jar file (slug: sourtangie)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
SOURTANGIE_HOLD10_DESCENT_GENTLE = [
    Waypoint(time_s=0,  temp_f=440, note='Session open — hot open'),
    Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F'),
    Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

SOURTANGIE_430 = [
    Waypoint(time_s=0,  temp_f=380, note='Session open'),
    Waypoint(time_s=4,  temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8,  temp_f=430, note='Endpoint'),
    Waypoint(time_s=60, temp_f=430, note='Hold'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 10),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 11, 1, 5, 3, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_HOLD10_DESCENT_GENTLE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 440°F, then gentle descent; jar opener, baseline skipped',
        swab='dark amber',
        session_char='Dark amber swab with minimal reclaim; small taffy load, first dab of the day, full 60s; strong effect, no harshness reported.',
        intensity='strong',
        dab_notes='I\'m gonna run the 440 hold descent curve on this. The format is super sticky, it reminds me of taffy, so hard to precisely portion load. But I\'m pretty sure I loaded a small one. [Report:] I did my dab at the 440 hold descent. [Swab, both runs:] dark amber, minimal. Both swabs, I thought it was weird too. [Intensity:] strong strong. [Full 60 on both.]',
        analysis='First read on the Sour Tangie jar — the bounded 440°F hold into the gentle descent to 400°F, small taffy load, first dab of the day. Strong effect, no harshness, full 60s. Strong on a deliberately modest load validates the 710 first-run potency caution: the jar is potent and the small load was the right call. The dark amber swab is the surprise on a load this small — but the minimal reclaim says the material delivered rather than cooked in place (contrast FW106 R31, where dark amber came with heavy reclaim from sustained peak cooking material uninhaled). Swab is a within-strain signal only and this is the jar\'s first data point, so dark amber isn\'t yet a floor signal to act on — with only hot-curve runs so far, strain/material character and a hot 440°F open can\'t be separated. Same rig as recent runs (Rig 6). No flavor read this session, so the inferred limonene/bitter-citrus signature is still untested solo.',
    ),
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 10),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 11, 1, 10, 0, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 430°F — 380→430 fast ramp (8s), hold to 60s',
        swab='dark amber',
        session_char='Dark amber swab (a shade darker than Run 1, same to a casual eye), minimal reclaim; bigger-than-normal load, second dab of the day, full 60s; strong effect. Loaded for a big-draw-first, occasional-user opener who coughed/gagged at the 380°F open and tapped out; remainder finished on the 430°F hold.',
        intensity='strong',
        dab_notes='I had most of Sarah\'s dab running on a 380 to 430 ascent curve we ran before, a baseline variation. I did the majority of the 430 part. Sarah is my wife, I loaded her a dab and switched the curve to the ascent to 430 curve. She took a big draw starting at 380 and coughed and gagged. Didn\'t want any more so I finished the rest on that curve. [Load:] bigger than normal but I wouldn\'t say large. [Swab:] dark amber, minimal — Sarah\'s dab maybe slightly darker but casual observer would say same. [Intensity:] strong strong. [Full 60.]',
        analysis='Second dab of the day, on the 380→430 fast-ramp ascent — a bigger-than-normal (but not large) load, opened with a big draw right at the 380°F open by an occasional user who coughed and gagged and tapped out; the majority was finished on the 430°F hold. Strong again, full 60s, swab dark amber with minimal reclaim — maybe a shade darker than Run 1, but same to a casual eye. The dark-amber / minimal-reclaim pairing now shows on two different hot curves (the 440-hold-descent and this 430 ascent) — directional, within this jar, that the color tracks strain/material rather than either specific curve, since the shape differed and the swab didn\'t. Same rig both runs (Rig 6); equipment controlled. The cough/gag on a big draw at the 380°F open is hard to read: a big first draw into a fast-ramping cold start delivers dense vapor quickly, so terpene-load cough (documented on Rig 6 — Hive #1 R8, FW106 R1) is as consistent as harshness — and an occasional user taking an unusually big draw leaves technique and tolerance uncontrolled. Not weighted as a curve signal. Run 2 vs. Run 1 can\'t isolate anything — curve, load, and session order all differ.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Sour Tangie',
    profile_anchor='#sourtangie-profile',
    next_text='Run 3: baseline 420°F fast ramp, first dab, modest load — standard reference point, and a test of whether the dark amber lightens at a cooler endpoint',
    accent=None,
    slug='sourtangie',
    info=[
        ('Strain', 'Sour Tangie (East Coast Sour Diesel × Tangie — DNA Genetics / Crockett; Tangie: California Orange × Skunk #1; Sour Diesel: Chemdawg \'91 × Super Skunk, disputed)'),
        ('Consistency', 'Live rosin (Persy tier)'),
        ('Producer', '710 Labs'),
        ('Nose', 'Super faint — jar cold from dispensary freezer; no distinct notes yet. Weak secondary signal; expect it to open as it warms.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred dominant from the Tangie side (California Orange × Skunk #1 — citrus/orange lineage); caryophyllene and myrcene from the Sour Diesel side (Chemdawg \'91 × Super Skunk — diesel/gas, though DNA hedges this cross and a competing "DNL" origin exists). Consistent with the limonene-forward bitter-citrus/tangerine character logged when Sour Tangie ran as a layer in the closed Mango Banana #9 + Z + Sour Tangie jar. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Two runs in, both hot curves (440-hold-descent, 430 ascent), both strong with no harshness, both dark amber with minimal reclaim on Rig 6 — the jar delivers hard and clean. Dark amber on two runs is a warm-swab/floor signal, but because both opened hot we can\'t separate the jar\'s character from the endpoint temperature. Run 3: drop to the current baseline (380 → 400 @4s → 420 @8s, hold to 60s), first dab, modest load — that both answers the floor signal and gives this new jar a standard reference point it doesn\'t have yet. Keep it first-dab to dodge the session-order confound that muddies the Run 1/Run 2 comparison. Expected: still strong, swab lightening toward golden at 420°F with reclaim still minimal if the color was heat-driven. Surprising: dark amber persists at 420°F — that points to strain/material character over endpoint, meaning swab won\'t be a fine-calibration lever for this jar.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
