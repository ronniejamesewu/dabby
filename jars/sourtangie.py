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

SOURTANGIE_HOLD10_DESCENT_GENTLE_430 = [
    Waypoint(time_s=0,  temp_f=430, note='Session open — hot open'),
    Waypoint(time_s=10, temp_f=430, note='Hold at peak — one draw at 430°F'),
    Waypoint(time_s=35, temp_f=415, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

SOURTANGIE_HOLD_DESCENT_450 = [
    Waypoint(time_s=0,  temp_f=450, note='Session open — hot open'),
    Waypoint(time_s=10, temp_f=450, note='Hold at peak — one draw at 450°F'),
    Waypoint(time_s=30, temp_f=425, note='Gentle descent midpoint'),
    Waypoint(time_s=45, temp_f=410, note='Floor — shorter cycle'),
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
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 12),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 12, 20, 23, 14, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_HOLD10_DESCENT_GENTLE_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 430°F, then gentle descent (teal); cooler open than Runs 1/3/4, ran two cycles',
        swab='dark golden, minimal',
        session_char='Dark golden swab with minimal reclaim — the jar\'s first lighter read after four dark-amber runs; bigger-than-normal load (the taffy resists portioning), second dab of the day, two full 60s cycles. Terp-forward, tasty, dense vapor; strong. Harshness escalated mild→medium at the bottom of the throat and in the chest, and a water sip did not clear it. Stopped on a lot of hits plus the harshness turning unpleasant.',
        intensity='strong',
        dab_notes='Holy shit that first cycle was kicking. So much terps. [Going for another round.] Second cycle just kept delivering. Tasty hits dense vapor, mild and then medium harshness at bottom of throat and in chest. Water didn\'t mediate. I\'m stopping because I\'ve had a lot of hits and also the harshness is unpleasant. [Swab:] Swabs were dark golden, pretty minimal. [Load:] Bigger than normal load cause of the format.',
        analysis='Run 5 is the jar\'s first teal run — the 430°F bounded-hold descent, a 10°F cooler open than the 440°F curve of Runs 1/3/4 — taken to test whether the persistent dark-amber swab is heat-driven or strain character. Not the clean measurement planned (first-dab, single-cycle baseline 420°F ramp): this was a 2nd dab, two full 60s cycles, bigger-than-normal load (the taffy resists portioning — Run 4\'s standing problem). The swab is the payoff: dark golden, minimal reclaim — the jar\'s first read lighter than its four dark-amber runs, and lighter despite being a two-cycle run, where second cycles darken independent of endpoint (bp4rw13 R5–R8, FW106 R27). That the darkening confound points the other way makes the lightening a real directional signal that the color is at least partly heat-driven — but it\'s one run, curve/order/load all differ from the amber runs, and swab is within-strain only, so it\'s an observation, not settled. Bigger load, minimal reclaim, strong, dense = deliver-side, not cooked — the descent absorbing an over-load, as on Run 4. Harshness escalated mild→medium at the bottom of the throat and chest, and a water sip didn\'t clear it — the log\'s first full water non-response (six prior were full resets, LunarZ R3 partial). Vapor density and cumulative exposure are the leading, inseparable candidates: the bigger load draws denser vapor, and 2nd dab + two cycles + a lot of hits is a session-long airway load a single sip wouldn\'t reset — the accumulation-over-thermal read the user flagged on Run 3, single-instance weight. Chest location adds to the hot-open Rig 6 group (papzp22 R7, bp4rw13 R8, LunarZ R1–R3, Sour Tangie R3), here at a 430°F open like LunarZ R2/R3; no persistence reported, so in-session location only, not the chest-and-lingers conjunction. Terp-forward and tasty, consistent with the R3–R4 fresh-press read (weak signal). Rig 6 throughout; strong.',
    ),
    CompletedRun(
        strain='Sour Tangie',
        run_date=date(2026, 7, 12),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 7, 13, 1, 8, 4, tzinfo=timezone.utc),
        waypoints=SOURTANGIE_HOLD10_DESCENT_GENTLE_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 430°F, then gentle descent (teal); same curve as Run 5, ran two cycles',
        swab='amber, normal',
        session_char='Amber swab with normal reclaim — lighter than the four 440°F-open runs (R1–R4) and in line with Run 5\'s dark-golden read at the same cooler open. Third dab of the day, full 60s cycle 1 into a second cycle stopped after the second draw; tasty and dense throughout, strong (quite high). Harshness built from ~20s left in cycle 1 to a solid medium by the second draw of cycle 2, throat-and-chest; no water taken. Stopped on the harshness.',
        intensity='strong',
        dab_notes='Ok, I did it. Tasty and dense throughout. It wasn\'t done at first cycle so did a second. Harshness building from maybe 20 seconds left in first cycle to a solid medium in second draw of second cycle. I stopped after that. Swabs are Amber, normal amount. Intensity is quite high. I think my intuition is building for shorter cycle at a 450 hold and gentle descent. [Harshness location:] both throat and chest. [Water:] no.',
        analysis='Run 6 repeats the teal 430°F bounded-hold descent (same curve as Run 5), a 3rd dab of the day over two cycles — full 60s cycle 1 into a second cycle stopped after the second draw. Like Run 5, not the clean first-dab single-cycle isolation the plan called for; that read has now failed to happen two runs running. Swab amber with normal reclaim. Both 430°F-open runs (R5 dark golden, R6 amber) came in lighter than the four 440°F-open runs (R1–R4, all dark amber) — and R6 stayed lighter despite being a two-cycle run, where second cycles darken independent of endpoint (bp4rw13 R5–R8, FW106 R27). Two consistent runs with the darkening confound pointing the other way is directional, within this jar, that the swab color is at least partly heat-driven (cooler open → lighter swab); load and session order still differ across the amber and lighter runs, and swab is within-strain only, so directional, not settled. Normal reclaim with strong, dense vapor reads deliver-side, not cooked (contrast FW106 R31\'s dark amber with heavy reclaim from sustained peak). Harshness built from ~20s left in cycle 1 to a solid medium by the second draw of cycle 2, throat-and-chest; no water was taken. That escalation matches Run 5 (also 430 teal, later dab, two cycles, escalating mild→medium chest-and-throat) — two consistent runs now that this curve under heavy cumulative load throws escalating chest-and-throat harshness. Vapor density and cumulative exposure stay the leading, inseparable candidates: dense vapor plus a 3rd dab carried across two cycles is a session-long airway load. Because no water was taken, Run 6 doesn\'t extend Run 5\'s water non-response — whether a sip resets this curve under lighter load stays open. Chest location adds to the hot-open Rig 6 group (papzp22 R7, bp4rw13 R8, LunarZ R1–R3, Sour Tangie R3/R5), here at a 430°F open like LunarZ R2/R3 and Sour Tangie R5; no persistence reported, so in-session location only, not the chest-and-lingers conjunction. Tasty and dense throughout, consistent with the R3–R5 terp-forward reads (weak palate signal). Same rig (Rig 6); load not stated. Against Runs 1/3/4/5, order and cycle count differ — no clean isolation.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Sour Tangie',
    profile_anchor='#sourtangie-profile',
    next_text='Run 7: 450°F bounded hold + shorter gentle descent (450→450@10s→425@30s→410@45s) — run it as a genuine first dab, single cycle, modest load, so the shorter cycle also delivers the clean-order read Runs 5–6 kept missing',
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
    next_ai_analysis='Follow the building intuition: a hotter 450°F bounded hold into a gentle descent, capped to a single shorter cycle. The shorter/single cycle directly targets what Runs 5 and 6 both indict — escalating chest-and-throat harshness that tracks cumulative exposure (later dab + two cycles), not open temperature — while the hotter open front-loads the terpene bolus this jar keeps delivering. Run it as a genuine first dab, modest load: that finally controls order and cycle count, turning the shorter-cycle idea into the clean read the last two runs kept missing. Keep the descent slope at or above the sapphire\'s ~1°F/s passive decay, or the PID just holds near 450 and cooks it (FW106 R31). Expected: strong terp-forward delivery, harshness mild-or-clean when the session ends before load accumulates, amber-to-dark-amber swab (hotter open darkens, but a single cycle drops the two-cycle darkening). Surprising: escalating chest harshness again on a clean short first-dab single cycle — that points at the curve or this jar on Rig 6, not load, and argues for dropping the peak rather than raising it.',
    next_waypoints=SOURTANGIE_HOLD_DESCENT_450,
    jar_index='',
)
