# Ejercicio 5: Del mockup a la página

**Módulo:** [9. Imagen a código](../../modulos/09-imagen-a-codigo.md) · **Tiempo:** 30 min
**Archivos:** `ejercicios/ej5-imagen-a-codigo/mockup-catalogo.png` y `src/`

## Escenario

Diseño entregó el mockup del catálogo de **Farmacia Demo**. Tu trabajo es convertirlo en una página que consuma la API de la farmacia.

![Mockup](../../assets/mockup-catalogo.png)

## Requisitos funcionales

- Ruta `GET /catalogo` que sirve la página.
- Los productos que `requiere_receta` muestran una etiqueta **"Requiere receta"** como en el mockup.
- Las tarjetas se cargan desde `GET /products` (con `fetch`).
- El filtro de categoría usa el parámetro `?categoria=` de la API.
- La búsqueda filtra por nombre.
- Solo HTML, CSS y JavaScript. **Sin librerías externas.**

## Parte 1: primera versión (10 min)

1. Selecciona un modelo con **visión**.
2. Adjunta `mockup-catalogo.png` al chat.
3. En modo Agent, escribe un prompt con **contexto, intención y restricciones** (módulo 5). Debe pedir crear `src/templates/catalogo.html` y la ruta en `src/app.py`.
4. Revisa los diffs y arranca la app: `cd src && python app.py` → `http://localhost:5000/catalogo`.

## Parte 2: compara e itera (15 min)

Abre el mockup junto a tu página y **anota 3 diferencias visuales concretas** (por ejemplo: color del botón, espaciado, tamaño de la etiqueta).

Itera **dos veces** con mensajes de seguimiento precisos:

1. Una corrección visual ("las tarjetas deben tener 3 columnas en escritorio").
2. Una mejora de comportamiento que **no se ve en el mockup**:
    - estado vacío cuando no hay resultados,
    - o diseño responsivo para celular.

## Parte 3: revisión (5 min)

Revisa el código generado:

- [ ] ¿Usa `textContent` para pintar nombres, o inserta HTML sin escapar? (riesgo XSS)
- [ ] ¿La página funciona con teclado? ¿El buscador tiene etiqueta accesible?
- [ ] ¿Maneja el error si la API falla?

## Criterios de aceptación

- [ ] `/catalogo` muestra los 6 productos con nombre, categoría y precio.
- [ ] El filtro y la búsqueda funcionan.
- [ ] Anotaste 3 diferencias contra el mockup y corregiste al menos 2.
- [ ] Hay estado vacío o diseño responsivo.
- [ ] Identificaste al menos 1 problema de calidad en el código generado.

---

*Solución de referencia: `soluciones/ej5/` (solo para el instructor).*
