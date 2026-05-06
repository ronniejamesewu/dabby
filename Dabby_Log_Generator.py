#!/usr/bin/env python3
from datetime import datetime
"""
Dabby the House Rig — Session Profile & Calibration Log Generator
Produces Dabby_Profile_Log.html — a mobile-responsive, screen-optimized web document.
To update: edit DATA and SECTIONS sections, then run with python3.
"""

# ── PALETTE ────────────────────────────────────────────────────────────────────
GREEN_DARK  = "#2D5A3D"
GREEN_MID   = "#4A7C59"
GREEN_LIGHT = "#F0F7F2"
AMBER       = "#B8860B"
AMBER_LIGHT = "#FFF8E7"
GREY_TEXT   = "#555555"
GREY_LIGHT  = "#888888"
GREY_BG     = "#F5F5F5"

WWZ_INFO = [
    ("Strain",      "WW Z (White Widow × Zkittlez lineage — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Piney with sweet undertone (weak secondary signal only)"),
    ("Status",      "DIALED — Run 1"),
]

CAG_INFO = [
    ("Strain",      "Caramel Apple Gelato (Gelato lineage: Sunset Sherbet × Thin Mint GSC — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Muted — no distinct notes (weak secondary signal, consistent with heavier terpene profile)"),
    ("Status",      "IN CALIBRATION — Run 1 complete, Run 2 pending"),
]

# NOTE: This is a stub. The full generator is in Dabby_Log_Generator.py on disk.
# Run: python3 Dabby_Log_Generator.py to regenerate index.html
