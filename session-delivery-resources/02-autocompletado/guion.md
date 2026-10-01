# Módulo 2: Autocompletado (100 min)

**Material:** [`docs/modulos/02-autocompletado.md`](../../docs/modulos/02-autocompletado.md) · **Ejercicio:** [`ej1`](../../docs/ejercicios/ej1-autocompletado.md)

| Min | Qué hacer |
|---|---|
| 0–6 | Teoría ghost text + demo en vivo (`calcular_iva`): `Tab`, `Esc`, `Alt+]`, `Ctrl+→` |
| 6–16 | **Tramo A** (alumnos) |
| 16–22 | Teoría comentarios + demo. Muestra mejorar el comentario en vez del código |
| 22–32 | **Tramo B** (alumnos) |
| 32–38 | Teoría NES + demo del renombrado en cascada |
| 38–48 | **Tramo C** (alumnos) |
| 48–50 | Puesta en común rápida: ¿qué rechazaron? |
| 50–100 | **Ejercicio completo: `inventario.py`**. Tú circulas por el salón |

## Qué revisar mientras circulas

- Tramo A: `es_email_valido`. Suele aceptar `a@b` o casos raros. Úsalo para mostrar que **hay que probar**.
- Tramo B: ¿reescriben comentarios o editan código a mano? Pide lo primero.
- Tramo C: ¿quedó algún `"nombre"` sin cambiar? Es la trampa del ejercicio.
- Ejercicio completo: que no usen el chat y que ejecuten `pytest` seguido.

## Errores frecuentes

| Error | Qué decir |
|---|---|
| Aceptan todo con `Tab` sin leer | "Lee antes de aceptar. ¿Qué pasa si el stock es negativo?" |
| Sin sugerencias (extensión desconectada) | Revisar sesión de GitHub en VS Code |
| `Ctrl+Enter` no abre el panel | El atajo varía por versión y sistema; buscar en Keyboard Shortcuts |

## Solución

`soluciones/ej1/inventario.py`. Ritmo: si a los 80 min nadie termina, muestra la clase `Inventario` completa y revisa qué sugerencias fueron mejores.
