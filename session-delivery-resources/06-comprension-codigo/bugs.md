# Bugs sembrados en el script legacy (solo para el instructor)

Hay una versión por pista: `reporte_ventas.py` (Python) y `reporte_ventas.js` (JavaScript). Los tres bugs son equivalentes, pero **el Bug 3 se comporta distinto** (ver la sección de JavaScript al final).

## Pista Python: `reporte_ventas.py`

Salida **con bugs** sobre `ventas.csv`: el top calcula mal y termina con `ZeroDivisionError`.

| # | Bug | Línea (original) | Síntoma | Corrección | ¿Se nota? |
|---|---|---|---|---|---|
| 1 | **Off-by-one**: `range(len(r) - 1)` omite la última fila | `for i in range(len(r) - 1)` | Falta la venta del 30-ene (Luis, 1798.00): sus totales y los de la región Sur salen menores | `range(len(r))` o iterar `for fila in r` | **No**: solo comparando a mano |
| 2 | **Orden por texto**: `str(z[1][0])` ordena lexicográficamente | `key=lambda z: str(z[1][0])` | El top queda en orden incorrecto (p. ej. `"9475.0"` queda por encima de `"17841.0"`) | `key=lambda z: z[1][0]` | **No**: parece un ranking razonable |
| 3 | **División entre cero**: la región `Occidente` no tiene ventas | `g[k][0] / g[k][1]` | `ZeroDivisionError` al imprimir el ticket promedio | Proteger el caso sin ventas (mostrar "sin ventas"), no ocultar con `try/except` genérico | **Sí**: falla con traceback |

## Valores correctos (solución de referencia)

```
TOP VENDEDORES
1 Marta 17841.0 3
2 Ana 9475.0 3
3 Luis 5196.0 3
TICKET PROMEDIO POR REGION
Norte 3158.33
Sur 1719.0
Centro 5947.0
Occidente sin ventas
TOTAL 35911.0
```

## Verificación manual (la que deben hacer los alumnos)

Ventas de **Marta**: 2094.00 + 4497.00 + 11250.00 = **17 841.00** (3 ventas).
Total general: **35 911.00**.

## Cómo discutirlo

- El Bug 3 es el que "grita"; los alumnos lo arreglan primero. Los otros dos requieren **desconfiar de los números**.
- Si Copilot propone `try/except ZeroDivisionError: pass`, el programa deja de fallar pero **pierde información**: discútanlo.
- Los bugs se enmascaran entre sí. Salida real al ir corrigiendo uno por uno:

    | Estado | Top 3 | Total |
    |---|---|---|
    | Original (Bug 3 falla antes de imprimir el total) | Ana, Jorge, Luis | no se imprime |
    | Solo Bug 3 | Ana, Jorge, Luis | 34113.0 |
    | Bugs 3 + 2 | **Marta**, Ana, Jorge | 34113.0 |
    | Todo corregido | Marta, Ana, **Luis** (5196.0) | 35911.0 |

  Tras corregir el Bug 2, Marta aparece primero; solo al corregir el Bug 1 Luis recupera su tercer lugar (la venta omitida valía 1798.00). Úsalo para mostrar por qué se corrige de uno en uno y se vuelve a ejecutar.


## Pista JavaScript: `reporte_ventas.js`

Mismos datos (`ventas.csv`) y mismos bugs. La diferencia: **ninguno detiene el programa**.

| # | Bug | Código | Síntoma | Corrección |
|---|---|---|---|---|
| 1 | **Off-by-one** | `for (var i = 0; i < r.length - 1; i++)` | Falta la venta del 30-ene (Luis, 1798): totales de Luis y de Sur menores | `i < r.length` o `for...of` |
| 2 | **Orden por texto** | `String(b[1][0]) > String(a[1][0]) ? 1 : -1` | El top queda mal: Marta (17841) queda fuera porque `"17841"` < `"3399"` como cadenas | `b[1][0] - a[1][0]` |
| 3 | **`0 / 0` da `NaN`** | `g[k][0] / g[k][1]` | La región `Occidente` imprime `NaN` en vez de fallar | Tratar el caso sin ventas (mostrar "sin ventas"); no convertir `NaN` en `0` |

### Salida real al corregir uno por uno

| Estado | Top 3 | Ticket Occidente | Total |
|---|---|---|---|
| Original | Ana (9475), Jorge (3399), Luis (3398) | `NaN` | 34113 |
| Solo Bug 2 | **Marta**, Ana, Jorge | `NaN` | 34113 |
| Bugs 2 + 1 | Marta, Ana, **Luis (5196)** | `NaN` | 35911 |
| Todo corregido | Marta, Ana, Luis | sin ventas | 35911 |

### Cómo discutirlo

- En JavaScript no hay un `traceback` que delate el Bug 3: hay que **mirar la salida**. Es la lección del ejercicio.
- Si Copilot propone `|| 0` para el `NaN`, el ticket de Occidente aparece como `0`: se ve "bien" pero es información falsa (no es un promedio de cero, es que no hubo ventas).
- `NaN` contagia: cualquier operación posterior con él también da `NaN`. Úsalo para explicar por qué conviene validar antes de operar.
