# 4. Contextualización

**Duración:** 20 min · **Tipo:** teoría + demo


!!! note "Pistas Python y JavaScript"
    Los ejemplos de este módulo usan archivos de la pista Python (`src/app.py`, `pytest`). En la pista JavaScript el equivalente es `src/app.js` con Jest: consulta las [equivalencias](../pistas.md#equivalencias-de-archivos).

Copilot responde con lo que ve. Controlar el contexto es la forma más barata de mejorar los resultados.

## Variables de contexto

| Variable | Qué agrega |
|---|---|
| `#file` | Un archivo específico (`#file:src/app.py`) |
| `#selection` | El texto seleccionado en el editor |
| `#codebase` | Búsqueda en todo el proyecto |

Ejemplos:

```text
Explica cómo se calcula el total en #file:src/app.py
¿Dónde se valida el campo precio? #codebase
Refactoriza #selection para usar un diccionario
```

## Adjuntar archivos e imágenes

- Arrastra un archivo o imagen al chat, o usa el botón **Add Context**.
- Las imágenes (mockups, capturas de errores, diagramas) requieren un modelo con visión.
- Menos contexto y más relevante supera a mucho contexto desordenado.

## Custom instructions

Archivo `.github/copilot-instructions.md`: reglas que Copilot aplica **a todas las conversaciones del proyecto**.

Buenas instrucciones son:

- **Cortas y concretas** (qué stack, qué estilo, qué evitar).
- **Verificables** ("type hints obligatorios", no "escribe buen código").
- Sobre el proyecto, no sobre temas generales.

Ejemplo en `soluciones/ej2/copilot-instructions.md`.

## Prompt files reutilizables

Archivos `.github/prompts/nombre.prompt.md` que se invocan con `/nombre` en el chat. Sirven para tareas repetibles: revisión de endpoints, generación de pruebas con el estándar del equipo, plantillas de PR.

```markdown
---
mode: ask
description: Revisa un endpoint Flask
---
Revisa ${selection} y lista problemas de validación, seguridad y pruebas faltantes.
```

Ejemplo completo en `soluciones/ej2/revisar-endpoint.prompt.md`.

## Demo del instructor (5 min)

1. Haz una pregunta sin contexto y otra con `#file`: compara.
2. Crea `.github/copilot-instructions.md` con una regla ("docstrings en español") y vuelve a pedir una función.
3. Crea un prompt file y ejecútalo con `/`.

## Puntos clave

1. El contexto correcto mejora más que un prompt largo.
2. Las instrucciones del proyecto evitan repetir reglas en cada mensaje.
3. Los prompt files convierten buenas prácticas en comandos del equipo.
