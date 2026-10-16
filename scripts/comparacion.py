"""Compara antes y después con los datos reales de los dos CSV.
Uso: python scripts/comparacion.py"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from util import cargar, matriz_valores, validar_mismos_participantes, NOMBRES
import pandas as pd

ra = sys.argv[1] if len(sys.argv) > 1 else "datos/pruebas_antes.csv"
rd = sys.argv[2] if len(sys.argv) > 2 else "datos/pruebas_despues.csv"
salida = sys.argv[3] if len(sys.argv) > 3 else "curva_emocional/curva_antes_despues.png"
resumen = sys.argv[4] if len(sys.argv) > 4 else "datos/resumen_comparacion.csv"

antes, despues = cargar(ra), cargar(rd)
validar_mismos_participantes(antes, despues)
a, d = matriz_valores(antes), matriz_valores(despues)
pa, pd_ = a.mean(axis=0), d.mean(axis=0)

fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
ax.axhspan(-3.4, 0, color="#fdecea", alpha=0.6, zorder=0); ax.axhline(0, color="#6b7280", lw=1)
for _, f in a.iterrows(): ax.plot(f.index, f.values, color="#dc2626", alpha=0.25, lw=1.3)
for _, f in d.iterrows(): ax.plot(f.index, f.values, color="#2563eb", alpha=0.25, lw=1.3)
ax.plot(pa.index, pa.values, marker="o", lw=4, color="#b91c1c", label="Antes, original")
ax.plot(pd_.index, pd_.values, marker="o", lw=4, color="#1d4ed8", label="Después, rediseño")
import textwrap
ax.set_xticks(list(NOMBRES)); ax.set_xticklabels([f"M{k}\n" + "\n".join(textwrap.wrap(v, 18)) for k, v in NOMBRES.items()], fontsize=9)
ax.set_ylim(-3.4, 3.4); ax.set_yticks(range(-3, 4)); ax.grid(axis="y", alpha=0.3)
ax.set_ylabel("Emoción reportada, de -3 a +3"); ax.set_title("Curva emocional promedio antes y después del rediseño", fontsize=14, fontweight="bold")
ax.legend(loc="lower right"); fig.tight_layout(); fig.savefig(salida); print("Guardado", salida)

res = pd.DataFrame({"momento": list(NOMBRES), "nombre": list(NOMBRES.values()),
                    "promedio_antes": pa.round(2).values, "promedio_despues": pd_.round(2).values})
res["diferencia"] = (res["promedio_despues"] - res["promedio_antes"]).round(2)
res.loc[len(res)] = ["Total", "Promedio general", round(pa.mean(), 2), round(pd_.mean(), 2), round(pd_.mean() - pa.mean(), 2)]
res.to_csv(resumen, index=False); print(res.to_string(index=False))
