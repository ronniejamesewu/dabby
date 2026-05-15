#!/usr/bin/env python3
"""
Dabby the House Rig — Session Log Generator
Produces index.html — a mobile-responsive, screen-optimized web document.
Data lives in Dabby_Data.py; this file is rendering logic only.
To log a new run: edit Dabby_Data.py, then add the run section in build_html().
"""

from datetime import datetime, date, timezone

from Dabby_Data import *
from Dabby_Data import _ACCENT_RESOLVED  # underscore names are skipped by wildcard import

# ── PALETTE ────────────────────────────────────────────────────────────────

GREEN_DARK  = "#2D5A3D"
GREEN_MID   = "#4A7C59"
GREEN_LIGHT = "#F0F7F2"
AMBER       = "#B8860B"
AMBER_LIGHT = "#FFF8E7"
GREY_TEXT   = "#555555"
GREY_LIGHT  = "#888888"
GREY_BG     = "#F5F5F5"

# ── CSS ──────────────────────────────────────────────────────────────────

CSS = f"""
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --green-dark:  {GREEN_DARK};
  --green-mid:   {GREEN_MID};
  --green-light: {GREEN_LIGHT};
  --amber:       {AMBER};
  --amber-light: {AMBER_LIGHT};
  --grey-text:   {GREY_TEXT};
  --grey-light:  {GREY_LIGHT};
  --grey-bg:     {GREY_BG};
  --text:        #1A1A1A;
  --border:      #CCCCCC;
  --radius:      6px;
  --font:        -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono:   "SF Mono", "Fira Code", "Consolas", monospace;
  --max-width:   780px;
  --page-pad:    2rem;
}}

html {{ font-size: 16px; }}
body {{
  font-family: var(--font);
  color: var(--text);
  background: #FAFAFA;
  line-height: 1.6;
  padding: 1rem;
}}

/* ── Layout ── */
.doc {{
  max-width: var(--max-width);
  margin: 0 auto;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  overflow: hidden;
}}

/* ── Cover ── */
.cover {{
  background: var(--green-dark);
  color: #fff;
  padding: 3rem var(--page-pad) 2.5rem;
  text-align: center;
}}
.cover h1 {{
  font-size: clamp(1.8rem, 5vw, 2.8rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
  color: #fff;
}}
.cover .subtitle {{
  font-size: 1rem;
  color: rgba(255,255,255,0.8);
  margin-bottom: 0.4rem;
}}
.cover .tagline {{
  font-size: 0.85rem;
  color: rgba(255,255,255,0.6);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}

/* ── Sections ── */
.section {{
  padding: 2rem var(--page-pad);
  border-bottom: 1px solid var(--border);
}}
.section:last-child {{ border-bottom: none; }}

/* ── Section header strip ── */
.section-header {{
  background: var(--green-light);
  margin: 0 calc(-1 * var(--page-pad)) 1.5rem;
  padding: 1rem var(--page-pad);
  border-bottom: 3px solid var(--green-mid);
}}
.section-header.grey {{
  background: var(--grey-bg);
  border-bottom-color: #4A7D9A;
}}
.section-header h2 {{
  font-size: clamp(1.1rem, 3vw, 1.4rem);
  font-weight: 700;
  color: var(--green-dark);
  margin-bottom: 0.3rem;
}}
.section-header.grey h2 {{ color: #4A7D9A; }}


/* ── Info table ── */
.info-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.9rem;
}}
.info-table tr {{ border-bottom: 1px solid var(--border); }}
.info-table tr:last-child {{ border-bottom: none; }}
.info-table td {{
  padding: 0.55rem 0.75rem;
  vertical-align: top;
}}
.info-table td:first-child {{
  font-weight: 600;
  color: var(--green-dark);
  width: 28%;
  white-space: nowrap;
}}
.info-table td:last-child {{
  color: var(--text);
}}

/* ── Curve table ── */
.curve-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.88rem;
}}
.curve-table th {{
  background: var(--green-dark);
  color: #fff;
  padding: 0.55rem 0.75rem;
  text-align: left;
  font-weight: 600;
}}
.curve-table th.amber-header {{
  background: var(--amber);
}}
.curve-table td {{
  padding: 0.5rem 0.75rem;
  vertical-align: top;
  border-bottom: 1px solid var(--border);
}}
.curve-table tr:nth-child(even) td {{ background: var(--green-light); }}
.curve-table tr:last-child td {{ border-bottom: none; }}
.curve-table td:first-child {{ font-weight: 700; white-space: nowrap; }}
.curve-table td:nth-child(2) {{ white-space: nowrap; }}

/* ── Terpene table ── */
.terpene-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.88rem;
}}
.terpene-table th {{
  background: var(--green-mid);
  color: #fff;
  padding: 0.55rem 0.75rem;
  text-align: left;
  font-weight: 600;
}}
.terpene-table td {{
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--border);
}}
.terpene-table tr:nth-child(even) td {{ background: var(--green-light); }}
.terpene-table tr:last-child td {{ border-bottom: none; }}

/* ── Swab table ── */
.swab-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.9rem;
}}
.swab-table tr {{ border-bottom: 1px solid var(--border); }}
.swab-table tr:last-child {{ border-bottom: none; }}
.swab-table td {{ padding: 0.55rem 0.75rem; vertical-align: top; }}
.swab-table td:first-child {{ font-weight: 700; width: 30%; }}
.swab-key.target  {{ color: var(--green-dark); }}
.swab-key.hot     {{ color: #B85C00; }}
.swab-key.severe  {{ color: #8B0000; }}
.swab-key.cool    {{ color: #2255AA; }}

/* ── Result rows ── */
.result-row {{ margin: 0.5rem 0; font-size: 0.92rem; }}
.result-row .label {{ font-weight: 700; color: var(--green-dark); }}
.result-row.amber .label {{ color: var(--amber); }}

/* ── Typography ── */
h3 {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--green-mid);
  margin: 1.2rem 0 0.5rem;
}}
h3.amber {{ color: var(--amber); }}
h3.grey  {{ color: var(--grey-text); }}
p {{
  font-size: 0.92rem;
  color: var(--text);
  margin: 0.5rem 0;
  line-height: 1.65;
}}
.note {{
  font-size: 0.85rem;
  color: var(--grey-text);
  line-height: 1.6;
  margin: 0.75rem 0;
  padding: 0.5rem 0.75rem;
  border-left: 3px solid var(--green-mid);
  background: var(--green-light);
  border-radius: 0 var(--radius) var(--radius) 0;
}}
.meta {{
  font-size: 0.82rem;
  color: var(--grey-light);
  margin-top: 0.3rem;
}}
.divider {{
  border: none;
  border-top: 2px solid var(--green-light);
  margin: 1.2rem 0;
}}
.divider.amber {{ border-top-color: var(--amber-light); }}

/* ── Strain browser ── */
.strain-browser {{
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  max-height: 380px;
  margin-bottom: 1rem;
}}
.search-wrap {{
  flex-shrink: 0;
  padding: 0.6rem;
  background: var(--grey-bg);
  border-bottom: 1px solid var(--border);
}}
.search-input {{
  width: 100%;
  padding: 0.55rem 0.75rem;
  border: 1px solid var(--border);
  border-radius: 7px;
  font-size: 0.88rem;
  font-family: var(--font);
  background: #fff;
  color: var(--text);
  -webkit-appearance: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}}
.search-input::placeholder {{ color: var(--grey-light); }}
.search-input:focus {{
  outline: none;
  border-color: var(--green-mid);
  box-shadow: 0 0 0 3px rgba(74,124,89,0.15);
}}
.strain-list {{
  overflow-y: auto;
  flex: 1;
  -webkit-overflow-scrolling: touch;
}}
.strain-row {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.7rem 1rem;
  border-bottom: 1px solid #f2f2f2;
  border-left: 4px solid var(--accent, var(--green-mid));
  transition: background 0.12s;
}}
.strain-row:last-child {{ border-bottom: none; }}
.strain-row:hover {{ background: var(--green-light); }}
.strain-row.hidden {{ display: none; }}
.strain-info {{ flex: 1; min-width: 0; }}
.strain-name {{
  display: block;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--green-dark);
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}
.strain-name:hover {{ text-decoration: underline; }}
.strain-meta {{
  font-size: 0.7rem;
  color: var(--grey-light);
  font-family: var(--font-mono);
  margin-top: 0.1rem;
}}
.strain-next {{
  font-size: 0.7rem;
  color: var(--grey-text);
  margin-top: 0.15rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
}}
.next-pill {{
  display: inline-block;
  padding: 0.28rem 0.75rem;
  background: var(--green-dark);
  border-radius: 20px;
  font-size: 0.75rem;
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  white-space: nowrap;
  flex-shrink: 0;
  transition: background 0.15s, transform 0.1s;
}}
.next-pill:hover {{ background: var(--green-mid); transform: translateX(2px); }}
.no-results {{
  padding: 1.5rem;
  text-align: center;
  font-size: 0.85rem;
  color: var(--grey-light);
  font-family: var(--font-mono);
  display: none;
}}
.ref-row {{
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}}
.ref-label {{
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--grey-light);
}}
.ref-row a {{
  font-size: 0.8rem;
  color: var(--grey-text);
  text-decoration: none;
  border-bottom: 1px solid var(--border);
  padding-bottom: 1px;
  transition: color 0.15s, border-color 0.15s;
}}
.ref-row a:hover {{ color: var(--green-dark); border-bottom-color: var(--green-dark); }}

/* ── Footer ── */
.footer {{
  padding: 1.2rem var(--page-pad);
  background: var(--grey-bg);
  font-size: 0.8rem;
  color: var(--grey-light);
  font-style: italic;
  text-align: center;
  border-top: 1px solid var(--border);
}}


/* ── Curve chart ── */
.curve-chart-wrap {{
  background: #fff;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.75rem 0.75rem 0.5rem;
  margin: 1rem 0 0.5rem;
}}
.curve-chart-legend {{
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 0.85rem;
  font-family: 'DM Mono', monospace;
  font-size: 0.72rem;
  font-weight: 400;
  letter-spacing: 0.03em;
  color: var(--grey-text);
}}
.curve-chart-legend span {{
  display: flex;
  align-items: center;
  gap: 6px;
}}
.legend-line {{
  width: 22px;
  height: 2.5px;
  display: inline-block;
  border-radius: 2px;
}}
.legend-box {{
  width: 12px;
  height: 12px;
  display: inline-block;
  border-radius: 2px;
}}
/* ── Dashboard ── */
.stats-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.75rem;
}}
.stat-card {{
  background: var(--green-light);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  border-top: 3px solid #ccc;
  padding: 0.9rem 0.75rem 0.75rem;
  text-align: center;
}}
.stat-card.c1 {{ border-top-color: #1DB954; }}
.stat-card.c2 {{ border-top-color: #4A7D9A; }}
.stat-card.c3 {{ border-top-color: {AMBER}; }}
.stat-card.c4 {{ border-top-color: {GREEN_MID}; }}
.stat-card.c5 {{ border-top-color: #7A9EBB; }}
.stat-card.c6 {{ border-top-color: #9B7A3A; }}
.stat-value {{
  font-family: 'DM Mono', monospace;
  font-size: 1.6rem;
  font-weight: 500;
  color: var(--green-dark);
  line-height: 1.1;
  margin-bottom: 0.35rem;
}}
.stat-label {{
  font-size: 0.78rem;
  color: var(--grey-text);
  font-family: 'DM Mono', monospace;
  font-weight: 400;
  letter-spacing: 0.03em;
  line-height: 1.3;
}}

/* ── Collapsible sections ── */
details.collapsible {{
  border-bottom: 1px solid var(--border);
}}
details.collapsible:last-child {{ border-bottom: none; }}
details.collapsible > summary {{
  background: var(--green-light);
  border-bottom: 3px solid var(--green-mid);
  padding: 1rem var(--page-pad);
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  user-select: none;
}}
details.collapsible.grey > summary {{
  background: var(--grey-bg);
  border-bottom-color: #4A7D9A;
}}
details.collapsible > summary::-webkit-details-marker {{ display: none; }}
details.collapsible > summary h2 {{
  font-size: clamp(1.1rem, 3vw, 1.4rem);
  font-weight: 700;
  color: var(--green-dark);
  flex: 1;
  margin: 0;
}}
details.collapsible.grey > summary h2 {{ color: #4A7D9A; }}
details.collapsible > summary::after {{
  content: '›';
  font-size: 1.3rem;
  color: var(--grey-light);
  line-height: 1;
  transition: transform 0.2s ease;
  display: inline-block;
}}
details.collapsible[open] > summary::after {{ transform: rotate(90deg); }}
details.collapsible > .collapsible-body {{ padding: 2rem var(--page-pad); }}

/* ── Pill group ── */
.pill-group {{
  display: flex;
  flex-direction: row;
  gap: 0.4rem;
  flex-shrink: 0;
  align-items: center;
}}
.last-pill {{
  display: inline-block;
  padding: 0.28rem 0.75rem;
  background: var(--accent, var(--green-mid));
  border-radius: 20px;
  font-size: 0.75rem;
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  white-space: nowrap;
  transition: opacity 0.15s;
}}
.last-pill:hover {{ opacity: 0.8; }}

/* ── Terpene reference table ── */
.terp-ref-wrap {{
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
}}
.terp-ref-table {{
  width: 100%;
  min-width: 680px;
  border-collapse: collapse;
  font-size: 0.85rem;
}}
.terp-ref-table th {{
  background: var(--grey-bg);
  color: var(--grey-text);
  padding: 0.5rem 0.75rem;
  text-align: left;
  font-weight: 600;
  border-bottom: 2px solid var(--border);
  white-space: nowrap;
}}
.terp-ref-table td {{
  padding: 0.45rem 0.75rem;
  border-bottom: 1px solid #f0f0f0;
  vertical-align: top;
}}
.terp-ref-table tr:hover td {{ background: var(--green-light); }}
.terp-ref-table .band-row td {{
  background: var(--grey-bg);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--grey-text);
  padding: 0.3rem 0.75rem;
  border-bottom: 1px solid var(--border);
}}
.terp-alias {{
  font-size: 0.75rem;
  color: var(--grey-light);
  display: block;
}}
.bp-cell {{
  white-space: nowrap;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--grey-text);
}}
.band-badge {{
  display: inline-block;
  padding: 0.18rem 0.5rem;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  white-space: nowrap;
}}
.band-low  {{ background: #D6EAF8; color: #1A4A6B; }}
.band-mid  {{ background: #FFF0CC; color: #8A6000; }}
.band-high {{ background: #FFE5CC; color: #7A3000; }}

/* ── Mobile ── */
@media (max-width: 600px) {{
  :root {{ --page-pad: 1rem; }}
  body {{ padding: 0.5rem; }}
  .info-table td:first-child {{ width: 35%; white-space: normal; }}
  .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
  .pill-group {{ flex-direction: column; gap: 0.3rem; align-items: flex-end; }}
}}
"""

