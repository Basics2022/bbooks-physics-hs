
import matplotlib.pyplot as plt
import numpy as np

# Planet data: Semi-major axis (AU) and Orbital period (Years)
planets = {
    'Mercury': (0.387, 0.241),
    'Venus': (0.723, 0.615),
    'Earth': (1.000, 1.000),
    'Mars': (1.524, 1.881),
    'Jupiter': (5.203, 11.86),
    'Saturn': (9.537, 29.46),
    'Uranus': (19.191, 84.01),
    'Neptune': (30.069, 164.8)
}

inner_planet = [ 'Mercury', 'Venus', 'Earth', 'Mars' ]

a_vals = np.array([v[0] for v in planets.values()])
T_vals = np.array([v[1] for v in planets.values()])
names = list(planets.keys())

# Theoretical curve T = a^1.5
a_theory = np.logspace(np.log10(0.3), np.log10(35), 100)
T_theory = a_theory**1.5

# plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(1,3, figsize=(12, 4))

for iplot in range(3):
    # Plot theoretical line
    # ax[iplot].plot(a_theory, T_theory, color='gray', linestyle='--', alpha=0.6, label=r"$\frac{T}{T_0} = {a^{1.5}}{a_0^{1.5}}$ (Kepler's 3rd Law)")
    ax[iplot].plot(a_theory, T_theory, color='gray', linestyle='--', alpha=0.6, label=r"$\frac{T}{T_0} = \frac{a^{1.5}}{a_0^{1.5}}$")
    
    # Plot planet data
    ax[iplot].scatter(a_vals, T_vals, color='firebrick', s=80, zorder=5)
    
    # Label planets
    for i, name in enumerate(names):
        if not (( name in inner_planet ) and ( iplot == 1 )):
            ax[iplot].annotate(name, (a_vals[i], T_vals[i]),
                        xytext=(5, -5), textcoords='offset points',
                        fontsize=11, fontweight='bold')
    
    # Set log scales
    if iplot == 2:
        ax[iplot].set_xscale('log')
        ax[iplot].set_yscale('log')
    
    # Labels and title
    ax[iplot].set_xlabel('Semi-major Axis $a$ (AU)', fontsize=13)
    ax[iplot].set_ylabel('Orbital Period $T$ (Earth Years)', fontsize=13)
    # ax[iplot].set_title('Kepler\'s Third Law of Planetary Motion', fontsize=16, pad=20)
    ax[iplot].legend(fontsize=12)
    
    # Grid and layout
    ax[iplot].grid(True, which="both", ls="-", alpha=0.2)

#> Zoom on inner planets
ax[0].set_xlim(0,2)
ax[0].set_ylim(0,3)
#> Subplot titles
ax[0].set_title("Inner planets")
ax[1].set_title("Outer planets")
ax[2].set_title("Log scale")
# #> Legend
# ax[2].legend(fontsize=12)

fig.suptitle("Kepler's Third Law")

plt.tight_layout()

# Save as png
filename = "kepler_third_law.png"
plt.savefig(filename, dpi=300)
print(f"Plot saved as {filename}")

