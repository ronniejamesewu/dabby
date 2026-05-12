#!/usr/bin/env python3
from datetime import datetime, date, timezone
"""
Dabby the House Rig — Session Log Generator
Produces index.html — a mobile-responsive, screen-optimized web document.
To update: edit DATA and SECTIONS sections, then run with python3.
"""

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
    for time, temp, note in rows:
        html += f'<tr><td>{time}</td><td>{temp}</td><td>{note}</td></tr>'
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
    for strain, run_date, sessions_prior, utc_logged_at, wps in COMPLETED_RUNS:
        pts = [(int(t.replace('s', '')), float(v.replace('°F', ''))) for t, v, _ in wps]
        opens.append(pts[0][1])
        endpoints.append(pts[-1][1])
        run_counts[strain] = run_counts.get(strain, 0) + 1
        if run_date is not None:
            date_counts[run_date] = date_counts.get(run_date, 0) + 1
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
    for strain, run_date, sessions_prior, utc_logged_at, wps in COMPLETED_RUNS:
        if run_date is not None:
            if strain not in last_dates or run_date > last_dates[strain]:
                last_dates[strain] = run_date

    sorted_strains = sorted(
        [(s, a, nt, ac, slug) for s, a, nt, ac, slug in STRAIN_STATUS if run_counts.get(s, 0) > 0],
        key=lambda x: run_counts[x[0]], reverse=True
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

    max_runs = run_counts[sorted_strains[0][0]] if sorted_strains else 0
    rows = ''
    for i, (strain, anchor, nt, accent, slug) in enumerate(sorted_strains):
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
            f'<span class="strain-next">{nt}</span>'
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
    """
    waypoints: list of (time_str, temp_str, note_str)
    e.g. [("0s","375°F","Session open"), ("65s","440°F","Endpoint")]
    Returns HTML string with canvas + inline script.
    """
    _chart_counter[0] += 1
    cid = chart_id or f"curve_{_chart_counter[0]}"

    # Parse waypoints into JS arrays
    pts = []
    for time_str, temp_str, _ in waypoints:
        t = int(time_str.replace('s',''))
        temp = float(temp_str.replace('°F','').replace('°f',''))
        pts.append(f"{{x:{t},y:{temp}}}")
    pts_js = '[' + ','.join(pts) + ']'

    # Determine y axis range
    all_temps = [float(w[1].replace('°F','')) for w in waypoints]
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
<canvas id="{cid}" role="img" aria-label="Temperature curve chart">Curve from {waypoints[0][1]} at {waypoints[0][0]} to {waypoints[-1][1]} at {waypoints[-1][0]}.</canvas>
</div>
</div>
<script>
(function(){{
  var mono="{mono}";
  var terps=[{{y:311,l:"Pinene"}},{{y:334,l:"Myrcene"}},{{y:349,l:"Limonene"}},{{y:367,l:"Terpinolene"}},{{y:388,l:"Linalool"}}];
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
        x:{{type:"linear",min:0,max:{waypoints[-1][0].replace('s','')},
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

# ── DATA ────────────────────────────────────────────────────────────────────

GLOBAL_INFO = [
    ("Device",       "Switch² (Dabby the House Rig)"),
    ("All Material", "Hash Rosin — ice water extracted, solventless. Consistency varies by jar — noted in each strain profile."),
    ("Insert",       "20mm (quartz current; sapphire profiles to be added when acquired)"),
    ("Technique",    "Cold start — pre-load into cold insert before every session"),
    ("Load Size",    "Rice grain (small)"),
    ("Offset Est.",  "Probably small under most operating conditions. Dominant uncertainties are vaporization cooling and dynamic lag during steep ascent. At flat or slowly-ascending phases the system approaches equilibrium. Setpoints are reasonable proxies for material contact temperature."),
    ("Draw Style",   "Long, slow draws throughout session"),
    ("Terp Tools",   "Cloud Vortex auto spinner cap + 6mm quartz pearl in insert — present in all sessions to date"),
    ("Session End",  "Stop when vapor production drops — do not ride timer on small loads"),
]

BASELINE_CURVE = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]

WWZ_INFO = [
    ("Strain",      "WW Z (White Widow × Zkittlez lineage — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Piney with sweet undertone (weak secondary signal only)"),
]
WWZ_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — minor, inferred"),
    ("Alpha-Pinene",  "311°F / 155°C", "Pine — inferred dominant; weakly supported by nose observation"),
    ("Myrcene",       "334°F / 168°C", "Earthy, sweet — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, floral — inferred (Z lineage)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
]
WWZ_RUN1 = [
    ("0s",  "375°F", "Session open"),
    ("15s", "378°F", "Extended flat — low-boiling terpene zone (~311°F pinene region)"),
    ("40s", "395°F", "Mid ascent — mid-range terpene zone (~334°F myrcene region)"),
    ("65s", "440°F", "Endpoint — upper terpene zone + THC completion"),
]

CAG_INFO = [
    ("Strain",      "Caramel Apple Gelato (Gelato lineage: Sunset Sherbet × Thin Mint GSC — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Muted — no distinct notes (weak secondary signal, consistent with heavier terpene profile)"),
]
CAG_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred, low room-temp volatility explains muted nose"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred from Gelato lineage"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
]
CAG_RUN1 = [
    ("0s",  "375°F", "Session open"),
    ("10s", "380°F", "Short flat phase"),
    ("30s", "395°F", "Mid ascent"),
    ("50s", "420°F", "Upper terpene zone"),
    ("65s", "450°F", "ENDPOINT TOO HOT — see diagnosis"),
]
CAG_RUN2 = [
    ("0s",  "375°F", "Session open"),
    ("10s", "380°F", "Short flat phase"),
    ("30s", "395°F", "Mid ascent"),
    ("50s", "415°F", "Upper terpene zone"),
    ("55s", "430°F", "Conservative endpoint"),
]

OC_INFO = [
    ("Strain",      "Orange Candy (Philosopher Seeds lineage: Naran J × Tropimango — unconfirmed)"),
    ("Producer",    "Nikka T"),
    ("Input",       "90 micron full melt bubble hash"),
    ("Consistency", "Cold cure"),
    ("Nose",        "Not yet recorded"),
]
OC_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred, low room-temp volatility"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred dominant, orange character"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred secondary"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
]
OC_RUNS12 = [
    ("0s",  "375°F", "Session open"),
    ("15s", "378°F", "Flat phase"),
    ("40s", "395°F", "Mid ascent"),
    ("65s", "450°F", "Endpoint — raised to compensate for estimated thermal offset"),
]
OC_RUN3 = [
    ("0s",  "375°F", "Session open"),
    ("15s", "378°F", "Flat phase"),
    ("35s", "410°F", "Steeper climb — faster progression through mid terpene zones"),
    ("65s", "440°F", "Endpoint — reduced; flatter tail allows insert surface to approach equilibrium"),
]
OC_RUN4 = [
    ("0s",  "380°F", "Session open — raised 5°F to increase opening vapor density"),
    ("15s", "390°F", "Halfway between open and mid waypoint"),
    ("35s", "410°F", "Halfway between open and endpoint"),
    ("65s", "440°F", "Endpoint — unchanged"),
]
OC_RUN5 = [
    ("0s",  "350°F", "Session open — lower opening setpoint under exploration"),
    ("30s", "410°F", "Mid ascent"),
    ("50s", "440°F", "Upper zone"),
    ("65s", "460°F", "Endpoint"),
]
OC_RUN6 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("35s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint — down 10°F from Runs 3–4"),
]
OC_RUN7 = [
    ("0s",  "430°F", "Steady hold — flat 430°F from session open"),
    ("60s", "430°F", "Endpoint"),
]

HIVE1_INFO = [
    ("Strain",      "The Hive #1 (Honey Banana × Papaya — Bloom Seed Co)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Myxed Up (washed and pressed)"),
    ("Input",       "159–73 micron ice water hash"),
    ("Nose",        "Very fragrant at cold nose. Spice noticeable (consistent with caryophyllene — weak secondary signal only)."),
]

HIVE1_RUN1 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("35s", "410°F", "Mid ascent"),
    ("65s", "440°F", "Endpoint"),
]
HIVE1_RUN2 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("35s", "410°F", "Mid ascent"),
    ("65s", "440°F", "Endpoint — repeated from Run 1"),
]
HIVE1_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred secondary (both parents)"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred dominant (both parents' fruit character)"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred (tropical fruit character consistent with lineage)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, floral — inferred (Papaya lineage)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
]
HIVE1_RUN3 = [
    ("0s",  "430°F", "Steady hold — flat 430°F from session open"),
    ("45s", "430°F", "Endpoint"),
]
HIVE1_RUN4 = [
    ("0s",  "430°F", "Steady hold — flat 430°F from session open"),
    ("60s", "430°F", "Endpoint — extended from Run 3's 45s"),
]
HIVE1_RUN5 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("35s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint — 430°F with ramp (down from 440°F in Runs 1–2)"),
]

