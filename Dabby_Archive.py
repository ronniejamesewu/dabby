"""Archived run data — jars closed and historically frozen.
Imports the data layer for all dataclasses, equipment constants, and shared waypoints.
Do not edit CompletedRun entries here — these are the permanent historical record.
"""
from Dabby_Data import *

# ── WW Z — INFO + WAYPOINTS ──────────────────────────────────────────────────

WWZ_INFO = [
    ("Strain",      "WW Z (White Widow × Zkittlez lineage — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Piney with sweet undertone (weak secondary signal only)"),
]

WWZ_RUN1 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=378, note="Extended flat — low-boiling terpene zone (~311°F pinene region)"),
    Waypoint(time_s=40, temp_f=395, note="Mid ascent — mid-range terpene zone (~334°F myrcene region)"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint — upper terpene zone + THC completion"),
]
WWZ_RUN2 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=400, note="Faster mid climb"),
    Waypoint(time_s=30, temp_f=420, note="Endpoint — fast ramp, down 20°F from Run 1"),
    Waypoint(time_s=60, temp_f=420, note="Hold"),
]
WWZ_RUN3 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=410, note="Steeper mid climb"),
    Waypoint(time_s=30, temp_f=430, note="Endpoint — fast ramp, up 10°F from Run 2"),
    Waypoint(time_s=50, temp_f=430, note="Hold"),
]
WWZ_RUN7 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=420, note="Endpoint — 420°F in 20s, 2°F/sec"),
    Waypoint(time_s=50, temp_f=420, note="Hold"),
]
WWZ_RUN9 = WWZ_RUN7

# ── MB9ZST — INFO + WAYPOINTS ─────────────────────────────────────────────────

MB9ZST_INFO = [
    ("Strain",      "Mango Banana #9 + Z + Sour Tangie"),
    ("Product",     "Persy Neapolitan — three-strain cold-cure blend, 2g jar"),
    ("Consistency", "Cold cure"),
    ("Producer",    "710 Labs"),
    ("Extraction",  "90μ full-melt bubble hash, hand-pressed"),
    ("Blend",       "Mango Banana #9 (SB 36 × Forbidden Banana) · Z (Zkittlez lineage) · Sour Tangie (Sour Diesel × Tangie)"),
    ("Character",   "Sativa-leaning hybrid — uplifting from Sour Tangie, tropical melon from Mango Banana, sweet/gas balance from Z. Neapolitan format means three separate layers in one jar; actual session character driven by which portion you pull from."),
    ("Nose",        "Not yet recorded"),
]

MB9ZST_BASELINE = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MB9ZST_RUN1 = MB9ZST_BASELINE
MB9ZST_RUN2 = MB9ZST_BASELINE
MB9ZST_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=420, note="Endpoint"),
    Waypoint(time_s=65, temp_f=420, note="Hold at 420°F"),
]
MB9ZST_RUN4 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=415, note="Endpoint — down 5°F from Run 3"),
    Waypoint(time_s=65, temp_f=415, note="Hold at 415°F"),
]
MB9ZST_RUN5 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=415, note="Endpoint — same as Run 4"),
    Waypoint(time_s=65, temp_f=415, note="Hold at 415°F"),
]
MB9ZST_RUN6 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=400, note="Faster mid climb"),
    Waypoint(time_s=30, temp_f=420, note="Endpoint — faster ramp, up 5°F from proposed"),
    Waypoint(time_s=60, temp_f=420, note="Hold — extended 10s via push button"),
]

# ── ARCHIVED RUNS ─────────────────────────────────────────────────────────────
# Chronologically ordered within each strain. Run numbers assigned positionally
# by runs_for() in the generator — order here is load-bearing.

