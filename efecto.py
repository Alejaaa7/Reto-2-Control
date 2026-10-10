import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import signal


def respuesta_escalon(sigma, wd, t):
    # Respuesta al escalón unitario de G(s) con polos -sigma ± j*wd
    wn2 = sigma**2 + wd**2
    G = signal.TransferFunction([wn2], [1, 2 * sigma, wn2])
    return signal.step(G, T=t)[1]


def sobrepico(sigma, wd):
    # Mp = exp(-pi*zeta / sqrt(1 - zeta^2))
    zeta = sigma / np.hypot(sigma, wd)
    return np.exp(-np.pi * zeta / np.sqrt(1 - zeta**2))


t = np.linspace(0, 6, 1500)
referencia = (1, 4)  # (sigma, wd)

casos = [
    ("A) Misma parte real σ, distinta ωd (polos más arriba)", (1, 8),
     "ts igual (≈4,5 s)\nmás oscilaciones\nMp aumenta (θ aumenta)"),
    ("B) Misma ωd, distinta σ (polos más a la izquierda)", (3, 4),
     "ts disminuye (≈1,5 s)\nmisma frecuencia\nMp disminuye (θ disminuye)"),
    ("C) Mismo ángulo θ, polos más lejos del origen", (2, 8),
     "Mp igual\nts disminuye (≈2,25 s)\nfrecuencia aumenta"),
]

COLOR_REF, COLOR_NUEVO = "#6b7280", "#C827F5"

fig, axs = plt.subplots(3, 2, figsize=(12, 12),
                        gridspec_kw={"width_ratios": [1, 1.6]})

for i, (titulo, nuevo, nota) in enumerate(casos):
    ax_s, ax_t = axs[i]

    # Plano s: polos y rectas desde el origen (ángulo θ) 
    for (sigma, wd), color, etiqueta in [(referencia, COLOR_REF, "referencia"),
                                         (nuevo, COLOR_NUEVO, "modificado")]:
        ax_s.plot([-sigma, -sigma], [wd, -wd], "x", color=color, ms=10,
                  mew=2.5, label=etiqueta)
        ax_s.plot([0, -sigma], [0, wd], color=color, lw=1, ls="--")
        ax_s.plot([0, -sigma], [0, -wd], color=color, lw=1, ls="--")
        ax_s.text(-sigma - 0.1, wd + 0.9, f"{-sigma:g}±j{wd:g}",
                  color=color, ha="center", fontsize=9)
    ax_s.axhline(0, color="k", lw=1)
    ax_s.axvline(0, color="k", lw=1)
    ax_s.set_xlim(-4.5, 1)
    ax_s.set_ylim(-10, 10)
    ax_s.set_xlabel("Re(s)")
    ax_s.set_ylabel("Im(s)")
    ax_s.set_title(titulo, fontsize=10, loc="left")
    ax_s.grid(alpha=0.3)
    if i == 0:
        ax_s.legend(loc="lower left", fontsize=8)

    # Respuesta al escalón unitario y envolvente 1 ± e^(-sigma t) 
    for (sigma, wd), color in [(referencia, COLOR_REF), (nuevo, COLOR_NUEVO)]:
        ax_t.plot(t, respuesta_escalon(sigma, wd, t), color=color, lw=2)
        ax_t.plot(t, 1 + np.exp(-sigma * t), color=color, lw=0.8, ls=":")
        ax_t.plot(t, 1 - np.exp(-sigma * t), color=color, lw=0.8, ls=":")
    ax_t.axhline(1, color="k", lw=1, ls="--")
    ax_t.set_xlim(0, 6)
    ax_t.set_ylim(0, 1.9)
    ax_t.set_xlabel("t (s)")
    ax_t.set_ylabel("y(t)")
    ax_t.grid(alpha=0.3)
    ax_t.text(5.95, 1.85, nota, ha="right", va="top", fontsize=9,
              color=COLOR_NUEVO,
              bbox=dict(boxstyle="round", fc="white", ec=COLOR_NUEVO))

    print(titulo,
          "| Mp ref =", round(sobrepico(*referencia), 3),
          "| Mp nuevo =", round(sobrepico(*nuevo), 3))

fig.suptitle("Efecto de la ubicación de los polos en la respuesta al escalón "
             "unitario\n(gris: referencia −1 ± j4, naranja: modificado; "
             "planos no a escala)", fontsize=12)
fig.tight_layout()
fig.savefig("polos_plano_s.png", dpi=140)
