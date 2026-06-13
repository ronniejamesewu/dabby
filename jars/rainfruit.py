"""Rain Fruit — jar file (slug: rainfruit)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
RF_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
RF_RUN2 = [
    Waypoint(time_s=0, temp_f=375, note='Session open — 5°F below baseline, testing lower open'),
    Waypoint(time_s=15, temp_f=385, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
RF_RUN3 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=15, temp_f=385, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=55, temp_f=420, note='Approach endpoint — down 10°F'),
    Waypoint(time_s=65, temp_f=420, note='Hold at 420°F for 10 seconds'),
]
RF_RUN4_NEXT = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=15, temp_f=385, note='Early ascent'),
    Waypoint(time_s=40, temp_f=412, note='Mid ascent — up 2°F'),
    Waypoint(time_s=55, temp_f=422, note='Approach endpoint — up 2°F'),
    Waypoint(time_s=65, temp_f=423, note='Endpoint — up 3°F from Run 3'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Rain Fruit',
        run_date=date(2026, 5, 10),
        sessions_prior_today=2,
        utc_logged_at=None,
        waypoints=RF_RUN1,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F — baseline ramp',
        swab='Notably clean — lighter than target. No darkening.',
        session_char='Really clear fruit notes throughout. Strong effects — pressure up and behind the eyes. No harshness.',
        intensity='Strong',
        analysis='Clean first run. Distinct fruit character, strong effect. No floor signal, no harshness. Repeat the same curve on Run 2 to confirm.',
    ),
    CompletedRun(
        strain='Rain Fruit',
        run_date=date(2026, 5, 11),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 11, 22, 44, tzinfo=timezone.utc),
        waypoints=RF_RUN2,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F &nbsp;|&nbsp; Open 5°F below baseline — testing lower open',
        swab='Light golden — clean.',
        session_char='Tasty. Got a bit hot in the last 10 seconds.',
        intensity='Mild',
        analysis='Curve felt well-suited to the strain overall. Tail heat in the last 10 seconds is consistent with the cross-strain pattern at 430°F endpoints (Hive #1 Run 5, Fembot #3 Runs 1–2). Swab is clean so this is a session character signal, not a floor indicator. Effects milder than Run 1 — likely session-to-session variability rather than a curve signal.',
    ),
    CompletedRun(
        strain='Rain Fruit',
        run_date=date(2026, 5, 11),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 5, 12, 0, 30, tzinfo=timezone.utc),
        waypoints=RF_RUN3,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F from prior runs',
        swab='Clean golden.',
        session_char='Notably less harshness. Slow build to intensity — not hard hitting.',
        intensity='Mild-moderate',
        analysis='420°F endpoint did not produce the tail harshness that appeared at 430°F on Run 2 — consistent with the cross-strain pattern. Clean swab means no floor signal. The slower, gentler build suggests some intensity lives in the higher-temperature band. The path forward is to walk the endpoint back up incrementally to find where harshness re-enters.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Rain Fruit',
    profile_anchor='#rainfruit-profile',
    next_text='Walk endpoint up incrementally — try 423°F on Run 4',
    accent=None,
    slug='rainfruit',
    info=[
        ('Strain', 'Rain Fruit'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Quasi Farms (Michigan)'),
        ('Micron', 'Not recorded'),
        ('Nose', 'Not yet recorded'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='420 hold worked — notably less harshness, clean golden swabs. Not hard hitting but slow build to intensity. Want to slowly walk up the curve.',
    next_ai_analysis='The 420°F endpoint is consistent with the hypothesis: dropping 10°F from the 430°F runs eliminated tail harshness without producing a floor signal. The trade-off is real — effects were milder and slower-building, suggesting the higher-temperature band contributes to intensity. Next step is to probe incrementally upward: try 423°F endpoint (same ramp shape, +3°F) to begin finding where harshness re-enters. Small steps keep the signal clean — each run is one data point on the harshness-intensity curve.',
    next_waypoints=RF_RUN4_NEXT,
    jar_index='',
)
