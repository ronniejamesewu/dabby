"""Dabby core — dataclasses, equipment, baselines, terpene reference, and validation.

Per-jar data lives in jars/<slug>.py; the jar_manifest assembles them.
This module holds only the stable shared layer: dataclasses, RIG_N constants,
BASELINE_* curves, GLOBAL_INFO, TERPENE_REFERENCE, color resolution, and the
(parameterized) validators. It rarely grows — only when a dataclass field,
equipment rig, or baseline curve is added.
"""

# ── CONTENTS ─────────────────────────────────────────────────────────────────
# Navigation index for this file. When you edit Dabby_Core.py — add a field,
# add a RIG_N, rename a section — update the line numbers below in the same
# edit. Skipping this makes the index wrong, which is worse than no index: it
# sends the next Claude to the wrong place. You have the file open. It takes
# 30 seconds. Don't leave a trap.
#
# Logging quick-reference (what a run-logging Claude needs):
#   CompletedRun fields → line  81    (schema for new RUNS entries)
#   StrainStatus fields  → line 114    (schema for STATUS blocks)
#
# Full index:
#   Line  42 — # ── DATACLASSES
#   Line  45 — Waypoint
#   Line  51 — Insert
#   Line  57 — CarbCap
#   Line  63 — Pearl
#   Line  68 — EquipmentConfig
#   Line  81 — CompletedRun
#   Line 114 — StrainStatus
#   Line 134 — TerpeneEntry
#   Line 144 — # ── DATA (FIRST_RUN_DATE, GLOBAL_INFO, BASELINE_416, BASELINE_CURVE)
#   Line 173 — # ── EQUIPMENT (RIG_1 – RIG_5)
#   Line 222 — # ── TERPENE REFERENCE
#   Line 266 — # ── COLOR RESOLUTION
#   Line 318 — # ── VALIDATION (validate, validate_accent_colors)
# ─────────────────────────────────────────────────────────────────────────────

from datetime import datetime, date, timezone
from dataclasses import dataclass
from typing import Literal

# ── DATACLASSES ────────────────────────────────────────────────────────────

@dataclass
class Waypoint:
    time_s: int
    temp_f: int
    note: str

@dataclass
class Insert:
    brand: str       # "Dr. Dabber", "OM Quartz", etc.
    model: str       # "stock", "Sapphire Plus (v2)", etc.
    material: str    # "quartz", "sapphire"

@dataclass
class CarbCap:
    brand: str       # "Cloud Vortex", "Gemcup Glass"
    model: str       # "21.0", "Gemlock joystick"
    airflow: str     # "stock" by default — variant string when known

@dataclass
class Pearl:
    diameter_mm: int
    material: str    # "quartz" — future materials TBD

@dataclass
class EquipmentConfig:
    insert: Insert
    carb_cap: CarbCap
    pearls: list[Pearl]   # empty list = no pearls; sorted in __post_init__ for stable equality
    glass_top: str        # flat string — no sub-dimensions to track yet
    # Guardrail 3: all four fields contribute to nested-dataclass equality.
    # pearls is sorted in __post_init__ so list order doesn't matter.
    # Insert / carb cap / pearls / glass top are all confound boundaries when comparing runs.

    def __post_init__(self):
        self.pearls = sorted(self.pearls, key=lambda p: (p.diameter_mm, p.material))

@dataclass
class CompletedRun:
    strain: str
    run_date: date | None
    sessions_prior_today: int | None
    utc_logged_at: datetime | None
    waypoints: list
    # Python-level optional only; validate() rejects None so every shipped run
    # carries explicit equipment — None never means "inherit a session default".
    equipment: EquipmentConfig = None

    # Semantic status — drives amber styling; amber is presentation, too_hot is the fact
    too_hot: bool = False

    # Curve description
    duration_seconds: int = 65
    endpoint_note: str = ""          # "steady (no ramp)", "same as Run 1", etc.

    # Session content — all fields live here; generator is rendering-only (Step 3)
    swab: str = ""
    session_char: str = ""
    intensity: str | None = None
    read: str = ""                   # interpretation
    verdict: str = ""
    extra_rows: list | None = None   # genuinely one-off result rows (e.g. OC R5 "Observation:")

    # Analysis (currently string literals in build_html() — migrated in Step 3)
    dab_notes: str = ""              # user's read
    analysis: str = ""               # AI synthesis (historically stable, rendered read-only)

    # Title date override for runs where run_date=None (pre-dataclass era entries logged as "May 2026")
    date_label: str = ""             # when set, used instead of derived run_date string in section title

