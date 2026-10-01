"""Solución de referencia del Ejercicio 1."""
from datetime import date, timedelta


class Inventario:
    def __init__(self):
        self._productos = {}

    def agregar(self, producto: dict) -> None:
        sku = producto["sku"]
        if sku in self._productos:
            raise ValueError(f"El SKU {sku} ya existe")
        self._productos[sku] = dict(producto)

    def eliminar(self, sku: str) -> None:
        del self._productos[sku]  # KeyError si no existe

    def buscar(self, texto: str) -> list:
        texto = texto.lower()
        return [p for p in self._productos.values() if texto in p["nombre"].lower()]

    def stock_bajo(self, umbral: int) -> list:
        return [p for p in self._productos.values() if p["stock"] < umbral]

    def proximos_a_caducar(self, dias: int, hoy: date | None = None) -> list:
        """Productos que ya caducaron o caducan en los próximos `dias`, del más urgente al menos."""
        limite = (hoy or date.today()) + timedelta(days=dias)
        proximos = [p for p in self._productos.values() if p["caducidad"] <= limite]
        return sorted(proximos, key=lambda p: p["caducidad"])

    def reporte(self) -> dict:
        productos = self._productos.values()
        return {
            "productos": len(self._productos),
            "unidades": sum(p["stock"] for p in productos),
            "valor_total": sum(p["stock"] * p["precio"] for p in productos),
        }
