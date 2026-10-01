"""Ajuste de stock y ficha de producto (versión corregida tras la revisión)."""
from flask import jsonify, request
from markupsafe import escape


def registrar_rutas(app, productos):
    @app.post("/products/<product_id>/stock")
    def ajustar_stock(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404

        datos = request.get_json(silent=True) or {}
        delta = datos.get("delta")
        # Defecto 1: se validaba nada; ahora solo se acepta un entero distinto de cero
        if not isinstance(delta, int) or isinstance(delta, bool) or delta == 0:
            return jsonify({"error": "'delta' debe ser un entero distinto de cero"}), 400
        if producto["stock"] + delta < 0:
            return jsonify({"error": "El stock no puede quedar negativo"}), 409

        producto["stock"] += delta
        return jsonify(producto)

    @app.get("/products/<product_id>/ficha")
    def ficha_producto(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return "Producto no encontrado", 404
        # Defecto 2: los datos del producto se escapan antes de insertarlos en el HTML
        return (
            f"<h1>{escape(producto['nombre'])}</h1>"
            f"<p>{escape(producto['descripcion'])}</p>"
            f"<p>Stock disponible: {escape(producto['stock'])}</p>"
        )