@dataclass
class StrainStatus:
    name: str
    profile_anchor: str
    next_text: str                   # hand-maintained dashboard one-liner (current revisable state)
    accent: str | None
    slug: str

    # Profile content (currently string literals in build_html() — migrated in Step 3)
    info: list | None = None         # rows for info_table()
    terpene_note: str = ""           # <p class="note"> in profile section

    # Current "What to Try Next" — revisable strain-level guidance (N5)
    # Today these are inline args to what_to_try_next_html(); Step 3 makes them explicit.
    # NOT sourced from any run's frozen analysis.
    next_dab_notes: str = ""
    next_ai_analysis: str = ""
    next_waypoints: list | None = None
    jar_index: str = ""         # Jar Index for finished jars — rendered in strain profile

@dataclass
class TerpeneEntry:
    name: str
    alias: str
    bp_f: int
    bp_c: int
    band: Literal["Low", "Mid", "High"]
    aroma: str
    qualities: str
    found_in: str

# ── DATA ────────────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)   # project start — drives the "active since" day count

GLOBAL_INFO = [
    ("Device",       "Switch² (Dabby the House Rig)"),
    ("All Material", "Hash Rosin — ice water extracted, solventless. Consistency varies by jar — noted in each strain profile."),
    ("Insert",       "20mm — quartz or sapphire. Sapphire requires fresh calibration from scratch; do not scale from quartz curves."),
    ("Technique",    "Cold start — pre-load into cold insert before every session"),
    ("Load Size",    "Rice grain (small)"),
    ("Offset Est.",  "Probably small under most operating conditions. Dominant uncertainties are vaporization cooling and dynamic lag during steep ascent. At flat or slowly-ascending phases the system approaches equilibrium. Setpoints are reasonable proxies for material contact temperature."),
    ("Draw Style",   "Long, slow draws throughout session"),
    ("Session End",  "Stop when vapor production drops — do not ride timer on small loads"),
]

BASELINE_416 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=416, note="Endpoint"),
    Waypoint(time_s=50, temp_f=416, note="Hold"),
]

BASELINE_CURVE = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=4,  temp_f=400, note="Steep early climb"),
    Waypoint(time_s=8,  temp_f=420, note="Endpoint"),
    Waypoint(time_s=60, temp_f=420, note="Hold"),
]

# ── EQUIPMENT ────────────────────────────────────────────────────────────────

RIG_1 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="stock", material="quartz"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=6, material="quartz")],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 2: Gemlock era. Dr. Dabber stock quartz insert, Gemcup Glass Gemlock joystick
# (stock airflow), no pearls, stock Dr. Dabber bubbler top. May 13 – May 21, 2026.
# Joystick broke mid-session May 21.
RIG_2 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="stock", material="quartz"),
    carb_cap=CarbCap(brand="Gemcup Glass", model="Gemlock joystick", airflow="stock"),
    pearls=[],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 3: Sapphire era. Dr. Dabber Sapphire Plus (v2) insert (new May 22, 2026);
# Cloud Vortex 21.0 spinner returning (stock airflow); 6mm quartz pearl; stock
# Dr. Dabber bubbler top. In use as of May 22, 2026.
RIG_3 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="Sapphire Plus (v2)", material="sapphire"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=6, material="quartz")],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 4: Sapphire insert, ruby pearl. Dr. Dabber Sapphire Plus (v2) insert;
# Cloud Vortex 21.0 spinner (stock airflow); 5mm synthetic ruby pearl;
# stock Dr. Dabber bubbler top. In use as of May 24, 2026.
RIG_4 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="Sapphire Plus (v2)", material="sapphire"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=5, material="synthetic ruby")],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 5: Sapphire insert, dual ruby pearls. Dr. Dabber Sapphire Plus (v2) insert;
# Cloud Vortex 21.0 spinner (stock airflow); two 5mm synthetic ruby pearls;
# stock Dr. Dabber bubbler top. In use as of May 25, 2026.
RIG_5 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="Sapphire Plus (v2)", material="sapphire"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=5, material="synthetic ruby"), Pearl(diameter_mm=5, material="synthetic ruby")],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 6: Sapphire insert, no pearls, Wym Stick Piston joystick. Dr. Dabber Sapphire Plus (v2)
# insert; Wym Stick Piston titanium joystick (.094" bore, stock airflow); no pearls;
# stock Dr. Dabber bubbler top.
RIG_6 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="Sapphire Plus (v2)", material="sapphire"),
    carb_cap=CarbCap(brand="Wym Stick", model="Piston", airflow='stock — .094" bore'),
    pearls=[],
    glass_top="Dr. Dabber stock bubbler",
)

