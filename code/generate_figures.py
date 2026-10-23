#!/usr/bin/env python3
"""
Generates publication-quality figures for the repeated-root manuscript:
1. fig_state_diagram.png - Directed state-transition graph for M=2 and M=3 factor selections.
2. fig_hull_distribution.png - Joint code-dimension vs hull-dimension heatmap and conditional mean profile.
3. fig_asymptotic_moments.png - Asymptotic mean hull ratio E[H]/n and variance scaling vs multiplicity M.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import os

os.makedirs("figures", exist_ok=True)
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'text.usetex': False
})

# ------------------------------------------------------------------------------
# Figure 1: State Transition Graph for M=2
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-1.5, 2.5)
ax.axis('off')

# State positions
positions = {0: (0.5, 0.5), 1: (2.0, 1.5), 2: (3.5, 0.5)}

# Draw states (circles)
for state, (px, py) in positions.items():
    circle = plt.Circle((px, py), 0.35, color='#1f77b4', ec='black', lw=2, zorder=4)
    ax.add_patch(circle)
    ax.text(px, py, f"$u = {state}$", color='white', weight='bold', ha='center', va='center', fontsize=12, zorder=5)

# Self loops and edges
# Transitions for M=2:
# 0 -> 0: weight 1
# 0 -> 1: x^d y^d
# 0 -> 2: x^2d y^2d
# 1 -> 0: 1
# 1 -> 1: x^d y^d
# 1 -> 2: x^2d y^d
# 2 -> 0: 1
# 2 -> 1: x^d
# 2 -> 2: x^2d

# Draw arrows and annotations
# Edge 0 -> 1
ax.annotate("", xy=(1.75, 1.3), xytext=(0.75, 0.7),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#2ca02c', shrinkA=5, shrinkB=5))
ax.text(1.1, 1.15, r"$x^d y^d$", color='#2ca02c', weight='bold', fontsize=11)

# Edge 1 -> 0
ax.annotate("", xy=(0.65, 0.8), xytext=(1.65, 1.4),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#d62728', shrinkA=5, shrinkB=5, ls='--'))
ax.text(1.1, 0.65, r"$1$", color='#d62728', weight='bold', fontsize=11)

# Edge 1 -> 2
ax.annotate("", xy=(3.25, 0.7), xytext=(2.25, 1.3),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#2ca02c', shrinkA=5, shrinkB=5))
ax.text(2.9, 1.15, r"$x^{2d} y^d$", color='#2ca02c', weight='bold', fontsize=11)

# Edge 2 -> 1
ax.annotate("", xy=(2.35, 1.4), xytext=(3.35, 0.8),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#d62728', shrinkA=5, shrinkB=5, ls='--'))
ax.text(2.9, 0.65, r"$x^d$", color='#d62728', weight='bold', fontsize=11)

# Edge 0 -> 2 (horizontal bottom curve)
ax.annotate("", xy=(3.15, 0.35), xytext=(0.85, 0.35),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#9467bd', connectionstyle="arc3,rad=-0.3", shrinkA=5, shrinkB=5))
ax.text(2.0, -0.2, r"$x^{2d} y^{2d}$", color='#9467bd', weight='bold', ha='center', fontsize=11)

# Edge 2 -> 0 (horizontal bottom curve)
ax.annotate("", xy=(0.85, 0.2), xytext=(3.15, 0.2),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#8c564b', connectionstyle="arc3,rad=-0.5", shrinkA=5, shrinkB=5, ls='--'))
ax.text(2.0, -0.65, r"$1$", color='#8c564b', weight='bold', ha='center', fontsize=11)

# Self loops
# 0 -> 0
ax.annotate("", xy=(0.3, 0.8), xytext=(0.3, 0.2),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black', connectionstyle="arc3,rad=1.8", shrinkA=5, shrinkB=5))
ax.text(-0.25, 0.5, r"$1$", color='black', weight='bold', fontsize=11)

# 1 -> 1
ax.annotate("", xy=(1.8, 1.8), xytext=(2.2, 1.8),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black', connectionstyle="arc3,rad=1.8", shrinkA=5, shrinkB=5))
ax.text(2.0, 2.3, r"$x^d y^d$", color='black', weight='bold', ha='center', fontsize=11)

# 2 -> 2
ax.annotate("", xy=(3.7, 0.2), xytext=(3.7, 0.8),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black', connectionstyle="arc3,rad=1.8", shrinkA=5, shrinkB=5))
ax.text(4.25, 0.5, r"$x^{2d}$", color='black', weight='bold', fontsize=11)

ax.set_title(r"State Transition Diagram $\mathbf{T}_{2, d}(x, y)$ for Multiplicity $M = 2$", pad=15)
plt.tight_layout()
fig.savefig("figures/fig_state_diagram.png", bbox_inches='tight')
plt.close(fig)
print("=> figures/fig_state_diagram.png generated.")

# ------------------------------------------------------------------------------
# Figure 2: Joint Distribution Heatmap and Moments for n=42 over F2 (M=2)
# ------------------------------------------------------------------------------
from verify_all import compute_family_enumerator, poly_to_dict

orbit_data_42 = [(1, 1), (2, 1), (3, 2), (6, 1), (6, 2)]
Phi_42 = compute_family_enumerator(orbit_data_42, 2)
dist_42 = poly_to_dict(Phi_42)

dims = range(43)
hulls = range(43)
grid = np.zeros((43, 43))
for (k, h), count in dist_42.items():
    if k <= 42 and h <= 42:
        grid[h, k] = count

# Compute conditional mean and variance
mean_h_vec = np.zeros(43)
std_h_vec = np.zeros(43)
valid_k = []
for k in range(43):
    col = grid[:, k]
    tot = np.sum(col)
    if tot > 0:
        h_vals = np.arange(43)
        mean_h = np.sum(h_vals * col) / tot
        var_h = np.sum((h_vals**2) * col) / tot - mean_h**2
        mean_h_vec[k] = mean_h
        std_h_vec[k] = np.sqrt(max(0, var_h))
        valid_k.append(k)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

# Left: Log-Heatmap
im = ax1.imshow(np.log1p(grid), origin='lower', aspect='auto', cmap='viridis', extent=[0, 42, 0, 42])
ax1.plot([0, 42], [0, 42], color='red', linestyle=':', label='Self-Orthogonal ($h = k$)')
ax1.plot([0, 21, 42], [0, 21, 0], color='orange', linestyle='--', label=r'Theoretical Hull Bound $\min(k, n-k)$')
ax1.set_xlabel("Code Dimension $k$")
ax1.set_ylabel("Galois Hull Dimension $h$")
ax1.set_title(r"(a) Joint Enumerator Heatmap $\log(1 + A_{k, h})$ ($n=42, M=2$)")
ax1.legend(loc='upper right', framealpha=0.9)
cbar = fig.colorbar(im, ax=ax1)
cbar.set_label(r"$\log(1 + \text{Code Count})$")

# Right: Conditional Mean and Standard Deviation
valid_k = np.array(valid_k)
ax2.plot(valid_k, mean_h_vec[valid_k], 'o-', color='#1f77b4', lw=2, label=r"Conditional Mean $\mathbb{E}[H \mid \dim(C) = k]$")
ax2.fill_between(valid_k, np.maximum(0, mean_h_vec[valid_k] - std_h_vec[valid_k]),
                 mean_h_vec[valid_k] + std_h_vec[valid_k], color='#1f77b4', alpha=0.2, label=r"$\pm 1\sigma$ Dispersion Band")
ax2.axhline(y=42 * (5/18), color='#2ca02c', linestyle='--', lw=1.5, label=r"Global Mean $\mathbb{E}[H] = n \cdot \frac{2M+1}{6(M+1)} = 11.67$")
ax2.set_xlabel("Code Dimension $k$")
ax2.set_ylabel("Hull Dimension Statistics")
ax2.set_title(r"(b) Conditional Hull Statistics $\mathbb{E}[H \mid k] \pm \sigma$")
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='lower center', framealpha=0.9)

plt.tight_layout()
fig.savefig("figures/fig_hull_distribution.png", bbox_inches='tight')
plt.close(fig)
print("=> figures/fig_hull_distribution.png generated.")

# ------------------------------------------------------------------------------
# Figure 3: Asymptotic Scaling vs Multiplicity M
# ------------------------------------------------------------------------------
M_vals = np.arange(1, 21)
mean_ratio_orbit_gt1 = (2 * M_vals + 1) / (6 * (M_vals + 1))
mean_ratio_orbit_1_even = (M_vals / (4 * (M_vals + 1)))
mean_ratio_orbit_1_odd = (M_vals - 1) / (4 * M_vals)
mean_ratio_orbit_1 = np.where(M_vals % 2 == 0, mean_ratio_orbit_1_even, mean_ratio_orbit_1_odd)

var_ratio_orbit_gt2 = (M_vals * (M_vals + 2) * (M_vals**2 + 2*M_vals + 2)) / (60 * (M_vals + 1)**2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

# (a) Mean Hull Dimension Ratio
ax1.plot(M_vals, mean_ratio_orbit_gt1, 's-', color='#d62728', lw=2, label=r"Orbits $\ell \geq 2$: $\frac{2M+1}{6(M+1)}$")
ax1.plot(M_vals, mean_ratio_orbit_1, 'o--', color='#1f77b4', lw=2, label=r"Orbits $\ell = 1$: $\frac{\lfloor M^2/4 \rfloor}{M(M+1)}$")
ax1.axhline(y=1/3, color='black', linestyle=':', lw=1.5, label=r"Asymptotic Bound $\lim_{M \to \infty} \frac{\mathbb{E}[H]}{n} = \frac{1}{3}$")
ax1.axhline(y=1/4, color='gray', linestyle='-.', lw=1.5, label=r"Simple-Root Baseline ($M=1$): $\frac{1}{4}$")
ax1.set_xlabel("Multiplicity $M = p^a$")
ax1.set_ylabel(r"Expected Hull Fraction $\mathbb{E}[H] / n_{\mathcal{O}}$")
ax1.set_title(r"(a) Average Hull Dimension Fraction vs Multiplicity $M$")
ax1.set_xticks(range(1, 21, 2))
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='lower right', framealpha=0.9)

# (b) Asymptotic Variance per Step
ax2.plot(M_vals, var_ratio_orbit_gt2, '^-', color='#2ca02c', lw=2, label=r"Effective Variance $\sigma^2_{\mathrm{step}}(M)$ ($\ell \geq 3$)")
ax2.plot(M_vals, (M_vals**2)/60, 'k--', alpha=0.6, label=r"Leading Asymptotic Growth $\sim \frac{M^2}{60}$")
ax2.set_xlabel("Multiplicity $M = p^a$")
ax2.set_ylabel(r"Effective Variance per Step $\sigma^2_{\mathrm{step}}$")
ax2.set_title(r"(b) Variance Scaling per Step vs Multiplicity $M$")
ax2.set_xticks(range(1, 21, 2))
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', framealpha=0.9)

plt.tight_layout()
fig.savefig("figures/fig_asymptotic_moments.png", bbox_inches='tight')
plt.close(fig)
print("=> figures/fig_asymptotic_moments.png generated.")
print("ALL FIGURES GENERATED SUCCESSFULLY.")
