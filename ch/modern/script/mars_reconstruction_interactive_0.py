import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import json



# ======================================================================
#> Earth and Mars data
earth_orbit_params = { 'a': 1.0000, 'e': 0.0167, 'perihelion_th': 102.9*np.pi/180., 'T': 365 }
mars_orbit_params  = { 'a': 1.5237, 'e': 0.0934, 'perihelion_th': 336.1*np.pi/180., 'T': 687 }

# Evaluate points
def solve_kepler(M, e, tol=1e-6):
    """ Solve Kepler's equation using Newton's method """
    E = M
    while True:
        delta = E - e * np.sin(E) - M
        if abs(delta) < tol:
            break
        E -= delta / (1 - e * np.cos(E))
    return E

def evaluate_trajectory_1day(orbit_params):
    """ Return x,y coordinates of points of the orbits with time step = 1 day """

    # Find points on a orbit
    T = orbit_params['T']
    a = orbit_params['a']
    e = orbit_params['e']
    th0 = orbit_params['perihelion_th']
    n = 2 * np.pi / T
    t = np.linspace(0, T, int(T))

    # Arrays to store positions
    x, y = [], []

    for t_i in t:
        M = n * t_i             # Mean anomaly
        E = solve_kepler(M, e)  # Eccentric anomaly
        # Convert to polar coordinates
        r = a * (1 - e * np.cos(E))
        theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2),
                              np.sqrt(1 - e) * np.cos(E / 2))
        # Convert to cartesian coordinates
        x.append(r * np.cos(theta))
        y.append(r * np.sin(theta))

    rr = np.array([x, y])

    return np.array([ [np.cos(th0), -np.sin(th0)], [np.sin(th0),  np.cos(th0)] ]) @ rr

#> Evaluate trajectories
rre = evaluate_trajectory_1day(earth_orbit_params)
rrm = evaluate_trajectory_1day(mars_orbit_params)

#> Given initial conditions, sample relative positions every Mars year
im0 = 20
im0n, im0d = 6, 10
im0v = im0 + np.arange(0, im0n) * im0d
nmars_years = 5
marsT = mars_orbit_params['T']
earthT = earth_orbit_params['T']

ie_points = {}
im_points = {}
th_m_dict = {}   # angle of Mars as seen from the Earth
th_s_dict = {}   # angle of Sun as seen from the Earth

#> Evaluate indices of days of Earth and Mars
imars_years = 0
for i0 in im0v:

    #> For each Mars year, find the indices of Earth position in the nmars_years years
    ie_points[imars_years] = ( i0 + marsT * np.arange(nmars_years) ) % earthT
    im_points[imars_years] =   i0 % marsT

    th_m_dict[imars_years] = np.arctan2(
        rrm[1, im_points[imars_years]] - rre[1, ie_points[imars_years]],
        rrm[0, im_points[imars_years]] - rre[0, ie_points[imars_years]])
    th_s_dict[imars_years] = np.arctan2(
        - rre[1,ie_points[imars_years]], - rre[0,ie_points[imars_years]])

    imars_years += 1

th_m = np.array([ th_m_dict[k] for k in th_m_dict.keys()])
th_s = np.array([ th_s_dict[k] for k in th_s_dict.keys()])

print("th_m: \n", th_m)
print("th_s: \n", th_s)

# # --- 1. Create Fake Data ---
# nmars_years = 5
# t = np.linspace(0, 2*np.pi, 100)
# Earth (1 AU) and Mars (1.5 AU) circular orbits
# rre = np.array([np.cos(t), np.sin(t)])
# rrm = np.array([1.5*np.cos(t), 1.5*np.sin(t)])
# # 5 specific points in time
# im_points = [10, 30, 50, 70, 90]

# # Fake angles (th_s = Sun-Earth, th_m = Sun-Mars)
# # Each year has 5 observations
# th_s = np.array([np.linspace(0, np.pi/2, 5) + i for i in range(5)])
# th_m = np.array([np.linspace(0, np.pi/4, 5) + i for i in range(5)])


# ======================================================================
# --- 2. Build Plotly Figure ---
fig = go.Figure()

# Static Orbits
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='black', size=10), name='Sun'))
fig.add_trace(go.Scatter(x=rre[0], y=rre[1], mode='lines', line=dict(dash='dash', color='gray'), name='Earth Orbit'))
fig.add_trace(go.Scatter(x=rrm[0], y=rrm[1], mode='lines', line=dict(dash='dash', color='orange'), name='Mars Orbit'))

