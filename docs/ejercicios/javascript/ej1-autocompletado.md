# Ejercicio 1: Autocompletado (JavaScript)

**Módulo:** [2. Autocompletado](../../modulos/02-autocompletado.md) · **Tiempo:** 30 min (3 tramos aislados) + 50 min (ejercicio completo)
**Carpeta:** `ejercicios/ej1-autocompletado/`

!!! warning "Regla del ejercicio"
    Nada de chat. Solo autocompletado, comentarios y NES.

## Tramo A: ghost text (10 min)

**Archivo:** `tramoA_ghostText.js`

1. En cada función, borra el cuerpo y escribe de nuevo solo la firma.
2. Observa la sugerencia. Practica: `Tab` (aceptar), `Esc` (descartar), `Alt+]` (otra alternativa), `Ctrl+→` (aceptar una palabra).
3. Para `esEmailValido`, revisa con cuidado: ¿la sugerencia valida bien `a@b`, `a@@b.com` o un correo vacío?

**Entregable:** las 4 funciones completas y una nota con **una sugerencia que rechazaste** y por qué.

## Tramo B: guiado por comentarios (10 min)

**Archivo:** `tramoB_comentarios.js`

1. Bajo cada comentario, escribe la firma de la función y deja que Copilot complete.
2. Si la sugerencia no es lo que querías, **mejora el comentario** (no el código) y vuelve a intentar.
3. Prueba cada función con `PRODUCTOS` en `node` (por ejemplo `node -i`).

**Entregable:** 4 funciones funcionando. Anota cuántos comentarios tuviste que reescribir.

## Tramo C: Next Edit Suggestions (10 min)

**Archivo:** `tramoC_nes.js`

1. Confirma que `github.copilot.nextEditSuggestions.enabled` está activo.
2. En `crearProducto` cambia la propiedad `nombre` por `nombreComercial`.
3. Sigue las sugerencias de Copilot con `Tab` y **revisa cada una** antes de aceptar. Ojo con la desestructuración `({ nombre })` y con los accesos `p.nombre`.
4. Al terminar, busca (`Ctrl+F`) si quedó alguna referencia a `nombre` que NES no detectó.

**Entregable:** el archivo con `nombreComercial` en todos lados y consistente.

## Ejercicio completo: módulo de inventario (50 min)

**Archivo:** `inventario.js` · **Validación:** `inventario.test.js`

Construye la clase `Inventario` de la farmacia usando **solo autocompletado** y expórtala con `module.exports = { Inventario }`:

| Método | Comportamiento |
|---|---|
| `agregar(producto)` | Guarda un producto (objeto con `sku`, `nombre`, `stock`, `precio` y `caducidad` como `Date`). Si el `sku` ya existe, lanza un `Error` |
| `eliminar(sku)` | Elimina el producto. Si no existe, lanza un `Error` |
| `buscar(texto)` | Devuelve productos cuyo nombre contenga el texto, **sin distinguir mayúsculas** |
| `stockBajo(umbral)` | Devuelve productos con `stock` menor al umbral |
| `proximosACaducar(dias, hoy)` | Devuelve los productos que **ya caducaron o caducan en los próximos `dias`**, ordenados del más urgente al menos. `hoy` es opcional (por defecto, la fecha actual) |
| `reporte()` | Devuelve `{ productos, unidades, valorTotal }` con `valorTotal = suma(stock * precio)` |

### Cómo trabajar

1. Escribe un comentario JSDoc de la clase describiendo lo que quieres.
2. Escribe cada firma y deja que Copilot proponga.
3. Ejecuta las pruebas con frecuencia:

```bash
npm run test:ej -- ej1
```

### Criterios de aceptación

- [ ] Las 8 pruebas de `inventario.test.js` pasan.
- [ ] Todos los métodos tienen JSDoc.
- [ ] No usaste el chat.
- [ ] Puedes explicar cada línea del código final.

### Para quien termine antes

Agrega `actualizarStock(sku, delta)` que impida dejar el stock en negativo, y escribe a mano (con autocompletado) dos pruebas para ella.

---

*Solución de referencia: `soluciones/ej1/inventario.js` (solo para el instructor).*
