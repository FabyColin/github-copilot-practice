# Módulo 8: Pruebas unitarias (10 min) y Ejercicio 4 (55 min)

**Material:** [`docs/modulos/08-pruebas-unitarias.md`](../../docs/modulos/08-pruebas-unitarias.md) · **Ejercicio:** [`ej4`](../../docs/ejercicios/ej4-agent-descuentos.md)

## Teoría (10 min)

| Min | Qué hacer |
|---|---|
| 0–3 | `/tests`: qué revisar en pruebas generadas (nombre, `assert` concreto, independencia) |
| 3–6 | Iterar hasta verde: "explica si falla la prueba o el código **antes** de corregir" |
| 6–10 | Casos borde y cobertura. Anuncia la **mutación manual** |

Aclara que el temario habla de Jest y aquí se usa **pytest** (mismo concepto).

## Ejercicio 4 (55 min)

| Parte | Min | Qué observar |
|---|---|---|
| 1. Plan | 10 | ¿Ajustan algo del plan o lo aceptan tal cual? |
| 2. Agent | 20 | Que lean los comandos, usen Undo y un checkpoint |
| 3. Pruebas | 25 | Casos borde explícitos y mutación manual |

## Puntos de control

- A los **10 min**: todos con un plan.
- A los **30 min**: todos con código funcionando. A quien siga atorado, dale `soluciones/ej4/descuentos.py` para que haga solo la parte de pruebas.
- A los **45 min**: todos con pruebas corriendo; comienza la mutación manual.

## Qué revisar

- `git status`: ¿solo `src/app.py`, `src/descuentos.py` y pruebas?
- ¿El agente **editó las pruebas para que pasen** en lugar de arreglar el código? Es la señal de alerta principal.
- Cobertura de `descuentos.py` mayor o igual a 85 %.

## Solución de referencia

`soluciones/ej4/`: `descuentos.py`, `app.py` y 26 pruebas (cobertura de `descuentos.py`: 100 %). Para probarla sin tocar `src/`:

```bash
mkdir /tmp/ej4 && cp -r src/. /tmp/ej4/
cp soluciones/ej4/app.py soluciones/ej4/descuentos.py /tmp/ej4/
cp soluciones/ej4/tests/*.py /tmp/ej4/tests/
cd /tmp/ej4 && pytest --cov=descuentos
```

## Errores frecuentes

| Error | Qué decir |
|---|---|
| Pruebas sin `assert` útil | "Cobertura no es calidad" |
| El agente toca `templates/` o `requirements.txt` | "Recuerda el alcance: dilo en el prompt" |
| Cupón vencido no se prueba | "¿Qué pasa el último día de vigencia?" |
