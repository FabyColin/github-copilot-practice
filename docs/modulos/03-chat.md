# 3. Chat

**Duración:** 20 min · **Tipo:** teoría + demo

## Chat en panel vs inline chat

| | Chat en panel | Inline chat (`Ctrl+I`) |
|---|---|---|
| Dónde | Barra lateral | Sobre el código |
| Úsalo para | Conversaciones largas, varios archivos, preguntas de diseño | Cambios puntuales en una selección |
| Resultado | Respuesta con bloques de código | Diff directamente en el editor |

## Modos: Ask, Plan y Agent

| Modo | Qué hace | Cuándo usarlo |
|---|---|---|
| **Ask** | Responde preguntas, no modifica archivos | Entender, explorar, pedir opinión |
| **Plan** | Investiga y propone un plan paso a paso antes de actuar | Cambios medianos o grandes que quieres revisar primero |
| **Agent** | Edita varios archivos y ejecuta comandos, con tu aprobación | Implementar una tarea completa |

Regla práctica: **Ask para entender, Plan para decidir, Agent para ejecutar.**

!!! note
    La interfaz del chat cambia con frecuencia entre versiones. Si ves nombres distintos, busca el equivalente.

## Slash commands

| Comando | Qué hace |
|---|---|
| `/explain` | Explica el código seleccionado |
| `/fix` | Propone una corrección para un error o problema |
| `/tests` | Genera pruebas para el código seleccionado |
| `/doc` | Genera documentación o docstrings |

## Selección de modelo

El selector del chat permite elegir el modelo. En general:

- Modelos **rápidos y ligeros** para tareas simples y preguntas.
- Modelos de **razonamiento** para depuración difícil, diseño y planes complejos.
- Algunos modelos consumen más solicitudes premium que otros.

## Demo del instructor (5 min)

1. Selecciona una función de `src/app.py` → `Ctrl+I` → "agrega validación de precio negativo".
2. Abre el panel → modo Ask → "¿qué endpoints expone esta app?".
3. Repite la misma pregunta con otro modelo y compara.

## Puntos clave

1. Elige el modo según el riesgo de la tarea.
2. Inline para lo puntual, panel para lo amplio.
3. Compara modelos antes de asumir que uno es mejor.