# ── TERPENE REFERENCE ────────────────────────────────────────────────────────

TERPENE_REFERENCE = [
    # Low band — below 356°F / 180°C
    TerpeneEntry(name="Humulene",          alias="alpha-humulene",              bp_f=225, bp_c=107, band="Low",  aroma="Woody, spicy-clove",                   qualities="Calming; appetite-suppressing character",   found_in="Hops, allspice, cloves, coriander"),
    TerpeneEntry(name="Alpha-Pinene",      alias="alpha-pinene",                bp_f=313, bp_c=156, band="Low",  aroma="Pine forest",                          qualities="Alerting; opens airways",                  found_in="Pine, rosemary, dill, basil, sage"),
    TerpeneEntry(name="Camphene",          alias="camphene",                    bp_f=318, bp_c=159, band="Low",  aroma="Cool camphor, musky earth",             qualities="Limited evidence",                         found_in="Fir, nutmeg, rosemary, sage"),
    TerpeneEntry(name="Beta-Pinene",       alias="beta-pinene",                 bp_f=331, bp_c=166, band="Low",  aroma="Pine forest, fresh",                   qualities="Alerting; focus-associated",               found_in="Pine, dill, basil, rosemary"),
    TerpeneEntry(name="Myrcene",           alias="beta-myrcene",                bp_f=333, bp_c=167, band="Low",  aroma="Musky, earthy, sweet herbal",           qualities="Relaxing, sedating",                       found_in="Mangoes, hops, lemongrass, thyme"),
    TerpeneEntry(name="Carene",            alias="delta-3-carene",              bp_f=340, bp_c=171, band="Low",  aroma="Musky citrus, sweet pine",              qualities="Uplifting; focus-associated",              found_in="Rosemary, cedar, basil, pepper"),
    TerpeneEntry(name="Phellandrene",      alias="alpha/beta-phellandrene",     bp_f=342, bp_c=172, band="Low",  aroma="Citrusy, peppermint",                  qualities="Uplifting character",                      found_in="Eucalyptus, dill, water fennel"),
    TerpeneEntry(name="Terpinene",         alias="alpha-terpinene",             bp_f=343, bp_c=173, band="Low",  aroma="Piney, smokey, herbaceous",             qualities="Supporting",                               found_in="Tea tree, eucalyptus, marjoram"),
    TerpeneEntry(name="Limonene",          alias="limonene",                    bp_f=349, bp_c=176, band="Low",  aroma="Citrus",                                qualities="Uplifting; stress-easing",                 found_in="Citrus rinds, juniper, peppermint"),
    TerpeneEntry(name="Eucalyptol",        alias="cineole",                     bp_f=349, bp_c=176, band="Low",  aroma="Cool camphor, minty",                  qualities="Alerting; opens airways",                  found_in="Eucalyptus, tea tree, mugwort"),
    TerpeneEntry(name="Cymene",            alias="p-cymene",                    bp_f=351, bp_c=177, band="Low",  aroma="Mild sweet aged wood, lemon",           qualities="Supporting",                               found_in="Thyme, oregano, cumin, cilantro"),
    TerpeneEntry(name="Ocimene",           alias="beta/trans-beta-ocimene",     bp_f=352, bp_c=178, band="Low",  aroma="Tropical fruit, woody green citrus",   qualities="Uplifting character",                      found_in="Basil, orchids, kumquats, parsley"),
    # Mid band — 356–446°F / 180–230°C
    TerpeneEntry(name="Terpinolene",       alias="alpha-terpinolene",           bp_f=369, bp_c=187, band="Mid",  aroma="Fresh, herbal, sweet, floral, piney",  qualities="Uplifting; sedating in isolation",         found_in="Limes, cumin, lilac, nutmeg"),
    TerpeneEntry(name="Linalool",          alias="linalool",                    bp_f=388, bp_c=198, band="Mid",  aroma="Floral, citrusy-sweet",                qualities="Calming, sedating",                        found_in="Lavender, citrus, rosemary, basil"),
    TerpeneEntry(name="Sabinene",          alias="sabinene hydrate / thujanol", bp_f=396, bp_c=202, band="Mid",  aroma="Woodsy, spicy",                        qualities="Supporting",                               found_in="Norway Spruce, nutmeg, holm oak"),
    TerpeneEntry(name="Fenchol",           alias="fenchyl alcohol",             bp_f=397, bp_c=203, band="Mid",  aroma="Lemon-lime, piney, camphor",           qualities="Supporting",                               found_in="Basil, aster flowers"),
    TerpeneEntry(name="Borneol",           alias="bornyl alcohol",              bp_f=414, bp_c=212, band="Mid",  aroma="Cool minty, camphor",                  qualities="Calming, sedating",                        found_in="Rosemary, mint, ginger, camphor"),
    TerpeneEntry(name="Isoborneol",        alias="exo-borneol",                 bp_f=414, bp_c=212, band="Mid",  aroma="Woody-sweet, spicy",                   qualities="Calming, sedating",                        found_in="Valerian, sage, thyme"),
    TerpeneEntry(name="Terpineol",         alias="alpha-terpineol",             bp_f=430, bp_c=221, band="Mid",  aroma="Lilac, floral blossom",                qualities="Calming, sedating",                        found_in="Pine oil, petitgrain, cajuput"),
    TerpeneEntry(name="Citronellol",       alias="beta-citronellol",            bp_f=435, bp_c=224, band="Mid",  aroma="Rose, citrus",                         qualities="Relaxing; variable",                       found_in="Citronella, roses, geraniums"),
    TerpeneEntry(name="Pulegone",          alias="pulegone",                    bp_f=435, bp_c=224, band="Mid",  aroma="Minty-camphor, resinous",              qualities="Calming, sedating",                        found_in="Catnip, pennyroyal, rosemary"),
    TerpeneEntry(name="Geraniol",          alias="geraniol",                    bp_f=446, bp_c=230, band="Mid",  aroma="Sweet floral, fruity",                 qualities="Supporting",                               found_in="Roses, lemongrass, citronella"),
    # High band — above 446°F / 230°C
    TerpeneEntry(name="Anethole",          alias="anethole",                       bp_f=454, bp_c=234, band="High", aroma="Licorice, sweet",                      qualities="Sedating character",                   found_in="Anise, fennel, star anise"),
    TerpeneEntry(name="Guaiene",           alias="alpha/beta-guaiene",             bp_f=455, bp_c=235, band="High", aroma="Sweet, woody, earthy, spicy",          qualities="Supporting",                           found_in="Palo Santo"),
    TerpeneEntry(name="Geranyl Acetate",   alias="geranyl acetate",                bp_f=468, bp_c=242, band="High", aroma="Sweet floral, pear-like",              qualities="Supporting",                           found_in="Lemongrass, coriander, geraniums"),
    TerpeneEntry(name="Elemene",           alias="alpha/beta/delta/gamma-elemene", bp_f=487, bp_c=253, band="High", aroma="Waxy, herbal",                         qualities="Limited research",                     found_in="Ginseng, Chinese Yu Jin"),
    TerpeneEntry(name="Caryophyllene",     alias="beta/trans-caryophyllene",       bp_f=493, bp_c=256, band="High", aroma="Spicy, peppery",                       qualities="Calming; CB2 receptor binding",        found_in="Black pepper, cloves, hops, oregano"),
    TerpeneEntry(name="Cedrene",           alias="alpha/beta-cedrene",             bp_f=505, bp_c=263, band="High", aroma="Light woodsy",                         qualities="Supporting",                           found_in="Cedarwood, juniper, cypress"),
    TerpeneEntry(name="Valencene",         alias="valencene",                      bp_f=520, bp_c=271, band="High", aroma="Sweet fresh citrus",                   qualities="Alerting, uplifting",                  found_in="Valencia oranges"),
    TerpeneEntry(name="Farnesene",         alias="alpha/beta-farnesene",           bp_f=523, bp_c=273, band="High", aroma="Green apple",                          qualities="Calming, sedating",                    found_in="Apple skins, pears"),
    TerpeneEntry(name="Nerolidol",         alias="cis/trans-nerolidol",            bp_f=529, bp_c=276, band="High", aroma="Woody bark, waxy, floral",             qualities="Calming, sedating",                    found_in="Neroli, jasmine, ginger, lavender"),
    TerpeneEntry(name="Caryophyllene Oxide", alias="beta-caryophyllene oxide",     bp_f=536, bp_c=280, band="High", aroma="Dry, fresh, spicy-sweet",              qualities="Calming; CB2 receptor binding",        found_in="Black pepper, caraway, cloves"),
    TerpeneEntry(name="Guaiol",            alias="guaiol",                         bp_f=550, bp_c=288, band="High", aroma="Piney, woody, rose-like",              qualities="Supporting",                           found_in="Cypress pines, guaiacum plant"),
    TerpeneEntry(name="Eudesmol",          alias="gamma/alpha/beta-eudesmol",      bp_f=574, bp_c=301, band="High", aroma="Woody-sweet",                          qualities="Mildly sedating",                      found_in="Cypress, valerian, eucalyptus"),
    TerpeneEntry(name="Bisabolol",         alias="alpha-bisabolol / levomenol",    bp_f=599, bp_c=315, band="High", aroma="Sweet floral, honey, mild coconut",    qualities="Calming, soothing",                    found_in="Chamomile"),
    TerpeneEntry(name="Phytol",            alias="phytol",                         bp_f=637, bp_c=336, band="High", aroma="Grassy",                               qualities="Mildly sedating",                      found_in="Green tea"),
]

