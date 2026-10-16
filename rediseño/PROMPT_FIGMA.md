# Prompt para Figma

Sirve para la función de IA de Figma, que genera un primer borrador a partir de texto. Se llama First Draft o Figma Make según la cuenta. Se pega todo el bloque. Después se ajusta a mano con la guía `GUIA_FIGMA.md`.

## Bloque para pegar

```
Diseña en versión escritorio de 1366 por 927 píxeles la pantalla "Paso 4. Confirma tu dirección de entrega" de una tienda en línea llamada SuperOfertas Ecuador. Es un rediseño de una pantalla de mapa que antes tenía colores chillones, una cuenta regresiva de oferta y un botón de omitir enorme. La nueva versión debe ser calmada, clara y de confianza. Usa solo datos ficticios. Escribe todos los textos en español.

Estilo. Fondo gris muy claro #F8FAFC, tarjetas blancas con borde #D1D5DB y esquinas de 10 px. Texto #1F2937 y texto secundario #4B5563. Color de marca azul oscuro #12326B. Botón principal azul #1D4ED8 con texto blanco. Tipografía Inter o Segoe UI. Buen contraste y letra grande.

Estructura de arriba hacia abajo.
1. Encabezado blanco de 66 px de alto. A la izquierda el logo en texto "SuperOfertas Ecuador" en azul oscuro y negrita. A la derecha los enlaces "Ayuda" y "Mi cuenta".
2. Una franja verde muy clara de 40 px con el texto centrado "Envío gratis incluido en tu pedido". Sin cuenta regresiva y sin colores rojos.
3. Barra de progreso con cinco pasos conectados por líneas. Carrito, Domicilio y Quién recibe aparecen completados con un círculo azul oscuro y un visto. El paso 4 Mapa es el actual, con círculo azul resaltado. El paso 5 Pagar está pendiente, con círculo gris. Debajo, en texto pequeño, "Paso 4 de 5".
4. Título grande "Confirma tu dirección de entrega" y debajo "Revisa que el punto del mapa sea el lugar donde quieres recibir tu pedido."
5. Dos columnas. A la izquierda, una tarjeta de 833 por 444 px con un mapa ficticio de calles en beige y blanco, un parque verde y las etiquetas "Barrio Ejemplo", "Av. Imaginaria", "Calle Inventada" y "Sector Lejano". Un solo pin azul grande sobre Calle Inventada, con una etiqueta azul oscuro al lado que dice "Calle Inventada 123". Botones de zoom más y menos abajo a la izquierda. A la derecha, una tarjeta blanca con "Dirección de entrega", la dirección "Calle Inventada 123, Barrio Ejemplo" en negrita de 22 px, la línea "Ciudad Demo, Provincia Demo", una etiqueta amarilla pálida "Por confirmar" y un enlace azul subrayado "Corregir dirección".
6. Fila de acciones debajo del mapa. A la izquierda un botón secundario blanco con borde "← Volver a quién recibe". A la derecha un enlace pequeño gris subrayado "Omitir por ahora" y al lado el botón principal azul grande "Confirmar dirección".
7. Una nota pequeña centrada al final "Prototipo de rediseño con datos ficticios".

Crea además dos frames más del mismo tamaño y estilo.
Frame 2, "Dirección confirmada". Igual al primero, pero la etiqueta cambia a verde "Dirección confirmada ✓" y debajo aparece un mensaje verde claro "Listo, tu dirección quedó confirmada. Ya puedes pasar al pago." El botón principal ahora dice "Continuar a pagar →" y desaparece el enlace "Omitir por ahora".
Frame 3, "Paso 5". El paso 4 queda completado y el 5 resaltado, con "Paso 5 de 5". En el centro el título "Paso 5 de 5. Pagar" y el texto "Aquí continúa el pago." con un botón secundario "Volver al mapa".

Prototipo. Conecta con interacción al hacer clic el botón "Confirmar dirección" del frame 1 con el frame 2, y el botón "Continuar a pagar →" del frame 2 con el frame 3. El botón "Volver al mapa" regresa al frame 1.
```

## Si la IA no lo deja bien
No pasa nada. Usa el borrador solo como base y corrige con `GUIA_FIGMA.md`, que tiene las medidas, colores y textos exactos. Puedes arrastrar a Figma la captura `prototipo/captura-despues.png` como referencia y reconstruir encima.

## Lo que debe quedar en el archivo de Figma
- Página `Original` con la imagen `evidencias/original/B-4-mapa.png.jpeg` en un frame.
- Página `Rediseño` con los tres frames y las conexiones del prototipo.
- Enlace compartido con permiso de ver para cualquiera que tenga el enlace, pegado en `enlace_figma.md`.
