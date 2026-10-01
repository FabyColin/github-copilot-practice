# Ejercicio 2: Configura tu copiloto y mejora un prompt

**Módulos:** [3. Chat](../../modulos/03-chat.md), [4. Contextualización](../../modulos/04-contextualizacion.md), [5. Prompting](../../modulos/05-prompting.md) · **Tiempo:** 30 min
**Archivos:** `ejercicios/ej2-chat-contexto-prompting/utilidades.py` y `src/app.py`

## Parte 1: chat, slash commands y modelos (8 min)

Abre `utilidades.py`. Tiene cuatro funciones con nombres crípticos (`f1` a `f4`).

1. Selecciona `f1` y usa **inline chat** (`Ctrl+I`): "renombra la función y las variables con nombres descriptivos y agrega type hints".
2. Selecciona `f2` y ejecuta `/doc` en el panel.
3. Selecciona `f3` y ejecuta `/explain`. Después `/fix`: el promedio móvil tiene un bug en los últimos elementos. Antes de aceptar el arreglo, **pide la causa**.
4. En modo **Ask** pregunta lo mismo con dos modelos distintos y compara.

**Anota:** qué modelo respondió mejor y por qué.

## Parte 2: contexto e instrucciones del proyecto (10 min)

1. Con `#file:src/app.py`, pregunta: "¿Qué validaciones faltan en `POST /products`?"
2. Crea `.github/copilot-instructions.md` con **al menos 4 reglas verificables**. Ejemplo de temas: type hints, idioma de docstrings, estilo de nombres, validación de entrada.
3. Crea `.github/prompts/revisar-endpoint.prompt.md` que revise un endpoint seleccionado y devuelva una tabla de problemas.
4. Selecciona un endpoint y ejecútalo con `/revisar-endpoint`.

## Parte 3: mejora un prompt (12 min)

Prompt vago de partida:

```text
hazme validaciones
```

1. Ejecútalo tal cual en modo **Ask** y guarda la respuesta.
2. Reescríbelo con **contexto, intención, restricciones y ejemplo** (módulo 5).
3. Ejecútalo y compara.
4. La respuesta casi sirve, pero no del todo: **itera** con un mensaje de seguimiento preciso (no empieces de cero).

## Criterios de aceptación

- [ ] `utilidades.py` tiene nombres descriptivos, type hints y docstrings.
- [ ] El bug de `f3` está corregido y puedes explicar su causa.
- [ ] `copilot-instructions.md` tiene reglas **verificables** (no "escribe buen código").
- [ ] El prompt file funciona al invocarlo con `/`.
- [ ] Las instrucciones se reflejan en una respuesta nueva **sin que las repitas** en el mensaje.
- [ ] Guardaste el prompt vago, el mejorado y tu mensaje de iteración.

## Para quien termine antes

Crea un segundo prompt file, `generar-pruebas.prompt.md`, con el estándar de pruebas del equipo (pytest, `parametrize`, un caso borde por función).

---

*Soluciones de referencia: `soluciones/ej2/` (solo para el instructor).*
