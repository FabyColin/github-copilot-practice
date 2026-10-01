# 5. Prompting

**Duración:** 15 min · **Tipo:** teoría. Se practica en el [Ejercicio 2](../ejercicios/ej2-chat-contexto-prompting.md).

## Anatomía de un buen prompt

| Elemento | Pregunta que responde | Ejemplo |
|---|---|---|
| **Contexto** | ¿Dónde estamos? | "En la API Flask de `#file:src/app.py`…" |
| **Intención** | ¿Qué quiero lograr? | "…agrega validación al endpoint `POST /products`" |
| **Restricciones** | ¿Qué límites hay? | "…sin nuevas dependencias, no cambies otros endpoints" |
| **Ejemplo** | ¿Cómo se ve lo correcto? | "Si el precio es negativo, responde 400 con `{'error': '...'}`" |

### Antes y después

❌ `hazme validaciones`

✅ `En #file:src/app.py agrega validación al endpoint POST /products: nombre obligatorio (texto no vacío), precio numérico mayor o igual a 0 y categoría dentro de CATEGORIAS. Si falla, responde 400 con {"error": "<motivo>"}. No cambies los demás endpoints ni agregues dependencias.`

## Antipatrones

| Antipatrón | Problema | Mejor |
|---|---|---|
| Prompt vago | El modelo adivina | Contexto + intención + restricciones |
| Pedir todo a la vez | Cambios enormes, difíciles de revisar | Dividir en pasos pequeños |
| Sin límites de alcance | El agente toca archivos no deseados | "Solo modifica X; no toques Y" |
| Mezclar temas | Respuestas confusas | Un tema por conversación |
| Aceptar sin leer | Bugs en producción | Revisar cada cambio |

## Acotar el alcance

Frases útiles:

- "Modifica **solo** `src/app.py`."
- "No cambies las pruebas existentes."
- "Antes de editar, dime qué archivos vas a tocar."

## Iterar en lugar de empezar de cero

Cuando la respuesta casi sirve:

1. **Señala lo que está bien**: "La estructura está bien."
2. **Señala lo que falla, con precisión**: "El caso de precio cero devuelve 400; debe aceptarse."
3. **Pide un cambio acotado**: "Corrige solo eso."

Empezar de cero pierde el contexto acumulado y suele repetir los mismos errores.

## Puntos clave

1. Contexto + intención + restricciones + ejemplo.
2. Pasos pequeños, revisables.
3. Iterar con precisión supera a reiniciar.
