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
]

# ── Status ──
STATUS = StrainStatus(
    name='LunarZ',
    profile_anchor='#lunarz-profile',
    next_text='Run 4: genuinely first dab of the day, modest load, same 430°F bounded-hold descent — the clean test Runs 2 and 3 both failed to deliver',
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
    next_ai_analysis='Three runs, three chest instances — all non-first dabs at normal-or-larger loads, so the curve/strain-on-Rig-6 read stays confounded by session order and load. Run 4 earns its keep only as a real first dab of the day on a modest load; anything else is a fourth confounded point. Keep water as technique, not a withheld variable — but note whether it fully clears (like R2) or only reduces (like R3). If chest harshness shows on a genuinely clean first-dab modest run, the bounded 430°F hold itself becomes the suspect and the next move is dropping the hold to 420°F or capping to a single cycle. Expected: chest lighter or absent on a real first-dab modest load. Surprising: chest again at ~30s — that puts the curve, not load/order, on the hook.',
    next_waypoints=LUNARZ_HOLD10_DESCENT_430,
    jar_index='',
)