# ── HELPERS ────────────────────────────────────────────────────────────────

def info_table(rows):
    html = '<table class="info-table">'
    for label, value in rows:
        html += f'<tr><td>{label}</td><td>{value}</td></tr>'
    return html + '</table>'

def curve_table(rows, amber=False):
    hdr = "amber-header" if amber else ""
    html = f'<table class="curve-table"><thead><tr>'
    for col in ["Time", "Setpoint", "Notes"]:
        html += f'<th class="{hdr}">{col}</th>'
    html += '</tr></thead><tbody>'
    for wp in rows:
        html += f'<tr><td>{wp.time_s}s</td><td>{wp.temp_f}°F</td><td>{wp.note}</td></tr>'
    return html + '</tbody></table>'

def terpene_table(rows):
    html = '<table class="terpene-table"><thead><tr>'
    for col in ["Terpene", "Boiling Point", "Character"]:
        html += f'<th>{col}</th>'
    html += '</tr></thead><tbody>'
    for terpene, bp, char in rows:
        html += f'<tr><td>{terpene}</td><td>{bp}</td><td>{char}</td></tr>'
    return html + '</tbody></table>'

def section_header(title, header_class=""):
    html = f'<div class="section-header {header_class}">'
    html += f'<h2>{title}</h2>'
    return html + '</div>'