# ── COLOR RESOLUTION ─────────────────────────────────────────────────────────

def _hex_to_hsl(hex_color):
    r, g, b = [int(hex_color.lstrip('#')[i:i+2], 16) / 255 for i in (0, 2, 4)]
    max_c, min_c = max(r, g, b), min(r, g, b)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        return 0, 0, l * 100
    d = max_c - min_c
    s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
    if max_c == r:   h = (g - b) / d + (6 if g < b else 0)
    elif max_c == g: h = (b - r) / d + 2
    else:            h = (r - g) / d + 4
    return (h / 6) * 360, s * 100, l * 100

def _hsl_to_hex(h, s, l):
    s /= 100; l /= 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if   0   <= h < 60:  r, g, b = c, x, 0
    elif 60  <= h < 120: r, g, b = x, c, 0
    elif 120 <= h < 180: r, g, b = 0, c, x
    elif 180 <= h < 240: r, g, b = 0, x, c
    elif 240 <= h < 300: r, g, b = x, 0, c
    else:                r, g, b = c, 0, x
    return '#{:02X}{:02X}{:02X}'.format(int((r+m)*255), int((g+m)*255), int((b+m)*255))

def _resolve_accent_colors(strain_list):
    # Distribute hues evenly across non-green space (0–89° and 166–359°, avoiding 90–165°).
    # Strains with an explicit accent hex in their StrainStatus use that color instead.
    # The generator passes the combined (closed + paused + active) status list so colors
    # resolve across the full set — there is no module-level STRAIN_STATUS to fall back to.
    NON_GREEN = [(0, 90), (166, 360)]
    total = sum(e - s for s, e in NON_GREEN)
    n = len(strain_list)
    step = total / n
    SAT, LGT = 38, 58
    auto_hues = []
    for i in range(n):
        pos = i * step
        for start, end in NON_GREEN:
            span = end - start
            if pos < span:
                auto_hues.append(start + pos)
                break
            pos -= span
    resolved = {}
    for i, s in enumerate(strain_list):
        resolved[s.name] = s.accent if s.accent is not None else _hsl_to_hex(auto_hues[i], SAT, LGT)
    return resolved

