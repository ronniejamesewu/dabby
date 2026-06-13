"""Lemon Heads + Blueberry Haze — jar file (slug: lhbh)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Lemon Heads + Blueberry Haze',
    profile_anchor='#lhbh-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='lhbh',
    info=[
        ('Strains', 'Lemon Heads (Lemon G × Face Off OG BX) + Blueberry Haze (Blueberry × Haze)'),
        ('Format', 'Close Friends Persy Thumbprint — two strains: outer ring cold cure badder (Lemon Heads), center jam (Blueberry Haze). 90μ persy-tier. Load position not reliably distinguishable.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Lemon Heads brings one of our favorite Lemon G profiles with a hint of gas. Blueberry Haze starts with a forward blueberry zing, then lets the haze linger. Bright citrus up front, haze on the backend.'),
        ('Nose', 'Not yet recorded'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred dominant from Lemon Heads (Lemon G × Face Off OG BX) — Lemon G is known for strong citrus/lemon character; myrcene and terpinolene inferred from Blueberry Haze (Blueberry × Haze). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='No runs yet. This is a two-strain Close Friends Persy Thumbprint — load position is not distinguishable by eye, so each run reflects whichever zone was loaded. Start from baseline curve (380°F open, 420°F in 8s, 60s session). Note nose and vapor character per run — it may help identify which strain contributed over time, but single-session flavor observations are noisy.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
