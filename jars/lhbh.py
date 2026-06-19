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
    CompletedRun(
        strain='Lemon Heads + Blueberry Haze',
        run_date=date(2026, 6, 18),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 18, 21, 44, 7, tzinfo=timezone.utc),
        waypoints=LHBH_425,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 425°F — first run on Rig 6',
        swab='dark golden',
        session_char='Dense vapor throughout until depletion at ~55s. Mild harshness entered at ~40s with vapor still thick. Sparse reclaim. Slight lemon candy note on cold nose and during run. Suspected smaller-than-normal load; low intensity.',
        intensity='Low — possibly still building at logging time.',
        dab_notes='Swabs were dark golden, sparse reclaim. Depletion of material based on vapor production drop was around 55 seconds. Very mild harshness showed up around the 40 second mark. Intensity is low right now, can\'t tell if it\'s building. I think maybe this load was less than normal. Also I think it was mostly lemon heads. I got a very slight lemon heads candy note on cold nose of jar and I tasted some of it in the run. So maybe for next time a larger load, and 425? 430? Vapor was very dense until depletion.',
        analysis='Defining observation is the vapor density sequence: dense throughout until depletion at ~55s, with mild harshness entering at ~40s while vapor was still thick. Harshness preceding depletion by 15s and co-occurring with dense vapor weakens the depletion framing — if material were running thin, vapor would be thinning too. This looks like a cumulative exposure or endpoint ceiling rather than an empty-insert signal. Cross-run context: Run 2 on Rig 5 also had harshness arrive with vapor flowing and material present — same pattern, different rig. The boundary is somewhere in the 40–50s range at 425°F on this strain across both rigs. Sparse reclaim with dark golden swab is consistent with the joystick vaporizing more completely; 60s duration is driving the swab color, matching the duration-swab pattern across all 60s FW106 runs on Rigs 4, 5, and 6. Lemon candy note on cold nose and during the run — two consecutive runs now with lemon character (Run 2: lemon on draw 1; Run 3: lemon candy in the run), directional confirmation that the outer-ring Lemon Heads character is there when that portion loads. Intensity low this run is load-size driven; Rig 6 delivery on this strain is otherwise confirmed — dense vapor throughout the session.',
    ),
    CompletedRun(
        strain='Lemon Heads + Blueberry Haze',
        run_date=date(2026, 6, 18),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 18, 23, 0, 0, tzinfo=timezone.utc),
        waypoints=LHBH_425,
        equipment=RIG_6,
        duration_seconds=35,
        endpoint_note='<strong>Endpoint:</strong> 425°F — larger load, stopped early (~35s estimated)',
        swab='golden with amber spots',
        session_char='Heavy vapor throughout. Harshness entered at ~30s; stopped early — exact stop time unknown, estimated ~35s. Larger than normal load.',
        intensity='Medium',
        dab_notes='Heavy vapor, a lot of harshness starting around 30 seconds. Swabs were golden with some amber spots. Medium intensity. Stopped early but didn\'t see the time. [Time: 5:00 PM MDT]',
        analysis='Key result: harshness arrived 10 seconds earlier on the larger load (~30s) than on the smaller load (~40s on Run 3) — same curve, same rig. Depletion predicts the opposite: more material means the load runs thin later, so harshness threshold should shift back. Earlier onset with more material cuts against that and aligns with vapor density or particle accumulation as the driver — bigger load, heavier vapor per draw, threshold crossed sooner. The two-run load-size comparison is one of the cleaner within-strain contrasts in the log; session-order confound (Run 3: first of day, Run 4: second) is real but unlikely to account for a 10-second directional shift. Golden swab with amber spots is a departure from Run 3\'s solid dark golden — amber spots may indicate patchy vaporization on a larger load, or load placement geometry. Medium intensity is load-consistent vs. Run 3\'s low. 425°F on Rig 6 has a ceiling around 30s on a loaded session; stopping early was the right call.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Lemon Heads + Blueberry Haze',
    profile_anchor='#lhbh-profile',
    next_text='Run 5: drop to 420°F on Rig 6, normal load — test whether the floor is clean',
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
    next_ai_analysis='Runs 3 and 4 together make the clearest load-size comparison in this jar: smaller load → harshness at ~40s; larger load → harshness at ~30s, same curve, same rig. Earlier onset on more material cuts against depletion and points at vapor density or particle accumulation. 425°F is producing harshness too early on a loaded session (~30s in a 60s window). Drop to 420°F on Rig 6 with a normal load — 420°F was clean on Rig 5 for this strain (Run 1, no harshness across two cycles) and may have headroom on the joystick. If harshness stays absent or late, 420°F is the operating point. If it enters early, the strain has a lower ceiling on Rig 6 than on Rig 5.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