# ── VALIDATION ───────────────────────────────────────────────────────────────

def validate(runs, statuses):
    strain_names = {s.name for s in statuses}
    errors = []

    # Uniqueness across the assembled status list — catches duplicate jars / slugs / anchors.
    for label, values in [("slug", [s.slug for s in statuses]),
                          ("name", [s.name for s in statuses]),
                          ("profile_anchor", [s.profile_anchor for s in statuses])]:
        seen = set()
        for v in values:
            if v in seen:
                errors.append(f"Duplicate {label}: '{v}'")
            seen.add(v)

    # Single pass per run: strain membership, waypoint sanity, equipment completeness.
    for i, run in enumerate(runs):
        if run.strain not in strain_names:
            errors.append(f"runs[{i}] strain '{run.strain}' not found in any STATUS.name")

        wps = run.waypoints
        if not wps:
            errors.append(f"runs[{i}] ({run.strain}): empty waypoints list")
        else:
            for j, wp in enumerate(wps):
                if not (200 <= wp.temp_f <= 650):
                    errors.append(f"runs[{i}] ({run.strain}) waypoint {j}: "
                                   f"temp_f={wp.temp_f} outside expected range 200–650°F")
            times = [wp.time_s for wp in wps]
            if times != sorted(times):
                errors.append(f"runs[{i}] ({run.strain}): waypoint times not monotonically increasing: {times}")

        eq = run.equipment
        if eq is None:
            errors.append(f"runs[{i}] ({run.strain}): equipment is None — "
                           f"every run must carry an explicit EquipmentConfig "
                           f"(None never means 'inherit a session default')")
        else:
            if not eq.glass_top:
                errors.append(f"runs[{i}] ({run.strain}): equipment.glass_top is empty")
            if not eq.insert.brand:
                errors.append(f"runs[{i}] ({run.strain}): equipment.insert.brand is empty")
            if not eq.insert.model:
                errors.append(f"runs[{i}] ({run.strain}): equipment.insert.model is empty")
            if not eq.insert.material:
                errors.append(f"runs[{i}] ({run.strain}): equipment.insert.material is empty")
            if not eq.carb_cap.brand:
                errors.append(f"runs[{i}] ({run.strain}): equipment.carb_cap.brand is empty")
            if not eq.carb_cap.model:
                errors.append(f"runs[{i}] ({run.strain}): equipment.carb_cap.model is empty")
            if not eq.carb_cap.airflow:
                errors.append(f"runs[{i}] ({run.strain}): equipment.carb_cap.airflow is empty")
            for j, pearl in enumerate(eq.pearls):
                if pearl.diameter_mm <= 0:
                    errors.append(f"runs[{i}] ({run.strain}): pearl[{j}].diameter_mm={pearl.diameter_mm} must be > 0")
                if not pearl.material:
                    errors.append(f"runs[{i}] ({run.strain}): pearl[{j}].material is empty")

    # Date ordering — within each strain, non-None run_dates must be ascending
    strain_run_dates = {}
    for run in runs:
        if run.run_date is not None:
            strain_run_dates.setdefault(run.strain, []).append(run.run_date)
    for strain, dates in strain_run_dates.items():
        for i in range(1, len(dates)):
            if dates[i] < dates[i - 1]:
                errors.append(
                    f"{strain}: run dates out of order — "
                    f"{dates[i - 1]} followed by {dates[i]}"
                )

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  {e}")
        raise SystemExit(1)

def validate_accent_colors(statuses, resolved_colors):
    # Only check manually-overridden colors — auto-assigned ones are valid by construction.
    overrides = [(s.name, s.accent) for s in statuses if s.accent is not None]
    if not overrides:
        return
    all_resolved = [(s.name, resolved_colors[s.name]) for s in statuses]
    warnings = []
    for strain, color in overrides:
        h, s, l = _hex_to_hsl(color)
        if 90 <= h <= 165:
            warnings.append(f"{strain} override {color}: hue {h:.0f}° in green range (90–165°) — clashes with UI chrome")
        if s > 50 and 35 <= l <= 70:
            warnings.append(f"{strain} override {color}: saturation {s:.0f}% too high — avoid miami vice brights")
        for other_strain, other_color in all_resolved:
            if other_strain == strain:
                continue
            oh, _, ol = _hex_to_hsl(other_color)
            hue_diff = min(abs(h - oh), 360 - abs(h - oh))
            if hue_diff < 30 and abs(l - ol) < 20:
                warnings.append(f"{strain} override {color} too close to {other_strain} {other_color}: {hue_diff:.0f}° apart")
    if warnings:
        print("ACCENT COLOR WARNINGS:")
        for w in warnings: print(f"  {w}")
