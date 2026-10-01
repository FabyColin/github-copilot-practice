# Módulo 4: Contextualización (20 min)

**Material:** [`docs/modulos/04-contextualizacion.md`](../../docs/modulos/04-contextualizacion.md)

| Min | Qué hacer |
|---|---|
| 0–6 | Variables `#file`, `#selection`, `#codebase`. Demo: misma pregunta con y sin contexto |
| 6–10 | Adjuntar archivos e imágenes (muestra arrastrar un archivo) |
| 10–15 | Custom instructions: crea `.github/copilot-instructions.md` en vivo con una regla ("docstrings en español") y pide una función |
| 15–20 | Prompt files: crea uno y ejecútalo con `/` |

## Demo sugerida

1. Pregunta "¿cómo se calcula el total?" **sin** contexto → respuesta genérica.
2. Misma pregunta con `#file:src/app.py` → respuesta precisa.
3. Crea las instrucciones, pide una función nueva: se cumplen las reglas sin repetirlas.

## Errores frecuentes

- Instrucciones largas y vagas ("escribe código de calidad"). Exige reglas **verificables**.
- Olvidar que el archivo debe estar en `.github/copilot-instructions.md` exactamente.
- Prompt files en la ruta equivocada (`.github/prompts/`, extensión `.prompt.md`).

## Importante

Este módulo prepara el **Ejercicio 2**, donde los alumnos crean sus propios archivos. En la demo **no** dejes tu `copilot-instructions.md` en el repo que usarán ellos: bórralo o trabaja en una copia. Referencia: `soluciones/ej2/`.