# Interactive Years
colors = [ 'steelblue', 'orange', 'green', 'red', 'purple'  ] # 'red', 'blue', 'green', 'purple', 'magenta']
for i in range(nmars_years):
    ix, iy = rrm[0, im_points[i]], rrm[1, im_points[i]]
    # Mars Trace (Indices: 3, 5, 7, 9, 11)
    fig.add_trace(go.Scatter(x=[ix], y=[iy], mode='markers', 
                             marker=dict(size=12, color=colors[i], line=dict(width=2, color='black')), name=f'Mars Yr {i}'))
    # Earth Reconstruction Trace (Indices: 4, 6, 8, 10, 12)
    fig.add_trace(go.Scatter(x=[0]*5, y=[0]*5, mode='markers', 
                             marker=dict(size=12, color=colors[i], opacity=0.7), name=f'Earth Recon {i}'))

#> Reference positions
for i in range(nmars_years):
    ix, iy = rrm[0, im_points[i]], rrm[1, im_points[i]]
    # Mars Trace (Indices: 3, 5, 7, 9, 11)
    fig.add_trace(go.Scatter(x=[ix], y=[iy], mode='markers',
                             marker=dict(size=14, color=colors[i], symbol='cross',), name=f'Mars Yr {i} Ref.'))

# --- 3. Add 10 Sliders (X on Left, Y on Right) ---
sliders = []
v_range = np.linspace(-2., 2.0, 201)
for i in range(nmars_years):
    ix, iy = rrm[0, im_points[i]], rrm[1, im_points[i]]
    idx_x = (np.abs(v_range - ix)).argmin()
    idx_y = (np.abs(v_range - iy)).argmin()
    
    # X Slider
    sliders.append(dict(
        active=int(idx_x), currentvalue={"prefix": f"Yr{i} X: "},
        len=0.4, x=0.05, y=-0.1-(i*0.15),
        steps=[dict(label=f"Y{i}X", method="restyle", args=[{"x": [[v]]}, [3+i*2]]) for v in v_range]
    ))
    # Y Slider
    sliders.append(dict(
        active=int(idx_y), currentvalue={"prefix": f"Yr{i} Y: "},
        len=0.4, x=0.55, y=-0.1-(i*0.15),
        steps=[dict(label=f"Y{i}Y", method="restyle", args=[{"y": [[v]]}, [3+i*2]]) for v in v_range]
    ))

fig.update_layout(sliders=sliders, height=900, margin=dict(b=450, t=50),
                  xaxis=dict(range=[-2.5, 2.5], scaleanchor="y", scaleratio=1),
                  yaxis=dict(range=[-2.5, 2.5]), template="plotly_white",
                  title="Mars Orbital Reconstruction (Standalone Demo)")

# --- 4. JavaScript Logic Injection ---
js_th_s = json.dumps(th_s.tolist())
js_th_m = json.dumps(th_m.tolist())

# Logic: reconstructs Earth points whenever a slider is moved
# Based on your RMat logic: (r11*mx + r12*my) * [-cos(th_s), -sin(th_s)]
post_script = f"""
    var gd = document.getElementsByClassName('plotly-graph-div')[0];
    var th_s = {js_th_s};
    var th_m = {js_th_m};

    function updateEarth(year) {{
        var mx = gd.data[3 + year*2].x[0];
        var my = gd.data[3 + year*2].y[0];
        var ex = [], ey = [];

        for (var j = 0; j < th_s[year].length; j++) {{
            var ts = th_s[year][j];
            var tm = th_m[year][j];

            // Determinant of RMat
            var det = Math.cos(ts)*Math.sin(tm) - Math.sin(ts)*Math.cos(tm);
            // Result of [ -sin(tm), cos(tm) ] / det dot [mx, my]
            var earth_dist = (-Math.sin(tm) * mx + Math.cos(tm) * my) / det;

            ex.push(earth_dist * -Math.cos(ts));
            ey.push(earth_dist * -Math.sin(ts));
        }}
        Plotly.restyle(gd, {{'x': [ex], 'y': [ey]}}, [4 + year*2]);
    }}

    // Watch for slider changes
    gd.on('plotly_sliderchange', function(e) {{
        var label = e.step.label; // e.g., "Y0X"
        var yr = parseInt(label.charAt(1));
        updateEarth(yr);
    }});

    // Initial run to show starting Earth points
    for (var i=0; i<{nmars_years}; i++) {{ updateEarth(i); }}
"""

fig.write_html("mars_recon_demo.html", post_script=post_script, include_plotlyjs='cdn')
print("Successfully created 'mars_recon_demo.html'")
