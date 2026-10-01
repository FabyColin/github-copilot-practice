# Ejercicio 4: Agent mode, descuentos y pruebas en verde

**Módulos:** [7. Agent mode](../../modulos/07-agent-mode.md) y [8. Pruebas unitarias](../../modulos/08-pruebas-unitarias.md) · **Tiempo:** 55 min
**Proyecto:** `src/` (farmacia en Flask)

## Escenario

El endpoint `POST /orders` calcula el total del pedido sin descuentos. Negocio pide:

### Reglas de negocio

| Regla | Detalle |
|---|---|
| **Descuento por volumen** | 5 a 9 piezas totales: 5 %. 10 o más: 10 % |
| **Cupones** | `SALUD10` (10 %) y `ADULTOMAYOR15` (15 %). Se envían en el campo `cupon` (sin distinguir mayúsculas) |
| **Cupón vencido o inexistente** | El pedido se rechaza con `400` y un mensaje claro |
| **Acumulación** | Volumen y cupón se suman, con un **tope total del 20 %** |
| **Receta** | Si algún producto tiene `requiere_receta` verdadero, el pedido debe traer `receta` (un folio de texto no vacío). Si falta o no es válido, `400` |
| **Validación** | `cantidad` debe ser un entero mayor que cero; si no, `400` |
| **Respuesta** | Incluye `subtotal`, `descuento`, `porcentaje_descuento` y `total` |

!!! note "Datos ficticios"
    Productos, precios, cupones y reglas son inventados con fines didácticos. No representan precios ni requisitos regulatorios reales.

### Restricciones

- La lógica de descuentos va en un módulo nuevo `src/descuentos.py`.
- Solo se modifica `src/app.py` y se crean `src/descuentos.py` y archivos de pruebas.
- **No** se modifican los endpoints de `/products` ni se agregan dependencias.

## Parte 1: planear (10 min)

1. Haz `git commit` (o crea una rama) para tener un punto de retorno.
2. En modo **Plan**, pega las reglas y las restricciones.
3. Lee el plan. Ajusta al menos una cosa (por ejemplo, la estructura de datos de los cupones).
4. **No ejecutes todavía.**

## Parte 2: ejecutar con control (20 min)

1. Pasa a modo **Agent** y ejecuta el plan.
2. Lee **cada comando de terminal** antes de aprobarlo.
3. Revisa los diffs por archivo. Practica **Undo** en al menos un cambio que no te guste.
4. Prueba un **checkpoint**: restaura uno y vuelve a avanzar.
5. Verifica con `git status` que **solo** se tocaron los archivos permitidos.

Prueba manual:

```bash
cd src && python app.py
```

```bash
curl -X POST localhost:5000/orders -H "Content-Type: application/json" \
  -d '{"items":[{"product_id":"p-001","cantidad":5}],"cupon":"SALUD10"}'
```

## Parte 3: pruebas en verde (25 min)

1. Con `/tests` genera pruebas para `descuentos.py` y para `POST /orders`.
2. Pide al agente que las ejecute **y que explique si el fallo está en la prueba o en el código antes de corregir**.
3. Pide explícitamente casos borde: 4 vs. 5 y 9 vs. 10 piezas, el tope del 20 %, receta faltante o inválida, cantidad negativa, cupón vencido, subtotal cero.
4. Mide cobertura:

```bash
cd src
pytest --cov=descuentos --cov-report=term-missing
```

5. **Mutación manual:** cambia un `>=` por `>` en `descuentos.py`. ¿Falla alguna prueba? Si no, tus pruebas son débiles. Revierte el cambio.

## Criterios de aceptación

- [ ] Todas las pruebas pasan.
- [ ] Cobertura de `descuentos.py` **mayor o igual al 85 %**.
- [ ] `git status` muestra solo los archivos permitidos.
- [ ] La prueba de mutación manual hizo fallar al menos una prueba.
- [ ] Un cupón vencido, una cantidad negativa y un medicamento con receta sin folio devuelven `400`.
- [ ] Puedes explicar el diff completo.

## Reflexión final (3 líneas)

¿Qué hizo el agente que **no** pediste? ¿Qué corregiste? ¿Qué harías distinto en el prompt?

---

*Solución de referencia: `soluciones/ej4/` (solo para el instructor).*
