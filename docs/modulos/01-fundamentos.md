# 1. Fundamentos

**Duración:** 20 min · **Tipo:** teoría

## Qué es GitHub Copilot y dónde vive

Copilot es un asistente de IA para desarrollo. No es una sola herramienta, sino varias superficies:

| Superficie | Para qué se usa |
|---|---|
| **IDE** (VS Code, Visual Studio, JetBrains…) | Autocompletado, chat, modo Agent. Es donde pasaremos el día |
| **github.com** | Chat web, asignar issues al cloud agent, code review en pull requests |
| **CLI** (`copilot`, `gh copilot`) | Preguntas y tareas desde la terminal |

## Planes, cuotas y qué consume créditos

Los planes (Free, Pro, Pro+, Business, Enterprise) cambian en límites y modelos disponibles. **Las cifras exactas cambian con frecuencia: verifícalas en la [página oficial de planes](https://github.com/features/copilot/plans) el día del curso.**

La idea importante es distinguir qué consume qué:

| Uso | Consumo |
|---|---|
| Sugerencias inline (completions) | Normalmente no consumen solicitudes premium en planes de pago |
| Chat y modo Agent | Cada interacción cuenta; los modelos más potentes pueden contar más |
| Cloud agent | Consume solicitudes premium por tarea |

!!! note "Para el instructor"
    Muestra en vivo el medidor de uso en github.com/settings/copilot y completa la tabla con las cuotas reales del plan de la audiencia.

## Privacidad, uso responsable y validación humana

- **Qué se envía:** el código y el contexto que Copilot necesita para responder. Revisa la política de tu plan sobre retención y entrenamiento.
- **No compartas** secretos, credenciales, datos personales ni código de clientes sin autorización.
- **Filtro de coincidencias con código público:** puede activarse en la configuración de la cuenta u organización.
- **Tú eres el autor.** Todo código sugerido debe revisarse, ejecutarse y probarse antes de aceptarse.

### Regla de oro del curso

> Si no puedes explicar lo que hace una sugerencia, no la aceptes.

## Puntos clave

1. Copilot acelera, pero no reemplaza la revisión humana.
2. Inline, chat y agente son herramientas distintas para tareas distintas.
3. Conocer lo que consume créditos evita sorpresas.
