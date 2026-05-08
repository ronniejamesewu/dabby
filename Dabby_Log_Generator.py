#!/usr/bin/env python3
from datetime import datetime, date
"""
Dabby the House Rig — Session Profile & Calibration Log Generator
Produces Dabby_Profile_Log.html — a mobile-responsive, screen-optimized web document.
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

/* ── Status badge ── */
.badge {{
  display: inline-block;
  padding: 0.4rem 0.9rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.03em;
}}
.badge.dialed   {{ background: var(--green-dark); color: #fff; }}
.badge.calib    {{ background: var(--amber-light); color: var(--amber); border: 1px solid var(--amber); }}
.badge.pending  {{ background: var(--grey-bg); color: var(--grey-text); border: 1px solid var(--border); }}
.badge.hot      {{ background: var(--amber-light); color: #8B4513; border: 1px solid var(--amber); }}
.badge-sm {{ padding: 0.2rem 0.6rem; font-size: 0.75rem; letter-spacing: 0; }}

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

/* ── Nav / TOC ── */
.toc ul {{
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}}
.toc a {{
  display: inline-block;
  padding: 0.3rem 0.7rem;
  background: #fff;
  border: 1px solid var(--green-mid);
  border-radius: 20px;
  font-size: 0.8rem;
  color: var(--green-dark);
  text-decoration: none;
  font-weight: 500;
}}
.toc a:hover {{ background: var(--green-dark); color: #fff; }}

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
  grid-template-columns: repeat(4, 1fr);
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
.dash-strain-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}}
.dash-strain-table th {{
  background: var(--green-dark);
  color: #fff;
  padding: 0.55rem 0.75rem;
  text-align: left;
  font-weight: 600;
}}
.dash-strain-table th.center {{ text-align: center; }}
.dash-strain-table td {{
  padding: 0.55rem 0.75rem;
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}}
.dash-strain-table tr:last-child td {{ border-bottom: none; }}
.dash-strain-table tr:nth-child(even) td {{ background: var(--green-light); }}
.dash-strain-table td:first-child {{ font-weight: 600; }}
.dash-strain-table td.center {{ text-align: center; }}
.next-text {{ color: var(--grey-text); font-size: 0.85rem; }}
.strain-link {{ color: var(--green-dark); text-decoration: none; }}
.strain-link:hover {{ text-decoration: underline; }}

/* ── Mobile ── */
@media (max-width: 600px) {{
  :root {{ --page-pad: 1rem; }}
  body {{ padding: 0.5rem; }}
  .info-table td:first-child {{ width: 35%; white-space: normal; }}
  .toc ul {{ flex-direction: column; }}
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

def dashboard_html():
    today = date.today()
    days = (today - FIRST_RUN_DATE).days + 1

    opens, endpoints, temp_sec, run_counts = [], [], {}, {}
    for strain, wps in COMPLETED_RUNS:
        pts = [(int(t.replace('s', '')), float(v.replace('°F', ''))) for t, v, _ in wps]
        opens.append(pts[0][1])
        endpoints.append(pts[-1][1])
        run_counts[strain] = run_counts.get(strain, 0) + 1
        for i in range(len(pts) - 1):
            t1, v1 = pts[i]; t2, v2 = pts[i + 1]
            dt = t2 - t1
            for s in range(dt):
                bucket = round((v1 + (v2 - v1) * s / dt) / 5) * 5
                temp_sec[bucket] = temp_sec.get(bucket, 0) + 1

    total    = len(COMPLETED_RUNS)
    avg_open = round(sum(opens) / total)
    avg_end  = round(sum(endpoints) / total)
    hot_temp = max(temp_sec, key=temp_sec.get)

    sorted_strains = sorted(
        [(s, a, bc, bt, nt) for s, a, bc, bt, nt in STRAIN_STATUS if run_counts.get(s, 0) > 0],
        key=lambda x: run_counts[x[0]], reverse=True
    )

    cards = (
        f'<div class="stats-grid">'
        f'<div class="stat-card c1"><div class="stat-value">{total}</div><div class="stat-label">runs over {days} days</div></div>'
        f'<div class="stat-card c2"><div class="stat-value">{avg_open}°</div><div class="stat-label">avg open</div></div>'
        f'<div class="stat-card c3"><div class="stat-value">{avg_end}°</div><div class="stat-label">avg endpoint</div></div>'
        f'<div class="stat-card c4"><div class="stat-value">{hot_temp}°</div><div class="stat-label">most time spent</div></div>'
        f'</div>'
    )

    rows = ''
    for i, (strain, anchor, bc, bt, nt) in enumerate(sorted_strains):
        medal = ' 🥇' if i == 0 else ''
        rows += (
            f'<tr>'
            f'<td><a href="{anchor}" class="strain-link">{strain}</a>{medal}</td>'
            f'<td class="center">{run_counts[strain]}</td>'
            f'<td class="center"><span class="badge badge-sm {bc}">{bt}</span></td>'
            f'<td class="next-text">{nt}</td>'
            f'</tr>'
        )

    table = (
        f'<table class="dash-strain-table">'
        f'<thead><tr><th>Strain</th><th class="center">Runs</th><th class="center">Status</th><th>Next</th></tr></thead>'
        f'<tbody>{rows}</tbody>'
        f'</table>'
    )

    s = '<div class="section" id="dashboard">'
    s += section_header("Dashboard")
    s += cards
    s += table
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
    ("Status",      "DIALED — Run 1"),
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
    ("Status",      "IN CALIBRATION — Run 1 complete, Run 2 pending"),
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
    ("Status",      "IN CALIBRATION — Runs 1–4 complete, Run 5 complete, Run 6 pending"),
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

HIVE1_INFO = [
    ("Strain",      "The Hive #1 (Honey Banana × Papaya — Bloom Seed Co)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Myxed Up (washed and pressed)"),
    ("Input",       "159–73 micron ice water hash"),
    ("Nose",        "Very fragrant at cold nose. Spice noticeable (consistent with caryophyllene — weak secondary signal only)."),
    ("Status",      "IN CALIBRATION — Runs 1–2 complete, Run 3 pending"),
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
    ("65s", "430°F", "Endpoint"),
]

# ── DASHBOARD DATA ────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)

COMPLETED_RUNS = [
    ("WW Z",                 WWZ_RUN1),
    ("Caramel Apple Gelato", CAG_RUN1),
    ("Orange Candy",         OC_RUNS12),
    ("Orange Candy",         OC_RUNS12),
    ("Orange Candy",         OC_RUN3),
    ("Orange Candy",         OC_RUN4),
    ("Orange Candy",         OC_RUN5),
    ("The Hive #1",          HIVE1_RUN1),
    ("The Hive #1",          HIVE1_RUN2),
]

STRAIN_STATUS = [
    # (name, profile_anchor, badge_class, badge_text, next_text)
    ("WW Z",                 "#wwz-profile",   "dialed", "Dialed",      "—"),
    ("Caramel Apple Gelato", "#cag-profile",   "calib",  "Calibrating", "Try 430°F endpoint"),
    ("Orange Candy",         "#oc-profile",    "calib",  "Calibrating", "Repeat Run 5 curve to confirm"),
    ("The Hive #1",          "#hive1-profile", "calib",  "Calibrating", "Run 3: steady 430°F flat hold"),
]

# ── SECTIONS ─────────────────────────────────────────────────────────────────

def build_html():
    sections = []

    # ── TOC
    toc_links = [
        ("#dashboard", "Dashboard"),
        ("#constants", "Constants"),
        ("#swab", "Swab Reference"),
        ("#baseline", "Baseline Curve"),
        ("#wwz-profile", "WW Z"),
        ("#wwz-run1", "WW Z Run 1"),
        ("#cag-profile", "Caramel Apple Gelato"),
        ("#cag-run1", "CAG Run 1"),
        ("#cag-run2", "CAG Run 2"),
        ("#oc-profile", "Orange Candy"),
        ("#oc-runs12", "OC Runs 1–2"),
        ("#oc-run3", "OC Run 3"),
        ("#oc-run4", "OC Run 4"),
        ("#oc-run5", "OC Run 5"),
        ("#hive1-profile", "The Hive #1"),
        ("#hive1-run1", "Hive #1 Run 1"),
        ("#hive1-run2", "Hive #1 Run 2"),
        ("#hive1-run3", "Hive #1 Run 3"),
    ]
    toc_links_html = '<ul>'
    for href, label in toc_links:
        toc_links_html += f'<li><a href="{href}">{label}</a></li>'
    toc_links_html += '</ul>'
    toc = f'<div class="section" id="toc">{section_header("Contents")}<div class="toc">{toc_links_html}</div></div>'

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
    s += section_header("WW Z — Strain Profile", "✓ DIALED — Run 1. No further calibration required.", "dialed")
    s += info_table(WWZ_INFO)
    s += '<h3>Inferred Terpene Profile</h3>'
    s += terpene_table(WWZ_TERPS)
    s += '</div>'
    sections.append(s)

    # ── WW Z Run 1
    s = f'<div class="section" id="wwz-run1">'
    s += section_header("WW Z — Run 1 — May 2026", "✓ DIALED — Profile locked.", "dialed")
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

    # ── Caramel Apple Gelato Strain Profile
    s = f'<div class="section" id="cag-profile">'
    s += section_header("Caramel Apple Gelato — Strain Profile", "⚠ IN CALIBRATION — Run 1 complete. Run 2 pending.", "calib", "")
    s += info_table(CAG_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += terpene_table(CAG_TERPS)
    s += '</div>'
    sections.append(s)

    # ── CAG Run 1
    s = f'<div class="section" id="cag-run1">'
    s += section_header("Caramel Apple Gelato — Run 1 — May 2026", "⚠ TOO HOT — Endpoint reduced for Run 2.", "hot", "")
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

    # ── CAG Run 2 Pending
    s = f'<div class="section" id="cag-run2">'
    s += section_header("Caramel Apple Gelato — Run 2 — Pending", "PENDING — Not yet completed.", "pending", "grey")
    s += '<h3>Proposed Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 55 seconds &nbsp;|&nbsp; <strong>Endpoint:</strong> 430°F</p>'
    s += curve_chart_html(CAG_RUN2)
    s += curve_table(CAG_RUN2)
    s += '<h3>Results</h3>'
    s += '<p>Run 2 not yet completed. Record swab color, vapor character, and any session observations. If swab is still darker than target, reduce endpoint further. If flavor remains limited with clean swab, this may be a lower terpene content material — note accordingly and lock curve.</p>'
    s += '</div>'
    sections.append(s)

    # ── Orange Candy Strain Profile
    s = f'<div class="section" id="oc-profile">'
    s += section_header("Orange Candy — Strain Profile", "⚠ IN CALIBRATION — Runs 1–5 complete. Run 6 pending.", "calib", "")
    s += info_table(OC_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += terpene_table(OC_TERPS)
    s += '</div>'
    sections.append(s)

    # ── OC Runs 1 & 2
    s = f'<div class="section" id="oc-runs12">'
    s += section_header("Orange Candy — Runs 1 &amp; 2 — May 2026", "⚠ TOO FLAT — Curve revised for Run 3.", "hot", "")
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
    s += section_header("Orange Candy — Run 3 — May 2026", "⚠ IN CALIBRATION — Close to dialed. Run 4 pending.", "calib", "")
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
    s += section_header("Orange Candy — Run 4 — May 5, 2026", "⚠ IN CALIBRATION — Close to dialed.", "calib", "")
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
    s += section_header("Orange Candy — Run 5 — May 6, 2026", "⚠ IN CALIBRATION — Mixed result. Curve to be repeated as Run 6.", "calib", "")
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

    # ── The Hive #1 Strain Profile
    s = f'<div class="section" id="hive1-profile">'
    s += section_header("The Hive #1 — Strain Profile", "⚠ IN CALIBRATION — Runs 1–2 complete. Run 3 pending.", "calib", "")
    s += info_table(HIVE1_INFO)
    s += '<h3 class="amber">Inferred Terpene Profile</h3>'
    s += '<p class="note">Profile inferred from Honey Banana × Papaya lineage (Bloom Seed Co). Terpene ratios and minor terpenes are not inferable from genetics alone — these are orientation points drawn from the generic cannabis palette, not strain-specific measurements. Start from baseline curve; swab results drive all adjustments.</p>'
    s += terpene_table(HIVE1_TERPS)
    s += '</div>'
    sections.append(s)

    # ── The Hive #1 Run 1
    s = f'<div class="section" id="hive1-run1">'
    s += section_header("The Hive #1 — Run 1 — May 8, 2026", "⚠ IN CALIBRATION — Clean swab. Repeat to confirm.", "calib", "")
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
    s += section_header("The Hive #1 — Run 2 — May 8, 2026", "⚠ IN CALIBRATION — Consistent result. Lower endpoint to explore.", "calib", "")
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

    # ── The Hive #1 Run 3 Pending
    s = f'<div class="section" id="hive1-run3">'
    s += section_header("The Hive #1 — Run 3 — Pending", "PENDING — Not yet completed.", "pending", "grey")
    s += '<h3>Proposed Curve</h3>'
    s += '<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp; <strong>Hold:</strong> 65 seconds &nbsp;|&nbsp; <strong>Setpoint:</strong> 430°F steady (no ramp)</p>'
    s += '<p class="note">Curve shape experiment: steady flat hold at 430°F from session open, rather than the ramped curve used in Runs 1–2. Testing whether a multi-stage ramp produces meaningfully different results from a single sustained setpoint. Swab is a floor indicator only within the normal range — session character is the primary readout.</p>'
    s += curve_chart_html(HIVE1_RUN3)
    s += curve_table(HIVE1_RUN3)
    s += '<h3>Results</h3>'
    s += '<p>Run 3 not yet completed. Record swab color and session character. Compare subjective experience and any harshness against Runs 1–2.</p>'
    s += '<p class="note">Also planned: repeat the Run 1–2 ramp (380→390→410°F) with 430°F endpoint — a separate variable from this steady-hold experiment. Both runs are needed before drawing conclusions about curve shape vs. endpoint temperature.</p>'
    s += '</div>'
    sections.append(s)

    # ── Assemble
    body = dash + toc + ''.join(sections)
    body += f'<div class="footer">Document last updated: {datetime.now().strftime("%B %d, %Y")} &nbsp;·&nbsp; Dabby the House Rig &nbsp;·&nbsp; Hash Rosin — Solventless — Cold Start Protocol</div>'

    cover = '''<div class="cover">
        <h1>Dabby the House Rig</h1>
        <p class="subtitle">Session Profile &amp; Calibration Log</p>
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
