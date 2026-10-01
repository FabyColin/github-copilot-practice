import pytest


def _pedido(client, items, cupon=None, receta=None):
    cuerpo = {"items": items}
    if cupon:
        cuerpo["cupon"] = cupon
    if receta is not None:
        cuerpo["receta"] = receta
    return client.post("/orders", json=cuerpo)


def test_pedido_sin_descuento(client):
    r = _pedido(client, [{"product_id": "p-001", "cantidad": 2}])
    assert r.status_code == 201
    assert r.get_json()["total"] == 90.0


def test_pedido_con_descuento_por_volumen(client):
    r = _pedido(client, [{"product_id": "p-001", "cantidad": 5}])  # 225.00 con 5 %
    assert r.get_json()["total"] == 213.75


def test_pedido_con_cupon(client):
    r = _pedido(client, [{"product_id": "p-005", "cantidad": 1}], "SALUD10")
    assert r.get_json()["total"] == 134.1


def test_pedido_con_tope_de_descuento(client):
    r = _pedido(client, [{"product_id": "p-001", "cantidad": 10}], "ADULTOMAYOR15")  # 450.00, tope 20 %
    assert r.get_json()["total"] == 360.0


def test_cupon_vencido_devuelve_400(client):
    r = _pedido(client, [{"product_id": "p-003", "cantidad": 1}], "VENCIDO20")
    assert r.status_code == 400


def test_medicamento_con_receta_sin_folio_devuelve_400(client):
    r = _pedido(client, [{"product_id": "p-002", "cantidad": 1}])
    assert r.status_code == 400
    assert "receta" in r.get_json()["error"].lower()


@pytest.mark.parametrize("receta", ["", "   ", 12345, None])
def test_folio_de_receta_invalido_devuelve_400(client, receta):
    r = _pedido(client, [{"product_id": "p-002", "cantidad": 1}], receta=receta)
    assert r.status_code == 400


def test_medicamento_con_receta_con_folio_se_acepta(client):
    r = _pedido(client, [{"product_id": "p-002", "cantidad": 1}], receta="RX-2026-0001")
    assert r.status_code == 201
    assert r.get_json()["total"] == 129.5


def test_producto_sin_receta_no_exige_folio(client):
    assert _pedido(client, [{"product_id": "p-001", "cantidad": 1}]).status_code == 201


def test_cantidad_negativa_devuelve_400(client):
    assert _pedido(client, [{"product_id": "p-001", "cantidad": -3}]).status_code == 400


def test_cantidad_no_entera_devuelve_400(client):
    assert _pedido(client, [{"product_id": "p-001", "cantidad": "2"}]).status_code == 400


def test_producto_inexistente_devuelve_404(client):
    assert _pedido(client, [{"product_id": "zzz", "cantidad": 1}]).status_code == 404


def test_pedido_vacio_devuelve_400(client):
    assert _pedido(client, []).status_code == 400
