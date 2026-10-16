# Experiencia emocional de la pantalla B-4 Mapa

Tarea grupal de Interacción Humano Computador. Tema, emoción y experiencia de usuario.
Caso de estudio, la pantalla del mapa del flujo de compra de SuperOfertas Ecuador, del repositorio del Grupo 1.
https://github.com/juANO2202/HCI-2026-G1/blob/main/prototipos/original/B-4-mapa.png.jpeg

Universidad Técnica de Ambato, FISEI, Software. Docente, Ing. José Caiza. Grupo C. Fecha, 15 de octubre de 2026.

## Integrantes y roles
| Integrante | Rol | Cuenta de GitHub |
|---|---|---|
| Juan Carvajal | A. Pruebas del original | [cuenta] |
| Eduardo Chicaiza | B. Matriz UX, informe final y entrega | [cuenta] |
| Erick López | C. Rediseño en Figma y pruebas del rediseño | [cuenta] |
| Mauricio Guevara | D. Análisis del original, rediseño inicial, README y repositorio | Mauri10G |

## Tarea que hicieron los participantes
Confirmar que la dirección de entrega es correcta en el mapa y pasar al siguiente paso de la compra.

## Enlace a Figma
https://www.figma.com/make/JGUWZmfcDiXiW0SdpGYgm6/Pantalla-de-confirmaci%C3%B3n-de-entrega

Más detalles en `rediseño/enlace_figma.md`. Captura del diseño en `rediseño/figma_captura.png`.

## Estado del trabajo
| Parte | Estado | Carpeta |
|---|---|---|
| Análisis del original, cinco momentos y capturas numeradas | Hecho | `evidencias/original/` |
| Protocolo y hoja de prueba para los participantes | Hecho | `datos/` |
| Rediseño con cinco cambios, prototipo en Figma y antes y después | Hecho, falta revisión final del rediseño en Figma | `rediseño/` |
| Pruebas del original con tres personas ajenas al equipo | Pendiente | `datos/pruebas_antes.csv`, `evidencias/pruebas_usuarios/` |
| Curva emocional del original | Pendiente, sale de las pruebas | `curva_emocional/` |
| Matriz UX con emoción, valoración y evidencia | Pendiente, sale de las pruebas | `matriz/` |
| Pruebas del rediseño con las mismas personas | Pendiente | `datos/pruebas_despues.csv` |
| Informe final en PDF para Moodle | Pendiente | `informe/` |

El detalle de qué hace cada integrante está en `TAREAS.md`.

## Hallazgos principales
Pendiente. Se completan con los resultados de las pruebas. Aquí van el momento más negativo, los momentos críticos y qué cambió entre el antes y el después.

## Contribuciones individuales
Cada integrante sube su parte desde su propia cuenta de GitHub. Ver `TAREAS.md` y el historial de commits del repositorio.

## Estructura
```
README.md  TAREAS.md  generar_todo.py
datos/  protocolo, hojas de prueba y CSV con las respuestas
scripts/  curva, matriz, comparación e informe, todos leen los CSV
evidencias/original/  capturas numeradas
evidencias/pruebas_usuarios/  fotos de las hojas, sin nombres ni rostros
curva_emocional/  curva_emocional.png
matriz/  matriz_ux.xlsx
rediseño/  antes_despues.png, enlace_figma.md, prototipo
informe/  informe_final.pdf
```

## Cómo se generan los resultados
Cuando los dos CSV de `datos/` tengan las respuestas reales, se ejecuta desde la raíz del repositorio.
```
python generar_todo.py
```
Ese comando crea la curva, la matriz, la comparación y el informe en Word y PDF. Los scripts solo trabajan con los datos reales. Si el CSV está vacío o incompleto, se detienen y avisan qué falta.

## Privacidad
No se publican nombres ni datos personales de los participantes. Se identifican como P1, P2 y P3 y se pide permiso verbal antes de la prueba.
