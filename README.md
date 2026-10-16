# Experiencia emocional de la pantalla B-4 Mapa

Tarea grupal de Interacción Humano Computador. Tema, emoción y experiencia de usuario.
Caso de estudio, la pantalla del mapa del flujo de compra de SuperOfertas Ecuador, del repositorio del Grupo 1.
https://github.com/juANO2202/HCI-2026-G1/blob/main/prototipos/original/B-4-mapa.png.jpeg

Universidad Técnica de Ambato, FISEI, Software. Docente, Ing. José Caiza. Grupo C.

## Integrantes y roles
| Integrante | Rol | Cuenta de GitHub |
|---|---|---|
| [INTEGRANTE 1] | A | [cuenta] |
| [INTEGRANTE 2] | B | [cuenta] |
| [INTEGRANTE 3] | C | [cuenta] |
| [INTEGRANTE 4] | D | [cuenta] |

## Qué hicimos
1. Analizamos la pantalla original, definimos la tarea y cinco momentos, y tomamos capturas numeradas. Carpeta `evidencias/original/`.
2. Probamos el original con tres personas ajenas al equipo y graficamos la curva emocional. Carpetas `datos/`, `evidencias/pruebas_usuarios/` y `curva_emocional/`.
3. Armamos la matriz UX con momento, emoción, evidencia, mejora y principio de IHC. Carpeta `matriz/`.
4. Rediseñamos la pantalla en Figma y la comparamos con el original. Carpeta `rediseño/`.
5. Probamos el rediseño con las mismas personas y comparamos. Carpeta `curva_emocional/` y `informe/`.

Tarea que hicieron los participantes. Confirmar que la dirección de entrega es correcta en el mapa y pasar al siguiente paso de la compra.

## Enlace a Figma
https://www.figma.com/make/JGUWZmfcDiXiW0SdpGYgm6/Pantalla-de-confirmaci%C3%B3n-de-entrega

Más detalles en `rediseño/enlace_figma.md`. Captura del diseño en `rediseño/figma_captura.png`.

## Hallazgos principales
[SE COMPLETA CUANDO ESTÉN LOS DATOS DE LAS PRUEBAS]

## Contribuciones individuales
Ver `TAREAS.md` y el historial de commits del repositorio.

## Estructura
```
README.md  TAREAS.md  generar_todo.py
datos/  protocolo, hojas de prueba y CSV con las respuestas
scripts/  curva, matriz y comparación, todos leen los CSV
evidencias/original/  capturas numeradas
evidencias/pruebas_usuarios/  fotos de las hojas, sin nombres ni rostros
curva_emocional/  curva_emocional.png
matriz/  matriz_ux.xlsx
rediseño/  antes_despues.png, enlace_figma.md, prototipo
informe/  informe_final.pdf
```

## Cómo se generan los resultados
```
python generar_todo.py
```
Ese comando crea la curva, la matriz, la comparación y el informe en Word y PDF. Los scripts solo trabajan con los datos reales de `datos/`. Si el CSV está vacío o incompleto, se detienen.

## Privacidad
No se publican nombres ni datos personales de los participantes. Se identifican como P1, P2 y P3 y se pidió permiso verbal.
