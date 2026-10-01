"""Reporte de ventas: top de vendedores, ticket promedio por sucursal y total.

Solución de referencia del Ejercicio 3 (versión legible y corregida).
"""
import csv
import sys

SUCURSALES = ["Norte", "Sur", "Centro", "Occidente"]


def leer_ventas(ruta):
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def totales_por_vendedor(ventas):
    totales = {}
    for venta in ventas:  # Bug 1 corregido: se procesan TODAS las filas
        acumulado = totales.setdefault(venta["vendedor"], {"monto": 0.0, "ventas": 0})
        acumulado["monto"] += float(venta["monto"])
        acumulado["ventas"] += 1
    return totales


def ticket_promedio_por_sucursal(ventas):
    acumulado = {sucursal: {"monto": 0.0, "ventas": 0} for sucursal in SUCURSALES}
    for venta in ventas:
        sucursal = acumulado[venta["sucursal"]]
        sucursal["monto"] += float(venta["monto"])
        sucursal["ventas"] += 1
    # Bug 3 corregido: sin ventas no hay promedio, en lugar de dividir entre cero
    return {
        sucursal: (datos["monto"] / datos["ventas"] if datos["ventas"] else None)
        for sucursal, datos in acumulado.items()
    }


def imprimir_reporte(ventas):
    totales = totales_por_vendedor(ventas)
    # Bug 2 corregido: se ordena por número, no por texto ("950.0" > "12000.0" como cadenas)
    ranking = sorted(totales.items(), key=lambda par: par[1]["monto"], reverse=True)

    print("TOP VENDEDORES")
    for posicion, (vendedor, datos) in enumerate(ranking[:3], start=1):
        print(posicion, vendedor, datos["monto"], datos["ventas"])

    print("TICKET PROMEDIO POR SUCURSAL")
    for sucursal, promedio in ticket_promedio_por_sucursal(ventas).items():
        print(sucursal, "sin ventas" if promedio is None else round(promedio, 2))

    print("TOTAL", sum(datos["monto"] for datos in totales.values()))


if __name__ == "__main__":
    imprimir_reporte(leer_ventas(sys.argv[1]))
