"""Momentos de interacción de la pantalla B-4 Mapa y la parte de la matriz que sale del análisis de diseño.
Las emociones, valoraciones y evidencias NO están aquí. Salen de los CSV con las pruebas reales."""

TAREA = "Confirmar que la dirección de entrega es correcta en el mapa y pasar al siguiente paso de la compra."

MOMENTOS = [
    {"id": 1, "nombre": "Llegar y primera impresión", "fase": "Antes", "captura": "C02",
     "mejora": "Quitar el banner rojo y la cuenta regresiva. Usar colores calmados y una barra de progreso.",
     "principio": "Heurística 8 de Nielsen, diseño estético y minimalista. Diseño emocional de Norman, nivel visceral."},
    {"id": 2, "nombre": "Explorar el mapa y ubicar la dirección", "fase": "Durante", "captura": "C03",
     "mejora": "Mejorar el contraste y la legibilidad de calles y avenidas del mapa; mantener un único pin coherente con la dirección escrita.",
     "principio": "Heurística 1 de Nielsen, visibilidad del estado. Heurística 4, consistencia entre pin y dirección."},
    {"id": 3, "nombre": "Leer la dirección y el aviso", "fase": "Durante", "captura": "C04",
     "mejora": "Quitar el aviso de presión, corregir los textos y mostrar la dirección en una tarjeta clara.",
     "principio": "Heurística 2 de Nielsen, lenguaje del usuario. WCAG 1.4.3, contraste de textos por verificar."},
    {"id": 4, "nombre": "Decidir entre guardar y omitir", "fase": "Durante", "captura": "C05",
     "mejora": "Confirmar dirección como acción principal habilitada cuando la selección sea válida; Omitir como enlace secundario.",
     "principio": "Heurística 3 de Nielsen, control y libertad. Heurística 5, prevención de errores. Jerarquía visual."},
    {"id": 5, "nombre": "Terminar el paso y saber qué sigue", "fase": "Después", "captura": "C06",
     "mejora": "Mostrar el estado Dirección confirmada, un mensaje y el botón Continuar a pagar, con el progreso del flujo.",
     "principio": "Heurística 1 de Nielsen, retroalimentación. Diseño emocional de Norman, nivel reflexivo."},
]
