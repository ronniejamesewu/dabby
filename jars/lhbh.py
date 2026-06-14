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
    CompletedRun(
        strain='Lemon Heads + Blueberry Haze',
        run_date=date(2026, 6, 13),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 14, 0, 57, 0, tzinfo=timezone.utc),
        waypoints=LHBH_425,
        equipment=RIG_5,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 425°F — up 5°F from Run 1',
        swab='golden',
        session_char='Lemon on first draw. Solid vapor through the whole cycle — no within-draw dropoff. Harshness on third draw with vapor still flowing and material remaining. Single cycle.',
        intensity='High',
        dab_notes='That was great. Got a hint of lemon in the first draw. Got some harshness in third draw. I was getting solid vapor through the whole cycle. I think there\'s more in there. Swabs are golden, roughly same amount of reclaim which is weird. Overall it was much improved. Intensity is pretty big. High. [Q: draw 3 harshness — vapor hadn\'t thinned.] Couldn\'t do a second pass — swabbing eliminated the ability to do it. But the lighter color maybe points to I was right that there was more to vape.',
        analysis='Run 2 answers the main Run 1 question: the within-draw dense-to-wispy dropoff was endpoint-sensitive. Solid vapor through the whole cycle at 425°F vs. the pronounced drop at 420°F across both of Run 1\'s cycles. Ramp was identical both runs (8s), so the 5°F endpoint bump is the more likely lever. Cross-strain context: FW106 Run 16 (June 12, Rig 4) showed the same within-draw thick-then-wispy pattern — hypothesis there was single-pearl heat loss during draws. LHBH Run 1 complicated that by showing the same pattern on Rig 5\'s dual pearls. Run 2 at 425°F resolving it on Rig 5 points at endpoint temperature, not pearl count, as the driver. BB36 #2 Run 6 and OC Run 14 showed the same wispy-to-solid shift when endpoint went up, but those changed ramp and endpoint together. LHBH is the cleanest isolation yet: same 8s ramp, only endpoint moved. Flavor broke through for the first time: lemon on draw 1 — Run 1 had nothing specific. Lighter golden swab at a higher endpoint is consistent with better vaporization efficiency. Harshness on draw 3 with vapor still flowing and material present is a clean temperature signal — not depletion. 420°F was clean across two cycles in Run 1; 425°F brought harshness on draw 3. The boundary sits in that 5°F band.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Lemon Heads + Blueberry Haze',
    profile_anchor='#lhbh-profile',
    next_text='Run 3: try 425°F with a 2-draw limit — test whether draw count is driving the harshness',
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
    next_ai_analysis='The draw 3 harshness is the open question. Two ways to probe it: (1) 2-draw limit at 425°F — keeps the vapor improvement, tests whether draw count is the driver; if draw 2 stays clean, 425°F is workable with discipline. (2) Drop to 422–423°F — incremental probe between the clean floor and the harshness point, same ramp. Option 1 is the sharper isolation — holds endpoint constant, changes only exposure. Try that first.',
    next_waypoints=LHBH_425,
    jar_index='',
)
