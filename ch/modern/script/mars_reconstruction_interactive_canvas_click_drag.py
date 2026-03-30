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
    T, a, e, th0 = orbit_params['T'], orbit_params['a'], orbit_params['e'], orbit_params['perihelion_th']
    n = 2 * np.pi / T
    t = np.linspace(0, T, int(T))
    x, y = [], []
    for t_i in t:
        M = n * t_i
        E = solve_kepler(M, e)
        r = a * (1 - e * np.cos(E))
        theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
        x.append(r * np.cos(theta))
        y.append(r * np.sin(theta))
    rr = np.array([x, y])
    rot = np.array([[np.cos(th0), -np.sin(th0)], [np.sin(th0), np.cos(th0)]])
    return rot @ rr

rre = evaluate_trajectory_1day(earth_orbit_params)
rrm = evaluate_trajectory_1day(mars_orbit_params)

im0, im0n, im0d = 20, 6, 10
im0v = im0 + np.arange(0, im0n) * im0d
nmars_years = 5
marsT, earthT = mars_orbit_params['T'], earth_orbit_params['T']

th_m_list, th_s_list, mars_init_list = [], [], []

for i0 in im0v:
    ie_points = (i0 + marsT * np.arange(nmars_years)).astype(int) % earthT
    im_point = int(i0 % marsT)
    tm = np.arctan2(rrm[1, im_point] - rre[1, ie_points], rrm[0, im_point] - rre[0, ie_points])
    ts = np.arctan2(-rre[1, ie_points], -rre[0, ie_points])
    th_m_list.append(tm.tolist())
    th_s_list.append(ts.tolist())
    mars_init_list.append({'x': rrm[0, im_point], 'y': rrm[1, im_point]})

payload = {
    "th_s": th_s_list,
    "th_m": th_m_list,
    "mars_init": mars_init_list,
    "orbit_m": rrm.tolist(),
    "orbit_e": rre.tolist()
}

