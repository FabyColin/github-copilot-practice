"""Ajuste de stock y ficha de producto.

Agrega dos rutas a la API de la tienda:
  POST /products/<id>/stock   suma o resta unidades al stock de un producto
  GET  /products/<id>/ficha   muestra una ficha HTML del producto
"""
from flask import jsonify, request


def registrar_rutas(app, productos):
    @app.post("/products/<product_id>/stock")
    def ajustar_stock(product_id):
        datos = request.get_json()
        producto = productos.get(product_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        producto["stock"] += datos["delta"]
        return jsonify(producto)

    @app.get("/products/<product_id>/ficha")
    def ficha_producto(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return "Producto no encontrado", 404
        return (
            f"<h1>{producto['nombre']}</h1>"
            f"<p>{producto['descripcion']}</p>"
            f"<p>Stock disponible: {producto['stock']}</p>"
        )
