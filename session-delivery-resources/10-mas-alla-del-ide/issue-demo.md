# Issue de ejemplo para el cloud agent

**Título:** Agregar paginación a `GET /products`

**Contexto**
La API de la farmacia (`src/app.py`) devuelve todos los productos en una sola respuesta. Con catálogos grandes esto será lento.

**Qué se necesita**
- Parámetros opcionales `pagina` (por defecto 1) y `tamano` (por defecto 10, máximo 50).
- La respuesta mantiene el arreglo de productos actual y agrega los encabezados `X-Total-Count` y `X-Pagina`.
- Valores inválidos (`pagina` o `tamano` menores que 1, o no numéricos) responden `400` con `{"error": "..."}`.

**Criterios de aceptación**
- [ ] `GET /products` sin parámetros sigue funcionando.
- [ ] Hay pruebas con pytest en `src/tests/` para: paginación normal, última página parcial, página fuera de rango y parámetros inválidos.
- [ ] `pytest src` pasa.

**Restricciones**
- No agregar dependencias nuevas.
- No cambiar los demás endpoints.
- Mantener nombres en español y type hints.
