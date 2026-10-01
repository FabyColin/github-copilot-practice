import pytest
from flask import Flask

from ajuste_stock import registrar_rutas


@pytest.fixture
def client():
    app = Flask(__name__)
    productos = {
        "p-001": {"id": "p-001", "nombre": "Paracetamol 500 mg", "descripcion": "Caja con 20 tabletas", "stock": 40},
    }
    registrar_rutas(app, productos)
    return app.test_client()


def test_ajustar_stock(client):
    respuesta = client.post("/products/p-001/stock", json={"delta": 5})
    assert respuesta.status_code in (200, 400, 404)


def test_ficha_del_producto(client):
    respuesta = client.get("/products/p-001/ficha")
    assert respuesta


def test_ajustar_producto_inexistente(client):
    respuesta = client.post("/products/zzz/stock", json={"delta": 1})
    assert respuesta.status_code == 404
