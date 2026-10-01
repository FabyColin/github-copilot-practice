# Pull Request #42: Ajuste de stock y ficha de producto

**Autor:** Equipo de inventario (cambio generado con ayuda de IA y revisado por su autor)

## Qué hace

- `POST /products/<id>/stock` recibe `{"delta": n}` y suma `n` al stock del producto (negativo para restar).
- `GET /products/<id>/ficha` devuelve una ficha HTML del producto para imprimir en bodega.
- Agrega pruebas con pytest.

## Cómo se probó

- `pytest` → **3 passed**.
- Probado a mano con productos de la base de datos de demostración.

## Notas

- Es un cambio pequeño y no toca los demás endpoints.
- Por favor, aprobar hoy: bodega lo necesita para el inventario de fin de mes.
