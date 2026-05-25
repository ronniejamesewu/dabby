#!/usr/bin/env python3
"""
Dabby the House Rig — Session Log Generator
Produces index.html — a mobile-responsive, screen-optimized web document.
Data lives in Dabby_Data.py; this file is rendering logic only.
To log a new run: edit Dabby_Data.py, then add the run section in build_html().
"""

from datetime import datetime, date, timezone, timedelta

from Dabby_Data import *
from Dabby_Data import _ACCENT_RESOLVED, _resolve_accent_colors  # underscore names are skipped by wildcard import
import Dabby_Data

from Dabby_Archive import ARCHIVED_RUNS, ARCHIVED_STATUS
COMPLETED_RUNS   = ARCHIVED_RUNS + COMPLETED_RUNS
STRAIN_STATUS    = ARCHIVED_STATUS + STRAIN_STATUS
_ACCENT_RESOLVED = _resolve_accent_colors(STRAIN_STATUS)   # re-run over full combined list

_RIG_LABELS = [(RIG_1, "Rig 1"), (RIG_2, "Rig 2"), (RIG_3, "Rig 3")]

def _fmt_equipment_display(eq):
    """Human-readable equipment string from EquipmentConfig. Format: 'Rig N — insert · cap · pearls · glass'."""
    rig_label = next((label for rig, label in _RIG_LABELS if rig == eq), None)

    ins = eq.insert
    if ins.model == "stock":
        insert_str = f"{ins.brand} stock {ins.material}"
    else:
        insert_str = f"{ins.brand} {ins.model}"

    cap = eq.carb_cap
    if cap.airflow == "stock":
        cap_str = f"{cap.brand} {cap.model}"
    else:
        cap_str = f"{cap.brand} {cap.model} ({cap.airflow} airflow)"

    pearl_parts = [f"{p.diameter_mm}mm {p.material} pearl" for p in eq.pearls]
    segments = [insert_str, cap_str]
    if pearl_parts:
        segments.append(" + ".join(pearl_parts))
    segments.append(eq.glass_top)

    body = " \N{MIDDLE DOT} ".join(segments)
    if rig_label:
        return f"{rig_label} \N{EM DASH} {body}"
    return body

# ── HELPERS ────────────────────────────────────────────────────────────────

