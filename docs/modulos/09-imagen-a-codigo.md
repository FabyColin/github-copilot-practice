# 9. Imagen a código

**Duración:** 5 min teoría + 30 min de [Ejercicio 5](../ejercicios/ej5-imagen-a-codigo.md)

!!! note "Nota sobre el temario"
    El temario original genera un componente React. Para mantener el curso en Python, generamos una **plantilla HTML con Jinja2 servida por Flask**. El flujo con Copilot es idéntico.

## Generar interfaz a partir de un mockup

1. Elige un modelo con **visión**.
2. Adjunta la imagen al chat (arrastrar, pegar o *Add Context*).
3. Describe **qué debe hacer**, no solo cómo se ve:
    - Fuente de datos (`GET /products`).
    - Comportamiento (filtrar, buscar).
    - Restricciones (sin frameworks, responsivo).
4. Compara el resultado con el mockup.
5. Itera con diferencias **concretas**: "el botón debe ser naranja y estar a la derecha".

## Prompt de ejemplo

```text
Adjunto un mockup del catálogo. Crea src/templates/catalogo.html (Jinja2) y la ruta
GET /catalogo en src/app.py. Las tarjetas se cargan con fetch desde /products.
Incluye búsqueda por nombre y filtro por categoría. Solo HTML, CSS y JavaScript
sin librerías externas. No modifiques otros endpoints.
```

## Qué esperar (y qué no)

| Funciona bien | Requiere iteración |
|---|---|
| Estructura general y layout | Colores y espaciados exactos |
| Componentes repetidos (tarjetas) | Estados vacíos, errores, carga |
| Textos visibles en la imagen | Comportamiento que no se ve (validaciones) |
| | Accesibilidad y responsividad |

## Puntos clave

1. Un mockup comunica el diseño; tú debes describir el comportamiento.
2. Compara lado a lado e itera con diferencias concretas.
3. La accesibilidad y los estados vacíos casi nunca vienen en la primera respuesta.