FEMBOT3_INFO = [
    ("Strain",      "Fembot #3 (Fuzzy Melon × Rambutan — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Riptide (CO)"),
    ("Input",       "169–73 micron ice water hash"),
    ("Character",   "Sativa-dominant — uplifting, energetic character inferred from lineage. Phenotype and wash quality drive actual experience."),
    ("Nose",        "Subtle garlic note at cold nose; strong overall fragrance, less distinct individual character"),
]

FEMBOT3_RUN1 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
FEMBOT3_RUN2 = [
    ("0s",  "430°F", "Steady hold — flat 430°F from session open"),
    ("60s", "430°F", "Endpoint"),
]
FEMBOT3_RUN3 = [
    ("0s",  "420°F", "Steady hold — flat 420°F from session open"),
    ("60s", "420°F", "Endpoint"),
]
HIVE1_NEXT = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("35s", "410°F", "Mid ascent"),
    ("65s", "425°F", "Endpoint — down 5°F from Run 5"),
]

FEMBOT3_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred secondary"),
    ("Limonene",      "349°F / 176°C", "Citrus-candy — inferred, consistent with melon/tropical lineage"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, fruity, floral — inferred likely dominant (Fuzzy Melon character)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]

MS23_INFO = [
    ("Strain",        "Mango Starburst #23 (Starburst 36 #217 × Starburst 36 #1)"),
    ("Consistency",   "Cold cure"),
    ("Producer",      "Terps Over Yields (CO)"),
    ("Jar",           "14 of 23"),
    ("Base genetics", "SB36 line — Starburst OG × '97 KC36"),
    ("Character",     "Sativa-dominant — upbeat, euphoric, flavor-forward character inferred from SB36 lineage. KC36 influence leans energetic rather than sedating. Phenotype and wash quality drive actual experience."),
    ("Nose",          "Diesel note pronounced at cold nose; sweetness underneath"),
]
MS23_RUN1 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
MS23_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred secondary"),
    ("Limonene",      "349°F / 176°C", "Citrus, orange peel — inferred likely dominant (SB36 tangie-like front end)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, candy-tropical — inferred prominent (SB36 candy-forward character)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]

MBD_INFO = [
    ("Strain",      "Maple Bacon Donut"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Micron",      "Not recorded"),
    ("Nose",        "Not yet recorded"),
]
MBD_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]
MBD_RUN1 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
MBD_RUN2 = [
    ("0s",  "380°F", "Session open — same curve as Run 1"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
MBD_NEXT = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]

RF_INFO = [
    ("Strain",      "Rain Fruit"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Micron",      "Not recorded"),
    ("Nose",        "Not yet recorded"),
]
RF_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]
RF_RUN1 = [
    ("0s",  "380°F", "Session open"),
    ("15s", "390°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
RF_RUN2 = [
    ("0s",  "375°F", "Session open — 5°F below baseline, testing lower open"),
    ("15s", "385°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("65s", "430°F", "Endpoint"),
]
RF_RUN3 = [
    ("0s",  "375°F", "Session open"),
    ("15s", "385°F", "Early ascent"),
    ("40s", "410°F", "Mid ascent"),
    ("55s", "420°F", "Approach endpoint — down 10°F"),
    ("65s", "420°F", "Hold at 420°F for 10 seconds"),
]
RF_RUN4_NEXT = [
    ("0s",  "375°F", "Session open"),
    ("15s", "385°F", "Early ascent"),
    ("40s", "412°F", "Mid ascent — up 2°F"),
    ("55s", "422°F", "Approach endpoint — up 2°F"),
    ("65s", "423°F", "Endpoint — up 3°F from Run 3"),
]

# ── DASHBOARD DATA ────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)

COMPLETED_RUNS = [
    # (strain, date, sessions_prior_today, utc_logged_at, waypoints)
    # sessions_prior_today: int = sessions run before this one on the same day; None if unknown
    # utc_logged_at: datetime (UTC) when the run was logged; None for entries predating this field
    ("WW Z",                 date(2026, 5, 2),  0,    None, WWZ_RUN1),
    ("Caramel Apple Gelato", None,              None, None, CAG_RUN1),
    ("Orange Candy",         None,              None, None, OC_RUNS12),
    ("Orange Candy",         None,              None, None, OC_RUNS12),
    ("Orange Candy",         None,              None, None, OC_RUN3),
    ("Orange Candy",         date(2026, 5, 5),  1,    None, OC_RUN4),
    ("Orange Candy",         date(2026, 5, 6),  0,    None, OC_RUN5),
    ("Orange Candy",         date(2026, 5, 9),  3,    None, OC_RUN6),
    ("Orange Candy",         date(2026, 5, 9),  4,    None, OC_RUN7),
    ("The Hive #1",          date(2026, 5, 7),  0,    None, HIVE1_RUN1),
    ("The Hive #1",          date(2026, 5, 7),  1,    None, HIVE1_RUN2),
    ("The Hive #1",          date(2026, 5, 8),  0,    None, HIVE1_RUN3),
    ("The Hive #1",          date(2026, 5, 8),  1,    None, HIVE1_RUN4),
    ("The Hive #1",          date(2026, 5, 8),  2,    None, HIVE1_RUN5),
    ("Fembot #3",            date(2026, 5, 9),  0,    None, FEMBOT3_RUN1),
    ("Fembot #3",            date(2026, 5, 9),  1,    None, FEMBOT3_RUN2),
    ("Mango Starburst #23",  date(2026, 5, 9),  2,    None, MS23_RUN1),
    ("Maple Bacon Donut",    date(2026, 5, 10), 0,    None, MBD_RUN1),
    ("Maple Bacon Donut",    date(2026, 5, 10), 1,    None, MBD_RUN2),
    ("Rain Fruit",           date(2026, 5, 10), 2,    None, RF_RUN1),
    ("Rain Fruit",           date(2026, 5, 11), 0,    datetime(2026, 5, 11, 22, 44, tzinfo=timezone.utc), RF_RUN2),
    ("Rain Fruit",           date(2026, 5, 11), 1,    datetime(2026, 5, 12,  0, 30, tzinfo=timezone.utc), RF_RUN3),
]

STRAIN_STATUS = [
    # (name, profile_anchor, next_text, accent, slug)
    # accent: hex string override, or None to auto-assign from the distributed palette
    # slug drives last-run anchor: #{slug}-run{n} where n = run count from COMPLETED_RUNS
    ("WW Z",                 "#wwz-profile",     "—",                                                                                    None, "wwz"),
    ("Caramel Apple Gelato", "#cag-profile",     "Try 430°F endpoint",                                                                   None, "cag"),
    ("Orange Candy",         "#oc-profile",      "Ramp (Run 6) outperforming flat hold — repeat ramp to confirm, or try 420°F flat hold", None, "oc"),
    ("The Hive #1",          "#hive1-profile",   "Try 420–425°F endpoint on Run 6",                                                      None, "hive1"),
    ("Fembot #3",            "#fembot3-profile", "Try 420°F steady hold on Run 3",                                                       None, "fembot3"),
    ("Mango Starburst #23",  "#ms23-profile",    "Repeat Run 1 curve to confirm",                                                        None, "ms23"),
    ("Maple Bacon Donut",    "#mbd-profile",     "Repeat same curve — watch swab trend",                                                  None, "mbd"),
    ("Rain Fruit",           "#rainfruit-profile","Walk endpoint up incrementally — try 423°F on Run 4",                              None, "rainfruit"),
]

TERPENE_REFERENCE = [
    # (name, alias, bp_f, bp_c, band, aroma, qualities, found_in)
    # Low band — below 356°F / 180°C
    ("Humulene",          "alpha-humulene",              225, 107, "Low",  "Woody, spicy-clove",                   "Calming; appetite-suppressing character",   "Hops, allspice, cloves, coriander"),
    ("Alpha-Pinene",      "alpha-pinene",                313, 156, "Low",  "Pine forest",                          "Alerting; opens airways",                  "Pine, rosemary, dill, basil, sage"),
    ("Camphene",          "camphene",                    318, 159, "Low",  "Cool camphor, musky earth",             "Limited evidence",                         "Fir, nutmeg, rosemary, sage"),
    ("Beta-Pinene",       "beta-pinene",                 331, 166, "Low",  "Pine forest, fresh",                   "Alerting; focus-associated",               "Pine, dill, basil, rosemary"),
    ("Myrcene",           "beta-myrcene",                333, 167, "Low",  "Musky, earthy, sweet herbal",           "Relaxing, sedating",                       "Mangoes, hops, lemongrass, thyme"),
    ("Carene",            "delta-3-carene",              340, 171, "Low",  "Musky citrus, sweet pine",              "Uplifting; focus-associated",              "Rosemary, cedar, basil, pepper"),
    ("Phellandrene",      "alpha/beta-phellandrene",     342, 172, "Low",  "Citrusy, peppermint",                  "Uplifting character",                      "Eucalyptus, dill, water fennel"),
    ("Terpinene",         "alpha-terpinene",             343, 173, "Low",  "Piney, smokey, herbaceous",             "Supporting",                               "Tea tree, eucalyptus, marjoram"),
    ("Limonene",          "limonene",                    349, 176, "Low",  "Citrus",                                "Uplifting; stress-easing",                 "Citrus rinds, juniper, peppermint"),
    ("Eucalyptol",        "cineole",                     349, 176, "Low",  "Cool camphor, minty",                  "Alerting; opens airways",                  "Eucalyptus, tea tree, mugwort"),
    ("Cymene",            "p-cymene",                    351, 177, "Low",  "Mild sweet aged wood, lemon",           "Supporting",                               "Thyme, oregano, cumin, cilantro"),
    ("Ocimene",           "beta/trans-beta-ocimene",     352, 178, "Low",  "Tropical fruit, woody green citrus",   "Uplifting character",                      "Basil, orchids, kumquats, parsley"),
    # Mid band — 356–446°F / 180–230°C
    ("Terpinolene",       "alpha-terpinolene",           369, 187, "Mid",  "Fresh, herbal, sweet, floral, piney",  "Uplifting; sedating in isolation",         "Limes, cumin, lilac, nutmeg"),
    ("Linalool",          "linalool",                    388, 198, "Mid",  "Floral, citrusy-sweet",                "Calming, sedating",                        "Lavender, citrus, rosemary, basil"),
    ("Sabinene",          "sabinene hydrate / thujanol", 396, 202, "Mid",  "Woodsy, spicy",                        "Supporting",                               "Norway Spruce, nutmeg, holm oak"),
    ("Fenchol",           "fenchyl alcohol",             397, 203, "Mid",  "Lemon-lime, piney, camphor",           "Supporting",                               "Basil, aster flowers"),
    ("Borneol",           "bornyl alcohol",              414, 212, "Mid",  "Cool minty, camphor",                  "Calming, sedating",                        "Rosemary, mint, ginger, camphor"),
    ("Isoborneol",        "exo-borneol",                 414, 212, "Mid",  "Woody-sweet, spicy",                   "Calming, sedating",                        "Valerian, sage, thyme"),
    ("Terpineol",         "alpha-terpineol",             430, 221, "Mid",  "Lilac, floral blossom",                "Calming, sedating",                        "Pine oil, petitgrain, cajuput"),
    ("Citronellol",       "beta-citronellol",            435, 224, "Mid",  "Rose, citrus",                         "Relaxing; variable",                       "Citronella, roses, geraniums"),
    ("Pulegone",          "pulegone",                    435, 224, "Mid",  "Minty-camphor, resinous",              "Calming, sedating",                        "Catnip, pennyroyal, rosemary"),
    ("Geraniol",          "geraniol",                    446, 230, "Mid",  "Sweet floral, fruity",                 "Supporting",                               "Roses, lemongrass, citronella"),
    # High band — above 446°F / 230°C
    ("Anethole",              "anethole",                       454, 234, "High", "Licorice, sweet",                      "Sedating character",                   "Anise, fennel, star anise"),
    ("Guaiene",               "alpha/beta-guaiene",             455, 235, "High", "Sweet, woody, earthy, spicy",          "Supporting",                           "Palo Santo"),
    ("Geranyl Acetate",       "geranyl acetate",                468, 242, "High", "Sweet floral, pear-like",              "Supporting",                           "Lemongrass, coriander, geraniums"),
    ("Elemene",               "alpha/beta/delta/gamma-elemene", 487, 253, "High", "Waxy, herbal",                         "Limited research",                     "Ginseng, Chinese Yu Jin"),
    ("Caryophyllene",         "beta/trans-caryophyllene",       493, 256, "High", "Spicy, peppery",                       "Calming; CB2 receptor binding",        "Black pepper, cloves, hops, oregano"),
    ("Cedrene",               "alpha/beta-cedrene",             505, 263, "High", "Light woodsy",                         "Supporting",                           "Cedarwood, juniper, cypress"),
    ("Valencene",             "valencene",                      520, 271, "High", "Sweet fresh citrus",                   "Alerting, uplifting",                  "Valencia oranges"),
    ("Farnesene",             "alpha/beta-farnesene",           523, 273, "High", "Green apple",                          "Calming, sedating",                    "Apple skins, pears"),
    ("Nerolidol",             "cis/trans-nerolidol",            529, 276, "High", "Woody bark, waxy, floral",             "Calming, sedating",                    "Neroli, jasmine, ginger, lavender"),
    ("Caryophyllene Oxide",   "beta-caryophyllene oxide",       536, 280, "High", "Dry, fresh, spicy-sweet",              "Calming; CB2 receptor binding",        "Black pepper, caraway, cloves"),
    ("Guaiol",                "guaiol",                         550, 288, "High", "Piney, woody, rose-like",              "Supporting",                           "Cypress pines, guaiacum plant"),
    ("Eudesmol",              "gamma/alpha/beta-eudesmol",      574, 301, "High", "Woody-sweet",                          "Mildly sedating",                      "Cypress, valerian, eucalyptus"),
    ("Bisabolol",             "alpha-bisabolol / levomenol",    599, 315, "High", "Sweet floral, honey, mild coconut",    "Calming, soothing",                    "Chamomile"),
    ("Phytol",                "phytol",                         637, 336, "High", "Grassy",                               "Mildly sedating",                      "Green tea"),
]

# ── SECTIONS ─────────────────────────────────────────────────────────────────

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

def _resolve_accent_colors():
    # Distribute hues evenly across non-green space (0–89° and 166–359°, avoiding 90–165°).
    # Strains with an explicit accent hex in STRAIN_STATUS use that color instead.
    NON_GREEN = [(0, 90), (166, 360)]
    total = sum(e - s for s, e in NON_GREEN)
    n = len(STRAIN_STATUS)
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
    for i, (name, _, _, accent, _) in enumerate(STRAIN_STATUS):
        resolved[name] = accent if accent is not None else _hsl_to_hex(auto_hues[i], SAT, LGT)
    return resolved

_ACCENT_RESOLVED = _resolve_accent_colors()

def validate_accent_colors():
    # Only check manually-overridden colors — auto-assigned ones are valid by construction.
    overrides = [(name, color) for name, _, _, color, _ in STRAIN_STATUS if color is not None]
    if not overrides:
        return
    all_resolved = [(name, _ACCENT_RESOLVED[name]) for name, *_ in STRAIN_STATUS]
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

def terpene_reference_html():
    BAND_LABELS = {
        "Low":  "Low — below 356°F / 180°C",
        "Mid":  "Mid — 356–446°F / 180–230°C",
        "High": "High — above 446°F / 230°C",
    }
    rows = ""
    current_band = None
    for name, alias, bp_f, bp_c, band, aroma, qualities, found_in in TERPENE_REFERENCE:
        if band != current_band:
            current_band = band
            rows += f'<tr class="band-row"><td colspan="6">{BAND_LABELS.get(band, band)}</td></tr>'
        rows += (
            f'<tr>'
            f'<td><strong>{name}</strong><span class="terp-alias">{alias}</span></td>'
            f'<td class="bp-cell">{bp_f}°F / {bp_c}°C</td>'
            f'<td><span class="band-badge band-{band.lower()}">{band}</span></td>'
            f'<td>{aroma}</td>'
            f'<td>{qualities}</td>'
            f'<td style="font-size:0.78rem;color:var(--grey-text);">{found_in}</td>'
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
    validate_accent_colors()
    _ac = _ACCENT_RESOLVED

    # sessions_prior lookup keyed by (strain, 1-indexed run number)
    _cnt = {}
    _spr = {}
    for _s, _rd, _sp, _ul, _wp in COMPLETED_RUNS:
        _cnt[_s] = _cnt.get(_s, 0) + 1
        _spr[(_s, _cnt[_s])] = _sp

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

    sections.append(what_to_try_next_html(
        "mbd-next",
        dab_notes="Watch the swab — darker golden on Run 1, lighter on Run 2. Repeat same curve.",
        ai_analysis="Two runs, swab trending cleaner, distinct flavor on Run 2, no harshness. Repeat the same curve on Run 3 to confirm the trend before adjusting anything. If darker golden persists across more runs, consider dropping endpoint to 420°F.",
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
