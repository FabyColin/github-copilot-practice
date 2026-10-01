def _pedido(client, items, cupon=None):
    cuerpo = {"items": items}
    if cupon:
        cuerpo["cupon"] = cupon
    return client.post("/orders", json=cuerpo)


def test_pedido_sin_descuento(client):
    r = _pedido(client, [{"product_id": "p-001", "cantidad": 2}])
    assert r.status_code == 201
    assert r.get_json()["total"] == 379.8


def test_pedido_con_descuento_por_volumen(client):
    r = _pedido(client, [{"product_id": "p-003", "cantidad": 10}])  # 295.00 x 5 %
    assert r.get_json()["total"] == 280.25


def test_pedido_con_cupon(client):
    r = _pedido(client, [{"product_id": "p-002", "cantidad": 1}], "BIENVENIDA10")
    assert r.get_json()["total"] == 1349.10


def test_cupon_vencido_devuelve_400(client):
    r = _pedido(client, [{"product_id": "p-002", "cantidad": 1}], "VENCIDO20")
    assert r.status_code == 400


def test_cantidad_negativa_devuelve_400(client):
    assert _pedido(client, [{"product_id": "p-001", "cantidad": -3}]).status_code == 400


def test_cantidad_no_entera_devuelve_400(client):
    assert _pedido(client, [{"product_id": "p-001", "cantidad": "2"}]).status_code == 400


def test_producto_inexistente_devuelve_404(client):
    assert _pedido(client, [{"product_id": "zzz", "cantidad": 1}]).status_code == 404


def test_pedido_vacio_devuelve_400(client):
    assert _pedido(client, []).status_code == 400
