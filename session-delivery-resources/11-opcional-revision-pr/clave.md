# Clave del ejercicio opcional (solo para el instructor)

El "PR" agrega dos rutas (`POST /products/<id>/stock` y `GET /products/<id>/ficha`) con **tres defectos sembrados**. Los tres pasan inadvertidos si solo se mira que "las pruebas están en verde".

| # | Defecto | Dónde | Gravedad |
|---|---|---|---|
| 1 | **Entrada sin validar** (`delta`) | `ajustar_stock` / `router.post('/products/:id/stock')` | Alta |
| 2 | **XSS reflejado** en la ficha | `ficha_producto` / `router.get('/products/:id/ficha')` | Alta |
| 3 | **Pruebas que no pueden fallar** | `test_ajuste_stock.py` / `ajusteStock.test.js` | Media (esconde a los otros dos) |

## Defecto 1: `delta` sin validar

Se usa `datos["delta"]` / `req.body.delta` directamente.

| Entrada | Python | JavaScript |
|---|---|---|
| `{"delta": "abc"}` | **500** (`TypeError`) | 200, stock `"40abc"` (se concatena texto) |
| `{"delta": "5"}` | **500** | 200, stock **`"405"`** (concatena, no suma) |
| `{}` (sin `delta`) | **500** (`KeyError`) | 200, stock `40undefined` |
| `{"delta": -999}` | 200, stock **-959** | 200, stock **-987** (sobre un producto de 12) |

La versión JavaScript es peor: **no falla**, corrompe el dato en silencio.

Reproducir:

```bash
# Python (python demo_app.py, puerto 5001)  |  JavaScript (node ejercicios/ej-opcional-revision-pr/demoApp.js)
curl -X POST localhost:5001/products/p-001/stock -H "Content-Type: application/json" -d '{"delta":"5"}'
curl -X POST localhost:5001/products/p-001/stock -H "Content-Type: application/json" -d '{"delta":-999}'
```

Corrección esperada: aceptar solo enteros (no booleanos) distintos de cero, responder `400` con mensaje claro, y rechazar con `409` si el stock quedaría negativo. Ver `soluciones/ej-opcional/`.

## Defecto 2: XSS reflejado

Nombre y descripción se insertan en el HTML sin escapar. Quien pueda crear o editar productos (`POST /products` ya existe) puede inyectar script que se ejecuta al abrir la ficha en el mostrador o la bodega.

```bash
curl -X POST localhost:5001/products -H "Content-Type: application/json" -d '{"nombre":"<script>alert(1)</script>"}'
# abrir en el navegador: http://localhost:5001/products/<id devuelto>/ficha
```

Corrección esperada: escapar (`markupsafe.escape` en Flask; función `escapar` en Express) o usar un motor de plantillas con autoescape.

## Defecto 3: pruebas que no pueden fallar

| Prueba | Por qué no vale |
|---|---|
| Python `assert respuesta.status_code in (200, 400, 404)` | Acepta casi cualquier resultado, incluido el error de validación |
| Python `assert respuesta` | Un objeto `Response` siempre es "verdadero": nunca falla |
| JS `request(...).then(...)` **sin `return` ni `await`** | Jest termina la prueba antes de que se ejecute el `expect`: pasa aunque la aserción fuera falsa |
| JS `expect(respuesta).toBeDefined()` | Un objeto de respuesta siempre está definido |

Además **ninguna** prueba cubre: delta inválido, delta negativo, stock negativo ni HTML malicioso. Por eso "3 passed" no significa nada.

Demostración útil en vivo: cambiar `producto["stock"] += datos["delta"]` por `producto["stock"] = 0` y volver a correr las pruebas débiles: siguen en verde.

## Qué se espera de los alumnos

Un buen resultado **no** exige encontrar los tres. Se valora:

1. Hallazgos con evidencia (comprobaron algo ejecutando).
2. Haber detectado, al menos, que las pruebas no protegen el comportamiento.
3. Una decisión justificada (lo razonable es **pedir cambios**).
4. Comparación honesta con Copilot, incluidos sus falsos positivos.

Otros hallazgos válidos (menores): no hay autenticación en las rutas, el ajuste no es atómico ante peticiones concurrentes, falta registro de movimientos de inventario, la ficha devuelve HTML sin `Content-Type` explícito ni estructura de documento.

## Verificación de la clave

El CI comprueba que: (a) las pruebas débiles del PR pasan, (b) las pruebas estrictas de `soluciones/ej-opcional/` **fallan** contra el código con defectos, y (c) pasan contra la versión corregida. Resultado de referencia: 15 pruebas estrictas en cada pista, 11 de ellas fallan contra el código del PR.
