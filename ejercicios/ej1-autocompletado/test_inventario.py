"""Pruebas de validación del cierre del Ejercicio 1 (las entrega el instructor)."""
import pytest

from inventario import Inventario


@pytest.fixture
def inv():
    i = Inventario()
    i.agregar({"sku": "A1", "nombre": "Martillo", "stock": 40, "precio": 190.0})
    i.agregar({"sku": "B2", "nombre": "Taladro", "stock": 3, "precio": 1500.0})
    i.agregar({"sku": "C3", "nombre": "Cinta aislante", "stock": 0, "precio": 30.0})
    return i


def test_agregar_duplicado_lanza_error(inv):
    with pytest.raises(ValueError):
        inv.agregar({"sku": "A1", "nombre": "Otro", "stock": 1, "precio": 1.0})


def test_eliminar(inv):
    inv.eliminar("A1")
    assert inv.buscar("martillo") == []


def test_eliminar_inexistente_lanza_error(inv):
    with pytest.raises(KeyError):
        inv.eliminar("ZZZ")


def test_buscar_ignora_mayusculas(inv):
    assert [p["sku"] for p in inv.buscar("CINTA")] == ["C3"]


def test_stock_bajo(inv):
    assert sorted(p["sku"] for p in inv.stock_bajo(5)) == ["B2", "C3"]


def test_reporte_incluye_valor_total(inv):
    reporte = inv.reporte()
    assert reporte["productos"] == 3
    assert reporte["unidades"] == 43
    assert reporte["valor_total"] == pytest.approx(40 * 190.0 + 3 * 1500.0)
