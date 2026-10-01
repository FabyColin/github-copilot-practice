"""Reglas de descuento por volumen y cupones (solución de referencia del Ejercicio 4)."""
from datetime import date

DESCUENTO_MAXIMO = 0.30

# Descuento por unidades totales del pedido: (mínimo de unidades, porcentaje)
ESCALAS_VOLUMEN = [(25, 0.10), (10, 0.05)]

CUPONES = {
    "BIENVENIDA10": {"porcentaje": 0.10, "vence": date(2099, 12, 31)},
    "VERANO15": {"porcentaje": 0.15, "vence": date(2099, 12, 31)},
    "VENCIDO20": {"porcentaje": 0.20, "vence": date(2020, 1, 1)},
}


class CuponInvalido(ValueError):
    """El cupón no existe o ya venció."""


def descuento_por_volumen(unidades: int) -> float:
    for minimo, porcentaje in ESCALAS_VOLUMEN:
        if unidades >= minimo:
            return porcentaje
    return 0.0


def descuento_por_cupon(codigo: str | None, hoy: date | None = None) -> float:
    if not codigo:
        return 0.0
    cupon = CUPONES.get(codigo.upper())
    if cupon is None:
        raise CuponInvalido(f"El cupón {codigo} no existe")
    if cupon["vence"] < (hoy or date.today()):
        raise CuponInvalido(f"El cupón {codigo} está vencido")
    return cupon["porcentaje"]


def calcular_total(subtotal: float, unidades: int, codigo: str | None = None, hoy: date | None = None) -> dict:
    """Combina descuento por volumen y por cupón, con un tope del 30 %."""
    if subtotal < 0 or unidades < 0:
        raise ValueError("El subtotal y las unidades no pueden ser negativos")
    porcentaje = min(
        descuento_por_volumen(unidades) + descuento_por_cupon(codigo, hoy),
        DESCUENTO_MAXIMO,
    )
    descuento = round(subtotal * porcentaje, 2)
    return {
        "subtotal": round(subtotal, 2),
        "descuento": descuento,
        "porcentaje_descuento": porcentaje,
        "total": round(subtotal - descuento, 2),
    }
