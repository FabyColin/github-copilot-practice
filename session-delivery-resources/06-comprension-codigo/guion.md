# Módulo 6: Comprensión y corrección (10 min) y Ejercicio 3 (30 min)

**Material:** [`docs/modulos/06-comprension-y-correccion.md`](../../docs/modulos/06-comprension-y-correccion.md) · **Ejercicio:** [`ej3`](../../docs/ejercicios/ej3-codigo-legacy.md) · **Bugs:** [`bugs.md`](bugs.md)

## Teoría (10 min)

| Min | Qué hacer |
|---|---|
| 0–4 | Estrategia para explicar código: panorama → detalle → dependencias |
| 4–8 | Reporte de bug: esperado / obtenido / reproducción. Pide **causa antes que parche** |
| 8–10 | `#codebase` para navegar |

## Ejercicio 3 (30 min)

| Parte | Min |
|---|---|
| 1. Entender (sin leer antes el código) | 10 |
| 2. Diagnosticar y corregir 3 bugs | 15 |
| 3. Refactor sin cambiar el resultado | 5 |

## Qué observar

- ¿Piden la causa o solo aceptan el parche?
- ¿Verifican ejecutando? El Bug 1 es silencioso: solo se detecta calculando a mano.
- ¿Copilot "arregla" el Bug 3 con un `try/except` que oculta el problema? Úsalo como ejemplo de arreglo superficial.

## Si el grupo es de la pista JavaScript

Los tres bugs son silenciosos (el Bug 3 imprime `NaN` en lugar de fallar). Insiste en **verificar la salida a mano**. Detalle en [`bugs.md`](bugs.md#pista-javascript-reporte_ventasjs).

## Cierre (2 min)

Pregunta: "¿Qué bug les costó más y por qué?" (casi siempre el Bug 1 o el 2: no lanzan error).