ARCHIVED_RUNS = [
    # ── WW Z (Runs 1–9) ──────────────────────────────────────────────────────
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 2), sessions_prior_today=0, utc_logged_at=None, equipment=RIG_1, waypoints=WWZ_RUN1,
        duration_seconds=65, endpoint_note='<strong>Rate:</strong> ~0.6°F/sec',
        swab='Light golden/amber. Clean. No dark coloration.',
        extra_rows=[
            ("Vapor:",   "Spectacular. Full session expressed well across the arc."),
            ("Verdict:", "Clean on first run. Baseline curve well-matched to this material."),
        ],
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 18), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 19, 2, 52, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN2,
        duration_seconds=60, endpoint_note='<strong>Endpoint:</strong> 420°F — fast ramp; down 20°F from Run 1',
        swab='Wheat — very clean.',
        dab_notes="Sneaky — felt light at first, enough that I finished the last 20 seconds of Sarah's dab when she didn't want it. But 5 minutes after that I was stoned as a bat. Having a hard time sitting up. Harsh in the throat in mine but interestingly not in finishing Sarah's. Maybe the harshness comes from the terpene mass up front? And not the heat? No real flavors coming through, Sarah says she hates the taste and is almost gagging. I don't find it tasty but I don't mind the taste.",
        analysis="Run 1 (spinner, 6mm pearl, slow ramp to 440°F) and Run 2 (Gemlock, no pearl, fast ramp to 420°F) differ on equipment, curve shape, and endpoint — no isolation is possible between them. Swab came back wheat-clean, lighter than Run 1's golden/amber, consistent with the Gemlock running lighter swabs across other strains. Strong delayed onset despite the lower endpoint — stoned as a bat ~5 minutes post-dab. Harshness was present in the full session; absent when finishing Sarah's last 20 seconds (tail end of her run). User hypothesis: harshness is front-loaded rather than endpoint-driven. The observation is real; the mechanism is speculative — a lighter partial load producing less irritation regardless of session position is equally consistent. Not a working position until something tests it. No distinct flavor; Sarah found the taste actively unpleasant.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 19), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 20, 1, 20, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN3,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 430°F — fast ramp (30s), 20s hold; up 10°F from Run 2',
        swab="One light golden with a small amber spot; the other barely absorbed anything — cleanest swab so far.",
        session_char="Harshness at 414°F on the display during the ramp, lingered through the hold at low intensity, never spiked — a couple of coughs. Creative, sharp, stoned.",
        intensity="Good — creative, sharp, and stoned. Not as hard as Run 2; less material consumed.",
        dab_notes="Two swabs: one light golden with a small spot of amber, the other barely absorbed anything — cleanest run I've ever seen swab-wise. Harshness hit at exactly 414°F on the app display. Lingered and increased over the dab but never increased fast — mild, just a cough or two. Good intensity, not as hard as last night but I didn't take the last third of a second hit. I feel creative and sharp, and also stoned. This feels a little bit like trying to run a distillation column in my throat and lungs.",
        analysis="Cleanest swab in the log for this strain — one light golden with a small amber spot, the other barely absorbed anything. No floor signal at 430°F. Harshness appeared at 414°F on the display during the ramp (somewhere in the 15s–30s window), lingered at low intensity through the hold, never spiked — a couple of coughs, not acute. This is a different profile from typical tail harshness: it started mid-climb rather than at the endpoint. User raised a methodological point this session — reported 'tail harshness' may be a threshold-crossing description rather than an endpoint-specific signal; harshness builds continuously and registers when it becomes noteworthy, not when the curve hits a particular temperature. Consistent with that framing, the harshness here was mild throughout and never became the story. Effect was good: creative, sharp, stoned — consistent with Z lineage. Less hard-hitting than Run 2 but user also took less material.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 19), sessions_prior_today=1, utc_logged_at=datetime(2026, 5, 20, 4, 48, 24, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN3,
        duration_seconds=60, endpoint_note='<strong>Endpoint:</strong> 430°F — repeated from Run 3',
        swab="Darker than Run 3 — maybe amber.",
        session_char="Harshness around 420°F on display (mid-ramp). Creative, sharp, stoned via body sensation.",
        intensity="Similar to Run 3",
        dab_notes="Harshness didn't show up until around 420 on display. I added 10 seconds with the button. But only needed maybe 5, it was cashed. Swabs were darker than last time, maybe to amber. In theory nothing different this time but really different results. Feels similar to last time, creative and sharp but definitely also stoned via body sensation.",
        analysis="Run 4 repeats the same curve as Run 3 (380→410@15s→430@30s, hold to 50s) with one procedural difference: push-button extension to 60s, with material cashed around 55s. Load was in the ballpark with Run 3 — same jar section, possibly slightly less — which rules out load size as an explanation for the swab shift. The amber swab points at the extension: ~5s of 430°F hold after the load was spent, not a signal about the curve itself. Harshness appeared at ~420°F on the display, up from 414°F in Run 3. Both are mid-ramp (15–30s window), neither at the endpoint hold. The 6°F shift is within run-to-run variability, consistent with the threshold-crossing framing: harshness builds through the ramp and is noticed when it crosses a perceivable level, not pinned to a specific temperature. Effect was consistent — creative, sharp, stoned with body sensation.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 20), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 21, 1, 40, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN3,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 430°F — same curve as Runs 3–4, no push-button extension',
        swab="Clean light golden.",
        session_char="A little coughing, no harshness.",
        intensity="Mild — smaller load (user's read).",
        dab_notes="It was great, a little coughing but no harshness. Clean light golden swabs. A little mild on effect, my guess is smaller load.",
        analysis="Same curve as Runs 3–4 (380→410@15s→430@30s, hold to 50s), no push-button extension. Swab clean light golden — consistent with the Gemlock pattern. No harshness this run; Runs 3 and 4 both had harshness appearing mid-ramp at 414–420°F on the display. The difference may be load size — smaller load, less vapor density, less irritation regardless of temperature — but user couldn't confirm load was meaningfully different, so this is a confound, not a finding. Coughing without harshness is worth the distinction: vapor volume can produce coughing without the hot/irritating quality of harshness. Effect mild, consistent with user's smaller-load read.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 20), sessions_prior_today=1, utc_logged_at=datetime(2026, 5, 21, 3, 2, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN3,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 430°F — same curve as Runs 3-5, deliberate full load',
        swab="Light golden — same as Run 5.",
        session_char="Tail harshness in the last part.",
        intensity="Strong — hit really hard.",
        dab_notes="Swabs looked the same as last time, light golden. This one was more normal load. Harshness in the last part, and hit really hard. So load size really influenced both.",
        analysis="Load-size hypothesis from Run 5 tested. Run 5 (smaller load, no harshness, mild effect) vs. Run 6 (fuller load, tail harshness, hard hit) on the same curve and equipment — the cleanest within-strain comparison in the log. Both harshness and effect strength scaled up with load. Swab stayed light golden, consistent with every Gemlock run on this strain. The curve produces harshness under a full load; the question is whether that's load-density-at-430°F specifically, or just load-density at any temperature.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 21), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 21, 22, 16, tzinfo=timezone.utc), equipment=RIG_2, waypoints=WWZ_RUN7,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 420°F — fast ramp (20s, 2°F/sec); 30s hold',
        swab="Light golden — clean.",
        session_char="First half clean, no harshness; second half mild harshness, cough, throat irritation.",
        intensity="Hard but manageable — fastest onset on this strain.",
        dab_notes="First draw was about 20 seconds. No harshness, but not a ton of flavor either. That's been true across this strain. Got a little harsh in second half, mild cough, irritation in throat. Effect is nice fast, maybe fastest onset I've seen from this strain. Hard but still manageable. I'm not wiped out. Normal load.",
        analysis="Fast ramp (2°F/sec, 420°F in 20s) — most compressed climb in the WW Z dataset. First half clean; harshness returned in the second half during the hold, mild but present. Normal load. Endpoint dropped 10°F from Runs 3–6 and harshness still appeared — temperature alone didn't resolve it. Run 5 (small load, 430°F, no harshness) points at load size as a candidate, but it's one uncontrolled data point. Two competing mechanisms: smaller load → less dense vapor → less irritation; or smaller load → material spent sooner → less accumulated heat exposure after the load is done. Both are consistent with the data so far. Fastest onset of any WW Z run — concentrated delivery consistent with the lower endpoint.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 21), sessions_prior_today=1, utc_logged_at=datetime(2026, 5, 22, 1, 28, tzinfo=timezone.utc), equipment=RIG_1, waypoints=WWZ_RUN7,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 420°F — fast ramp (20s, 2°F/sec); 30s hold &nbsp;|&nbsp; <strong>Equipment:</strong> First run back on Cloud Vortex 21.0 + 6mm pearl',
        swab="Light golden — same as Gemlock runs.",
        session_char="First 30 seconds smooth; second 20 seconds rising harshness — more harsh than Run 7.",
        intensity="Medium. Slow onset (mood factor possible — Gemlock broke this session). Duration: roughly 2.5–3 hours.",
        dab_notes="First 30 seconds smooth, second 20 rising harshness. More harsh than previous run. Swabs were light golden, same as with Gemlock. Seems to have slow onset, or maybe breaking the joystick was a buzzkill. Effect duration roughly 2.5–3 hours.",
        analysis="First run back on Cloud Vortex 21.0 + 6mm pearl after the Gemlock broke. Small load — one of three roughly equal chunks, imprecise split. Equipment change and load change happened simultaneously: the load-size experiment can't be isolated here. More harshness than Run 7 despite the smaller load — counterintuitive if load size is the driver, but the spinner reintroducing a pearl and different airflow dynamics is an equally plausible explanation. Swab returned light golden, same as every Gemlock run on this strain — doesn't obviously support the Gemlock-lighter-swab hypothesis, though the load difference is a confound there too. Onset slower than Run 7; user flagged broken joystick as a mood factor, which is real and uncontrollable.",
    ),
    CompletedRun(strain="WW Z", run_date=date(2026, 5, 21), sessions_prior_today=2, utc_logged_at=datetime(2026, 5, 22, 5, 58, tzinfo=timezone.utc), equipment=RIG_1, waypoints=WWZ_RUN9,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 420°F — fast ramp (20s, 2°F/sec); 30s hold — same as Runs 7–8',
        swab="Clean light golden.",
        session_char="Harshness in the second half. Medium intensity, delayed onset.",
        intensity="Medium, delayed onset.",
        dab_notes="Clean light golden swabs, harshness in the second half. Medium intensity, delayed onset. Kind of a whimper of a last dab.",
        analysis="Run 9 repeats the same curve as Runs 7–8 (fast ramp to 420°F in 20s, hold to 50s) on the spinner config with a small load — the final chunk of the jar. Harshness returned in the second half, consistent with Run 8 (small load, spinner, same outcome). Two consecutive small-load runs on the spinner both produced harshness; Run 5 (small load, Gemlock) was clean on the same endpoint. This is the clearest equipment signal in the WW Z dataset: the spinner appears to contribute to harshness at 420°F in a way the Gemlock didn't. The endpoint itself remains a candidate — 420°F sits near the cross-strain harshness boundary and harshness appeared mid-ramp at 414–420°F on display in Runs 3–4 regardless of config. Medium intensity and delayed onset consistent with Run 8. Jar done at 9 runs.",
    ),

    # ── Mango Banana #9 + Z + Sour Tangie (Runs 1–6) ─────────────────────────
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 13), sessions_prior_today=0,   utc_logged_at=datetime(2026, 5, 13, 23, 27, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN1,
        endpoint_note="<strong>Endpoint:</strong> 430°F — baseline ramp &nbsp;|&nbsp; <strong>Equipment:</strong> First session with Gemlock joystick, no pearl",
        swab="Very light golden.",
        session_char="Pronounced flavors up front. Bitter citrus note with a distinct tangerine quality — consistent with Sour Tangie lineage (limonene-forward). Slight harshness at the end. Also appeared as a bitter/citrus rind note in Maple Bacon Donut Run 4 (May 12) — cross-strain parallel, genetics connection unclear, worth watching.",
        intensity="Strong — face tingling.",
        extra_rows=[("Equipment note:", "First run with Gemlock joystick, no pearl. Swab lighter than typical for a first run. Hypothesis: joystick may be more efficient — cleaner swab and/or more material vaporized in the same window. Single data point; something to watch.")],
    ),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 13), sessions_prior_today=1,   utc_logged_at=datetime(2026, 5, 14,  4, 55, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN2,
        endpoint_note="<strong>Endpoint:</strong> 430°F — baseline ramp repeated",
        swab="Light golden — same as Run 1.",
        session_char="Big flavors up front. Visible vapor at lower temps than expected. Slight harshness at the end.",
        intensity="Strong — not too cloudy mentally, noticeably lazy physically.",
    ),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 14), sessions_prior_today=0,   utc_logged_at=datetime(2026, 5, 15,  2,  0, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN3,
        endpoint_note='<strong>Endpoint:</strong> 420°F with 20-second hold — ramp 375→400→420°F',
        swab='Light golden — "lightly toasted marshmallow." Clean.',
        session_char="Nice. Climb rate felt right, hold felt right. Still a bit harsh at the end.",
        intensity="High",
    ),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 14), sessions_prior_today=1,   utc_logged_at=datetime(2026, 5, 15,  4, 34, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN4,
        endpoint_note="<strong>Endpoint:</strong> 415°F with 20-second hold — down 5°F from Run 3",
        swab="Golden — slightly darker than Run 3. Still in the clean range.",
        session_char="Less harsh at the tail than prior runs — still present but attenuating. More material in swabs at the end.",
        intensity="Decent — second dab of the evening, tolerance factor in play.",
    ),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 17), sessions_prior_today=0,   utc_logged_at=datetime(2026, 5, 18,  1,  9, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN5,
        endpoint_note="<strong>Endpoint:</strong> 415°F with 20-second hold — same as Run 4",
        swab="Super light golden — clean. Lighter than Run 4.",
        session_char="Tiny bit of harshness in the throat. Tiny bit of burnt taste at the very last draw.",
        dab_notes="Ran the same curve as last time, the 415 hold. Only one dab left in the jar. A tiny bit of harshness in the throat and a tiny bit of burnt taste at the very last draw. Swabs were their typical super light golden, so clean. Pretty hard hit.",
        intensity="Pretty hard hit.",
        analysis="Harshness at 415°F is now consistent across two runs (Runs 4 and 5) — the same two-run pattern that triggered the step-down recommendation for BB36#1 at the same endpoint. The burnt taste at the very last draw is a new and more specific observation: it points at the final seconds of the 20-second hold as the problem zone, not the ascent. Swab came back super light golden — lighter than Run 4, which runs counter to the hypothesis that lower endpoints leave more material behind. One data point, swab noise is real. Intensity landed hard with no same-day tolerance confound, consistent with the strain's potency pattern.",
    ),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 17), sessions_prior_today=1,   utc_logged_at=datetime(2026, 5, 18,  5,  1, tzinfo=timezone.utc), equipment=RIG_2, waypoints=MB9ZST_RUN6,
        duration_seconds=60,
        endpoint_note="<strong>Endpoint:</strong> 420°F — faster ramp (30s), 60s total (planned 50s + push-button extension)",
        swab="Super light golden — clean.",
        session_char="Super tasty first half. Faster to 420°F hit harder than prior ramps. Last few draws harsh in the push-button extension.",
        dab_notes="Using the proposed next curve but 420 for the hold instead of 415. Swabs were the regular clean light golden. Faster to 420 definitely seems to hit harder, and the first half was super tasty, I didn't miss the lingering lower longer. The shorter duration didn't finish the material loaded, I added 10 more seconds via the push button on Dabby. Very stoned. The last few draws were expectedly harsh.",
        intensity="Very stoned.",
        analysis="Fastest ramp in the MB9ZST dataset — 420°F in 30s vs. 45s in Run 3. The harder hit and front-loaded flavor are consistent with that: same temperature, more vaporization concentrated in the early window. 'Didn't miss the lingering lower longer' is the clearest preference signal in the strain's history — the compressed front end works better than the drawn-out one. The push-button extension to 60s added 10s of hold at 420°F beyond the plan, and the harshness arrived there — consistent with the full MB9ZST/420°F pattern. Swab came back light golden throughout, same as every other Gemlock run on this strain. Jar done at 6 runs.",
    ),
]

