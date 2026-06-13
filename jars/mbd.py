"""Maple Bacon Donut — jar file (slug: mbd)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
MBD_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
MBD_RUN2 = [
    Waypoint(time_s=0, temp_f=380, note='Session open — same curve as Run 1'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
MBD_RUN3 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=15, temp_f=385, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=55, temp_f=420, note='Approach endpoint — down 10°F from prior runs'),
    Waypoint(time_s=65, temp_f=420, note='Hold at 420°F for 10 seconds'),
]
MBD_RUN4 = [
    Waypoint(time_s=0, temp_f=380, note='Session open — same as Runs 1 and 2'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
MBD_NEXT = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=405, note='Steeper early ascent'),
    Waypoint(time_s=35, temp_f=440, note='Mid climb'),
    Waypoint(time_s=60, temp_f=460, note='Endpoint — up 30°F, faster ramp'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Maple Bacon Donut',
        run_date=date(2026, 5, 10),
        sessions_prior_today=0,
        utc_logged_at=None,
        waypoints=MBD_RUN1,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab='Darker golden — between light golden target and amber. Nothing tasted burnt. Flagged as something to watch on subsequent runs.',
        session_char='Tasty first half, second half faded to generic. Milder effect — likely tolerance after 5 sessions the prior day.',
        intensity='Mild — tolerance confound (5 sessions prior day)',
    ),
    CompletedRun(
        strain='Maple Bacon Donut',
        run_date=date(2026, 5, 10),
        sessions_prior_today=1,
        utc_logged_at=None,
        waypoints=MBD_RUN2,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F — same as Run 1',
        swab='Lighter than Run 1 — closer to the light golden target.',
        session_char='Distinct bacon character on the first half. Effects came on noticeably after this session.',
        intensity='Moderate',
        analysis='Swab trending cleaner on repeat. Flavor expressed distinctly on the first half. No harshness on either run. The Run 1 milder effect reads as a tolerance confound — effects landed clearly on Run 2.',
    ),
    CompletedRun(
        strain='Maple Bacon Donut',
        run_date=date(2026, 5, 11),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 5, 12, 5, 24, tzinfo=timezone.utc),
        waypoints=MBD_RUN3,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F, ramp from 375°F open',
        swab='Clean golden.',
        session_char='Little bit harsh in the last 5 seconds. No harshness earlier in the session.',
        intensity='Medium-hard',
    ),
    CompletedRun(
        strain='Maple Bacon Donut',
        run_date=date(2026, 5, 12),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 13, 2, 30, tzinfo=timezone.utc),
        waypoints=MBD_RUN4,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F — same as Runs 1 and 2',
        swab='Light golden.',
        session_char='Tail harshness again, consistent with prior 430°F runs. Interesting bitter note throughout — citrus rind character.',
        intensity='Big effect, seemingly short duration.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Maple Bacon Donut',
    profile_anchor='#mbd-profile',
    next_text='Try faster ramp to 460°F on Run 5',
    accent=None,
    slug='mbd',
    info=[
        ('Strain', 'Maple Bacon Donut'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Quasi Farms (Michigan)'),
        ('Micron', 'Not recorded'),
        ('Nose', 'Not yet recorded'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='Run 4 back to 430°F: light golden swab, tail harshness consistent with prior 430°F pattern, interesting bitter/citrus rind note throughout, big effect, seemingly short duration.',
    next_ai_analysis="Tail harshness at 430°F is consistent across runs. Run 5 moves in a different direction — faster ramp to 460°F — rather than continuing to work the lower end. That's an exploratory step; the session character at 460°F is unknown for MBD. The citrus rind note is worth watching on Run 5 to see whether it changes with the faster climb. The short duration observation from Run 4 is a single data point, unclear if it means anything. Swab has been clean throughout, so the harshness is coming from endpoint temperature, not material condition.",
    next_waypoints=MBD_NEXT,
    jar_index='',
)
