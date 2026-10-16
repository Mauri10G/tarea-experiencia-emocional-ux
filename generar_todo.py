"""Genera curva, matriz, comparación e informe con un solo comando.
Uso desde la raíz del repositorio. python generar_todo.py
Antes hay que llenar datos/pruebas_antes.csv y datos/pruebas_despues.csv con las respuestas reales."""
import os, subprocess, sys, shutil
for c in ("curva_emocional", "matriz", "informe"): os.makedirs(c, exist_ok=True)
for s in ("curva.py", "matriz.py", "comparacion.py", "informe.py"):
    r = subprocess.run([sys.executable, os.path.join("scripts", s)])
    if r.returncode: sys.exit(f"Se detuvo en {s}. Revisa el mensaje de arriba.")
exe = shutil.which("soffice") or shutil.which("libreoffice")
if exe:
    subprocess.run([exe, "--headless", "--convert-to", "pdf", "--outdir", "informe", "informe/informe_final.docx"])
else:
    print("No encontré LibreOffice. Abre informe/informe_final.docx en Word y expórtalo a PDF como informe/informe_final.pdf.")
print("Listo.")