# ── ARCHIVED STATUS ───────────────────────────────────────────────────────────
# Finished-jar StrainStatus entries. next_waypoints=None for all — finished jars
# do not render a proposed future curve.

ARCHIVED_STATUS = [
    StrainStatus(name="WW Z", profile_anchor="#wwz-profile", next_text="Jar done — 9 runs. If it shows up again: fast ramp to 420°F is a reasonable starting point", accent=None, slug="wwz",
        info=WWZ_INFO,
        terpene_note='<strong>Terpene inference:</strong> Pinene inferred dominant — weakly supported by piney nose observation. Standard cannabis palette otherwise. See <a href="#terpene-ref">Terpene Reference</a>.',
        next_dab_notes="Run 9 (small load, spinner): clean light golden swab, harshness in second half, medium intensity, delayed onset. Kind of a whimper of a last dab. Jar done.",
        next_ai_analysis="Jar done. Equipment config is the more likely harshness driver — Runs 8–9 (small load, spinner) both produced harshness where Run 5 (same load class, Gemlock) was clean. The 420°F endpoint also sits near the harshness boundary regardless of config. If this strain shows up again, the fast ramp to 420°F (380→400@10s→420@20s, hold to 50s) is a reasonable starting point. Harshness on the spinner at that endpoint is a known risk — step down to 415°F if it persists, or test a joystick if one's available.",
        next_waypoints=None,
        jar_index=(
            "<div style='text-align:center;margin-top:1em;'>"
            "<strong>Runs on the jar:</strong> 9<br>"
            "<strong>Runs that ended without harshness:</strong> 1<br>"
            "<strong>Dabs taken by Sarah that were logged:</strong> 0<br>"
            "<strong>Sarah's review of the flavor:</strong> \"almost gagging\"<br>"
            "<strong>Temperature at which harshness first appeared mid-ramp, Run 3:</strong> 414°F<br>"
            "<strong>Temperature at which harshness first appeared mid-ramp, Run 4:</strong> 420°F<br>"
            "<strong>Variables cleanly isolated in the load-size experiment before equipment changed:</strong> 0<br>"
            "<strong>Session on which the Gemlock joystick broke:</strong> the one right before the last two runs<br>"
            "<strong>Description of the final dab:</strong> \"kind of a whimper of a last dab\"<br>"
            "<strong>Fraction of the jar described as \"spectacular vapor\":</strong> 1 in 9"
            "</div>"
        ),
    ),
    StrainStatus(name="Mango Banana #9 + Z + Sour Tangie", profile_anchor="#mb9zst-profile",  next_text="Jar finished — 6 runs, May 13–17, 2026",                                            accent=None, slug="mb9zst",
        info=MB9ZST_INFO,
        terpene_note=(
            "<strong>Terpene inference:</strong> Limonene inferred prominent from Sour Tangie (Sour Diesel × Tangie) and Mango Banana lineages; "
            "myrcene from Mango Banana (SB36 × Forbidden Banana); terpinolene from Z and Sour Tangie character. "
            "This is the generic cannabis palette applied to a three-component blend — the Neapolitan format means each layer "
            "may have a different terpene balance. Not measured. See <a href=\"#terpene-ref\">Terpene Reference</a>."
        ),
        next_dab_notes="Run 6 at 420°F (faster ramp to 30s, planned 50s extended to 60s via push button): super light golden swab, very tasty first half, faster to 420 hit harder than the slower ramp. Extension into harsh territory. Jar done.",
        next_ai_analysis=(
            "Jar finished. Six runs over five days, May 13–17, 2026. This was also the Gemlock joystick's debut jar — every data point in this strain's history was collected on the new rig, so the baseline cross-strain confound never resolved. "
            "Harshness appeared in the tail on all six runs across three endpoint temperatures (430°F, 420°F, 415°F) and two curve shapes. A clean tail was never achieved. "
            "The fastest ramp (Run 6) produced the best first-half character and the hardest hit — the right shape arrived on the last dab of the jar."
        ),
        next_waypoints=None,
        jar_index=(
            "<div style='text-align:center;margin-top:1em;'>"
            "<strong>Number of runs on a 2g jar:</strong> 6<br>"
            "<strong>Days from first dab to last:</strong> 5<br>"
            "<strong>Endpoint temperatures tried in search of a clean tail:</strong> 3<br>"
            "<strong>Runs that ended with a clean tail:</strong> 0<br>"
            "<strong>Swabs described as “lightly toasted marshmallow”:</strong> 1<br>"
            "<strong>Named strains in the Neapolitan ever individually identified:</strong> 0 of 3<br>"
            "<strong>Equipment changes mid-jar:</strong> 0 <em>(though this jar was the equipment change)</em><br>"
            "<strong>Seconds added to the final run by push button:</strong> 10<br>"
            "<strong>Remaining dabs:</strong> 0"
            "</div>"
        ),
    ),
]
