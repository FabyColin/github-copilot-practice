"""Reporte de ventas: top de vendedores, ticket promedio por región y total.

Solución de referencia del Ejercicio 3 (versión legible y corregida).
"""
import csv
import sys

REGIONES = ["Norte", "Sur", "Centro", "Occidente"]


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


def ticket_promedio_por_region(ventas):
    acumulado = {region: {"monto": 0.0, "ventas": 0} for region in REGIONES}
    for venta in ventas:
        region = acumulado[venta["region"]]
        region["monto"] += float(venta["monto"])
        region["ventas"] += 1
    # Bug 3 corregido: sin ventas no hay promedio, en lugar de dividir entre cero
    return {
        region: (datos["monto"] / datos["ventas"] if datos["ventas"] else None)
        for region, datos in acumulado.items()
    }


def imprimir_reporte(ventas):
    totales = totales_por_vendedor(ventas)
    # Bug 2 corregido: se ordena por número, no por texto ("950.0" > "12000.0" como cadenas)
    ranking = sorted(totales.items(), key=lambda par: par[1]["monto"], reverse=True)

    print("TOP VENDEDORES")
    for posicion, (vendedor, datos) in enumerate(ranking[:3], start=1):
        print(posicion, vendedor, datos["monto"], datos["ventas"])

    print("TICKET PROMEDIO POR REGION")
    for region, promedio in ticket_promedio_por_region(ventas).items():
        print(region, "sin ventas" if promedio is None else round(promedio, 2))

    print("TOTAL", sum(datos["monto"] for datos in totales.values()))


if __name__ == "__main__":
    imprimir_reporte(leer_ventas(sys.argv[1]))