# ======================================================================
# 2. HTML/JS TEMPLATE
# ======================================================================

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Kepler Reconstruction - Interactive Drag</title>
    <style>
        body { font-family: -apple-system, sans-serif; display: flex; background: #f8f9fa; margin: 0; height: 100vh; overflow: hidden; }
        #controls { width: 320px; min-width: 300px; padding: 20px; background: #fff; overflow-y: auto; border-right: 1px solid #eee; }
        #viewport { flex-grow: 1; display: flex; justify-content: center; align-items: center; background: #f0f0f0; }
        canvas { background: white; border: 1px solid #ddd; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 95%; max-height: 95%; }
        .group { margin-bottom: 12px; padding: 10px; border-left: 5px solid; background: #fafafa; border-radius: 4px; }
        label { display: block; font-size: 11px; font-weight: bold; text-transform: uppercase; color: #666; }
        .val-container { display: flex; justify-content: space-between; margin-top: 5px; font-family: monospace; font-size: 13px; }
        .val { color: #007bff; font-weight: bold; }
        h3 { margin-top: 0; font-size: 18px; }
    </style>
</head>
<body>
<div id="controls">
    <h3>Kepler Reconstruction</h3>
    <p style="font-size: 12px; color: #666;"><b>Click and Drag</b> the colored Mars circles to reconstruct the orbit. Faint crosses represent the target positions.</p>
    <div id="ui"></div>
</div>
<div id="viewport"><canvas id="cv"></canvas></div>

<script>
const DATA = %PAYLOAD%;
const th_s = DATA.th_s, th_m = DATA.th_m, mars_init = DATA.mars_init;
const orbit_m = DATA.orbit_m, orbit_e = DATA.orbit_e;
const colors = ['#4682B4', '#FFA500', '#2E8B57', '#FF4500', '#9370DB', '#00CED1'];

const canvas = document.getElementById('cv');
const ctx = canvas.getContext('2d');
canvas.width = 800; canvas.height = 800;
const scale = 180; 

let marsPos = mars_init.map(p => ({...p}));
let isDragging = false;
let selectedIdx = -1;

// Build UI (Readout only)
const ui = document.getElementById('ui');
marsPos.forEach((p, i) => {
    const div = document.createElement('div');
    div.className = 'group'; div.style.borderColor = colors[i % colors.length];
    div.innerHTML = `
        <label>Year ${i} Mars Position (AU)</label>
        <div class="val-container">
            <span>X: <span class="val" id="vx${i}">${p.x.toFixed(3)}</span></span>
            <span>Y: <span class="val" id="vy${i}">${p.y.toFixed(3)}</span></span>
        </div>
    `;
    ui.appendChild(div);
});

// --- INTERACTION LOGIC ---
function getMousePos(evt) {
    const rect = canvas.getBoundingClientRect();
    // Account for CSS scaling of the canvas
    const cssScaleX = canvas.width / rect.width;
    const cssScaleY = canvas.height / rect.height;
    return {
        x: ((evt.clientX - rect.left) * cssScaleX - 400) / scale,
        y: (400 - (evt.clientY - rect.top) * cssScaleY) / scale
    };
}

canvas.addEventListener('mousedown', (e) => {
    const pos = getMousePos(e);
    marsPos.forEach((p, i) => {
        const d = Math.sqrt((p.x - pos.x)**2 + (p.y - pos.y)**2);
        if (d < 0.15) { isDragging = true; selectedIdx = i; }
    });
});

window.addEventListener('mousemove', (e) => {
    const pos = getMousePos(e);
    
    // Cursor feedback
    let hovering = false;
    marsPos.forEach(p => {
        if (Math.sqrt((p.x - pos.x)**2 + (p.y - pos.y)**2) < 0.15) hovering = true;
    });
    canvas.style.cursor = isDragging ? 'grabbing' : (hovering ? 'grab' : 'default');

    if (!isDragging) return;
    
    marsPos[selectedIdx].x = pos.x;
    marsPos[selectedIdx].y = pos.y;
    document.getElementById('vx' + selectedIdx).innerText = pos.x.toFixed(3);
    document.getElementById('vy' + selectedIdx).innerText = pos.y.toFixed(3);
});

window.addEventListener('mouseup', () => { isDragging = false; selectedIdx = -1; });

// --- DRAWING LOGIC ---
function drawCircle(x, y, r, col, lw, fill=true) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI*2);
    ctx.strokeStyle = '#000'; ctx.lineWidth = lw + 1;
    if (fill) { ctx.fillStyle = col; ctx.fill(); }
    ctx.stroke();
}

function drawCross(x, y, s, col, lw) {
    ctx.beginPath(); ctx.strokeStyle = col; ctx.lineWidth = lw;
    ctx.moveTo(x-s, y); ctx.lineTo(x+s, y);
    ctx.moveTo(x, y-s); ctx.lineTo(x, y+s);
    ctx.stroke();
}

function render() {
    ctx.clearRect(0, 0, 800, 800);
    const cx = 400, cy = 400;

    // Background Orbits
    ctx.lineWidth = 2.5; ctx.strokeStyle = '#e0e0e0';
    [orbit_m, orbit_e].forEach(orbit => {
        ctx.beginPath();
        for(let i=0; i<orbit[0].length; i++) ctx.lineTo(cx + orbit[0][i]*scale, cy - orbit[1][i]*scale);
        ctx.stroke();
    });

    // Sun
    ctx.fillStyle = '#333'; ctx.beginPath(); ctx.arc(cx, cy, 6, 0, 7); ctx.fill();

    marsPos.forEach((p, i) => {
        const mx = p.x, my = p.y, color = colors[i % colors.length];
        const mPx = cx + mx * scale, mPy = cy - my * scale;

        th_s[i].forEach((ts, j) => {
            const tm = th_m[i][j];
            const det = Math.cos(ts)*Math.sin(tm) - Math.sin(ts)*Math.cos(tm);
            const dist = (-Math.sin(tm)*mx + Math.cos(tm)*my) / det;
            const ex = dist * -Math.cos(ts), ey = dist * -Math.sin(ts);
            const ePx = cx + ex * scale, ePy = cy - ey * scale;

            ctx.setLineDash([2, 3]); ctx.lineWidth = 2;
            ctx.strokeStyle = '#eee'; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(ePx, ePy); ctx.stroke();
            ctx.strokeStyle = color + '44'; ctx.beginPath(); ctx.moveTo(mPx, mPy); ctx.lineTo(ePx, ePy); ctx.stroke();
            ctx.setLineDash([]);
            drawCircle(ePx, ePy, 5, color, 1);
        });

        // Ref Cross
        drawCross(cx + mars_init[i].x*scale, cy - mars_init[i].y*scale, 15, color, 4);
        // Interactive Mars Circle
        drawCircle(mPx, mPy, 10, color, 2);
    });
    requestAnimationFrame(render);
}
render();
</script>
</body>
</html>
"""

final_output = html_template.replace("%PAYLOAD%", json.dumps(payload))
with open("mars_recon_canvas_click.html", "w") as f:
    f.write(final_output)
print("Success! Created mars_recon_canvas.html with Click and Drag.")
