"""Pruebas mínimas de la base. En el Ejercicio 4 el alumno las amplía con /tests."""


def test_listar_productos(client):
    respuesta = client.get("/products")
    assert respuesta.status_code == 200
    assert len(respuesta.get_json()) == 6


def test_producto_inexistente(client):
    assert client.get("/products/no-existe").status_code == 404
