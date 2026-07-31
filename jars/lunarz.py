"""LunarZ — jar file (slug: lunarz)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
LUNARZ_HOLD10_DESCENT_GENTLE = [
    Waypoint(time_s=0,  temp_f=440, note='Session open — hot open'),
    Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F'),
    Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

LUNARZ_HOLD10_DESCENT_430 = [
    Waypoint(time_s=0,  temp_f=430, note='Session open — hold at 430°F'),
    Waypoint(time_s=10, temp_f=430, note='Hold at peak — one draw at 430°F'),
    Waypoint(time_s=35, temp_f=415, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

LUNARZ_HOLD15_DESCENT_430 = [
    Waypoint(time_s=0,  temp_f=430, note='Session open — hold at 430°F'),
    Waypoint(time_s=15, temp_f=430, note='Hold at peak — extended 15s hold'),
    Waypoint(time_s=37, temp_f=415, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

# "Orange" preset — the smoothed 440°F bounded hold borrowed from Lemon Heads +
# Blueberry Haze; waypoints duplicated locally per the jar-isolation invariant.
LUNARZ_HOLD15_DESCENT_440_SMOOTH = [
    Waypoint(time_s=0,  temp_f=440, note='Session open — hot open'),
    Waypoint(time_s=15, temp_f=440, note='Hold at peak — extended 15s hold'),
    Waypoint(time_s=38, temp_f=420, note='Descent midpoint — sits on the line, no slope change'),
    Waypoint(time_s=60, temp_f=400, note='Floor — single constant ~0.9°F/s descent throughout'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 10),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 7, 11, 5, 11, 1, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD10_DESCENT_GENTLE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 440°F, then gentle descent; jar opener, baseline skipped',
        swab='dark golden',
        session_char='Dark golden swab, normal reclaim; slightly-larger-than-normal load, 3rd dab of the day, bounded 440°F hold into a gentle descent to 400°F. Medium-high intensity, super flavorful through cycle 1 and the first draw of cycle 2 with faint citrus; chest harshness entered on the second cycle after a dense draw and a short wispy one, lingering past session end. Stopped after the wispy draw.',
        intensity='medium-high',
        dab_notes='[Curve choice:] I\'m doing the 440 10 second hold descent curve instead. [Load:] I loaded slightly larger than normal but thank you for the warning. [Cycle 1:] Whoa this guy wants maybe less heat. And a second cycle. I\'m gonna stay on this curve but leave a note on the jar and to try a lower temp hold, maybe 430. I\'ll report back after second cycle. [Report:] Some harshness in chest after one big dense hit and one short wispy hit. Terminated after the second one. Swabs are dark golden, normal amount of reclaim. Intensity is medium high. It was super flavorful throughout first cycle and first rip of second cycle. Some citrus but faint. [Did it linger:] it lingered.',
        analysis='First read on LunarZ — bounded 440°F hold into the gentle descent to 400°F, slightly-larger-than-normal load, 3rd dab of the day. Delivered rather than cooked: medium-high, super flavorful through cycle 1 and the first draw of cycle 2, dark golden swab with normal reclaim — a fifth deliver-side run on this curve alongside dbrb R1, Sour Tangie R1, and bp4rw13 R12 (all Rig 6; directional, not a pattern). Chest harshness on the second cycle\'s dense-then-wispy draws, lingering past session end, is consistent with the chest-located/persisting thread on hot-open descents (papzp22 R7, bp4rw13 R8; Low confidence, muddied by countering runs) — the wispy draw points at cycle-2 depletion at onset. Faint citrus fits the inferred limonene but rides on one run and a weak palate; with no prior LunarZ run, the dark golden swab is a within-strain baseline, not yet a floor signal, and the user\'s "wants less heat" read is captured at single-data-point weight.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 11),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 7, 12, 4, 6, 36, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD10_DESCENT_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 430°F, down 10°F from Run 1\'s hold',
        swab='dark golden',
        session_char='Dark golden swab, normal reclaim; large load, 3rd dab of the day, 10s hold at 430°F into the gentle descent to 400°F — down 10°F from Run 1. Two cycles: dense, tasty vapor throughout cycle 1 with mild-to-medium heartburn-like chest harshness; water between cycles resolved it, nothing lingering post-session. Cycle 2 excellent on the remaining material — one big draw and half another before going wispy with a touch of toast. High intensity.',
        intensity='high',
        dab_notes='[Pre-dab:] This curve is teal in the switch app. [Cycle 1:] First cycle complete. I must have loaded large because the dense and tasty vapor never stopped. There\'s mild to medium harshness in chest. Feels like heartburn. I\'m gonna run a second cycle just to see. [Cycle 2:] Whoa fuck yeah that was really good. Second cycle being that good is strange. I got 1 big hit and half a second hit before it got wispy and a tiny bit toasty. [Report:] Swabs were dark golden, normal amount. Intensity is pretty high right now, kinda like I did one and a half dabs. [Water / did it linger:] Water between cycles and I don\'t feel it now.',
        analysis='First data point on the "wants less heat" read: hold dropped 440°F→430°F and chest harshness appeared anyway — earlier than Run 1 (cycle 1 vs. cycle 2), mild-to-medium, heartburn-like. Not the clean test the plan called for: the load ran large (user: "I must have loaded large because the dense and tasty vapor never stopped") and it was again a 3rd dab — order and rig matched Run 1, so load is the muddying variable. The persistence half split from Run 1: water between cycles, harshness resolved, nothing felt minutes out — where Run 1 (no water recorded) lingered. Consistent with the water-reset pattern (five prior instances, two strains, all Rig 6 — LunarZ makes a third) and it leaves the chest-and-lingers conjunction a one-run event. Cycle 2 peaked on fresh material from the big load — one big draw and half another before wispy with a touch of toast; fast depletion plus thin-residue scorch fits (Hive #1 R10 framing). High intensity tracks the load. Swab dark golden two-for-two across a 440°F and 430°F hold — directional for strain character, not a heat flag; second-cycle darkening confound both times.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 12),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 12, 7, 13, 23, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD10_DESCENT_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 430°F, same curve as Run 2',
        swab='dark golden',
        session_char='Dark golden swab, normal reclaim; normal load, fourth consecutive dab of a continuous night — logged as the calendar day\'s first, but session order is fully loaded. 10s hold at 430°F into the gentle descent to 400°F, same curve as Run 2. Two cycles, two draws into the second. Mild-to-medium chest harshness entering ~30s into cycle 1; a water sip reduced but did not eliminate it. Strong intensity, delivered rather than cooked.',
        intensity='strong',
        dab_notes='[Report:] Wow, so good. Two cycles, two draws in second cycle. [Session order:] It WASNT the clean test run. It\'s the fourth dab of the day. [Swab / chest / load / intensity:] Swab was dark golden, normal amount. Yes chest harshness mild to medium starting around 30 seconds on first cycle. Load was normal, not modest. Hit pretty hard. Pretty pretty pretty hard. [Water / did it linger:] I did sip some water and it did reduce but did not eliminate.',
        analysis='Not the clean test it was meant to be: fourth straight dab of a continuous night (logged as the calendar day\'s first) on a normal — not modest — load, so session order and tolerance stay as loaded as Runs 1–2. Chest harshness returned, mild-to-medium, ~30s into cycle 1 — three straight LunarZ runs with chest-located harshness on the bounded-hold descent (440°F R1, 430°F R2/R3), consistent with the Rig 6 chest-location thread but confounded by order and load every time. Dropping to 430°F hasn\'t cleared it over two runs, weakening the Run 1 "wants less heat" read; load down from R2\'s large to normal didn\'t remove it either (both onset cycle 1). Persistence split three ways: R1 lingered (no water), R2 cleared (water), R3 reduced but didn\'t eliminate (water) — the log\'s first partial water response; heavier 4th-dab exposure is one candidate, single-run weight. Strong intensity at normal load, dark golden swab with normal reclaim — delivered, not cooked; dark golden three-for-three is a within-strain baseline and second-cycle-darkening confound, not a floor signal.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 19),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 19, 22, 30, 0, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD15_DESCENT_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 15s hold at 430°F ("purple" preset), then gentle descent; extended from Runs 2–3\'s 10s teal hold, curve borrowed from an OC run',
        swab='dark golden',
        session_char='Dark golden swab with very minimal reclaim; large load, 2nd dab of the day, three cycles on the 15s-hold 430°F "purple" descent (a longer hold than Runs 2–3\'s 10s teal). Medium-high intensity. Heavy terpene-load coughing — enough that the cycle timer became unusable. No chest/heartburn harshness — the first LunarZ run without it; instead throat-located harshness, "super dry," that a water sip reset.',
        intensity='medium-high',
        dab_notes='I used the 430 extended hold curve and a large load. it was really good. [Swab:] swabs were very minimal amount, and dark golden. [Preset:] the curve is now purple on presets. if you had a different curve for purple this supersedes that. [Intensity / cycles:] it hit medium high. 3 cycles, i coughed so much i couldnt keep up with the cycle timer. [Harshness:] heartburn wasnt an issue, but it did get kind of harsh in my throat, it felt super dry. a sip of water helped.',
        analysis='Run 4 ran the 430 extended-hold descent — a 15-second hold at 430°F before the drop to 400°F, longer than Runs 2–3\'s 10-second teal hold — on a preset now colored purple, the curve borrowed from an OC run. Heavy session and a stack of deviations from the owed clean test: 2nd dab of the day, large load, three cycles (coughing heavy enough that the cycle timer was unusable), so like Runs 2–3 it isolates nothing — a fourth confounded point, as flagged. The headline is what didn\'t happen: no chest/heartburn harshness, the first LunarZ run of four without it (R1 lingered, R2 cleared with water, R3 partially cleared). Instead the harshness was throat-located and "super dry" — the mucosal/airway signal tracked separately from the chest facet — and a water sip helped, another Rig 6 water-reset instance. Read carefully, though: the chest\'s absence is confounded — the curve changed (longer hold), and a wall of terpene-load coughing can mask a harshness read (LHBH R8) — so it\'s mild, not clean, counter-evidence to load/cumulative exposure driving LunarZ\'s chest, since a large-load three-cycle session is exactly where that hypothesis predicts chest and it didn\'t come. The heavy coughing is the terpene-load cough mechanism, distinct from harshness (the Sour Tangie R7 distinction). Swab dark golden, very minimal reclaim — LunarZ four-for-four dark golden, a within-strain baseline, not a floor signal; very minimal reclaim despite a large load and three cycles reads as strong delivery, material consumed rather than cooked. Medium-high intensity, matching R1. Rig 6 throughout.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 19),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 7, 20, 1, 58, 31, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD15_DESCENT_430,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 430°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 15s hold at 430°F ("purple" preset), same curve as Run 4',
        swab='golden',
        session_char='Golden swab with minimal reclaim; normal load, 3rd dab of the day, two and a half cycles on the purple 15s-hold 430°F descent — stayed tasty throughout, stopped a draw into the third as it thinned and satiety hit. Hit very hard (strong). Bottom-of-throat harshness plus some heartburn — the chest facet back after Run 4 had none; no persistence reported.',
        intensity='strong',
        dab_notes='purple curve, normal load. [Report:] Golden, minimal reclaim on the swabs, two and a half cycles it stayed tasty all the way, I stopped after first draw of third I had enough and it was starting to thin a bit. Hit very hard! Harshness in bottom of throat and some heartburn.',
        analysis='Run 5 — same purple 15s-hold 430°F descent as Run 4, 3rd dab of the day, normal load, two and a half cycles (stopped a draw into the third as it thinned and satiety hit). Stayed tasty the whole way — good retention across 2.5 cycles on a normal load. Hit very hard, strong — up from R4\'s medium-high despite the lighter load, so the day\'s cumulative dosing is the likelier driver than this dab alone. The read that matters: chest/heartburn came back (bottom-of-throat harshness plus some heartburn) where R4 — earlier today, larger load, more cycles — had none. Two purple runs back-to-back, same curve and rig, and the chest tracked the later 3rd-dab slot, not the bigger load: within-day cumulative exposure fits the chest better than per-dab load here, consistent with the standing counter-reading that chest co-varies with cumulative session exposure rather than the hot open itself (and with Sour Tangie\'s within-day throat escalation). Confounds remain — R4\'s wall of coughing may have masked its chest, and neither run is the clean first-dab test — so directional, not settled. No persistence reported, so chest-location in-session, not the chest-and-lingers conjunction. Swab golden, minimal reclaim — the first LunarZ read called lighter than dark golden, but golden-vs-dark-golden sits inside this project\'s uncalibrated color-call noise (and R5 ran fewer material-cycles than R4), so it\'s noted, not a floor signal. Rig 6 throughout.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 29),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 29, 21, 44, 51, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD15_DESCENT_440_SMOOTH,
        equipment=RIG_7,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 15s hold at 440°F into a single constant ~0.9°F/s descent ("orange" preset), borrowed from Lemon Heads + Blueberry Haze; first 440°F open since Run 1',
        swab='dark golden',
        session_char='Dark golden swab with plentiful reclaim; larger-than-normal load, first dab of the day, two cycles on the smoothed 440°F bounded hold ("orange") — the jar\'s first run off Rig 6 and its first 440°F open since Run 1. Cycle 1 super tasty with heavy terpene coughing and a tiny bit of harshness at the base of the throat, no chest; a water sip lessened it but did not clear it. Heartburn arrived during cycle 2 alongside the throat harshness and cleared after a few drinks of water. Very high intensity. Second cycle stopped with 15s left on the curve — wispy vapor and satiety, material remaining.',
        intensity='very high',
        dab_notes='[Pre-dab:] Let\'s do the lunarz experiment on rig 7. Except let\'s do it on the orange curve. [Cycle 1:] First cycle, super tasty, tiny bit of harshness at base of throat. Hasn\'t gone to chest. Lots of terp coughing. [Report:] Water lessened but didn\'t clear. After second cycle it\'s both heartburn and base of throat now. Very high intensity. Swabs dark golden. Second cycle terminated with 15 seconds left, it was wispy and I had enough. [Load / reclaim / heartburn timing and persistence:] Load was larger than normal. Reclaim was plentiful. During cycle two, gone after a few drinks of water.',
        analysis='Curve, top and load all moved off the plan, so nothing isolates. But this was the jar\'s first genuine first dab, and chest/heartburn still came — Runs 1–5 were all 2nd-dab-or-later, and the R4/R5 pair had put chest on the later dab slot. Day accumulation isn\'t it. Onset was cycle 2 after a throat-only cycle 1, same as Run 1 (the only other 440°F open), so within-session exposure survives. The water result is the sharper one and splits inside the run. All three prior non-Rig-6 instances failed the clean reset but were all chest-located, so top and location had never varied independently; a throat-only instance off Rig 6 was the cell that separates them. This is it — sip lessened, didn\'t clear. Then the cycle-2 heartburn cleared after a few drinks. One datum toward the top, one against. Third RBR run, chest on all three (papzp22 R10, BB36 #2 R7, here) — occurrence, not mechanism; "super tasty" leaves that top\'s taste read unsettled. Very high intensity, the jar\'s strongest and first on a first dab, with load and the 440°F open both unseparable. Heavy coughing again, as Run 4. Dark golden five of six — within-strain baseline; plentiful reclaim tracks the larger two-cycle load. Ended wispy on satiety with material left, not on harshness.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 29),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 30, 1, 43, 29, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD15_DESCENT_440_SMOOTH,
        equipment=RIG_7,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 15s hold at 440°F into a single constant ~0.9°F/s descent ("orange" preset), same curve as Run 6',
        swab='beige to light gold',
        session_char='Beige-to-light-gold swab; modest load, 2nd dab of the day, a single cycle on the smoothed 440°F bounded hold ("orange") — same curve and same top as Run 6. No harshness anywhere, throat or chest: the jar\'s first fully clean run in seven. Very strong intensity. Stopped with under 10 seconds left on the curve as the vapor thinned.',
        intensity='very strong',
        dab_notes='[Pre-dab:] Let\'s tee up the next lunarz dab. [Report:] Very nice, very strong. I kind of wonder how terpy it would be without the rbr. Swabs were beige to light gold. [Curve / cycles / load / harshness:] Orange, one cycle. Load was modest. No harshness. [Stop point:] stopped with less than 10 seconds left.',
        analysis='The jar\'s first clean run in seven — no harshness, throat or chest, on a modest single cycle. Same strain, curve and top as Run 6, which put throat in cycle 1 and heartburn in cycle 2; what moved down was load and cycle count, and this ran at the later dab slot (2nd, against R6\'s first). That is the closest matched pair LunarZ has, and it points at within-session exposure — the narrower reading Run 6 left standing when chest on a first dab killed day accumulation. Load and cycles moved together, so neither is isolated on its own. Very strong on the least material and fewest cycles the jar has run: Runs 5 and 6 hit strong and very high carrying a normal-to-larger load or a full day behind them, and this carried neither — one run, but intensity is not tracking load here. Fourth run on the recycler and the first without chest, also the first on a modest load, the run that top has owed since its debut; chest goes three of four there, broken by the exposure-light run, which is what the cumulative-exposure reading predicts rather than anything about the glass. User wondered whether it would be terpier without the recycler — nothing here tests that, and LunarZ has read tasty on all seven runs, five of them on the bubbler. Beige-to-light-gold swab, the jar\'s lightest, is what a single cycle produces. Stopped on thinning vapor with under 10 seconds left: satiety, not harshness.',
    ),
    CompletedRun(
        strain='LunarZ',
        run_date=date(2026, 7, 30),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 7, 31, 3, 23, 11, tzinfo=timezone.utc),
        waypoints=LUNARZ_HOLD15_DESCENT_440_SMOOTH,
        equipment=RIG_8,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 15s hold at 440°F into a single constant ~0.9°F/s descent ("orange" preset), same curve as Runs 6–7; the jar\'s first run on the Calibear Fab Recycler top',
        swab='golden',
        session_char='Golden swab, very minimal; normal load, 2nd dab of the day, a single cycle on the smoothed 440°F bounded hold ("orange") — same curve as Runs 6–7, on a third glass top. Load depleted with about 10 seconds left on the curve. No harshness anywhere. Mild-to-medium effect. Flavor nice but muted against the jar\'s stock-bubbler runs.',
        intensity='mild to medium',
        dab_notes='[Pre-dab:] Keeping rig 8, lets gooooooo [Report:] Sean\'s golden, very minimal. Load depleted before end of cycle, about 10 seconds left. Effect mild to medium. Flavor was nice but muted. No harshness [Muted against what:] The stock bubbler runs [Unprompted:] The two recycler tops are definitely smoother [Load / cycles:] Load was normal, one cycle',
        analysis='Flavor down against this jar\'s own bubbler runs — the log\'s third comparative read, and the first inside a jar that\'s run all three tops. It splits the two recyclers rather than grouping them: LunarZ read super tasty on the RBR against that same baseline, though nobody asked it to compare. Runs 7 and 8 are the log\'s tightest top-against-top pair — same jar, curve, dab slot and single cycle, load modest→normal, RBR→Calibear. Flavor and intensity both down on more material, but the intensity is day-stacking: R7 followed a very-high two-cycle dab, this followed a medium-high single. Four clean of five on the Calibear now, and the user reads both recyclers as smoother. Still exposure-confounded — every harshness instance on either top carried a bigger load or more cycles. Golden and minimal off one cycle is expected; ended on depletion with curve left, the descent shape again.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='LunarZ',
    profile_anchor='#lunarz-profile',
    next_text='Run 9: the orange 440°F curve back on the stock bubbler (Rig 6), normal load — closes the three-top set inside one jar.',
    accent=None,
    slug='lunarz',
    info=[
        ('Strain', 'LunarZ (Moonbow #112 × Planet Purple F2 #144 — bred by Archive, seed-hunted by 710 Labs; Moonbow: Zkittlez × Do-Si-Dos; Planet Purple: Sherbadough × Moonbow)'),
        ('Consistency', 'Live rosin badder (Persy tier)'),
        ('Producer', '710 Labs'),
        ('Nose', 'Faint gas — jar cold from dispensary freezer; some gas present but not loud. Weak secondary signal; expect it to open as it warms.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene and caryophyllene inferred dominant from the Zkittlez × Do-Si-Dos / Sherbadough stack (Zkittlez, Do-Si-Dos, Sunset Sherbert) — sweet candy-fruit ("Z") over a gas/OG underside; linalool plausible from the Do-Si-Dos/Sherbert side. Only the immediate Moonbow × Planet Purple cross is 710 Labs-anchored; the parent generations and below are corroborated across independent sources, not producer-confirmed. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='LunarZ is the only jar that can complete the set: five bubbler runs, two on the RBR, one on the Calibear. Run 9 puts the orange curve back on the stock bubbler at a normal load, dab slot wherever it falls — closing the three-top comparison and testing the smoothness-costs-flavor read from both ends. Expected: flavor louder than Run 8, harshness back if it goes past one cycle. Surprising: no better on the bubbler, which puts Run 8\'s muted read on the material or the night.',
    next_waypoints=LUNARZ_HOLD15_DESCENT_440_SMOOTH,
    jar_index='',
)
