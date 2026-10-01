"""Pruebas de validación del cierre del Ejercicio 1 (vienen incluidas; no las modifiques)."""
from datetime import date

import pytest

from inventario import Inventario

HOY = date(2026, 10, 1)


@pytest.fixture
def inv():
    i = Inventario()
    i.agregar({"sku": "A1", "nombre": "Paracetamol 500 mg", "stock": 120, "precio": 45.0, "caducidad": date(2027, 6, 30)})
    i.agregar({"sku": "B2", "nombre": "Amoxicilina 500 mg", "stock": 3, "precio": 129.5, "caducidad": date(2026, 11, 15)})
    i.agregar({"sku": "C3", "nombre": "Vitamina C 1 g", "stock": 0, "precio": 89.0, "caducidad": date(2026, 10, 20)})
    i.agregar({"sku": "D4", "nombre": "Jarabe para la tos", "stock": 5, "precio": 70.0, "caducidad": date(2026, 9, 15)})
    return i


def test_agregar_duplicado_lanza_error(inv):
    with pytest.raises(ValueError):
        inv.agregar({"sku": "A1", "nombre": "Otro", "stock": 1, "precio": 1.0, "caducidad": HOY})


def test_eliminar(inv):
    inv.eliminar("A1")
    assert inv.buscar("paracetamol") == []


def test_eliminar_inexistente_lanza_error(inv):
    with pytest.raises(KeyError):
        inv.eliminar("ZZZ")


def test_buscar_ignora_mayusculas(inv):
    assert [p["sku"] for p in inv.buscar("VITAMINA")] == ["C3"]


def test_stock_bajo(inv):
    assert sorted(p["sku"] for p in inv.stock_bajo(5)) == ["B2", "C3"]


def test_proximos_a_caducar_incluye_vencidos_y_ordena_por_fecha(inv):
    # Límite: 1-oct + 60 días = 30-nov. D4 ya venció; C3 y B2 vencen dentro del plazo; A1 no.
    assert [p["sku"] for p in inv.proximos_a_caducar(60, hoy=HOY)] == ["D4", "C3", "B2"]


def test_proximos_a_caducar_con_plazo_corto(inv):
    assert [p["sku"] for p in inv.proximos_a_caducar(30, hoy=HOY)] == ["D4", "C3"]


def test_reporte_incluye_valor_total(inv):
    reporte = inv.reporte()
    assert reporte["productos"] == 4
    assert reporte["unidades"] == 128
    assert reporte["valor_total"] == pytest.approx(120 * 45.0 + 3 * 129.5 + 5 * 70.0)
