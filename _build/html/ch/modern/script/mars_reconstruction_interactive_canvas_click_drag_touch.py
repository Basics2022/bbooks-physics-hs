import numpy as np
import json

# --- 1. ORBITAL PHYSICS (Same as your previous version) ---
earth_orbit_params = { 'a': 1.0000, 'e': 0.0167, 'perihelion_th': 102.9*np.pi/180., 'T': 365 }
mars_orbit_params  = { 'a': 1.5237, 'e': 0.0934, 'perihelion_th': 336.1*np.pi/180., 'T': 687 }

def solve_kepler(M, e, tol=1e-6):
    E = M
    while True:
        delta = E - e * np.sin(E) - M
        if abs(delta) < tol: break
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
        x.append(r * np.cos(theta)); y.append(r * np.sin(theta))
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
    th_m_list.append(tm.tolist()); th_s_list.append(ts.tolist())
    mars_init_list.append({'x': rrm[0, im_point], 'y': rrm[1, im_point]})

payload = {"th_s": th_s_list, "th_m": th_m_list, "mars_init": mars_init_list, "orbit_m": rrm.tolist(), "orbit_e": rre.tolist()}

# --- 2. HTML/JS TEMPLATE (Touch & Layout Fixed) ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Kepler Reconstruction - Astronomical Symbols</title>
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: sans-serif; display: flex; flex-direction: column; 
            margin: 0; height: 100vh; background: #f0f0f0; overflow: hidden; 
        }
        #viewport { 
            flex: 1; display: flex; justify-content: center; align-items: center; 
            background: #fff; border-bottom: 1px solid #ccc; overflow: hidden;
        }
        canvas { 
            max-width: 100%; max-height: 100%; height: auto; width: auto;
            touch-action: none;
        }
        #controls { 
            height: 180px; min-height: 180px; background: #fff; padding: 10px; 
            overflow-x: auto; white-space: nowrap; 
        }
        #ui { display: inline-flex; gap: 10px; padding-bottom: 10px; }
        .group { 
            display: inline-block; min-width: 140px; padding: 10px; 
            border-top: 4px solid; background: #fafafa; border-radius: 4px;
            font-size: 12px; vertical-align: top;
        }
        .val { color: #007bff; font-weight: bold; float: right; font-family: monospace; }
        h3 { margin: 0 0 8px 0; font-size: 14px; }
    </style>
</head>
<body>
<div id="viewport"><canvas id="cv"></canvas></div>
<div id="controls">
    <h3>Kepler Recon <small style="font-weight:normal; color:#666;">(Drag ♂ symbols)</small></h3>
    <div id="ui"></div>
</div>

<script>
const DATA = %PAYLOAD%;
const th_s = DATA.th_s, th_m = DATA.th_m, mars_init = DATA.mars_init;
const orbit_m = DATA.orbit_m, orbit_e = DATA.orbit_e;
const colors = ['#4682B4', '#FFA500', '#2E8B57', '#FF4500', '#9370DB'];

const canvas = document.getElementById('cv');
const ctx = canvas.getContext('2d');
canvas.width = 800; canvas.height = 800;
const scale = 180; 

let marsPos = mars_init.map(p => ({...p}));
let isDragging = false, selectedIdx = -1;

const ui = document.getElementById('ui');
marsPos.forEach((p, i) => {
    const div = document.createElement('div');
    div.className = 'group'; div.style.borderColor = colors[i % colors.length];
    div.innerHTML = `<b>Year ${i}</b><br>X: <span class="val" id="vx${i}">${p.x.toFixed(2)}</span><br>Y: <span class="val" id="vy${i}">${p.y.toFixed(2)}</span>`;
    ui.appendChild(div);
});

function getCoords(e) {
    const rect = canvas.getBoundingClientRect();
    const clientX = (e.touches ? e.touches[0].clientX : e.clientX);
    const clientY = (e.touches ? e.touches[0].clientY : e.clientY);
    const x = ((clientX - rect.left) * (800 / rect.width) - 400) / scale;
    const y = (400 - (clientY - rect.top) * (800 / rect.height)) / scale;
    return {x, y};
}

function handleStart(e) {
    const {x, y} = getCoords(e);
    marsPos.forEach((p, i) => {
        if (Math.sqrt((p.x - x)**2 + (p.y - y)**2) < 0.25) { isDragging = true; selectedIdx = i; }
    });
}
function handleMove(e) {
    if (!isDragging) return;
    const {x, y} = getCoords(e);
    marsPos[selectedIdx].x = x; marsPos[selectedIdx].y = y;
    document.getElementById('vx'+selectedIdx).innerText = x.toFixed(2);
    document.getElementById('vy'+selectedIdx).innerText = y.toFixed(2);
}
function handleEnd() { isDragging = false; selectedIdx = -1; }

canvas.addEventListener('mousedown', handleStart);
window.addEventListener('mousemove', handleMove);
window.addEventListener('mouseup', handleEnd);
canvas.addEventListener('touchstart', handleStart, {passive: false});
window.addEventListener('touchmove', handleMove, {passive: false});
window.addEventListener('touchend', handleEnd);

// NEW: Function to draw planet symbols
function drawSymbol(x, y, symbol, color, size) {
    ctx.fillStyle = color;
    ctx.font = `${size}px serif`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // Draw a small white backing for readability
    ctx.shadowColor = "white";
    ctx.shadowBlur = 4;
    ctx.fillText(symbol, x, y);
    ctx.shadowBlur = 0;
}

function render() {
    ctx.clearRect(0, 0, 800, 800);
    const cx = 400, cy = 400;

    // --- 1. Labels & Trajectories ---
    ctx.setLineDash([]);
    ctx.lineWidth = 2;
    ctx.font = "italic 12px sans-serif";
    
    // Mars Orbit
    ctx.strokeStyle = '#eee';
    ctx.beginPath();
    for(let i=0; i<orbit_m[0].length; i++) ctx.lineTo(cx + orbit_m[0][i]*scale, cy - orbit_m[1][i]*scale);
    ctx.stroke();
    ctx.fillStyle = "#aaa";
    ctx.fillText("Mars Trajectory", cx + 1.6*scale, cy - 1.2*scale);

    // Earth Orbit
    ctx.beginPath();
    for(let i=0; i<orbit_e[0].length; i++) ctx.lineTo(cx + orbit_e[0][i]*scale, cy - orbit_e[1][i]*scale);
    ctx.stroke();
    ctx.fillText("Earth Trajectory", cx + 0.8*scale, cy - 0.7*scale);

    // Sun Label
    ctx.fillStyle = '#333';
    ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 7); ctx.fill();
    ctx.fillText("Sun (☉)", cx, cy - 15);

    // --- 2. Interaction Data ---
    marsPos.forEach((p, i) => {
        const mx = p.x, my = p.y, color = colors[i % colors.length];
        const mPx = cx + mx * scale, mPy = cy - my * scale;
        
        th_s[i].forEach((ts, j) => {
            const tm = th_m[i][j], det = Math.cos(ts)*Math.sin(tm) - Math.sin(ts)*Math.cos(tm);
            const dist = (-Math.sin(tm)*mx + Math.cos(tm)*my) / det;
            const ex = dist * -Math.cos(ts), ey = dist * -Math.sin(ts);
            
            // Sight lines
            ctx.setLineDash([2, 3]); ctx.strokeStyle = color + '44';
            ctx.beginPath(); ctx.moveTo(mPx, mPy); ctx.lineTo(cx + ex*scale, cy - ey*scale); ctx.stroke();
            
            // Earth Symbols (⊕)
            drawSymbol(cx + ex*scale, cy - ey*scale, "⊕", color, 16);
        });

        // Ref target (Faint Cross)
        ctx.strokeStyle = '#ddd'; ctx.lineWidth = 1; ctx.beginPath();
        let rx = cx + mars_init[i].x*scale, ry = cy - mars_init[i].y*scale;
        ctx.moveTo(rx-8, ry); ctx.lineTo(rx+8, ry); ctx.moveTo(rx, ry-8); ctx.lineTo(rx, ry+8); ctx.stroke();
        
        // Interactive Mars Symbols (♂)
        drawSymbol(mPx, mPy, "♂", color, 24);
    });
    requestAnimationFrame(render);
}
render();
</script>
</body>
</html>
"""

final_output = html_template.replace("%PAYLOAD%", json.dumps(payload))
with open("mars_recon_canvas_click_touch.html", "w") as f: f.write(final_output)