def result_row(label, value, amber=False):
    cls = "result-row amber" if amber else "result-row"
    return f'<p class="{cls}"><span class="label">{label}</span> {value}</p>'

def accent_header(title, accent):
    return (f'<div class="section-header" style="border-bottom-color:{accent};">'
            f'<h2 style="color:{accent};">{title}</h2></div>')

def ordinal(n):
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10 if n % 100 not in (11, 12, 13) else 0, "th")
    return f"{n}{suffix}"

def session_order_note(sessions_prior):
    if not sessions_prior:
        return ''
    return f'<p class="meta">{ordinal(sessions_prior + 1)} session of the day &mdash; {sessions_prior} prior</p>'

def collapsible_section(section_id, title, content_html, header_class=""):
    grey = "grey" if header_class == "grey" else ""
    cls  = f"collapsible {grey}".strip()
    s  = f'<details class="{cls}" id="{section_id}">'
    s += f'<summary><h2>{title}</h2></summary>'
    s += f'<div class="collapsible-body">{content_html}</div>'
    s += '</details>'
    return s

def what_to_try_next_html(section_id, dab_notes, ai_analysis, proposed_waypoints=None, accent=None):
    s = f'<div class="section" id="{section_id}">'
    if accent:
        s += (f'<div class="section-header grey" style="border-bottom-color:{accent};">'
              f'<h2 style="color:{accent};">What to Try Next</h2></div>')
    else:
        s += section_header("What to Try Next", header_class="grey")
    s += result_row("Dab Notes:", dab_notes)
    s += result_row("AI Analysis:", ai_analysis)
    if proposed_waypoints:
        s += '<h3>Proposed Curve</h3>'
        s += curve_chart_html(proposed_waypoints)
        s += curve_table(proposed_waypoints)
    s += '</div>'
    return s

def dashboard_html():
    today = date.today()
    days = (today - FIRST_RUN_DATE).days + 1

    opens, endpoints, temp_sec, run_counts, date_counts = [], [], {}, {}, {}
    for run in COMPLETED_RUNS:
        pts = [(wp.time_s, wp.temp_f) for wp in run.waypoints]
        opens.append(pts[0][1])
        endpoints.append(pts[-1][1])
        run_counts[run.strain] = run_counts.get(run.strain, 0) + 1
        if run.run_date is not None:
            date_counts[run.run_date] = date_counts.get(run.run_date, 0) + 1
        for i in range(len(pts) - 1):
            t1, v1 = pts[i]; t2, v2 = pts[i + 1]
            dt = t2 - t1
            for s in range(dt):
                bucket = round((v1 + (v2 - v1) * s / dt) / 5) * 5
                temp_sec[bucket] = temp_sec.get(bucket, 0) + 1

    total          = len(COMPLETED_RUNS)
    avg_open       = round(sum(opens) / total)
    avg_end        = round(sum(endpoints) / total)
    hot_temp       = max(temp_sec, key=temp_sec.get)
    max_dabs_day   = max(date_counts.values()) if date_counts else 0
    unique_strains = len(run_counts)

    last_dates = {}
    for run in COMPLETED_RUNS:
        if run.run_date is not None:
            if run.strain not in last_dates or run.run_date > last_dates[run.strain]:
                last_dates[run.strain] = run.run_date

    sorted_strains = sorted(
        [s for s in STRAIN_STATUS if run_counts.get(s.name, 0) > 0],
        key=lambda s: run_counts[s.name], reverse=True
    )

    cards = (
        f'<div class="stats-grid">'
        f'<div class="stat-card c1"><div class="stat-value">{total}</div><div class="stat-label">runs over {days} days</div></div>'
        f'<div class="stat-card c5"><div class="stat-value">{max_dabs_day}</div><div class="stat-label">most dabs in a day</div></div>'
        f'<div class="stat-card c6"><div class="stat-value">{unique_strains}</div><div class="stat-label">unique strains</div></div>'
        f'<div class="stat-card c2"><div class="stat-value">{avg_open}°</div><div class="stat-label">avg open</div></div>'
        f'<div class="stat-card c3"><div class="stat-value">{avg_end}°</div><div class="stat-label">avg endpoint</div></div>'
        f'<div class="stat-card c4"><div class="stat-value">{hot_temp}°</div><div class="stat-label">most time spent</div></div>'
        f'</div>'
    )

    max_runs = run_counts[sorted_strains[0].name] if sorted_strains else 0
    rows = ''
    for i, ss in enumerate(sorted_strains):
        strain       = ss.name
        anchor       = ss.profile_anchor
        slug         = ss.slug
        color        = _ACCENT_RESOLVED.get(strain, "#888888")
        medal        = ' 🥇' if run_counts[strain] == max_runs else ''
        n            = run_counts[strain]
        session_word = 'session' if n == 1 else 'sessions'
        ld           = last_dates.get(strain)
        if ld:
            date_str = ld.strftime('%b %d').replace(' 0', ' ')
            meta = f'{n} {session_word} &middot; {"" if n == 1 else "last "}{date_str}'
        else:
            meta = f'{n} {session_word}'
        next_anchor = anchor.replace('-profile', '-next')
        last_anchor = f'#{slug}-run{n}'
        rows += (
            f'<div class="strain-row" data-strain="{strain.lower()}" style="--accent:{color}">'
            f'<div class="strain-info">'
            f'<a href="{anchor}" class="strain-name">{strain}{medal}</a>'
            f'<span class="strain-meta">{meta}</span>'
            f'<span class="strain-next">{ss.next_text}</span>'
            f'</div>'
            f'<div class="pill-group">'
            f'<a href="{last_anchor}" class="last-pill">&uarr; Last</a>'
            f'<a href="{next_anchor}" class="next-pill">&rarr; Next</a>'
            f'</div>'
            f'</div>'
        )

    browser = (
        f'<div class="strain-browser">'
        f'<div class="search-wrap">'
        f'<input class="search-input" type="search" placeholder="Search strains…" id="strainSearch" autocomplete="off">'
        f'</div>'
        f'<div class="strain-list">'
        f'{rows}'
        f'<div class="no-results" id="noResults">No strains match</div>'
        f'</div>'
        f'</div>'
    )

    js = (
        '<script>'
        '(function(){'
        'var inp=document.getElementById("strainSearch");'
        'var rows=document.querySelectorAll(".strain-row");'
        'var none=document.getElementById("noResults");'
        'inp.addEventListener("input",function(){'
        'var q=this.value.toLowerCase().trim();'
        'var v=0;'
        'rows.forEach(function(r){'
        'var m=!q||r.dataset.strain.includes(q);'
        'r.classList.toggle("hidden",!m);'
        'if(m)v++;'
        '});'
        'none.style.display=v===0?"block":"none";'
        '});'
        '})();'
        # Auto-open <details> when navigated to via anchor link
        '(function(){'
        'function openDetails(hash){'
        'if(!hash)return;'
        'var el=document.querySelector(hash);'
        'if(el&&el.tagName==="DETAILS")el.open=true;'
        '}'
        'openDetails(window.location.hash);'
        'window.addEventListener("hashchange",function(){openDetails(window.location.hash);});'
        'document.querySelectorAll("a[href^=\'#\']").forEach(function(a){'
        'a.addEventListener("click",function(){'
        'var t=document.querySelector(this.getAttribute("href"));'
        'if(t&&t.tagName==="DETAILS")t.open=true;'
        '});'
        '});'
        '})();'
        '</script>'
    )

    s = '<div class="section" id="dashboard">'
    s += section_header("Dashboard")
    s += cards
    s += browser
    s += js
    s += '</div>'
    return s


# ── CHART ────────────────────────────────────────────────────────────────────

_chart_counter = [0]

