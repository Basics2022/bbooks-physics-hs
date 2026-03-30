import numpy as np
import json

# ======================================================================
# 1. ORBITAL PHYSICS & DATA GENERATION
# ======================================================================

earth_orbit_params = { 'a': 1.0000, 'e': 0.0167, 'perihelion_th': 102.9*np.pi/180., 'T': 365 }
mars_orbit_params  = { 'a': 1.5237, 'e': 0.0934, 'perihelion_th': 336.1*np.pi/180., 'T': 687 }

def solve_kepler(M, e, tol=1e-6):
    E = M
    while True:
        delta = E - e * np.sin(E) - M
        if abs(delta) < tol:
            break
        E -= delta / (1 - e * np.cos(E))
    return E

def evaluate_trajectory_1day(orbit_params):
    T = orbit_params['T']
    a = orbit_params['a']
    e = orbit_params['e']
    th0 = orbit_params['perihelion_th']
    n = 2 * np.pi / T
    t = np.linspace(0, T, int(T))
    x, y = [], []
    for t_i in t:
        M = n * t_i
        E = solve_kepler(M, e)
        r = a * (1 - e * np.cos(E))
        theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2),
                               np.sqrt(1 - e) * np.cos(E / 2))
        x.append(r * np.cos(theta))
        y.append(r * np.sin(theta))
    rr = np.array([x, y])
    # Apply rotation for perihelion
    rot = np.array([[np.cos(th0), -np.sin(th0)], [np.sin(th0), np.cos(th0)]])
    return rot @ rr

# Evaluate trajectories
rre = evaluate_trajectory_1day(earth_orbit_params)
rrm = evaluate_trajectory_1day(mars_orbit_params)

# Sampling logic
im0, im0n, im0d = 20, 6, 10
im0v = im0 + np.arange(0, im0n) * im0d
nmars_years = 5
marsT = mars_orbit_params['T']
earthT = earth_orbit_params['T']

th_m_list, th_s_list, mars_init_list = [], [], []

for i0 in im0v:
    ie_points = (i0 + marsT * np.arange(nmars_years)).astype(int) % earthT
    im_point = int(i0 % marsT)
    
    # Angles from Earth to Mars and Earth to Sun
    tm = np.arctan2(rrm[1, im_point] - rre[1, ie_points],
                    rrm[0, im_point] - rre[0, ie_points])
    ts = np.arctan2(-rre[1, ie_points], -rre[0, ie_points])
    
    th_m_list.append(tm.tolist())
    th_s_list.append(ts.tolist())
    mars_init_list.append({'x': rrm[0, im_point], 'y': rrm[1, im_point]})

# Package into JSON
payload = {
    "th_s": th_s_list,
    "th_m": th_m_list,
    "mars_init": mars_init_list,
    "orbit_m": rrm.tolist(),
    "orbit_e": rre.tolist()
}

