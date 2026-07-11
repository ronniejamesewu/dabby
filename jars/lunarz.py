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
]

# ── Status ──
STATUS = StrainStatus(
    name='LunarZ',
    profile_anchor='#lunarz-profile',
    next_text='Run 2: lower the hold to 430°F (same bounded-hold descent), first dab, modest load — test the "wants less heat" read on a cleaner setup',
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
    next_ai_analysis='Run 2: drop the hold from 440°F to 430°F, same bounded-hold-descent shape, first dab, modest load. Follows the user\'s Run 1 "wants less heat" read and backs off the 440°F open tied to the lingering chest harshness, while a first-dab modest load strips the 3rd-dab and larger-load confounds that muddy Run 1. One run in, so this is a first calibration step, not a confirmed direction. Note the two separate signals from Run 1 for the readback: whether chest harshness shows up *during* the session (in-session chest-location row), and separately whether anything lingers or appears *after* it ends (post-session discomfort row) — LunarZ R1 is one of only two runs in the log with the chest-and-lingers conjunction, so a clean Run 2 either replicates it or isolates it as one-off. Expected: still delivers strong with flavor, chest harshness lighter or gone at the cooler open. Surprising: same chest harshness at 430°F — that would point at curve shape or rig over the 440°F peak.',
    next_waypoints=LUNARZ_HOLD10_DESCENT_430,
    jar_index='',
)
