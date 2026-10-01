# Instrucciones para GitHub Copilot en este proyecto

## Contexto
Este proyecto es una API REST de una farmacia (productos, existencias y pedidos) hecha con Express, con una interfaz en React (Vite) y pruebas con Jest. Todos los datos de ejemplo son ficticios.

## Estilo de código
- JavaScript moderno (ES2022): `const`/`let`, funciones flecha, desestructuración. Nada de `var`.
- Funciones nuevas con JSDoc (`@param` y `@returns`) en español.
- Nombres de variables y funciones en español y en `camelCase`; componentes React en `PascalCase`.
- Sin dependencias nuevas a menos que se pidan explícitamente.

## Seguridad y calidad
- Valida siempre la entrada del usuario en los endpoints.
- Nunca dejes secretos ni contraseñas en el código.
- No registres ni imprimas datos personales ni folios de receta reales; en ejemplos y pruebas usa datos ficticios.
- En React, pinta datos con JSX o `textContent`; nunca uses `dangerouslySetInnerHTML` con datos externos.

## Pruebas
- Toda función nueva lleva pruebas con Jest en `src/tests/` (API) o junto al componente (React).
- Cubre al menos un caso borde por función.