def curve_chart_html(waypoints, chart_id=None):
    """waypoints: list[Waypoint]. Returns HTML string with canvas + inline script."""
    _chart_counter[0] += 1
    cid = chart_id or f"curve_{_chart_counter[0]}"

    # Build JS arrays from Waypoint objects
    pts = []
    for wp in waypoints:
        pts.append(f"{{x:{wp.time_s},y:{wp.temp_f}}}")
    pts_js = '[' + ','.join(pts) + ']'

    # Build terpene BP line array from TERPENE_REFERENCE
    _CHART_TERPS = ["Alpha-Pinene", "Myrcene", "Limonene", "Terpinolene", "Linalool"]
    _chart_terp_entries = [t for t in TERPENE_REFERENCE if t.name in _CHART_TERPS]
    terps_js = '[' + ','.join(
        f'{{y:{t.bp_f},l:"{t.name.replace("Alpha-", "")}"}}'
        for t in _chart_terp_entries
    ) + ']'

    # Determine y axis range
    all_temps = [wp.temp_f for wp in waypoints]
    y_max = max(max(all_temps) + 15, 455)
    y_min = 300
    mono = "'DM Mono', monospace"

    html = f'''<div class="curve-chart-wrap">
<div class="curve-chart-legend">
  <span><span class="legend-line" style="background:#1DB954;"></span>Setpoint (°F)</span>
  <span><span class="legend-line" style="height:0;border-top:2px dashed #4A7D9A;"></span>Terpene BPs</span>
  <span><span class="legend-box" style="background:rgba(210,90,80,0.12);border:1px solid rgba(210,90,80,0.35);"></span>THC range</span>
</div>
<div style="position:relative;width:100%;height:200px;">
<canvas id="{cid}" role="img" aria-label="Temperature curve chart">Curve from {waypoints[0].temp_f}°F at {waypoints[0].time_s}s to {waypoints[-1].temp_f}°F at {waypoints[-1].time_s}s.</canvas>
</div>
</div>
<script>
(function(){{
  var mono="{mono}";
  var terps={terps_js};
  new Chart(document.getElementById("{cid}"),{{
    type:"line",
    data:{{datasets:[{{
      label:"Setpoint",data:{pts_js},
      borderColor:"#1DB954",backgroundColor:"transparent",
      borderWidth:2,
      pointRadius:2.7,pointStyle:"circle",
      pointBackgroundColor:"#1DB954",pointBorderColor:"#1DB954",pointBorderWidth:0,
      pointHoverRadius:5,pointHoverBackgroundColor:"#1DB954",pointHoverBorderColor:"#fff",pointHoverBorderWidth:1.5,
      fill:false,tension:0,parsing:false,clip:false
    }}]}},
    options:{{responsive:true,maintainAspectRatio:false,parsing:false,
      layout:{{padding:{{left:4,right:4,top:4,bottom:0}}}},
      plugins:{{
        legend:{{display:false}},
        tooltip:{{
          backgroundColor:"#111",borderColor:"#1DB954",borderWidth:1,
          titleColor:"#888",bodyColor:"#1DB954",
          titleFont:{{family:mono,size:10,weight:"300"}},
          bodyFont:{{family:mono,size:13,weight:"500"}},
          padding:10,cornerRadius:4,
          callbacks:{{title:function(i){{return i[0].raw.x+"s"}},label:function(i){{return i.raw.y+"°F"}}}}
        }}
      }},
      scales:{{
        x:{{type:"linear",min:0,max:{waypoints[-1].time_s},
          title:{{display:true,text:"seconds",color:"#aaa",font:{{family:mono,size:10,weight:"300"}}}},
          ticks:{{stepSize:10,color:"#aaa",font:{{family:mono,size:10}}}},
          grid:{{color:"rgba(0,0,0,0.05)"}},border:{{color:"rgba(0,0,0,0.08)"}}}},
        y:{{min:{y_min},max:{y_max},
          title:{{display:true,text:"°F",color:"#aaa",font:{{family:mono,size:10,weight:"300"}}}},
          ticks:{{stepSize:25,color:"#aaa",font:{{family:mono,size:10}}}},
          grid:{{color:"rgba(0,0,0,0.05)"}},border:{{color:"rgba(0,0,0,0.08)"}}}}
      }}
    }},
    plugins:[{{id:"ann",beforeDraw:function(c){{
      var ctx=c.ctx,ca=c.chartArea,ys=c.scales.y;
      if(!ca)return;
      ctx.save();

      // THC band
      ctx.fillStyle="rgba(210,90,80,0.09)";
      ctx.fillRect(ca.left,ys.getPixelForValue(428),ca.right-ca.left,ys.getPixelForValue(315)-ys.getPixelForValue(428));

      // THC pill label
      ctx.font="400 11px "+mono;
      var pt="THC",pp={{x:6,y:3}};
      var pw=ctx.measureText(pt).width+pp.x*2,ph=17;
      var px=ca.right-pw-6,py=ys.getPixelForValue(428)+5;
      ctx.fillStyle="rgba(210,90,80,0.18)";
      ctx.beginPath();ctx.roundRect(px,py,pw,ph,3);ctx.fill();
      ctx.fillStyle="rgba(170,50,40,0.9)";
      ctx.fillText(pt,px+pp.x,py+ph-pp.y-1);

      // Terpene BP lines + labels
      terps.forEach(function(t){{
        var yp=ys.getPixelForValue(t.y);
        if(yp<ca.top||yp>ca.bottom)return;
        ctx.strokeStyle="#4A7D9A";
        ctx.lineWidth=1;ctx.setLineDash([4,4]);
        ctx.beginPath();ctx.moveTo(ca.left,yp);ctx.lineTo(ca.right-110,yp);ctx.stroke();
        ctx.setLineDash([]);
        ctx.font="400 11px "+mono;
        ctx.fillStyle="#555555";
        ctx.fillText(t.l+" "+t.y+"°F",ca.right-108,yp+4);
      }});

      ctx.restore();
    }}}}]
  }});
}})();
</script>'''
    return html

# ── SECTIONS ─────────────────────────────────────────────────────────────────

def terpene_reference_html():
    BAND_LABELS = {
        "Low":  "Low — below 356°F / 180°C",
        "Mid":  "Mid — 356–446°F / 180–230°C",
        "High": "High — above 446°F / 230°C",
    }
    rows = ""
    current_band = None
    for t in TERPENE_REFERENCE:
        if t.band != current_band:
            current_band = t.band
            rows += f'<tr class="band-row"><td colspan="6">{BAND_LABELS.get(t.band, t.band)}</td></tr>'
        rows += (
            f'<tr>'
            f'<td><strong>{t.name}</strong><span class="terp-alias">{t.alias}</span></td>'
            f'<td class="bp-cell">{t.bp_f}°F / {t.bp_c}°C</td>'
            f'<td><span class="band-badge band-{t.band.lower()}">{t.band}</span></td>'
            f'<td>{t.aroma}</td>'
            f'<td>{t.qualities}</td>'
            f'<td style="font-size:0.78rem;color:var(--grey-text);">{t.found_in}</td>'
            f'</tr>'
        )
    table = (
        '<div class="terp-ref-wrap">'
        '<table class="terp-ref-table"><thead><tr>'
        '<th>Terpene</th><th>Boiling Point</th><th>Band</th><th>Aroma / Flavor</th><th>Reported Qualities</th><th>Found In</th>'
        f'</tr></thead><tbody>{rows}</tbody></table></div>'
    )
    note = '<p class="note">Boiling points are approximate. Volatility band is a persistence heuristic — lower band evaporates earlier. Terpenes are not psychoactive in the THC sense; qualities reflect common descriptive associations, not medical claims. Sources: <a href="https://theamazingflower.com/pages/terpenes" target="_blank" rel="noopener">The Amazing Flower</a>; <a href="https://finestlabs.com/terpene-boiling-points/" target="_blank" rel="noopener">Finest Labs</a>; <a href="https://thepressclub.co/blogs/tips-tricks/boiling-points-of-common-terpenes-in-cannabis" target="_blank" rel="noopener">The Press Club</a>.</p>'
    content = note + table
    return collapsible_section("terpene-ref", "Terpene Reference", content, header_class="grey")


