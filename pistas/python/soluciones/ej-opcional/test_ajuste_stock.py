"""Pruebas que sí verifican algo (corrigen el Defecto 3)."""
import pytest
from flask import Flask

from ajuste_stock import registrar_rutas

XSS = "<script>alert(1)</script>"


@pytest.fixture
def entorno():
    app = Flask(__name__)
    productos = {
        "p-001": {"id": "p-001", "nombre": "Paracetamol 500 mg", "descripcion": "Caja con 20 tabletas", "stock": 40},
        "p-xss": {"id": "p-xss", "nombre": XSS, "descripcion": "<b onclick=x>", "stock": 1},
    }
    registrar_rutas(app, productos)
    return app.test_client(), productos


def test_suma_stock(entorno):
    client, productos = entorno
    respuesta = client.post("/products/p-001/stock", json={"delta": 5})
    assert respuesta.status_code == 200
    assert respuesta.get_json()["stock"] == 45
    assert productos["p-001"]["stock"] == 45


def test_resta_stock(entorno):
    client, _ = entorno
    assert client.post("/products/p-001/stock", json={"delta": -40}).get_json()["stock"] == 0


@pytest.mark.parametrize("delta", ["abc", "5", 1.5, None, True, 0, [], {}])
def test_delta_invalido_devuelve_400_y_no_modifica(entorno, delta):
    client, productos = entorno
    respuesta = client.post("/products/p-001/stock", json={"delta": delta})
    assert respuesta.status_code == 400
    assert productos["p-001"]["stock"] == 40


def test_sin_delta_devuelve_400(entorno):
    client, _ = entorno
    assert client.post("/products/p-001/stock", json={}).status_code == 400
    assert client.post("/products/p-001/stock").status_code == 400


def test_stock_no_puede_quedar_negativo(entorno):
    client, productos = entorno
    respuesta = client.post("/products/p-001/stock", json={"delta": -41})
    assert respuesta.status_code == 409
    assert productos["p-001"]["stock"] == 40


def test_producto_inexistente(entorno):
    client, _ = entorno
    assert client.post("/products/zzz/stock", json={"delta": 1}).status_code == 404
    assert client.get("/products/zzz/ficha").status_code == 404


def test_ficha_muestra_los_datos(entorno):
    client, _ = entorno
    html = client.get("/products/p-001/ficha").get_data(as_text=True)
    assert "<h1>Paracetamol 500 mg</h1>" in html
    assert "Stock disponible: 40" in html


def test_ficha_escapa_html_malicioso(entorno):
    client, _ = entorno
    html = client.get("/products/p-xss/ficha").get_data(as_text=True)
    assert "<script>" not in html
    assert "&lt;script&gt;" in html
    assert "<b onclick" not in html