def _classify_curve_shape(waypoints):
    temps = [wp.temp_f for wp in waypoints]
    if len(temps) < 2:
        return "Hold"
    diffs = [temps[i+1] - temps[i] for i in range(len(temps)-1)]
    signs = [1 if d > 0 else (-1 if d < 0 else 0) for d in diffs]
    groups = [signs[0]]
    for s in signs[1:]:
        if s != groups[-1]:
            groups.append(s)
    if len(groups) > 4:
        return "Complex"
    names = {1: "Ramp Up", -1: "Ramp Down", 0: "Hold"}
    return " + ".join(names[g] for g in groups)

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
    if dab_notes:
        s += result_row("Notes on What's Next:", dab_notes)
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

    MDT = timezone(timedelta(hours=-6))
    timed_runs = [r for r in COMPLETED_RUNS if r.utc_logged_at is not None]
    if timed_runs:
        def _tod_min(r): local = r.utc_logged_at.astimezone(MDT); return local.hour * 60 + local.minute
        earliest_str = min(timed_runs, key=_tod_min).utc_logged_at.astimezone(MDT).strftime('%I:%M %p').lstrip('0')
        latest_str   = max(timed_runs, key=_tod_min).utc_logged_at.astimezone(MDT).strftime('%I:%M %p').lstrip('0')
        day_firsts = {}
        for r in timed_runs:
            key = r.run_date if r.run_date is not None else r.utc_logged_at.astimezone(MDT).date()
            if key not in day_firsts or r.utc_logged_at < day_firsts[key]:
                day_firsts[key] = r.utc_logged_at
        mins = [dt.astimezone(MDT).hour * 60 + dt.astimezone(MDT).minute for dt in day_firsts.values()]
        avg_min = round(sum(mins) / len(mins))
        avg_h, avg_m = divmod(avg_min, 60)
        avg_h12 = avg_h % 12 or 12
        avg_str = f'{avg_h12}:{avg_m:02d} {"AM" if avg_h < 12 else "PM"}'
    else:
        earliest_str = latest_str = avg_str = '&mdash;'

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
        f'<div class="stat-card c7"><div class="stat-value">{earliest_str}</div><div class="stat-label">earliest dab</div></div>'
        f'<div class="stat-card c8"><div class="stat-value">{latest_str}</div><div class="stat-label">latest dab</div></div>'
        f'<div class="stat-card c9"><div class="stat-value">{avg_str}</div><div class="stat-label">avg first dab of the day</div></div>'
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
        rows += (
            f'<div class="strain-row" data-strain="{strain.lower()}" style="--accent:{color}">'
            f'<div class="strain-info">'
            f'<a href="{anchor}" class="strain-name">{strain}{medal}</a>'
            f'<span class="strain-meta">{meta}</span>'
            f'<span class="strain-next">{ss.next_text}</span>'
            f'</div>'
            f'<div class="pill-group">'
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

# ── DATA-DRIVEN RENDER HELPERS ───────────────────────────────────────────────

def has_runs(strain_name):
    return any(r.strain == strain_name for r in COMPLETED_RUNS)

def runs_for(strain_name):
    return [r for r in COMPLETED_RUNS if r.strain == strain_name]

def render_strain_profile(ss):
    accent = _ACCENT_RESOLVED[ss.name]
    s  = f'<div class="section" id="{ss.slug}-profile">'
    s += accent_header(f"{ss.name} — Strain Profile", accent)
    s += info_table(ss.info)
    if ss.terpene_note:
        s += f'<p class="note">{ss.terpene_note}</p>'
    if ss.jar_index:
        s += '<h3>Jar Index</h3>'
        s += ss.jar_index
    s += '</div>'
    return s

def render_run_section(ss, i, run, first_of_day=False):
    if run.run_date:
        date_str = f"{run.run_date.strftime('%B')} {run.run_date.day}, {run.run_date.year}"
    else:
        date_str = run.date_label
    fire       = ' 🔥' if first_of_day else ''
    title      = f"{ss.name} — Run {i} — {date_str}{fire}"
    section_id = f"{ss.slug}-run{i}"

    equipment_str = _fmt_equipment_display(run.equipment)

    c  = session_order_note(run.sessions_prior_today)
    c += '<h3 class="amber">Curve</h3>' if run.too_hot else '<h3>Curve</h3>'
    c += (f'<p><strong>Mode:</strong> {_classify_curve_shape(run.waypoints)} &nbsp;|&nbsp;'
          f' <strong>Duration:</strong> {run.duration_seconds} seconds &nbsp;|&nbsp;'
          f' {run.endpoint_note}</p>')
    c += f'<p><strong>Equipment:</strong> {equipment_str}</p>'
    c += curve_chart_html(run.waypoints)
    c += curve_table(run.waypoints, amber=run.too_hot)
    c += '<h3 class="amber">Results</h3>' if run.too_hot else '<h3>Results</h3>'
    if run.swab:
        c += result_row("Swab:", run.swab, amber=run.too_hot)
    if run.session_char:
        c += result_row("Session:", run.session_char, amber=run.too_hot)
    if run.intensity is not None:
        c += result_row("Intensity:", run.intensity, amber=run.too_hot)
    if run.read:
        c += result_row("Read:", run.read, amber=run.too_hot)
    if run.verdict:
        c += result_row("Verdict:", run.verdict, amber=run.too_hot)
    if run.extra_rows:
        for label, value in run.extra_rows:
            c += result_row(label, value, amber=run.too_hot)
    if run.dab_notes:
        c += result_row("Notes on this dab:", run.dab_notes)
    if run.analysis:
        c += result_row("AI Run Analysis:", run.analysis)
    return collapsible_section(section_id, title, c)

def render_what_to_try_next(ss):
    accent = _ACCENT_RESOLVED[ss.name]
    return what_to_try_next_html(
        f"{ss.slug}-next",
        dab_notes=ss.next_dab_notes,
        ai_analysis=ss.next_ai_analysis,
        proposed_waypoints=ss.next_waypoints,
        accent=accent,
    )

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


def rig_reference_html():
    """Collapsible Rig Reference block — one table row per RIG_N constant."""
    def _short_date(d):
        return d.strftime('%b %d, %Y').replace(' 0', ' ')

    rig_stats = {label: {"runs": [], "dates": []} for _, label in _RIG_LABELS}
    for run in COMPLETED_RUNS:
        for rig, label in _RIG_LABELS:
            if run.equipment == rig:
                rig_stats[label]["runs"].append(run)
                if run.run_date is not None:
                    rig_stats[label]["dates"].append(run.run_date)
                break

    rows = ""
    for rig, label in _RIG_LABELS:
        ins = rig.insert
        cap = rig.carb_cap

        insert_cell = (f"{ins.brand} stock {ins.material}" if ins.model == "stock"
                       else f"{ins.brand} {ins.model}")

        cap_cell = (f"{cap.brand} {cap.model}" if cap.airflow == "stock"
                    else f"{cap.brand} {cap.model}<br><small>{cap.airflow} airflow</small>")

        pearl_cell = (" + ".join(f"{p.diameter_mm}mm {p.material}" for p in rig.pearls)
                      or "&mdash;")

        stats = rig_stats[label]
        n     = len(stats["runs"])
        dates = stats["dates"]
        if n == 0:
            active_cell = "not yet used"
        elif not dates:
            active_cell = f"{n} run{'s' if n != 1 else ''} (dates unknown)"
        else:
            first     = _short_date(min(dates))
            last      = _short_date(max(dates))
            date_span = first if first == last else f"{first} &ndash; {last}"
            active_cell = f"{date_span}<br><small>{n} run{'s' if n != 1 else ''}</small>"

        rows += (
            f'<tr>'
            f'<td style="white-space:nowrap"><strong>{label}</strong></td>'
            f'<td>{insert_cell}</td>'
            f'<td>{cap_cell}</td>'
            f'<td>{pearl_cell}</td>'
            f'<td>{rig.glass_top}</td>'
            f'<td>{active_cell}</td>'
            f'</tr>'
        )

    table = (
        '<div class="terp-ref-wrap">'
        '<table class="terp-ref-table"><thead><tr>'
        '<th style="white-space:nowrap">Rig</th><th>Insert</th><th>Carb Cap</th>'
        '<th>Pearls</th><th>Glass Top</th><th>Active</th>'
        f'</tr></thead><tbody>{rows}</tbody></table></div>'
    )
    note = (
        '<p class="note">Physical equipment configuration per rig. '
        'Two runs are directly comparable only when their EquipmentConfig matches exactly &mdash; '
        'insert, carb cap, pearls, and glass top are all confound boundaries.</p>'
    )
    return collapsible_section("rig-ref", "Rig Reference", note + table, header_class="grey")


def build_html():
    validate()
    validate_accent_colors()
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
    c += f'<p><strong>Mode:</strong> {_classify_curve_shape(BASELINE_CURVE)} &nbsp;|&nbsp; <strong>Duration:</strong> {BASELINE_CURVE[-1].time_s} seconds &nbsp;|&nbsp; <strong>Open:</strong> {BASELINE_CURVE[0].temp_f}°F &nbsp;|&nbsp; <strong>Endpoint:</strong> {BASELINE_CURVE[-1].temp_f}°F</p>'
    c += curve_chart_html(BASELINE_CURVE)
    c += curve_table(BASELINE_CURVE)
    c += '<p class="note">Terpene zone annotations in individual run curves are approximate orientation points — not measured targets. The same common cannabis terpenes appear across most strains. Annotations reflect boiling point ranges, not confirmed strain-specific data.</p>'
    c += '<h3>Rationale</h3>'
    c += '<p>380°F opening and fast 20-second ramp reflect the shape that has performed best across strains in the log. 416°F endpoint sits below the cross-strain harshness boundary (≥430°F produced tail harshness on seven strains). All waypoints are starting points — swab results drive adjustment.</p>'
    sections.append(collapsible_section("baseline", "Baseline Curve", c, header_class="grey"))

    # Terpene Reference
    sections.append(terpene_reference_html())

    # Rig Reference
    sections.append(rig_reference_html())

    # ── First-of-day detection ────────────────────────────────────────────────
    _seen_dates = set()
    _first_of_day = set()
    for _r in COMPLETED_RUNS:
        if _r.run_date is not None and _r.run_date not in _seen_dates:
            _first_of_day.add(id(_r))
            _seen_dates.add(_r.run_date)

    # ── Strain sections (data-driven) ────────────────────────────────────────
    for _ss in STRAIN_STATUS:
        sections.append(render_strain_profile(_ss))
        for _i, _run in enumerate(runs_for(_ss.name), start=1):
            sections.append(render_run_section(_ss, _i, _run, first_of_day=id(_run) in _first_of_day))
        sections.append(render_what_to_try_next(_ss))

    # ── Assemble ──────────────────────────────────────────────────────────────
    body = dash + ''.join(sections)
    body += f'<div class="footer">Document last updated: {datetime.now().strftime("%B %d, %Y")} &nbsp;·&nbsp; Dabby the House Rig</div>'

    cover = '''<div class="cover">
        <h1>Dabby the House Rig</h1>
        <p class="subtitle">Session Log</p>
    </div>'''

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dabby the House Rig — Session Log</title>
<link rel="stylesheet" href="style.css">
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

# ── HANDOFF STATE ────────────────────────────────────────────────────────────

def generate_handoff_state():
    """Return HANDOFF_STATE.md as a string — machine-generated from Dabby_Data.py."""
    MDT = timezone(timedelta(hours=-6))
    now_mdt = datetime.now(MDT)

    run_counts, last_dates, last_equipment = {}, {}, {}
    for run in COMPLETED_RUNS:
        name = run.strain
        run_counts[name] = run_counts.get(name, 0) + 1
        if run.run_date is not None:
            if name not in last_dates or run.run_date > last_dates[name]:
                last_dates[name] = run.run_date
        last_equipment[name] = run.equipment  # last entry wins

    total = len(COMPLETED_RUNS)
    all_dates = [r.run_date for r in COMPLETED_RUNS if r.run_date is not None]
    first_date = min(all_dates) if all_dates else None
    last_date  = max(all_dates) if all_dates else None
    active_strains = [ss for ss in STRAIN_STATUS if run_counts.get(ss.name, 0) > 0]

    def fmt_date(d):
        return d.strftime('%B %d, %Y').replace(' 0', ' ') if d else "unknown"

    def fmt_equipment(eq):
        if eq is None:
            return "unknown"
        return _fmt_equipment_display(eq)

    lines = []
    lines.append("# Dabby — Session State")
    lines.append("*Generated by `Dabby_Log_Generator.py` — do not edit by hand.*")
    lines.append(f"*Last generated: {now_mdt.strftime('%B %d, %Y').replace(' 0', ' ')} at {now_mdt.strftime('%I:%M %p').lstrip('0')} MDT*")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- **Total runs:** {total} across {len(active_strains)} strains")
    if first_date:
        days = (last_date - first_date).days + 1
        lines.append(f"- **Active since:** {fmt_date(first_date)} ({days} days)")
        lines.append(f"- **Last run date:** {fmt_date(last_date)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Strain Status")
    lines.append("")

    for ss in active_strains:
        n  = run_counts[ss.name]
        ld = last_dates.get(ss.name)
        eq = last_equipment.get(ss.name)
        session_word = "session" if n == 1 else "sessions"

        lines.append(f"### {ss.name}")
        lines.append(f"**{n} {session_word}** &nbsp;·&nbsp; Last: {fmt_date(ld)} &nbsp;·&nbsp; Equipment: {fmt_equipment(eq)}")
        lines.append("")
        lines.append(f"**Next:** {ss.next_text}")
        lines.append("")
        if ss.next_dab_notes:
            lines.append(f"**Dab Notes:** {ss.next_dab_notes}")
            lines.append("")
        if ss.next_ai_analysis:
            lines.append(f"**AI Analysis:** {ss.next_ai_analysis}")
            lines.append("")
        if ss.next_waypoints:
            lines.append("**Proposed Curve:**")
            for wp in ss.next_waypoints:
                lines.append(f"- {wp.time_s}s → {wp.temp_f}°F — {wp.note}")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)

# ── WRITE ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    html = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Written: index.html")

    state = generate_handoff_state()
    with open("HANDOFF_STATE.md", "w", encoding="utf-8") as f:
        f.write(state)
    print("Written: HANDOFF_STATE.md")
