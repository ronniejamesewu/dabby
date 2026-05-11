#!/usr/bin/env python3
from datetime import datetime, date
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
  border-bottom-color: var(--border);
}}
.section-header h2 {{
  font-size: clamp(1.1rem, 3vw, 1.4rem);
  font-weight: 700;
  color: var(--green-dark);
  margin-bottom: 0.3rem;
}}
.section-header.grey h2 {{ color: var(--grey-text); }}


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

/* ── Mobile ── */
@media (max-width: 600px) {{
  :root {{ --page-pad: 1rem; }}
  body {{ padding: 0.5rem; }}
  .info-table td:first-child {{ width: 35%; white-space: normal; }}
  .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
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

def section_header(title, status=None, badge_class=None, header_class=""):
    html = f'<div class="section-header {header_class}">'
    html += f'<h2>{title}</h2>'
    if status and badge_class:
        html += f'<span class="badge {badge_class}">{status}</span>'
    return html + '</div>'

def result_row(label, value, amber=False):
    cls = "result-row amber" if amber else "result-row"
    return f'<p class="{cls}"><span class="label">{label}</span> {value}</p>'

def what_to_try_next_html(section_id, your_read, my_read, proposed_waypoints=None):
    s = f'<div class="section" id="{section_id}">'
    s += section_header("What to Try Next", header_class="grey")
    s += result_row("Your read:", your_read)
    s += result_row("My read:", my_read)
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
    for strain, run_date, wps in COMPLETED_RUNS:
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
    for strain, run_date, wps in COMPLETED_RUNS:
        if run_date is not None:
            if strain not in last_dates or run_date > last_dates[strain]:
                last_dates[strain] = run_date

    sorted_strains = sorted(
        [(s, a, nt, ac) for s, a, nt, ac in STRAIN_STATUS if run_counts.get(s, 0) > 0],
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
    for i, (strain, anchor, nt, accent) in enumerate(sorted_strains):
        color        = accent if accent else ACCENT_PALETTE[i % len(ACCENT_PALETTE)]
        medal        = ' 🥇' if run_counts[strain] == max_runs else ''
        n            = run_counts[strain]
        session_word = 'session' if n == 1 else 'sessions'
        ld           = last_dates.get(strain)
        if ld:
            date_str = ld.strftime('%b %-d')
            meta = f'{n} {session_word} &middot; {"" if n == 1 else "last "}{date_str}'
        else:
            meta = f'{n} {session_word}'
        next_anchor = anchor.replace('-profile', '-next')
        rows += (
            f'<div class="strain-row" data-strain="{strain.lower()}" style="--accent:{color}">'
            f'<div class="strain-info">'
            f'<a href="{anchor}" class="strain-name">{strain}{medal}</a>'
            f'<span class="strain-meta">{meta}</span>'
            f'</div>'
            f'<a href="{next_anchor}" class="next-pill">&rarr; Next</a>'
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

    ref = (
        f'<div class="ref-row">'
        f'<span class="ref-label">Reference</span>'
        f'<a href="#constants">Constants</a>'
        f'<a href="#swab">Swab Reference</a>'
        f'<a href="#baseline">Baseline Curve</a>'
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
        '</script>'
    )

    s = '<div class="section" id="dashboard">'
    s += section_header("Dashboard")
    s += cards
    s += browser
    s += ref
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
    ("0s",  "375°F", "Session open — lowest temperature point"),
    ("15s", "378°F", "Flat phase — most volatile terpenes"),
    ("40s", "395°F", "Mid ascent — mid-range terpenes"),
    ("65s", "440°F", "Endpoint — THC completion"),
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
    ("0s",  "380°F", "Session open — 5°F above baseline; increases opening vapor density"),
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

# ── DASHBOARD DATA ────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)

COMPLETED_RUNS = [
    ("WW Z",                 date(2026, 5, 2),  WWZ_RUN1),
    ("Caramel Apple Gelato", None,              CAG_RUN1),
    ("Orange Candy",         None,              OC_RUNS12),
    ("Orange Candy",         None,              OC_RUNS12),
    ("Orange Candy",         None,              OC_RUN3),
    ("Orange Candy",         date(2026, 5, 5),  OC_RUN4),
    ("Orange Candy",         date(2026, 5, 6),  OC_RUN5),
    ("Orange Candy",         date(2026, 5, 10), OC_RUN6),
    ("Orange Candy",         date(2026, 5, 10), OC_RUN7),
    ("The Hive #1",          date(2026, 5, 8),  HIVE1_RUN1),
    ("The Hive #1",          date(2026, 5, 8),  HIVE1_RUN2),
    ("The Hive #1",          date(2026, 5, 8),  HIVE1_RUN3),
    ("The Hive #1",          date(2026, 5, 9),  HIVE1_RUN4),
    ("The Hive #1",          date(2026, 5, 9),  HIVE1_RUN5),
    ("Fembot #3",            date(2026, 5, 9),  FEMBOT3_RUN1),
    ("Fembot #3",            date(2026, 5, 9),  FEMBOT3_RUN2),
    ("Mango Starburst #23",  date(2026, 5, 9),  MS23_RUN1),
]

ACCENT_PALETTE = [
    "#6B9E78", "#C4956A", "#D4784A", "#C9A84C",
    "#8B7BC4", "#D4A44C", "#7A9EBB", "#C47A7A",
    "#7AB5C4", "#A4C47A",
]

STRAIN_STATUS = [
    # (name, profile_anchor, next_text, accent)
    ("WW Z",                 "#wwz-profile",     "—",                                                                                    "#6B9E78"),
    ("Caramel Apple Gelato", "#cag-profile",     "Try 430°F endpoint",                                                                   "#C4956A"),
    ("Orange Candy",         "#oc-profile",      "Ramp (Run 6) outperforming flat hold — repeat ramp to confirm, or try 420°F flat hold", "#D4784A"),
    ("The Hive #1",          "#hive1-profile",   "Try 420–425°F endpoint on Run 6",                                                      "#C9A84C"),
    ("Fembot #3",            "#fembot3-profile", "Try 420°F steady hold on Run 3",                                                       "#8B7BC4"),
    ("Mango Starburst #23",  "#ms23-profile",    "Repeat Run 1 curve to confirm",                                                        "#D4A44C"),
]

# ── SECTIONS ─────────────────────────────────────────────────────────────────

def build_html():
    sections = []

    dash = dashboard_html()

    # ── Device & Session Constants
    s = f'<div class="section" id="constants">'
    s += section_header("Device &amp; Session Constants")
    s += '<p class="note">These parameters apply to every session in this log unless explicitly noted otherwise.</p>'
    s += info_table(GLOBAL_INFO)
    s += '<p class="note">IR reads titanium, not insert surface.</p>'
    s += '</div>'
    sections.append(s)

    # ── Swab Reference
    s = f'<div class="section" id="swab">'
    s += section_header("Swab Color Reference")
    s += '<p class="note">Swab color is a qualitative directional signal within a strain. Do not compare across strains — starting material color, oxidation state, and terpene-to-cannabinoid ratio all affect residue color independently of temperature.</p>'
    s += '''<table class="swab-table">
        <tr><td class="swab-key target">Target</td><td>Light golden / amber, slightly fluid. Clean vaporization, no significant degradation.</td></tr>
        <tr><td class="swab-key hot">Too hot</td><td>Amber shading toward brown. Possible degradation at session tail, or darker starting material. Reduce endpoint cautiously.</td></tr>
        <tr><td class="swab-key severe">Too hot (severe)</td><td>Dark brown or black. Likely overheated. Reduce setpoint significantly.</td></tr>
        <tr><td class="swab-key cool">Too cool</td><td>Cloudy or white crystalline residue. Possibly THCA not fully vaporizing — interpretation uncertain. Raise setpoint cautiously.</td></tr>
    </table>'''
    s += '</div>'
    sections.append(s)

    # ── Baseline Curve
    s = f'<div class="section" id="baseline">'
    s += section_header("Baseline Curve")
    s += '<p class="note">Single starting curve for all hash rosin sessions with cold start technique. Strain profiles document empirical deviations from this baseline via swab results and session observations. Do not design different starting curves based on strain name, inferred terpene profile, consistency, or provenance quality without empirical justification.</p>'
    s += '<h3>Parameters</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Rate:</strong> ~0.6°F/sec</p>'
    s += curve_chart_html(BASELINE_CURVE)
    s += curve_table(BASELINE_CURVE)
    s += '<p class="note">Terpene zone annotations in individual run curves are approximate orientation points based on inferred terpene profiles — not measured targets. The same common cannabis terpenes appear across most strains. Annotations reflect boiling point ranges, not confirmed strain-specific terpene data.</p>'
    s += '<h3>Rationale</h3>'
    s += '<p>Opening setpoint compensates for the estimated insert offset. 440°F endpoint targets more complete THC vaporization — all waypoints are starting points, swab results drive adjustment.</p>'
    s += '</div>'
    sections.append(s)

    # ── WW Z Strain Profile
    s = f'<div class="section" id="wwz-profile">'
    s += section_header("WW Z — Strain Profile")
    s += info_table(WWZ_INFO)
    s += '<h3>Inferred Terpene Profile</h3>'
    s += terpene_table(WWZ_TERPS)
    s += '</div>'
    sections.append(s)

    # ── WW Z Run 1
    s = f'<div class="section" id="wwz-run1">'
    s += section_header("WW Z — Run 1 — May 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Rate:</strong> ~0.6°F/sec</p>'
    s += curve_chart_html(WWZ_RUN1)
    s += curve_table(WWZ_RUN1)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden/amber. Clean. No dark coloration.")
    s += result_row("Vapor:", "Spectacular. Full session expressed well across the arc.")
    s += result_row("Verdict:", "Dialed on first run. Profile locked. Baseline curve confirmed appropriate for this material.")
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "wwz-next",
        your_read="Nothing recorded",
        my_read="One session, clean swab, described as spectacular. No floor signal, no harshness. Nothing to chase — repeat when you want to revisit it.",
        proposed_waypoints=None,
    ))

    # ── Caramel Apple Gelato Strain Profile
    s = f'<div class="section" id="cag-profile">'
    s += section_header("Caramel Apple Gelato — Strain Profile")
    s += info_table(CAG_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += terpene_table(CAG_TERPS)
    s += '</div>'
    sections.append(s)

    # ── CAG Run 1
    s = f'<div class="section" id="cag-run1">'
    s += section_header("Caramel Apple Gelato — Run 1 — May 2026")
    s += '<h3 class="amber">Curve Used</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 450°F</p>'
    s += curve_chart_html(CAG_RUN1)
    s += curve_table(CAG_RUN1, amber=True)
    s += '<h3 class="amber">Results</h3>'
    s += result_row("Swab:", "Amber shading toward light brown.", amber=True)
    s += result_row("Vapor:", "Limited flavor. Session did not express distinct character.", amber=True)
    s += result_row("Diagnosis:", "Endpoint of 450°F likely too aggressive — supported by swab darkening. Limited flavor may reflect endpoint temperature degrading terpene fraction at session tail, or may reflect moderate terpene content in this material independent of temperature. Both explanations are plausible; endpoint reduction will help distinguish them.", amber=True)
    s += result_row("Adjustment:", "Pull endpoint back to 430°F. Shorten hold to 55 seconds to reduce risk of outlasting small load.", amber=True)
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "cag-next",
        your_read="Nothing recorded",
        my_read="One data point at 450°F with an amber-toward-brown swab — reliable floor signal. Pull the endpoint back to 430°F. Nothing subtle here, it was just too hot.",
        proposed_waypoints=CAG_RUN2,
    ))

    # ── Orange Candy Strain Profile
    s = f'<div class="section" id="oc-profile">'
    s += section_header("Orange Candy — Strain Profile")
    s += info_table(OC_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += terpene_table(OC_TERPS)
    s += '</div>'
    sections.append(s)

    # ── OC Runs 1 & 2
    s = f'<div class="section" id="oc-runs12">'
    s += section_header("Orange Candy — Runs 1 &amp; 2 — May 2026")
    s += '<h3 class="amber">Curve Used — Runs 1 &amp; 2</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 450°F</p>'
    s += curve_chart_html(OC_RUNS12)
    s += curve_table(OC_RUNS12, amber=True)
    s += '<h3 class="amber">Observations</h3>'
    s += result_row("Result:", "Working well but first 40 seconds felt too flat and slow. Low vapor density in opening phase.", amber=True)
    s += result_row("Swab:", "Not recorded.", amber=True)
    s += result_row("Diagnosis:", "Opening too flat — low vapor density in first 40s. Steeper climb 15–35s drives earlier vapor production. Flatter tail 35–65s closes the offset — a slowly-arrived-at 440°F delivers more heat to the material than a steeply-arrived-at 450°F.", amber=True)
    s += '</div>'
    sections.append(s)

    # ── OC Run 3
    s = f'<div class="section" id="oc-run3">'
    s += section_header("Orange Candy — Run 3 — May 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    s += curve_chart_html(OC_RUN3)
    s += curve_table(OC_RUN3)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden/tan. Clean. Minimal peripheral darkening at tip edge — consistent with insert wall cooling, not degradation.")
    s += result_row("Session:", "Very nice. Strong effects. Opening draws wispy but flavorful. Good progression through session.")
    s += result_row("Verdict:", "Clean swab, strong result. Wispy opening draws suggest opportunity to raise opening setpoint slightly to improve vapor density at session start without affecting the clean tail.")
    s += '</div>'
    sections.append(s)

    # ── OC Run 4
    s = f'<div class="section" id="oc-run4">'
    s += section_header("Orange Candy — Run 4 — May 5, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    s += curve_chart_html(OC_RUN4)
    s += curve_table(OC_RUN4)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden. Clean both times.")
    s += result_row("Session:", "Fine. Not noticeably different from Run 3. Run repeated twice on May 5, 2026 — consistent results across both.")
    s += result_row("Verdict:", "Clean swab confirmed. Results stable. Lower opening setpoint (350°F) under exploration for Run 5 as next variable to test.")
    s += '</div>'
    sections.append(s)

    # ── OC Run 5
    s = f'<div class="section" id="oc-run5">'
    s += section_header("Orange Candy — Run 5 — May 6, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Open:</strong> 350°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 460°F</p>'
    s += curve_chart_html(OC_RUN5)
    s += curve_table(OC_RUN5, amber=True)
    s += '<h3 class="amber">Results</h3>'
    s += result_row("Swab:", "Darker than target — direction consistent with endpoint too hot.", amber=True)
    s += result_row("Session:", "Last portion tad harsh, consistent with elevated endpoint. Effect notably stronger than prior runs.", amber=True)
    s += result_row("Observation:", "User's hypothesis: higher temperature produced stronger effect. Logged as stated — one data point, not a confirmed finding. Confounders include session-to-session variability in tolerance, load size, and conditions.", amber=True)
    s += result_row("Next:", "Repeat same curve as Run 6 before drawing conclusions.", amber=True)
    s += '</div>'
    sections.append(s)

    # ── OC Run 6
    s = f'<div class="section" id="oc-run6">'
    s += section_header("Orange Candy — Run 6 — May 10, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    s += curve_chart_html(OC_RUN6)
    s += curve_table(OC_RUN6)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden. Clean.")
    s += result_row("Session:", "Very nice.")
    s += result_row("Next:", "Repeat to confirm, or test 350°F open / 460°F endpoint curve when ready.")
    s += '</div>'
    sections.append(s)

    # ── OC Run 7
    s = f'<div class="section" id="oc-run7">'
    s += section_header("Orange Candy — Run 7 — May 10, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 69 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    s += curve_chart_html(OC_RUN7)
    s += curve_table(OC_RUN7)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Plain amber — clean.")
    s += result_row("Session:", "Pleasant overall. Not as tasty as the ramp from lower temp. Harsh in the last 20 seconds.")
    s += result_row("Read:", "Swab is clean, so harshness is a session character signal, not a floor indicator. Comparing to Run 6 (ramp to 430°F, light golden, very nice) — the flat hold at the same endpoint produces clearly more harshness and less flavor character. Consistent with the pattern seen on Fembot #3: flat holds at 430°F track hotter in session feel than ramps to the same endpoint, even with a clean swab.")
    s += result_row("Next:", "Ramp curve (Run 6 shape) is outperforming the flat hold at 430°F. Repeat Run 6 ramp to confirm, or try 420°F flat hold to find the flat-hold ceiling.")
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "oc-next",
        your_read="Repeat Run 6 ramp to confirm, or try 420°F flat hold.",
        my_read="Run 6 (ramp to 430°F) vs Run 7 (flat 430°F) on the same day is the cleanest curve-shape comparison in the log. Ramp won clearly on flavor and harshness. Repeat the ramp before adding more variables — confirm it holds before dropping the endpoint.",
        proposed_waypoints=OC_RUN6,
    ))

    # ── The Hive #1 Strain Profile
    s = f'<div class="section" id="hive1-profile">'
    s += section_header("The Hive #1 — Strain Profile")
    s += info_table(HIVE1_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += '<p class="note">Profile inferred from Honey Banana × Papaya lineage (Bloom Seed Co). Terpene ratios and minor terpenes are not inferable from genetics alone — these are orientation points drawn from the generic cannabis palette, not strain-specific measurements. Start from baseline curve; swab results drive all adjustments.</p>'
    s += terpene_table(HIVE1_TERPS)
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 1
    s = f'<div class="section" id="hive1-run1">'
    s += section_header("The Hive #1 — Run 1 — May 8, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F</p>'
    s += curve_chart_html(HIVE1_RUN1)
    s += curve_table(HIVE1_RUN1)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — clean. No darkening.")
    s += result_row("Session:", "Nice flavors on the way up through the arc. Heavy indica effect.")
    s += result_row("Verdict:", "Clean swab on first run — curve appears well-matched to this material. Repeated as Run 2 to confirm.")
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 2
    s = f'<div class="section" id="hive1-run2">'
    s += section_header("The Hive #1 — Run 2 — May 8, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 440°F &nbsp;|&nbsp; Identical to Run 1.</p>'
    s += curve_chart_html(HIVE1_RUN2)
    s += curve_table(HIVE1_RUN2)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Very light — cleaner than Run 1.")
    s += result_row("Session:", "Really nice. Consistent with Run 1.")
    s += result_row("Verdict:", "Two clean runs, consistent character, swab lighter on repeat. 440°F endpoint may be higher than needed — material is fully expressing before the endpoint. Run 3: trying steady 430°F flat hold (no ramp) to test whether curve shape affects the result.")
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 3
    s = f'<div class="section" id="hive1-run3">'
    s += section_header("The Hive #1 — Run 3 — May 8, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 45 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    s += '<p class="note">Curve shape experiment: steady flat hold at 430°F from session open, rather than the ramped curve used in Runs 1–2. Testing whether a multi-stage ramp produces meaningfully different results from a single sustained setpoint. Swab is a floor indicator only — session character is the primary readout.</p>'
    s += curve_chart_html(HIVE1_RUN3)
    s += curve_table(HIVE1_RUN3)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — clean.")
    s += result_row("Session:", "First half: lots of flavor, low throat irritation. Second half: irritation increased, flavor faded to generic dab vapor — never harsh or burnt, just less distinct. Effect notably strong.")
    s += result_row("Read:", "At a flat 430°F from the open, all terpene fractions (pinene through linalool, all below 430°F) are available simultaneously — first hit may be the full palette combining at once rather than staged. The ramp climbs through each fraction sequentially, which may be what gives those runs more distinct flavor progression across the arc. 45 seconds was too short — vapor was still producing at session end. Not a temperature issue, just cut off early.")
    s += result_row("Verdict:", "One data point. Directionally supports the ramp producing more distinct staged flavor vs. the flat hold combining everything at once. If revisiting the flat hold, extend to 60 seconds. Next planned: repeat the Run 1–2 ramp (380→390→410°F) with 430°F endpoint to compare directly on the same endpoint.")
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 4
    s = f'<div class="section" id="hive1-run4">'
    s += section_header("The Hive #1 — Run 4 — May 9, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 60 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp) — extended from Run 3\'s 45s</p>'
    s += curve_chart_html(HIVE1_RUN4)
    s += curve_table(HIVE1_RUN4)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — clean. Consistent with Run 3.")
    s += result_row("Session:", "Similar to Run 3. Extended hold confirmed vapor was still producing at 45s in Run 3 — 60s felt more complete.")
    s += result_row("Verdict:", "Two flat-hold data points, both clean swabs, consistent character. Next: ramp to 430°F endpoint (380→390→410→430°F) — the original planned experiment — to compare curve shape on the same endpoint.")
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 5
    s = f'<div class="section" id="hive1-run5">'
    s += section_header("The Hive #1 — Run 5 — May 9, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F (ramp — same shape as Runs 1–2, endpoint reduced from 440°F)</p>'
    s += curve_chart_html(HIVE1_RUN5)
    s += curve_table(HIVE1_RUN5)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — a tad lighter than the flat-hold 430°F runs (Runs 3–4). Clean.")
    s += result_row("Session:", "Nice distinct flavors through the first two-thirds. Harsh in the last ~10 seconds. Effects quite potent.")
    s += result_row("Read:", "Distinct staged flavor character is consistent with the ramp — each terpene fraction vaporizes as the curve climbs through it, rather than all at once as in the flat hold. Swab difference vs. Runs 3–4 is within noise (too many uncontrolled variables). Harshness at session tail is a directional signal that 430°F may still be slightly above ideal for this material on the ramp.")
    s += result_row("Next:", "Try 420–425°F endpoint on Run 6. Keep ramp shape unchanged.")
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "hive1-next",
        your_read="Try 420–425°F endpoint, keep ramp shape.",
        my_read="Flat-hold 430°F was clean twice. Ramp to 430°F showed tail harshness once. Harshness is directional but one data point — the flat holds didn't show it at the same endpoint. 425°F ramp is a reasonable conservative step; could also repeat the ramp at 430°F first to confirm the harshness was real.",
        proposed_waypoints=HIVE1_NEXT,
    ))

    # ── Fembot #3 Strain Profile
    s = f'<div class="section" id="fembot3-profile">'
    s += section_header("Fembot #3 — Strain Profile")
    s += info_table(FEMBOT3_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += '<p class="note">Profile inferred from Fuzzy Melon × Rambutan lineage. Terpinolene-forward character is consistent with the sativa-dominant, uplifting profile typical of this lineage direction — not measured. These are orientation points from the generic cannabis palette, not strain-specific data. Start from baseline curve; swab results drive all adjustments.</p>'
    s += terpene_table(FEMBOT3_TERPS)
    s += '</div>'
    sections.append(s)

    # ── Fembot #3 Run 1
    s = f'<div class="section" id="fembot3-run1">'
    s += section_header("Fembot #3 — Run 1 — May 9, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    s += curve_chart_html(FEMBOT3_RUN1)
    s += curve_table(FEMBOT3_RUN1)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — clean. Two heads mostly white, two with light golden coloring. No darkening.")
    s += result_row("Session:", "Very tasty on the ascent. No visible vapor until mid-range. Slight harshness at the tail. Effects upbeat, creative, not too body-heavy — consistent with sativa-dominant character.")
    s += result_row("Next:", "Try steady 420°F flat hold (60s) on Run 2 — drop endpoint and change curve shape to test both variables.")
    s += '</div>'
    sections.append(s)

    # ── Fembot #3 Run 2
    s = f'<div class="section" id="fembot3-run2">'
    s += section_header("Fembot #3 — Run 2 — May 9, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 60 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    s += curve_chart_html(FEMBOT3_RUN2)
    s += curve_table(FEMBOT3_RUN2)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Light golden — clean. Consistent with Run 1.")
    s += result_row("Session:", "Very tasty, great effects. Harshness in the last third.")
    s += result_row("Read:", "Harshness at the tail is consistent with Run 1 (ramp to 430°F endpoint) — two data points now pointing at 430°F as slightly above ideal for this material, regardless of curve shape. Swab is clean, so this is a session character signal rather than a floor indicator.")
    s += result_row("Next:", "Try 420°F steady flat hold on Run 3.")
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "fembot3-next",
        your_read="Nothing recorded",
        my_read="Strongest signal in the log — harshness at 430°F on both a ramp and a flat hold. Two shapes, same outcome. 430°F is above ideal for this material. 420°F flat hold is the clear next test.",
        proposed_waypoints=FEMBOT3_RUN3,
    ))

    # ── Mango Starburst #23 Strain Profile
    s = f'<div class="section" id="ms23-profile">'
    s += section_header("Mango Starburst #23 — Strain Profile")
    s += info_table(MS23_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += '<p class="note">Profile inferred from SB36 lineage (Starburst OG × \'97 KC36). Limonene and terpinolene weighted toward prominent based on the line\'s documented citrus-candy, flavor-forward character — not measured. These are orientation points from the generic cannabis palette, not strain-specific data. Start from baseline curve; swab results drive all adjustments.</p>'
    s += terpene_table(MS23_TERPS)
    s += '</div>'
    sections.append(s)

    # ── Mango Starburst #23 Run 1
    s = f'<div class="section" id="ms23-run1">'
    s += section_header("Mango Starburst #23 — Run 1 — May 9, 2026")
    s += '<h3>Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    s += curve_chart_html(MS23_RUN1)
    s += curve_table(MS23_RUN1)
    s += '<h3>Results</h3>'
    s += result_row("Swab:", "Very clean — no darkening.")
    s += result_row("Session:", "Very piney character throughout — almost pine sol. Tasty, though not to user's taste preference. Heady effects. No harshness.")
    s += result_row("Note:", "Strong pine-forward character noted on first run. The SB36 lineage inference weighted limonene and terpinolene as prominent — the pronounced pine character is consistent with pinene playing a larger role than the inference anticipated. Logged as one data point; flavor character is a weak signal and single-session observations carry high uncertainty.")
    s += result_row("Verdict:", "Clean swab on first run. Curve well-matched to this material. Repeat on Run 2 to confirm.")
    s += '</div>'
    sections.append(s)

    sections.append(what_to_try_next_html(
        "ms23-next",
        your_read="Nothing recorded",
        my_read="One run, clean swab, no harshness. Pine-forward character was noted but single-session flavor observations are noisy. Repeat the same curve before changing anything — if it's pine again on Run 2, that's real.",
        proposed_waypoints=MS23_RUN1,
    ))

    # ── Assemble
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
