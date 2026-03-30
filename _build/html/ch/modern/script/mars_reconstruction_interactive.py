import numpy as np
import plotly.graph_objects as go
import json

# --- 1. Setup (Using your existing data variables) ---
# nmars_years, rre, rrm, th_s, th_m, im_points
# (Ensure these are defined as in previous steps)

fig = go.Figure()

# Background
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='black', size=10), name='Sun'))
fig.add_trace(go.Scatter(x=rre[0], y=rre[1], mode='lines', line=dict(dash='dash', color='gray'), name='Earth Orbit'))
fig.add_trace(go.Scatter(x=rrm[0], y=rrm[1], mode='lines', line=dict(dash='dash', color='orange'), name='Mars Orbit'))

# We will track the index where year-specific traces start
# Static traces = 3 (Sun, Earth Orb, Mars Orb)
start_idx = 3

for i in range(nmars_years):
    color = f'hsla({i*70}, 70%, 50%, 0.8)'
    
    # Trace: Mars Point (Index: start_idx + i*13)
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=12, color=color), name=f'Mars Yr {i}'))
    
    # Trace: Earth Points (Index: start_idx + i*13 + 1)
    fig.add_trace(go.Scatter(x=[0]*5, y=[0]*5, mode='markers', marker=dict(size=6, color=color), name=f'Earth Yr {i}'))
    
    # Traces: 5 Sun-Earth Lines (Indices: +2 to +6)
    for _ in range(5):
        fig.add_trace(go.Scatter(x=[0,0], y=[0,0], mode='lines', line=dict(dash='dot', width=1, color='gray'), showlegend=False))
        
    # Traces: 5 Mars-Earth Lines (Indices: +7 to +11)
    for _ in range(5):
        fig.add_trace(go.Scatter(x=[0,0], y=[0,0], mode='lines', line=dict(dash='dot', width=1, color=color), showlegend=False))

# --- 3. Sliders with Clean Labels ---
sliders = []
v_range = np.linspace(-2.0, 2.0, 41)
for i in range(nmars_years):
    y_pos = -0.15 - (i * 0.15) # Extra spacing
    
    sliders.append(dict(
        active=20, currentvalue={"prefix": f"Year {i} X Position: "},
        len=0.4, x=0.05, y=y_pos, pad={"t": 30},
        steps=[dict(label=f"{v:.2f}", method="restyle", args=[{"x": [[v]]}, [start_idx + i*12]]) for v in v_range]
    ))
    sliders.append(dict(
        active=20, currentvalue={"prefix": f"Year {i} Y Position: "},
        len=0.4, x=0.55, y=y_pos, pad={"t": 30},
        steps=[dict(label=f"{v:.2f}", method="restyle", args=[{"y": [[v]]}, [start_idx + i*12]]) for v in v_range]
    ))

fig.update_layout(sliders=sliders, height=1200, margin=dict(b=650, t=50),
                  xaxis=dict(range=[-2.5, 2.5], scaleanchor="y", scaleratio=1),
                  yaxis=dict(range=[-2.5, 2.5]), template="plotly_white")

# --- 4. JavaScript with Line Logic ---
js_th_s = json.dumps(th_s.tolist())
js_th_m = json.dumps(th_m.tolist())

post_script = f"""
    var gd = document.getElementsByClassName('plotly-graph-div')[0];
    var th_s = {js_th_s};
    var th_m = {js_th_m};

    function update(year) {{
        var m_idx = 3 + year * 12;
        var mx = gd.data[m_idx].x[0];
        var my = gd.data[m_idx].y[0];
        
        var ex_list = [], ey_list = [];
        var sun_lines_x = [], sun_lines_y = [];
        var mars_lines_x = [], mars_lines_y = [];

        for (var j = 0; j < th_s[year].length; j++) {{
            var ts = th_s[year][j], tm = th_m[year][j];
            var det = Math.cos(ts)*Math.sin(tm) - Math.sin(ts)*Math.cos(tm);
            var dist = (-Math.sin(tm)*mx + Math.cos(tm)*my) / det;
            
            var ex = dist * -Math.cos(ts);
            var ey = dist * -Math.sin(ts);
            
            ex_list.push(ex); ey_list.push(ey);
            
            // Prepare line updates
            // Sun-Earth Line: [0, ex], [0, ey]
            Plotly.restyle(gd, {{x: [[0, ex]], y: [[0, ey]]}}, [m_idx + 2 + j]);
            // Mars-Earth Line: [mx, ex], [my, ey]
            Plotly.restyle(gd, {{x: [[mx, ex]], y: [[my, ey]]}}, [m_idx + 7 + j]);
        }}
        
        // Update Earth Points
        Plotly.restyle(gd, {{x: [ex_list], y: [ey_list]}}, [m_idx + 1]);
    }}

    gd.on('plotly_sliderchange', e => {{
        // Extract Year from label: "Year 0 X Position" -> 0
        var yr = parseInt(e.step.label.split(' ')[0]) || 0; 
        // Note: For labels, we use the Step Index or a simple parse
        update(yr);
    }});
    
    for(var i=0; i<{nmars_years}; i++) {{ update(i); }}
"""

fig.write_html("mars_reconstruction.html", post_script=post_script, include_plotlyjs='cdn')
