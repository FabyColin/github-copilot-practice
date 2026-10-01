# 6. Comprensión y corrección de código

**Duración:** 10 min teoría + 30 min de [Ejercicio 3](../ejercicios/ej3-codigo-legacy.md)

## Explicar código legacy desconocido

Estrategia en tres pasos, de lo general a lo particular:

1. **Panorama** (modo Ask): "Resume qué hace este script, sus entradas y salidas."
2. **Detalle** (`/explain` sobre una selección): línea por línea o por bloques.
3. **Mapa de dependencias**: "¿Qué funciones llaman a esta? ¿Qué pasa si cambio su resultado?"

!!! tip
    Pide a Copilot que **renombre mentalmente** las variables: "propón nombres descriptivos para `f`, `d`, `r` y `t`". Es una forma rápida de entender el propósito.

## Diagnóstico y corrección de bugs

Un buen reporte de bug para Copilot incluye:

| Elemento | Ejemplo |
|---|---|
| Qué esperabas | "El top debería mostrar a Marta primero" |
| Qué pasó | "Muestra a Ana primero" |
| Cómo reproducirlo | `python reporte_ventas.py ventas.csv` |
| Error (si hay) | Pega el traceback |

Flujo:

1. Reproduce el problema.
2. Pide **causa** antes que corrección: "¿por qué ocurre?"
3. Aplica `/fix` o la corrección propuesta.
4. **Verifica**: vuelve a ejecutar y comprueba.

!!! warning
    Un fix que "hace desaparecer el error" no siempre corrige la causa. Exige la explicación.

## Navegar una base de código con preguntas

Con `#codebase` puedes preguntar:

- "¿Dónde se calcula el total del pedido?"
- "¿Qué endpoints modifican datos?"
- "¿Qué pruebas cubren esta función?"

Después **verifica abriendo los archivos** que menciona.

## Puntos clave

1. Entiende antes de cambiar.
2. Pide la causa, no solo el parche.
3. Verifica siempre ejecutando.
