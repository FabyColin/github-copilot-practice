# Ejercicio 5: Del mockup a un componente React

**Módulo:** [9. Imagen a código](../../modulos/09-imagen-a-codigo.md) · **Tiempo:** 30 min
**Archivos:** `ejercicios/ej5-imagen-a-codigo/mockup-catalogo.png` y `web/`

## Escenario

Diseño entregó el mockup del catálogo de **FerreMax**. Tu trabajo es convertirlo en un componente React que consuma la API de la tienda.

![Mockup](../../assets/mockup-catalogo.png)

## Requisitos funcionales

- Componente `web/Catalogo.jsx` que `App.jsx` renderiza.
- Las tarjetas se cargan desde `GET /products` con `fetch` dentro de `useEffect`.
- El filtro de categoría usa el parámetro `?categoria=` de la API.
- La búsqueda filtra por nombre.
- Solo React y CSS propio. **Sin librerías de componentes ni de estilos.**

Para verlo en el navegador, en dos terminales: `npm start` (API, puerto 5000) y `npm run dev` (Vite, puerto 5173).

## Parte 1: primera versión (10 min)

1. Selecciona un modelo con **visión**.
2. Adjunta `mockup-catalogo.png` al chat.
3. En modo Agent, escribe un prompt con **contexto, intención y restricciones** (módulo 5). Debe pedir crear `web/Catalogo.jsx` (y su CSS) y usarlo desde `web/App.jsx`.
4. Revisa los diffs y abre `http://localhost:5173`.

## Parte 2: compara e itera (15 min)

Abre el mockup junto a tu página y **anota 3 diferencias visuales concretas** (por ejemplo: color del botón, espaciado, tamaño de la etiqueta).

Itera **dos veces** con mensajes de seguimiento precisos:

1. Una corrección visual ("las tarjetas deben tener 3 columnas en escritorio").
2. Una mejora de comportamiento que **no se ve en el mockup**:
    - estado vacío cuando no hay resultados,
    - o estado de error cuando la API falla,
    - o diseño responsivo para celular.

## Parte 3: revisión (5 min)

Revisa el código generado:

- [ ] ¿Pinta los datos con JSX, o usa `dangerouslySetInnerHTML`? (riesgo XSS)
- [ ] ¿El `useEffect` limpia la petición si el componente se desmonta o el filtro cambia?
- [ ] ¿La página funciona con teclado? ¿El buscador y el selector tienen etiqueta accesible?
- [ ] ¿Maneja el error si la API falla?

Si te sobra tiempo, pide a Copilot una prueba con React Testing Library que simule `fetch` y verifique que se muestran los productos.

## Criterios de aceptación

- [ ] El catálogo muestra los 6 productos con nombre, categoría y precio.
- [ ] El filtro y la búsqueda funcionan.
- [ ] Anotaste 3 diferencias contra el mockup y corregiste al menos 2.
- [ ] Hay estado vacío, estado de error o diseño responsivo.
- [ ] Identificaste al menos 1 problema de calidad en el código generado.
- [ ] `npm test` sigue en verde.

---

*Solución de referencia: `soluciones/ej5/` (solo para el instructor).*
