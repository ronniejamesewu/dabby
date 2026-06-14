"""Lemon Heads + Blueberry Haze — jar file (slug: lhbh)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

LHBH_425 = [
    Waypoint(time_s=0,  temp_f=380, note='Session open'),
    Waypoint(time_s=4,  temp_f=400, note='Steep early climb'),
    Waypoint(time_s=8,  temp_f=425, note='Endpoint — up 5°F from Run 1'),
    Waypoint(time_s=60, temp_f=425, note='Hold'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──

RUNS = [
    CompletedRun(
        strain='Lemon Heads + Blueberry Haze',
        run_date=date(2026, 6, 13),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 13, 23, 14, 36, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_5,
        duration_seconds=65,
        endpoint_note='<strong>Endpoint:</strong> 420°F — baseline first run',
        swab='dark golden',
        session_char='Flavorful, no specific notes on character. No harshness throughout. Dense-then-wispy within-draw pattern both cycles. Draws cut out fast with material remaining. Two cycles: 60s baseline + ~40s second pass.',
        intensity='High — body tension, lots of creative thoughts; effects built over ~30 minutes.',
        dab_notes='Cold nose: predominantly gassy, with some fruit underneath. Interesting nutty note as well. Not super loud but jar is fresh from fridge. Run: interesting, flavorful but no specific notes. Draws never got harsh throughout entire cycle. Vapor had same dense then wispy nature to it we\'ve seen before. After cycle ended ran it again (second cycle, ~40s) and continued getting the dense then quickly wispy pattern. Swab dark golden, lots of reclaim. Draws cutting out fast — good hit then quickly nothing. It got heavier for sure, I\'d put it in high. Some body tension, lots of creative thoughts.',
        analysis='The defining observation on Run 1 is the dense-then-wispy within-draw pattern appearing on Rig 5 — the same pattern documented on Rig 4 (single pearl) on FW106 R16, where the hypothesis was single-pearl thermal loss during draws. That pattern was expected to be reduced on Rig 5\'s dual pearls; LHBH Run 1 shows it regardless. Either the dual-pearl thermal advantage is material-dependent — this material makes heavier demands on pearl heat maintenance than FW106 or BB36 #2 — or the pearl-count hypothesis was overclaiming. One run, can\'t distinguish. Dark golden swab and heavy reclaim are consistent with incomplete vaporization. No harshness across both cycles puts 420°F comfortably within range. Intensity landed high despite the inefficiency. Flavor was present but no specific character noted — the citrus/gas/haze profile 710 describes didn\'t come through distinctly on Run 1.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Lemon Heads + Blueberry Haze',
    profile_anchor='#lhbh-profile',
    next_text='Try 425°F endpoint on Run 2 — same baseline ramp, 5°F up from Run 1',
    accent=None,
    slug='lhbh',
    info=[
        ('Strains', 'Lemon Heads (Lemon G × Face Off OG BX) + Blueberry Haze (Blueberry × Haze)'),
        ('Format', 'Close Friends Persy Thumbprint — two strains: outer ring cold cure badder (Lemon Heads), center jam (Blueberry Haze). 90μ persy-tier. Load position not reliably distinguishable.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Lemon Heads brings one of our favorite Lemon G profiles with a hint of gas. Blueberry Haze starts with a forward blueberry zing, then lets the haze linger. Bright citrus up front, haze on the backend.'),
        ('Nose', 'Predominantly gassy, with some fruit underneath. Interesting nutty note. Not loud on fresh jar — consistent with cold-cure-in-fridge pattern; may open up over time.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred dominant from Lemon Heads (Lemon G × Face Off OG BX) — Lemon G is known for strong citrus/lemon character; myrcene and terpinolene inferred from Blueberry Haze (Blueberry × Haze). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='The within-draw dropoff and heavy reclaim are the threads to watch. Try 425°F on Run 2 — same baseline ramp, 5°F endpoint bump. More thermal headroom may sustain pearl temperature longer through each draw, extending the dense vapor window. Cross-strain pattern puts harshness risk at ≥430°F; 420°F was clean, so there\'s room to probe. Watch whether the within-draw dropoff extends or stays identical — that\'s the signal on whether endpoint temperature is the relevant variable for this pattern, or whether something else is driving it.',
    next_waypoints=LHBH_425,
    jar_index='',
)