def build_html():
    validate()
    validate_accent_colors()
    _ac = _ACCENT_RESOLVED

    # sessions_prior lookup keyed by (strain, 1-indexed run number)
    _cnt = {}
    _spr = {}
    for _run in COMPLETED_RUNS:
        _cnt[_run.strain] = _cnt.get(_run.strain, 0) + 1
        _spr[(_run.strain, _cnt[_run.strain])] = _run.sessions_prior_today

    sections = []

    dash = dashboard_html()

    # ── Reference sections (collapsible) ──────────────────────────────────────

    # Device & Session Constants
    c  = '<p class="note">These parameters apply to every session in this log unless explicitly noted otherwise.</p>'
    c += info_table(GLOBAL_INFO)
    c += '<p class="note">IR reads titanium, not insert surface.</p>'
    sections.append(collapsible_section("constants", "Device &amp; Session Constants", c, header_class="grey"))

    # Swab Color Reference
    c  = '<p class="note">Swab color is a qualitative directional signal within a strain. Do not compare across strains — starting material color, oxidation state, and terpene-to-cannabinoid ratio all affect residue color independently of temperature.</p>'
    c += '''<table class="swab-table">
        <tr><td class="swab-key target">Target</td><td>Light golden / amber, slightly fluid. Clean vaporization, no significant degradation.</td></tr>
        <tr><td class="swab-key hot">Too hot</td><td>Amber shading toward brown. Possible degradation at session tail, or darker starting material. Reduce endpoint cautiously.</td></tr>
        <tr><td class="swab-key severe">Too hot (severe)</td><td>Dark brown or black. Likely overheated. Reduce setpoint significantly.</td></tr>
        <tr><td class="swab-key cool">Too cool</td><td>Cloudy or white crystalline residue. Possibly THCA not fully vaporizing — interpretation uncertain. Raise setpoint cautiously.</td></tr>
    </table>'''
    sections.append(collapsible_section("swab", "Swab Color Reference", c, header_class="grey"))

    # Baseline Curve
    c  = '<p class="note">Single starting curve for all hash rosin sessions with cold start technique. Strain profiles document empirical deviations from this baseline via swab results and session observations. Do not design different starting curves based on strain name, inferred terpene profile, consistency, or provenance quality without empirical justification.</p>'
    c += '<h3>Parameters</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Open:</strong> 380°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    c += curve_chart_html(BASELINE_CURVE)
    c += curve_table(BASELINE_CURVE)
    c += '<p class="note">Terpene zone annotations in individual run curves are approximate orientation points — not measured targets. The same common cannabis terpenes appear across most strains. Annotations reflect boiling point ranges, not confirmed strain-specific data.</p>'
    c += '<h3>Rationale</h3>'
    c += '<p>380°F opening reflects the effective starting point used across most strains in the log. 430°F endpoint is where results have converged across multiple strains; all waypoints are starting points, swab results drive adjustment.</p>'
    sections.append(collapsible_section("baseline", "Baseline Curve", c, header_class="grey"))

    # Terpene Reference
    sections.append(terpene_reference_html())

    # ── WW Z ──────────────────────────────────────────────────────────────────

    s  = f'<div class="section" id="wwz-profile">'
    s += accent_header("WW Z — Strain Profile", _ac["WW Z"])
    s += info_table(WWZ_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Pinene inferred dominant — weakly supported by piney nose observation. Standard cannabis palette otherwise. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Rate:</strong> ~0.6°F/sec</p>'
    c += curve_chart_html(WWZ_RUN1)
    c += curve_table(WWZ_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden/amber. Clean. No dark coloration.")
    c += result_row("Vapor:", "Spectacular. Full session expressed well across the arc.")
    c += result_row("Verdict:", "Clean on first run. Baseline curve well-matched to this material.")
    sections.append(collapsible_section("wwz-run1", "WW Z — Run 1 — May 2, 2026", c))

    sections.append(what_to_try_next_html(
        "wwz-next",
        dab_notes="Nothing recorded",
        ai_analysis="One session, clean swab, described as spectacular. No floor signal, no harshness. Nothing to chase — repeat when you want to revisit it.",
        accent=_ac["WW Z"],
    ))

    # ── Caramel Apple Gelato ──────────────────────────────────────────────────

    s  = f'<div class="section" id="cag-profile">'
    s += accent_header("Caramel Apple Gelato — Strain Profile", _ac["Caramel Apple Gelato"])
    s += info_table(CAG_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Limonene and myrcene inferred from Gelato lineage. Muted nose consistent with heavier, less-volatile terpene profile. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3 class="amber">Curve Used</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 450°F</p>'
    c += curve_chart_html(CAG_RUN1)
    c += curve_table(CAG_RUN1, amber=True)
    c += '<h3 class="amber">Results</h3>'
    c += result_row("Swab:", "Amber shading toward light brown.", amber=True)
    c += result_row("Vapor:", "Limited flavor. Session did not express distinct character.", amber=True)
    c += result_row("Diagnosis:", "Endpoint of 450°F likely too aggressive — supported by swab darkening. Limited flavor may reflect endpoint temperature degrading terpene fraction at session tail, or may reflect moderate terpene content in this material independent of temperature. Both explanations are plausible; endpoint reduction will help distinguish them.", amber=True)
    c += result_row("Adjustment:", "Pull endpoint back to 430°F. Shorten hold to 55 seconds to reduce risk of outlasting small load.", amber=True)
    sections.append(collapsible_section("cag-run1", "Caramel Apple Gelato — Run 1 — May 2026", c))

    sections.append(what_to_try_next_html(
        "cag-next",
        dab_notes="Nothing recorded",
        ai_analysis="One data point at 450°F with an amber-toward-brown swab — reliable floor signal. Pull the endpoint back to 430°F. Nothing subtle here, it was just too hot.",
        proposed_waypoints=CAG_RUN2,
        accent=_ac["Caramel Apple Gelato"],
    ))

    # ── Orange Candy ──────────────────────────────────────────────────────────

    s  = f'<div class="section" id="oc-profile">'
    s += accent_header("Orange Candy — Strain Profile", _ac["Orange Candy"])
    s += info_table(OC_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Limonene inferred dominant from orange character (Naran J × Tropimango lineage — unconfirmed). See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3 class="amber">Curve Used</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 450°F</p>'
    c += curve_chart_html(OC_RUNS12)
    c += curve_table(OC_RUNS12, amber=True)
    c += '<h3 class="amber">Observations</h3>'
    c += result_row("Swab:", "Not recorded.", amber=True)
    c += result_row("Result:", "Working well but first 40 seconds felt too flat and slow. Low vapor density in opening phase. Same result on Run 2.", amber=True)
    sections.append(collapsible_section("oc-run1", "Orange Candy — Run 1 — May 2026", c))

    c  = '<h3 class="amber">Curve Used</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 450°F — same as Run 1</p>'
    c += curve_chart_html(OC_RUNS12)
    c += curve_table(OC_RUNS12, amber=True)
    c += '<h3 class="amber">Observations</h3>'
    c += result_row("Swab:", "Not recorded.", amber=True)
    c += result_row("Result:", "Same as Run 1 — opening too flat, low vapor density first 40s.", amber=True)
    c += result_row("Diagnosis:", "Opening too flat — low vapor density in first 40s. Steeper climb 15–35s drives earlier vapor production. Flatter tail 35–65s closes the offset — a slowly-arrived-at 440°F delivers more heat to the material than a steeply-arrived-at 450°F.", amber=True)
    sections.append(collapsible_section("oc-run2", "Orange Candy — Run 2 — May 2026", c))

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    c += curve_chart_html(OC_RUN3)
    c += curve_table(OC_RUN3)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden/tan. Clean. Minimal peripheral darkening at tip edge — consistent with insert wall cooling, not degradation.")
    c += result_row("Session:", "Very nice. Strong effects. Opening draws wispy but flavorful. Good progression through session.")
    c += result_row("Intensity:", "Strong")
    c += result_row("Verdict:", "Clean swab, strong result. Wispy opening draws suggest opportunity to raise opening setpoint slightly to improve vapor density at session start without affecting the clean tail.")
    sections.append(collapsible_section("oc-run3", "Orange Candy — Run 3 — May 2026", c))

    c  = session_order_note(_spr.get(("Orange Candy", 4)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    c += curve_chart_html(OC_RUN4)
    c += curve_table(OC_RUN4)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden. Clean both times.")
    c += result_row("Session:", "Fine. Not noticeably different from Run 3. Run repeated twice on May 5, 2026 — consistent results across both.")
    c += result_row("Verdict:", "Clean swab confirmed. Results stable. Lower opening setpoint (350°F) under exploration for Run 5 as next variable to test.")
    sections.append(collapsible_section("oc-run4", "Orange Candy — Run 4 — May 5, 2026", c))

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Open:</strong> 350°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 460°F</p>'
    c += curve_chart_html(OC_RUN5)
    c += curve_table(OC_RUN5, amber=True)
    c += '<h3 class="amber">Results</h3>'
    c += result_row("Swab:", "Darker than target — direction consistent with endpoint too hot.", amber=True)
    c += result_row("Session:", "Last portion tad harsh, consistent with elevated endpoint. Effect notably stronger than prior runs.", amber=True)
    c += result_row("Observation:", "User's hypothesis: higher temperature produced stronger effect. Logged as stated — one data point, not a confirmed finding. Confounders include session-to-session variability in tolerance, load size, and conditions.", amber=True)
    c += result_row("Next:", "Returned to ramp curve for Run 6 — see results below.", amber=True)
    sections.append(collapsible_section("oc-run5", "Orange Candy — Run 5 — May 6, 2026", c))

    c  = session_order_note(_spr.get(("Orange Candy", 6)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    c += curve_chart_html(OC_RUN6)
    c += curve_table(OC_RUN6)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden. Clean.")
    c += result_row("Session:", "Very nice.")
    c += result_row("Next:", "Repeat to confirm, or test 350°F open / 460°F endpoint curve when ready.")
    sections.append(collapsible_section("oc-run6", "Orange Candy — Run 6 — May 9, 2026", c))

    c  = session_order_note(_spr.get(("Orange Candy", 7)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 60 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    c += curve_chart_html(OC_RUN7)
    c += curve_table(OC_RUN7)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Plain amber — clean.")
    c += result_row("Session:", "Pleasant overall. Not as tasty as the ramp from lower temp. Harsh in the last 20 seconds.")
    c += result_row("Read:", "Swab is clean, so harshness is a session character signal, not a floor indicator. Comparing to Run 6 (ramp to 430°F, light golden, very nice) — the flat hold at the same endpoint produces clearly more harshness and less flavor character. Consistent with the pattern seen on Fembot #3: flat holds at 430°F track hotter in session feel than ramps to the same endpoint, even with a clean swab.")
    c += result_row("Next:", "Ramp curve (Run 6 shape) is outperforming the flat hold at 430°F. Repeat Run 6 ramp to confirm, or try 420°F flat hold to find the flat-hold ceiling.")
    sections.append(collapsible_section("oc-run7", "Orange Candy — Run 7 — May 9, 2026", c))

    sections.append(what_to_try_next_html(
        "oc-next",
        dab_notes="Repeat Run 6 ramp to confirm, or try 420°F flat hold.",
        ai_analysis="Run 6 (ramp to 430°F) vs Run 7 (flat 430°F) on the same day is the cleanest curve-shape comparison in the log. Ramp won clearly on flavor and harshness. Repeat the ramp before adding more variables — confirm it holds before dropping the endpoint.",
        proposed_waypoints=OC_RUN6,
        accent=_ac["Orange Candy"],
    ))

    # ── The Hive #1 ───────────────────────────────────────────────────────────

    s  = f'<div class="section" id="hive1-profile">'
    s += accent_header("The Hive #1 — Strain Profile", _ac["The Hive #1"])
    s += info_table(HIVE1_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Myrcene and terpinolene inferred from tropical fruit character; Honey Banana × Papaya lineage (Bloom Seed Co). Terpene ratios not inferable from genetics — standard palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    c += curve_chart_html(HIVE1_RUN1)
    c += curve_table(HIVE1_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean. No darkening.")
    c += result_row("Session:", "Nice flavors on the way up through the arc. Heavy indica effect.")
    c += result_row("Verdict:", "Clean swab on first run — curve appears well-matched to this material. Repeated as Run 2 to confirm.")
    sections.append(collapsible_section("hive1-run1", "The Hive #1 — Run 1 — May 7, 2026", c))

    c  = session_order_note(_spr.get(("The Hive #1", 2)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F — identical to Run 1</p>'
    c += curve_chart_html(HIVE1_RUN2)
    c += curve_table(HIVE1_RUN2)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Very light — cleaner than Run 1.")
    c += result_row("Session:", "Really nice. Consistent with Run 1.")
    c += result_row("Verdict:", "Two clean runs, consistent character, swab lighter on repeat. 440°F endpoint may be higher than needed — material is fully expressing before the endpoint. Run 3: trying steady 430°F flat hold (no ramp) to test whether curve shape affects the result.")
    sections.append(collapsible_section("hive1-run2", "The Hive #1 — Run 2 — May 7, 2026", c))

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 45 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    c += '<p class="note">Curve shape experiment: steady flat hold at 430°F from session open, rather than the ramped curve used in Runs 1–2. Testing whether a multi-stage ramp produces meaningfully different results from a single sustained setpoint. Swab is a floor indicator only — session character is the primary readout.</p>'
    c += curve_chart_html(HIVE1_RUN3)
    c += curve_table(HIVE1_RUN3)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean.")
    c += result_row("Session:", "First half: lots of flavor, low throat irritation. Second half: irritation increased, flavor faded to generic dab vapor — never harsh or burnt, just less distinct. Effect notably strong.")
    c += result_row("Read:", "At a flat 430°F from the open, all terpene fractions (pinene through linalool, all below 430°F) are available simultaneously — first hit may be the full palette combining at once rather than staged. The ramp climbs through each fraction sequentially, which may be what gives those runs more distinct flavor progression across the arc. 45 seconds was too short — vapor was still producing at session end. Not a temperature issue, just cut off early.")
    c += result_row("Verdict:", "One data point. Directionally supports the ramp producing more distinct staged flavor vs. the flat hold combining everything at once. If revisiting the flat hold, extend to 60 seconds. Next planned: repeat the Run 1–2 ramp (380→390→410°F) with 430°F endpoint to compare directly on the same endpoint.")
    sections.append(collapsible_section("hive1-run3", "The Hive #1 — Run 3 — May 8, 2026", c))

    c  = session_order_note(_spr.get(("The Hive #1", 4)))
    c += '<h3>Curve</h3>'
    c += "<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 60 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp) — extended from Run 3's 45s</p>"
    c += curve_chart_html(HIVE1_RUN4)
    c += curve_table(HIVE1_RUN4)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean. Consistent with Run 3.")
    c += result_row("Session:", "Similar to Run 3. Extended hold confirmed vapor was still producing at 45s in Run 3 — 60s felt more complete.")
    c += result_row("Verdict:", "Two flat-hold data points, both clean swabs, consistent character. Next: ramp to 430°F endpoint (380→390→410→430°F) — the original planned experiment — to compare curve shape on the same endpoint.")
    sections.append(collapsible_section("hive1-run4", "The Hive #1 — Run 4 — May 8, 2026", c))

    c  = session_order_note(_spr.get(("The Hive #1", 5)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F (ramp — same shape as Runs 1–2, endpoint reduced from 440°F)</p>'
    c += curve_chart_html(HIVE1_RUN5)
    c += curve_table(HIVE1_RUN5)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — a tad lighter than the flat-hold 430°F runs (Runs 3–4). Clean.")
    c += result_row("Session:", "Nice distinct flavors through the first two-thirds. Harsh in the last ~10 seconds. Effects quite potent.")
    c += result_row("Read:", "Distinct staged flavor character is consistent with the ramp — each terpene fraction vaporizes as the curve climbs through it, rather than all at once as in the flat hold. Swab difference vs. Runs 3–4 is within noise (too many uncontrolled variables). Harshness at session tail is a directional signal that 430°F may still be slightly above ideal for this material on the ramp.")
    c += result_row("Next:", "Try 420–425°F endpoint on Run 6. Keep ramp shape unchanged.")
    sections.append(collapsible_section("hive1-run5", "The Hive #1 — Run 5 — May 8, 2026", c))

    sections.append(what_to_try_next_html(
        "hive1-next",
        dab_notes="Try 420–425°F endpoint, keep ramp shape.",
        ai_analysis="Flat-hold 430°F was clean twice. Ramp to 430°F showed tail harshness once. Harshness is directional but one data point — the flat holds didn't show it at the same endpoint. 425°F ramp is a reasonable conservative step; could also repeat the ramp at 430°F first to confirm the harshness was real.",
        proposed_waypoints=HIVE1_NEXT,
        accent=_ac["The Hive #1"],
    ))

    # ── Fembot #3 ─────────────────────────────────────────────────────────────

    s  = f'<div class="section" id="fembot3-profile">'
    s += accent_header("Fembot #3 — Strain Profile", _ac["Fembot #3"])
    s += info_table(FEMBOT3_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Terpinolene inferred likely dominant from Fuzzy Melon character; Fuzzy Melon × Rambutan lineage. Standard cannabis palette otherwise — not measured. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    c += curve_chart_html(FEMBOT3_RUN1)
    c += curve_table(FEMBOT3_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean. Two heads mostly white, two with light golden coloring. No darkening.")
    c += result_row("Session:", "Very tasty on the ascent. No visible vapor until mid-range. Slight harshness at the tail. Effects upbeat, creative, not too body-heavy — consistent with sativa-dominant character.")
    c += result_row("Next:", "Try steady 420°F flat hold (60s) on Run 2 — drop endpoint and change curve shape to test both variables.")
    sections.append(collapsible_section("fembot3-run1", "Fembot #3 — Run 1 — May 9, 2026", c))

    c  = session_order_note(_spr.get(("Fembot #3", 2)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 60 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    c += curve_chart_html(FEMBOT3_RUN2)
    c += curve_table(FEMBOT3_RUN2)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean. Consistent with Run 1.")
    c += result_row("Session:", "Very tasty, great effects. Harshness in the last third.")
    c += result_row("Read:", "Harshness at the tail is consistent with Run 1 (ramp to 430°F endpoint) — two data points now pointing at 430°F as slightly above ideal for this material, regardless of curve shape. Swab is clean, so this is a session character signal rather than a floor indicator.")
    c += result_row("Next:", "Try 420°F steady flat hold on Run 3.")
    sections.append(collapsible_section("fembot3-run2", "Fembot #3 — Run 2 — May 9, 2026", c))

    sections.append(what_to_try_next_html(
        "fembot3-next",
        dab_notes="Nothing recorded",
        ai_analysis="Strongest signal in the log — harshness at 430°F on both a ramp and a flat hold. Two shapes, same outcome. 430°F is above ideal for this material. 420°F flat hold is the clear next test.",
        proposed_waypoints=FEMBOT3_RUN3,
        accent=_ac["Fembot #3"],
    ))

    # ── Mango Starburst #23 ───────────────────────────────────────────────────

    s  = f'<div class="section" id="ms23-profile">'
    s += accent_header("Mango Starburst #23 — Strain Profile", _ac["Mango Starburst #23"])
    s += info_table(MS23_INFO)
    s += "<p class=\"note\"><strong>Terpene inference:</strong> Limonene and terpinolene weighted from SB36 line's citrus-candy character; pronounced pine on Run 1 suggests pinene may be more prominent than inferred. Not measured. See <a href=\"#terpene-ref\">Terpene Reference</a>.</p>"
    s += '</div>'
    sections.append(s)

    c  = session_order_note(_spr.get(("Mango Starburst #23", 1)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    c += curve_chart_html(MS23_RUN1)
    c += curve_table(MS23_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Very clean — no darkening.")
    c += result_row("Session:", "Very piney character throughout — almost pine sol. Tasty, though not to user's taste preference. Heady effects. No harshness.")
    c += result_row("Note:", "Strong pine-forward character noted on first run. The SB36 lineage inference weighted limonene and terpinolene as prominent — the pronounced pine character is consistent with pinene playing a larger role than the inference anticipated. Logged as one data point; flavor character is a weak signal and single-session observations carry high uncertainty.")
    c += result_row("Verdict:", "Clean swab on first run. Curve well-matched to this material. Repeat on Run 2 to confirm.")
    sections.append(collapsible_section("ms23-run1", "Mango Starburst #23 — Run 1 — May 9, 2026", c))

    sections.append(what_to_try_next_html(
        "ms23-next",
        dab_notes="Nothing recorded",
        ai_analysis="One run, clean swab, no harshness. Pine-forward character was noted but single-session flavor observations are noisy. Repeat the same curve before changing anything — if it's pine again on Run 2, that's real.",
        proposed_waypoints=MS23_RUN1,
        accent=_ac["Mango Starburst #23"],
    ))

    # ── Maple Bacon Donut ─────────────────────────────────────────────────────

    s  = f'<div class="section" id="mbd-profile">'
    s += accent_header("Maple Bacon Donut — Strain Profile", _ac["Maple Bacon Donut"])
    s += info_table(MBD_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    c += curve_chart_html(MBD_RUN1)
    c += curve_table(MBD_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Darker golden — between light golden target and amber. Nothing tasted burnt. Flagged as something to watch on subsequent runs.")
    c += result_row("Session:", "Tasty first half, second half faded to generic. Milder effect — likely tolerance after 5 sessions the prior day.")
    c += result_row("Intensity:", "Mild — tolerance confound (5 sessions prior day)")
    sections.append(collapsible_section("mbd-run1", "Maple Bacon Donut — Run 1 — May 10, 2026", c))

    c  = session_order_note(_spr.get(("Maple Bacon Donut", 2)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F — same as Run 1</p>'
    c += curve_chart_html(MBD_RUN2)
    c += curve_table(MBD_RUN2)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Lighter than Run 1 — closer to the light golden target.")
    c += result_row("Session:", "Distinct bacon character on the first half. Effects came on noticeably after this session.")
    c += result_row("Intensity:", "Moderate")
    c += result_row("Read:", "Swab trending cleaner on repeat. Flavor expressed distinctly on the first half. No harshness on either run. The Run 1 milder effect reads as a tolerance confound — effects landed clearly on Run 2.")
    sections.append(collapsible_section("mbd-run2", "Maple Bacon Donut — Run 2 — May 10, 2026", c))

    c  = session_order_note(_spr.get(("Maple Bacon Donut", 3)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F, ramp from 375°F open</p>'
    c += curve_chart_html(MBD_RUN3)
    c += curve_table(MBD_RUN3)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Clean golden.")
    c += result_row("Session:", "Little bit harsh in the last 5 seconds. No harshness earlier in the session.")
    c += result_row("Intensity:", "Medium-hard")
    sections.append(collapsible_section("mbd-run3", "Maple Bacon Donut — Run 3 — May 11, 2026", c))

    c  = session_order_note(_spr.get(("Maple Bacon Donut", 4)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F — same as Runs 1 and 2</p>'
    c += curve_chart_html(MBD_RUN4)
    c += curve_table(MBD_RUN4)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden.")
    c += result_row("Session:", "Tail harshness again, consistent with prior 430°F runs. Interesting bitter note throughout — citrus rind character.")
    c += result_row("Intensity:", "Big effect, seemingly short duration.")
    sections.append(collapsible_section("mbd-run4", "Maple Bacon Donut — Run 4 — May 12, 2026", c))

    sections.append(what_to_try_next_html(
        "mbd-next",
        dab_notes="Run 4 back to 430°F: light golden swab, tail harshness consistent with prior 430°F pattern, interesting bitter/citrus rind note throughout, big effect, seemingly short duration.",
        ai_analysis="Tail harshness at 430°F is consistent across runs. Run 5 moves in a different direction — faster ramp to 460°F — rather than continuing to work the lower end. That's an exploratory step; the session character at 460°F is unknown for MBD. The citrus rind note is worth watching on Run 5 to see whether it changes with the faster climb. The short duration observation from Run 4 is a single data point, unclear if it means anything. Swab has been clean throughout, so the harshness is coming from endpoint temperature, not material condition.",
        proposed_waypoints=MBD_NEXT,
        accent=_ac["Maple Bacon Donut"],
    ))

    # ── Rain Fruit ────────────────────────────────────────────────────────────

    s  = f'<div class="section" id="rainfruit-profile">'
    s += accent_header("Rain Fruit — Strain Profile", _ac["Rain Fruit"])
    s += info_table(RF_INFO)
    s += '<p class="note"><strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.</p>'
    s += '</div>'
    sections.append(s)

    c  = session_order_note(_spr.get(("Rain Fruit", 1)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F — baseline ramp</p>'
    c += curve_chart_html(RF_RUN1)
    c += curve_table(RF_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Notably clean — lighter than target. No darkening.")
    c += result_row("Session:", "Really clear fruit notes throughout. Strong effects — pressure up and behind the eyes. No harshness.")
    c += result_row("Intensity:", "Strong")
    c += result_row("Verdict:", "Clean first run. Distinct fruit character, strong effect. No floor signal, no harshness. Repeat the same curve on Run 2 to confirm.")
    sections.append(collapsible_section("rainfruit-run1", "Rain Fruit — Run 1 — May 10, 2026", c))

    c  = session_order_note(_spr.get(("Rain Fruit", 2)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F &nbsp;|&nbsp; Open 5°F below baseline — testing lower open</p>'
    c += curve_chart_html(RF_RUN2)
    c += curve_table(RF_RUN2)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — clean.")
    c += result_row("Session:", "Tasty. Got a bit hot in the last 10 seconds.")
    c += result_row("Intensity:", "Mild")
    c += result_row("Read:", "Curve felt well-suited to the strain overall. Tail heat in the last 10 seconds is consistent with the cross-strain pattern at 430°F endpoints (Hive #1 Run 5, Fembot #3 Runs 1–2). Swab is clean so this is a session character signal, not a floor indicator. Effects milder than Run 1 — likely session-to-session variability rather than a curve signal.")
    sections.append(collapsible_section("rainfruit-run2", "Rain Fruit — Run 2 — May 11, 2026", c))

    c  = session_order_note(_spr.get(("Rain Fruit", 3)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F from prior runs</p>'
    c += curve_chart_html(RF_RUN3)
    c += curve_table(RF_RUN3)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Clean golden.")
    c += result_row("Session:", "Notably less harshness. Slow build to intensity — not hard hitting.")
    c += result_row("Intensity:", "Mild-moderate")
    c += result_row("Read:", "420°F endpoint resolved the tail harshness that appeared at 430°F on Run 2 — consistent with the cross-strain pattern. Clean swab means no floor signal. The slower, gentler build suggests some intensity lives in the higher-temperature band. The path forward is to walk the endpoint back up incrementally to find where harshness re-enters.")
    sections.append(collapsible_section("rainfruit-run3", "Rain Fruit — Run 3 — May 11, 2026", c))

    sections.append(what_to_try_next_html(
        "rainfruit-next",
        dab_notes="420 hold worked — notably less harshness, clean golden swabs. Not hard hitting but slow build to intensity. Want to slowly walk up the curve.",
        ai_analysis="The 420°F endpoint confirmed the hypothesis: dropping 10°F from the 430°F runs eliminated tail harshness without producing a floor signal. The trade-off is real — effects were milder and slower-building, suggesting the higher-temperature band contributes to intensity. Next step is to probe incrementally upward: try 423°F endpoint (same ramp shape, +3°F) to begin finding where harshness re-enters. Small steps keep the signal clean — each run is one data point on the harshness-intensity curve.",
        proposed_waypoints=RF_RUN4_NEXT,
        accent=_ac["Rain Fruit"],
    ))

    # ── Mango Banana #9 + Z + Sour Tangie ────────────────────────────────────
    s = f'<div class="section" id="mb9zst-profile">'
    s += accent_header("Mango Banana #9 + Z + Sour Tangie — Strain Profile", _ac["Mango Banana #9 + Z + Sour Tangie"])
    s += info_table(MB9ZST_INFO)
    s += '<h3>Terpene Profile — Inferred</h3>'
    s += '<p class="note">Terpene profile inferred from component strain genetics — not measured. This is the generic cannabis palette. Neapolitan format adds a further caveat: each layer may have a different terpene balance, and the session will vary depending on which portion is loaded.</p>'
    s += terpene_table(MB9ZST_TERPS)
    s += '</div>'
    sections.append(s)

    c  = session_order_note(_spr.get(("Mango Banana #9 + Z + Sour Tangie", 1)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F — baseline ramp &nbsp;|&nbsp; <strong>Equipment:</strong> First session with Gemlock joystick, no pearl</p>'
    c += curve_chart_html(MB9ZST_RUN1)
    c += curve_table(MB9ZST_RUN1)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Very light golden.")
    c += result_row("Session:", "Pronounced flavors up front. Bitter citrus note with a distinct tangerine quality — consistent with Sour Tangie lineage (limonene-forward). Slight harshness at the end. Also appeared as a bitter/citrus rind note in Maple Bacon Donut Run 4 (May 12) — cross-strain parallel, genetics connection unclear, worth watching.")
    c += result_row("Intensity:", "Strong — face tingling.")
    c += result_row("Equipment note:", "First run with Gemlock joystick, no pearl. Swab lighter than typical for a first run. Hypothesis: joystick may be more efficient — cleaner swab and/or more material vaporized in the same window. Single data point; something to watch.")
    sections.append(collapsible_section("mb9zst-run1", "Mango Banana #9 + Z + Sour Tangie — Run 1 — May 13, 2026", c))

    c  = session_order_note(_spr.get(("Mango Banana #9 + Z + Sour Tangie", 2)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F — baseline ramp repeated</p>'
    c += curve_chart_html(MB9ZST_RUN2)
    c += curve_table(MB9ZST_RUN2)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", "Light golden — same as Run 1.")
    c += result_row("Session:", "Big flavors up front. Visible vapor at lower temps than expected. Slight harshness at the end.")
    c += result_row("Intensity:", "Strong — not too cloudy mentally, noticeably lazy physically.")
    sections.append(collapsible_section("mb9zst-run2", "Mango Banana #9 + Z + Sour Tangie — Run 2 — May 13, 2026", c))

    c  = session_order_note(_spr.get(("Mango Banana #9 + Z + Sour Tangie", 3)))
    c += '<h3>Curve</h3>'
    c += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 420°F with 20-second hold — ramp 375→400→420°F</p>'
    c += curve_chart_html(MB9ZST_RUN3)
    c += curve_table(MB9ZST_RUN3)
    c += '<h3>Results</h3>'
    c += result_row("Swab:", 'Light golden — "lightly toasted marshmallow." Clean.')
    c += result_row("Session:", "Nice. Climb rate felt right, hold felt right. Still a bit harsh at the end.")
    c += result_row("Intensity:", "High")
    sections.append(collapsible_section("mb9zst-run3", "Mango Banana #9 + Z + Sour Tangie — Run 3 — May 14, 2026", c))

    sections.append(what_to_try_next_html(
        "mb9zst-next",
        dab_notes='Run 3 at 420°F endpoint (375→400→420, 20s hold): light golden swab — "lightly toasted marshmallow." Nice. Climb rate felt right, hold felt right. Still a bit harsh at the end. High intensity. Want sapphire soon.',
        ai_analysis="Tail harshness is persisting below 430°F — this run at 420°F still showed it. That's different from Rain Fruit, which resolved cleanly at 420°F. Two possible reads: (1) this material just wants a lower ceiling, or (2) the steeper approach on Run 3 is moving through the end zone faster than the baseline ramp, reading as hotter at the tail even at the same endpoint. Climb rate and hold both felt right, so the shape is working — a 5°F drop to 415°F is the cleanest next step. Worth watching: Rain Fruit showed milder, slower-building effects when dropped to 420°F. If 415°F tracks the same way here, that's a real trade-off to weigh — not just a harshness dial.",
        proposed_waypoints=MB9ZST_NEXT,
        accent=_ac["Mango Banana #9 + Z + Sour Tangie"],
    ))

    # ── Assemble ──────────────────────────────────────────────────────────────
    body = dash + ''.join(sections)
    body += f'<div class="footer">Document last updated: {datetime.now().strftime("%B %d, %Y")} &nbsp;·&nbsp; Dabby the House Rig &nbsp;·&nbsp; Hash Rosin — Solventless — Cold Start Protocol</div>'

    cover = '''<div class="cover">
        <h1>Dabby the House Rig</h1>
        <p class="subtitle">Session Log</p>
        <p class="tagline">Hash Rosin &nbsp;·&nbsp; Solventless &nbsp;·&nbsp; Cold Start Protocol</p>
    </div>'''

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dabby the House Rig — Session Log</title>
<style>{CSS}</style>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
</head>
<body>
<div class="doc">
{cover}
{body}
</div>
</body>
</html>"""

    return html

# ── WRITE ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    html = build_html()
    out = "index.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {out}")
