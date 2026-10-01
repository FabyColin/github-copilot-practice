# Ejercicio 1: Autocompletado

**Módulo:** [2. Autocompletado](../../modulos/02-autocompletado.md) · **Tiempo:** 30 min (3 tramos aislados) + 50 min (ejercicio completo)
**Carpeta:** `ejercicios/ej1-autocompletado/`

!!! warning "Regla del ejercicio"
    Nada de chat. Solo autocompletado, comentarios y NES.

## Tramo A: ghost text (10 min)

**Archivo:** `tramo_a_ghost_text.py`

1. En cada función, borra el cuerpo `...` y escribe de nuevo solo la firma.
2. Observa la sugerencia. Practica: `Tab` (aceptar), `Esc` (descartar), `Alt+]` (otra alternativa), `Ctrl+→` (aceptar una palabra).
3. Para `es_email_valido`, revisa con cuidado: ¿la sugerencia valida bien `a@b`, `a@@b.com` o un correo vacío?

**Entregable:** las 4 funciones completas y una nota con **una sugerencia que rechazaste** y por qué.

## Tramo B: guiado por comentarios (10 min)

**Archivo:** `tramo_b_comentarios.py`

1. Bajo cada comentario, escribe la firma de la función y deja que Copilot complete.
2. Si la sugerencia no es lo que querías, **mejora el comentario** (no el código) y vuelve a intentar.
3. Prueba cada función con `PRODUCTOS` en la terminal de Python.

**Entregable:** 4 funciones funcionando. Anota cuántos comentarios tuviste que reescribir.

## Tramo C: Next Edit Suggestions (10 min)

**Archivo:** `tramo_c_nes.py`

1. Confirma que `github.copilot.nextEditSuggestions.enabled` está activo.
2. En `crear_producto` cambia la llave `"nombre"` por `"nombre_comercial"`.
3. Sigue las sugerencias de Copilot con `Tab` y **revisa cada una** antes de aceptar.
4. Al terminar, busca (`Ctrl+F`) si quedó alguna referencia a `"nombre"` que NES no detectó.

**Entregable:** el archivo con `"nombre_comercial"` en todos lados y consistente.

## Ejercicio completo: módulo de inventario (50 min)

**Archivo:** `inventario.py` · **Validación:** `test_inventario.py`

Construye la clase `Inventario` de la farmacia usando **solo autocompletado**:

| Método | Comportamiento |
|---|---|
| `agregar(producto)` | Guarda un producto (`dict` con `sku`, `nombre`, `stock`, `precio` y `caducidad` como `date`). Si el `sku` ya existe, lanza `ValueError` |
| `eliminar(sku)` | Elimina el producto. Si no existe, lanza `KeyError` |
| `buscar(texto)` | Devuelve productos cuyo nombre contenga el texto, **sin distinguir mayúsculas** |
| `stock_bajo(umbral)` | Devuelve productos con `stock` menor al umbral |
| `proximos_a_caducar(dias, hoy=None)` | Devuelve los productos que **ya caducaron o caducan en los próximos `dias`**, ordenados del más urgente al menos. `hoy` es opcional (por defecto, la fecha actual) |
| `reporte()` | Devuelve `{"productos": n, "unidades": total_stock, "valor_total": suma(stock * precio)}` |

### Cómo trabajar

1. Escribe un docstring de módulo y de clase describiendo lo que quieres.
2. Escribe cada firma con tipos y deja que Copilot proponga.
3. Ejecuta las pruebas con frecuencia:

```bash
cd ejercicios/ej1-autocompletado
pytest -q
```

### Criterios de aceptación

- [ ] Las 8 pruebas de `test_inventario.py` pasan.
- [ ] Todos los métodos tienen type hints y docstring.
- [ ] No usaste el chat.
- [ ] Puedes explicar cada línea del código final.

### Para quien termine antes

Agrega `actualizar_stock(sku, delta)` que impida dejar el stock en negativo, y escribe a mano (con autocompletado) dos pruebas para ella.

---

*Solución de referencia: `soluciones/ej1/inventario.py` (solo para el instructor).*
