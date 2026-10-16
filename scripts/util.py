import sys
import pandas as pd
from config_momentos import MOMENTOS

NOMBRES = {m["id"]: m["nombre"] for m in MOMENTOS}

def cargar(ruta, minimo=3):
    """Lee un CSV de pruebas y comprueba que esté completo. Si no lo está, se detiene.
    No rellena ni inventa ningún valor."""
    try:
        df = pd.read_csv(ruta)
    except Exception as e:
        sys.exit(f"No pude leer {ruta}. {e}")
    cols = {"participante", "momento", "valor", "emocion_reportada", "comentario",
            "evidencia_observada", "tiempo_seg"}
    if not cols.issubset(df.columns):
        sys.exit(f"Al CSV {ruta} le faltan columnas. Necesita al menos {sorted(cols)}.")
    if df.empty:
        sys.exit(f"{ruta} está vacío. Primero hay que hacer las pruebas con usuarios reales.")
    if df["participante"].isna().any() or df["participante"].astype(str).str.strip().eq("").any():
        sys.exit(f"Hay participantes sin identificador en {ruta}.")
    df["participante"] = df["participante"].astype(str).str.strip()
    for campo in ("emocion_reportada", "comentario", "evidencia_observada"):
        if df[campo].isna().any() or df[campo].astype(str).str.strip().eq("").any():
            sys.exit(f"La columna {campo} de {ruta} tiene campos vacíos.")
    df["tiempo_seg"] = pd.to_numeric(df["tiempo_seg"], errors="coerce")
    if df["tiempo_seg"].isna().any() or (df["tiempo_seg"] < 0).any():
        sys.exit(f"Los tiempos de {ruta} deben ser números no negativos.")
    momentos = pd.to_numeric(df["momento"], errors="coerce")
    if momentos.isna().any() or not (momentos % 1 == 0).all():
        sys.exit(f"Los momentos de {ruta} deben ser enteros del 1 al 5.")
    df["momento"] = momentos.astype(int)
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    if df["valor"].isna().any():
        sys.exit(f"Hay valores vacíos o que no son números en {ruta}.")
    if not df["valor"].between(-3, 3).all() or not (df["valor"] % 1 == 0).all():
        sys.exit(f"Todos los valores de {ruta} deben ser enteros entre -3 y +3.")
    ids = [m["id"] for m in MOMENTOS]
    parts = sorted(df["participante"].unique())
    if len(parts) < minimo:
        sys.exit(f"{ruta} tiene {len(parts)} participantes y la tarea pide al menos {minimo}.")
    for p in parts:
        sub = df[df["participante"] == p]
        if sorted(sub["momento"].tolist()) != ids:
            sys.exit(f"El participante {p} de {ruta} debe tener exactamente un valor por cada momento {ids}.")
    return df

def validar_mismos_participantes(antes, despues):
    """Evita comparar personas distintas en el original y en el rediseño."""
    a = set(antes["participante"])
    d = set(despues["participante"])
    if a != d:
        sys.exit("Las pruebas de antes y después deben ser de las mismas personas. "
                 f"Solo en antes: {sorted(a - d)}. Solo en después: {sorted(d - a)}.")

def matriz_valores(df):
    return df.pivot(index="participante", columns="momento", values="valor").sort_index()

def momentos_criticos(promedios):
    """Devuelve el momento con el promedio más bajo y el de la mayor caída respecto al anterior."""
    ids = list(promedios.index)
    bajo = promedios.idxmin()
    caidas = {ids[i]: promedios.iloc[i] - promedios.iloc[i - 1] for i in range(1, len(ids))}
    caida = min(caidas, key=caidas.get)
    return bajo, caida, caidas[caida]
