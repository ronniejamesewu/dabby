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
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 11),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 11, 20, 5, 2, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_HOLD10_DESCENT_GENTLE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 440°F, then gentle descent; same curve as Run 1, ran two cycles',
        swab='dark amber, reddish tint',
        session_char='Dark amber swab with a reddish, dark-BBQ-sauce tint — darker than Runs 1–2, but a two-cycle run (second cycles darken independent of endpoint); minimal reclaim. First dab of the day, full 60s cycle 1 then a cashed second cycle; strong, energetic, functional, a tad racy. Delicious throughout, with a read of a fresh-press terpene difference. Mild throat-and-chest harshness in cycle 1 that resolved by the second cycle and did not return on the spent-material hot-air draw.',
        intensity='strong',
        dab_notes='440 descent, I ran a full cycle, then a second cycle but it was cashed and majority of the long draw (I was already feeling the first cycle) was empty. A point for the accumulation not thermal hypothesis of harshness. The swabs came back dark amber, almost a reddish tint to it-reminded me a little of a dark bbq sauce. Minimal amount. Intensity was quite high at first very energetic, very functional, a tad racy. [Flavor:] It was really delicious throughout, I think I can tell the difference in the fresh press terpenes. A little harshness in throat and chest very mild. [Resolved by the second cycle and did not return on that empty draw.]',
        analysis='Run 3 repeats Run 1\'s bounded 440°F hold into the gentle descent to 400°F — first dab of the day, the jar\'s first daylight run and its first flavor read. Delicious throughout, with a read of a fresh-press terpene difference; that\'s a subjective single-session impression (palate is a weak signal and this is the jar\'s first flavor data), so it\'s noted, not weighted — the inferred limonene/bitter-citrus character still isn\'t specifically confirmed. Mild throat-and-chest harshness appeared in cycle 1 (material present), resolved by the second cycle, and did not return on the cashed second-cycle draw — a long pull through spent material and hot air. That within-session structure (harshness with material, gone on the hot-air-only draw) is a cleaner point for accumulation over thermal than Run 1 offered, and is consistent with the empty-insert control — hot air alone doesn\'t cause harshness; material presence is the necessary condition (Session 106) — at single-instance weight. Chest location adds another instance to the hot-open Rig 6 group (papzp22 R7, bp4rw13 R8, LunarZ R1); no persistence reported and it resolved before session end, so this is chest-location in-session only, not the chest-and-lingers conjunction. Swab dark amber with a reddish, dark-BBQ-sauce tint — darker than Runs 1–2\'s dark amber, but this was a two-cycle run and second cycles darken swabs independent of endpoint (bp4rw13 R5–R8, FW106 R27), so the darker read is cycle-confounded, not a new floor signal; reclaim stayed minimal, so material delivered rather than cooked (the deliver-vs-cook read comes off reclaim and effect, not color). Strong — energetic, functional, a tad racy. Same rig throughout (Rig 6); load not stated this run.',
    ),
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 11),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 12, 0, 0, 49, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_HOLD10_DESCENT_GENTLE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 440°F, then gentle descent; same curve as Runs 1 &amp; 3, over-load carried a second cycle',
        swab='dark amber, dark-BBQ-sauce tint',
        session_char='Dark amber / dark-BBQ-sauce swab; normal reclaim, up from the minimal of Runs 1–3, tracking a bigger (unintentional) load. Second dab of the day, full 60s cycle 1 into a second cycle that cashed partway; dense and flavorful throughout, toast on the exhale of the final ~75%-of-a-draw once material was spent. Strong, energetic and functional (a "yoga strain"); delicious, same fresh-press terpene read as Run 3. No harshness reported.',
        intensity='strong',
        dab_notes='Wow, so good. I\'m going to be really interested in seeing the difference in this when it\'s cured. There\'s something really scrumptious to it as it is now. But so hard to load. I thought I loaded normal but it hit dense and flavorful all the way through first cycle and a bit draw of the second cycle. Second draw of second cycle it depleted at maybe 75% of a draw, and toast on the exhale of that one. So, a few thoughts. I loaded a bit more than the first run today. But I didn\'t mean to. It\'s just not easily controlled. So part of our question on how best to use this device expands to considering which curves balance performance with fault tolerance. [Swab:] that bbq sauce color, normal reclaim. Pretty high intensity. Still have a strong sense of "yummyness". [Effect:] This is definitely a yoga strain. I\'m glad I have 4 grams. If only it wasn\'t in taffy format.',
        analysis='Fourth hot-curve run, 2nd dab of the day, and the first clear load-overshoot — a bit more than the day\'s first dab, unintentional (the taffy resists portioning). The curve absorbed it: dense and flavorful through cycle 1 and most of a second, with toast only on the final cashed draw once material was spent — residue-scorch on depletion (same read as Hive #1 R10), not session order; the fast-depletion timing fits scorch before any accumulated-exposure framing. Reclaim came back normal, up from Runs 1–3\'s minimal, consistent with the bigger load leaving more residue; with the strong effect and dense vapor it still reads deliver-side, not cooked-in-place (contrast FW106 R31\'s dark amber with heavy reclaim from sustained peak). Swab dark amber / dark-BBQ-sauce again, but this was a two-cycle run and second cycles darken swabs independent of endpoint (bp4rw13 R5–R8, FW106 R27) — cycle-confounded like Run 3, and within-strain only. Strong and energetic (a "yoga strain"), matching Run 3\'s energetic/functional/racy read — two consistent daylight reads, directional for this jar running up rather than sedating; flavor delicious with the same fresh-press terpene impression, noted at weak-signal weight, so the inferred limonene/bitter-citrus still isn\'t specifically confirmed. No harshness this run, unlike Run 3\'s mild chest-and-throat. Same rig (Rig 6); against Runs 1/3 order and load both differ, so no isolation. As a single supporting observation, the over-load carrying into a second cycle rather than cooking is consistent with the descent-curve limiting-factor pattern and the load-fault-tolerance read — opening hot and descending puts peak heat where material is densest and the cool floor where depletion lands.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Sour Tangie',
    profile_anchor='#sourtangie-profile',
    next_text='Run 5: baseline 420°F fast ramp, first dab, single cycle, modest load — the still-pending cooler-endpoint reference; tests whether the dark amber lightens off a single cool cycle',
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
    next_ai_analysis='Four runs in, all hot curves, all strong, all dark amber — and the cooler-endpoint reference is still missing; four two-cycle hot runs can\'t say whether the dark swab is heat/cycle or strain character. Run 5: run the current baseline (380 → 400 @4s → 420 @8s, hold to 60s), first dab, single cycle, modest load — first-dab and single-cycle strip the session-order and second-cycle-darkening confounds. It\'s a measurement run, not a bet against the 440-hold-descent, which is already this jar\'s operating curve. Expected: swab lightens toward golden at 420°F single-cycle if the color was heat-driven. Surprising: dark amber persists single-cycle — then swab isn\'t a fine-calibration lever for this jar.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
