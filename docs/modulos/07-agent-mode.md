# 7. Agent mode

**Duración:** 20 min · **Tipo:** teoría + demo. Se practica en el [Ejercicio 4](../ejercicios/ej4-agent-descuentos.md).

El modo Agent trabaja por ti en varios pasos: lee archivos, edita varios a la vez, ejecuta comandos en la terminal, ve los errores y corrige. **Tú sigues al mando.**

## Planear antes de ejecutar

Para cualquier cambio no trivial:

1. Pide un plan (modo **Plan**) y léelo.
2. Ajusta lo que no te convenza: "no uses una clase nueva", "no toques `templates/`".
3. Solo entonces pasa a ejecutar.

Un plan que revisas en 2 minutos te ahorra 20 minutos de deshacer cambios.

## Ediciones multi-archivo y comandos con aprobación

- El agente propone ediciones en varios archivos; las ves como **diffs**.
- Antes de ejecutar un comando de terminal te pide **aprobación**. Léelo antes de aprobar: `pip install`, borrados y comandos de red merecen atención extra.
- Puedes rechazar un comando y explicar por qué.

## Revisión de diffs, checkpoints y cómo deshacer

| Necesidad | Qué hacer |
|---|---|
| Aceptar o rechazar un archivo | Botones **Keep** / **Undo** por archivo o por bloque |
| Volver a un punto anterior de la conversación | **Checkpoint**: restaura archivos y chat a ese momento |
| Cambios ya aceptados | `Ctrl+Z` en el archivo o `git restore` / `git diff` |
| Seguridad extra | Haz `git commit` antes de empezar una tarea grande |

!!! tip
    Trabaja en una rama limpia. Con `git diff` ves exactamente qué tocó el agente.

## Limitar alcance para evitar cambios no deseados

- Nombra los archivos permitidos: "Modifica solo `src/app.py` y crea `src/descuentos.py`."
- Prohíbe explícitamente: "No cambies las pruebas existentes ni `requirements.txt`."
- Pide confirmación: "Antes de instalar paquetes, pregúntame."
- Si el agente se desvía, **detén la sesión** y reformula; no sigas parchando.

## Demo del instructor (8 min)

1. Plan: "Agrega el campo `stock_minimo` a los productos y un endpoint `GET /products/bajo-stock`".
2. Revisa el plan, ajusta, ejecuta.
3. Recorre los diffs, rechaza un cambio, restaura un checkpoint.

## Puntos clave

1. Plan primero, ejecución después.
2. Los diffs son tu red de seguridad: léelos.
3. El alcance lo defines tú, de forma explícita.