# ======================================================================
# 2. HTML/JS TEMPLATE (Using Placeholder Replacement)
# ======================================================================

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Kepler Reconstruction - Canvas Engine</title>
    <style>
        body { font-family: -apple-system, sans-serif; display: flex; background: #f8f9fa; margin: 0; height: 100vh; color: #333; }
        #controls { width: 340px; padding: 20px; background: #fff; overflow-y: auto; box-shadow: 2px 0 10px rgba(0,0,0,0.05); }
        #viewport { flex-grow: 1; display: flex; justify-content: center; align-items: center; background: #fff; position: relative; }
        canvas { background: white; border: 1px solid #eee; border-radius: 4px; }
        .group { margin-bottom: 18px; padding: 12px; border-left: 5px solid; background: #fcfcfc; border-radius: 0 4px 4px 0; }
        label { display: block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
        input[type=range] { width: 100%; cursor: pointer; margin-bottom: 10px; }
        .val { float: right; font-family: 'Courier New', monospace; color: #007bff; font-weight: bold; }
        h3 { margin-top: 0; font-size: 18px; }
    </style>
</head>
<body>
<div id="controls">
    <h3>Kepler Reconstruction</h3>
    <p style="font-size: 12px; line-height: 1.4; color: #666;">
        Adjust <b>Mars (large crosses)</b> for each year. 
        Reconstruct Earth's orbit (small crosses) based on 
        the Sun and Mars angles.
    </p>
    <hr style="border:0; border-top:1px solid #eee; margin: 15px 0;">
    <div id="ui"></div>
</div>
<div id="viewport"><canvas id="cv"></canvas></div>

<script>
// Data injected from Python
const DATA = %PAYLOAD%;

const th_s = DATA.th_s;
const th_m = DATA.th_m;
const mars_init = DATA.mars_init;
const orbit_m = DATA.orbit_m;
const orbit_e = DATA.orbit_e;
const colors = ['#4682B4', '#FFA500', '#2E8B57', '#FF4500', '#9370DB', '#00CED1'];

const canvas = document.getElementById('cv');
const ctx = canvas.getContext('2d');
canvas.width = 800; canvas.height = 800;
const scale = 180; // Pixels per AU

let marsPos = mars_init.map(p => ({...p}));

// Build UI
const ui = document.getElementById('ui');
marsPos.forEach((p, i) => {
    const div = document.createElement('div');
    div.className = 'group'; 
    div.style.borderColor = colors[i % colors.length];
    div.innerHTML = `
        <label>Year ${i} Mars X <span class="val" id="vx${i}">${p.x.toFixed(3)}</span></label>
        <input type="range" min="-2.2" max="2.2" step="0.001" value="${p.x}" oninput="update(${i}, 'x', this.value)">
        <label>Year ${i} Mars Y <span class="val" id="vy${i}">${p.y.toFixed(3)}</span></label>
        <input type="range" min="-2.2" max="2.2" step="0.001" value="${p.y}" oninput="update(${i}, 'y', this.value)">
    `;
    ui.appendChild(div);
});

function update(i, axis, val) {
    marsPos[i][axis] = parseFloat(val);
    document.getElementById('v' + axis + i).innerText = marsPos[i][axis].toFixed(3);
}

function drawCross(x, y, s, col, lw, isRef=false) {
    ctx.beginPath();
    ctx.strokeStyle = isRef ? '#f0f0f0' : '#000';
    ctx.lineWidth = lw + 1.5;
    ctx.moveTo(x-s, y); ctx.lineTo(x+s, y);
    ctx.moveTo(x, y-s); ctx.lineTo(x, y+s);
    ctx.stroke();

    ctx.beginPath();
    ctx.strokeStyle = col;
    ctx.lineWidth = lw;
    ctx.moveTo(x-s, y); ctx.lineTo(x+s, y);
    ctx.moveTo(x, y-s); ctx.lineTo(x, y+s);
    ctx.stroke();
}

function drawCircle(x, y, r, col, lw) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = lw + 1.5;
    ctx.stroke();
    ctx.fillStyle = col;
    ctx.fill();
    ctx.lineWidth = lw;
    ctx.strokeStyle = col; // Optional: subtle ring
    ctx.stroke();
}

function render() {
    ctx.clearRect(0, 0, 800, 800);
    const cx = 400, cy = 400;

    // Draw Mars Orbit (faint background)
    ctx.beginPath();
    ctx.strokeStyle = '#e0e0e0';// '#f5f5f5';
    ctx.lineWidth = 2.5;
    for(let i=0; i<orbit_m[0].length; i++) {
        ctx.lineTo(cx + orbit_m[0][i]*scale, cy - orbit_m[1][i]*scale);
    }
    ctx.stroke();
    
    // Draw Earth Orbit (faint background)
    ctx.beginPath();
    ctx.strokeStyle = '#e0e0e0';// '#f5f5f5';
    ctx.lineWidth = 2.5;
    for(let i=0; i<orbit_m[0].length; i++) {
        ctx.lineTo(cx + orbit_e[0][i]*scale, cy - orbit_e[1][i]*scale);
    }
    ctx.stroke();

    // Draw Sun
    ctx.fillStyle = '#333';
    ctx.beginPath(); ctx.arc(cx, cy, 6, 0, Math.PI*2); ctx.fill();

    // Process each year
    marsPos.forEach((p, i) => {
        const mx = p.x, my = p.y;
        const mPx = cx + mx * scale, mPy = cy - my * scale;
        const color = colors[i % colors.length];

        th_s[i].forEach((ts, j) => {
            const tm = th_m[i][j];
            const det = Math.cos(ts)*Math.sin(tm) - Math.sin(ts)*Math.cos(tm);
            const dist = (-Math.sin(tm)*mx + Math.cos(tm)*my) / det;
            
            // Earth coordinates
            const ex = dist * -Math.cos(ts);
            const ey = dist * -Math.sin(ts);
            const ePx = cx + ex * scale, ePy = cy - ey * scale;

            // Sight Lines
            ctx.setLineDash([2, 3]);
            ctx.strokeStyle = '#eee';
            ctx.lineWidth = 2.5;
            ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(ePx, ePy); ctx.stroke();
            
            ctx.strokeStyle = color + '66'; // Transparent color for Mars-Earth line
            ctx.beginPath(); ctx.moveTo(mPx, mPy); ctx.lineTo(ePx, ePy); ctx.stroke();
            ctx.setLineDash([]);

            // Earth Data Point (Small Circles)
            drawCircle(ePx, ePy, 6, color, 1.5);
        });

        // "Truth" Reference (Faint Gray)
        const refX = cx + mars_init[i].x * scale;
        const refY = cy - mars_init[i].y * scale;
        drawCross(refX, refY, 15, color, 1, true);
        //drawCross(refX, refY, 10, '#f0f0f0', 1, true);

        // Interactive Mars Point (Circles)
        drawCircle(mPx, mPy, 8, color, 3);
    });

    requestAnimationFrame(render);
}

render();
</script>
</body>
</html>
"""

# ======================================================================
# 3. SAVE TO FILE
# ======================================================================

final_output = html_template.replace("%PAYLOAD%", json.dumps(payload))

filename = "mars_recon_canvas.html"
with open(filename, "w") as f:
    f.write(final_output)

print(f"Success! {filename} created.")
