"""Donny Burger + Rainbow Belts — jar file (slug: dbrb)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Donny Burger + Rainbow Belts',
    profile_anchor='#dbrb-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='dbrb',
    info=[
        ('Strains', 'Donny Burger (GMO × Han Solo Burger — Han Solo Burger: GMO × Larry OG F8; Larry OG: SFV OG × OG Kush) + Rainbow Belts (Z × Moonbow)'),
        ('Format', 'Close Friends Persy Thumbprint — two strains: outer ring cold cure badder (Donny Burger), center jam (Rainbow Belts). 90μ persy-tier. Load position not reliably distinguishable.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Donny Burger brings sweet GMO funk with garlic, onion, and spice. Rainbow Belts cuts through with lemon-lime, floral Z, and a smooth exhale. Gas, funk, and bright fruit.'),
        ('Nose', 'Not yet recorded'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Caryophyllene inferred dominant from GMO and OG lineage on the Donny Burger side (funky, gassy, garlic-onion character); limonene inferred from Rainbow Belts Z side (lemon-lime, citrus). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='No runs yet. This is a two-strain Close Friends Persy Thumbprint — load position is not distinguishable by eye, so each run reflects whichever zone was loaded. Start from baseline curve (380°F open, 420°F in 8s, 60s session). Note nose and vapor character per run — it may help identify which strain contributed over time, but single-session flavor observations are noisy.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
