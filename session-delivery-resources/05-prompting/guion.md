# Módulo 5: Prompting (15 min) y Ejercicio 2 (30 min)

**Material:** [`docs/modulos/05-prompting.md`](../../docs/modulos/05-prompting.md) · **Ejercicio:** [`ej2`](../../docs/ejercicios/ej2-chat-contexto-prompting.md)

## Teoría (15 min)

| Min | Qué hacer |
|---|---|
| 0–5 | Anatomía del prompt: contexto, intención, restricciones, ejemplo |
| 5–10 | **Demo en vivo del antes y después**: ejecuta `hazme validaciones` y luego el prompt completo. Muestra la diferencia |
| 10–12 | Antipatrones y acotar el alcance |
| 12–15 | Iterar vs. reiniciar: demuestra un mensaje de seguimiento preciso |

## Ejercicio 2 (30 min)

| Parte | Min | Qué observar |
|---|---|---|
| 1. Chat, slash commands, modelos | 8 | Que usen `Ctrl+I` y comparen modelos |
| 2. Contexto e instrucciones | 10 | Reglas **verificables**, no vagas |
| 3. Mejora del prompt | 12 | Que **iteren** en lugar de reiniciar |

## Revisión de las instrucciones

Mala: "Escribe código limpio y bueno." → no se puede verificar.
Buena: "Type hints obligatorios; docstrings en español; validar toda entrada."

## Bug de `f3` (parte 1)

`utilidades.py` tiene un promedio móvil que, en los últimos elementos, divide entre `n` ventanas incompletas (da valores menores a los reales). Corrección: calcular solo ventanas completas (`range(len(l) - n + 1)`). Referencia: `soluciones/ej2/utilidades.py`.

## Puesta en común (últimos 3 min)

Pide a 2 alumnos que muestren su prompt mejorado y el que casi funcionaba.
