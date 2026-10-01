# Módulo 7: Agent mode (20 min)

**Material:** [`docs/modulos/07-agent-mode.md`](../../docs/modulos/07-agent-mode.md) · **Se practica en:** [`ej4`](../../docs/ejercicios/ej4-agent-descuentos.md)

| Min | Qué hacer |
|---|---|
| 0–4 | Qué es el modo Agent y en qué se diferencia de Ask/Plan |
| 4–8 | Planear antes de ejecutar: justifica el plan como red de seguridad |
| 8–18 | **Demo en vivo** (abajo) |
| 18–20 | Recapitulación: plan, diffs, alcance |

## Demo en vivo (10 min)

Antes de empezar: `git status` limpio y un commit de partida.

1. Modo **Plan**: "Agrega el campo `stock_minimo` a los productos (por defecto 5) y un endpoint `GET /products/bajo-stock` que liste los productos con stock menor o igual a su mínimo. Modifica solo `src/app.py`. No agregues dependencias."
2. Lee el plan en voz alta. Ajusta una cosa.
3. Pasa a **Agent** y ejecuta. Lee cada comando antes de aprobar.
4. Recorre los diffs; **rechaza un cambio** en vivo con Undo.
5. Restaura un **checkpoint**.
6. Cierra con `git diff --stat`: ¿se tocó algo fuera del alcance?
7. Revierte la demo: `git restore .`

!!! warning
    No dejes los cambios de la demo en el repo de los alumnos.

## Mensajes clave

- "Si el agente se desvía, detén y reformula; no parches sobre un camino equivocado."
- "El alcance lo defines tú: nombra lo permitido y lo prohibido."

## Errores frecuentes

| Error | Qué decir |
|---|---|
| Aprobar comandos sin leerlos | "Un `pip install` o un borrado merece lectura" |
| Prompt enorme de entrada | "Divide: una tarea, un plan" |
| No hacer commit antes | "Sin punto de retorno, deshacer es adivinar" |
