from datetime import date

import pytest

from descuentos import (
    CuponInvalido,
    calcular_total,
    descuento_por_cupon,
    descuento_por_volumen,
)


@pytest.mark.parametrize(
    "unidades,esperado",
    [(0, 0.0), (4, 0.0), (5, 0.05), (9, 0.05), (10, 0.10), (500, 0.10)],
)
def test_descuento_por_volumen(unidades, esperado):
    assert descuento_por_volumen(unidades) == esperado


def test_cupon_valido_sin_importar_mayusculas():
    assert descuento_por_cupon("salud10") == 0.10


def test_sin_cupon():
    assert descuento_por_cupon(None) == 0.0
    assert descuento_por_cupon("") == 0.0


def test_cupon_inexistente():
    with pytest.raises(CuponInvalido):
        descuento_por_cupon("NOEXISTE")


def test_cupon_vencido():
    with pytest.raises(CuponInvalido):
        descuento_por_cupon("VENCIDO20")


def test_cupon_valido_en_su_ultimo_dia():
    assert descuento_por_cupon("VENCIDO20", hoy=date(2020, 1, 1)) == 0.20


def test_descuentos_se_acumulan():
    resultado = calcular_total(1000, 5, "SALUD10")  # 5 % + 10 %
    assert resultado["porcentaje_descuento"] == pytest.approx(0.15)
    assert resultado["total"] == 850


def test_descuento_con_tope_del_20_por_ciento():
    resultado = calcular_total(1000, 10, "ADULTOMAYOR15")  # 10 % + 15 % = 25 %, se recorta a 20 %
    assert resultado["porcentaje_descuento"] == 0.20
    assert resultado["total"] == 800


def test_en_el_tope_exacto_no_se_recorta():
    resultado = calcular_total(1000, 10, "SALUD10")  # 10 % + 10 % = 20 %
    assert resultado["porcentaje_descuento"] == pytest.approx(0.20)


@pytest.mark.parametrize("subtotal,unidades", [(-1, 1), (100, -1)])
def test_valores_negativos(subtotal, unidades):
    with pytest.raises(ValueError):
        calcular_total(subtotal, unidades)


def test_subtotal_cero():
    assert calcular_total(0, 0)["total"] == 0
