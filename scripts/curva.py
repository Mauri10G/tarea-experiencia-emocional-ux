"""Curva emocional con los datos reales de un CSV.
Uso: python scripts/curva.py [datos/pruebas_antes.csv] [curva_emocional/curva_emocional.png]"""
import sys, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from util import cargar, matriz_valores, momentos_criticos, NOMBRES

ruta = sys.argv[1] if len(sys.argv) > 1 else "datos/pruebas_antes.csv"
salida = sys.argv[2] if len(sys.argv) > 2 else "curva_emocional/curva_emocional.png"
titulo = sys.argv[3] if len(sys.argv) > 3 else "Curva emocional del original B-4 Mapa"

df = cargar(ruta)
m = matriz_valores(df)
prom = m.mean(axis=0)
bajo, caida, delta = momentos_criticos(prom)

fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
ax.axhspan(-3.4, 0, color="#fdecea", alpha=0.6, zorder=0)
ax.axhline(0, color="#6b7280", lw=1)
colores = ["#2563eb", "#059669", "#d97706", "#7c3aed", "#0891b2", "#be185d"]
for i, (p, fila) in enumerate(m.iterrows()):
    ax.plot(fila.index, fila.values, marker="o", lw=1.8, alpha=0.8, color=colores[i % len(colores)], label=p)
ax.plot(prom.index, prom.values, marker="o", lw=4, color="#111827", label="Promedio", zorder=5)
for mid, txt in ((bajo, "Promedio más bajo"), (caida, "Mayor caída")):
    y = prom[mid]
    ax.scatter([mid], [y], s=520, facecolors="none", edgecolors="#dc2626", linewidths=3, zorder=6)
    ax.annotate(f"{txt}\nMomento {mid}, {y:.1f}", (mid, y), textcoords="offset points", xytext=(0, -52 if y > -1.5 else 40),
                ha="center", fontsize=9, color="#b91c1c", fontweight="bold")
ax.set_ylim(-3.4, 3.4); ax.set_yticks(range(-3, 4))
ax.set_xticks(list(NOMBRES))
ax.set_xticklabels([f"M{k}\n" + "\n".join(textwrap.wrap(v, 18)) for k, v in NOMBRES.items()], fontsize=9)
ax.set_ylabel("Emoción reportada, de -3 muy negativa a +3 muy positiva")
ax.set_title(titulo, fontsize=14, fontweight="bold")
ax.legend(loc="upper right", fontsize=9, ncol=2)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout(); fig.savefig(salida); print("Guardado", salida)
print("\nPromedio por momento")
for k, v in prom.items(): print(f"  M{k} {NOMBRES[k]}: {v:.2f}")
print(f"\nMomento con el promedio más bajo: M{bajo}, {prom[bajo]:.2f}")
print(f"Mayor caída entre momentos seguidos: llegando a M{caida}, {delta:.2f}")
print(f"Promedio general: {prom.mean():.2f}, participantes: {len(m)}")
