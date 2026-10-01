"""Tienda de productos: API REST en Flask (proyecto base del curso).

Los datos viven en memoria y se reinician al arrancar la aplicación.
"""
import uuid

from flask import Flask, jsonify, render_template, request

CATEGORIAS = [
    "Electricidad",
    "Jardín y exteriores",
    "Herramientas manuales",
    "Ferretería",
    "Madera y construcción",
    "Pintura y acabados",
    "Plomería",
    "Herramientas eléctricas",
    "Almacenamiento y organización",
]


def _productos_iniciales():
    semilla = [
        ("p-001", "Martillo de acero", "Martillo 16 oz con mango antideslizante", 189.90, "Herramientas manuales", 40),
        ("p-002", "Taladro inalámbrico", "Taladro 20V con dos baterías", 1499.00, "Herramientas eléctricas", 12),
        ("p-003", "Cinta aislante", "Rollo de 18 m, color negro", 29.50, "Electricidad", 200),
        ("p-004", "Pintura vinílica blanca", "Cubeta de 19 litros", 1250.00, "Pintura y acabados", 18),
        ("p-005", "Manguera de jardín", "Manguera reforzada de 25 m", 349.00, "Jardín y exteriores", 25),
        ("p-006", "Llave mezcladora", "Llave monomando cromada", 899.00, "Plomería", 9),
    ]
    return {
        pid: {
            "id": pid,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "categoria": categoria,
            "stock": stock,
        }
        for pid, nombre, descripcion, precio, categoria, stock in semilla
    }


def create_app():
    app = Flask(__name__)
    productos = _productos_iniciales()

    @app.get("/catalogo")
    def catalogo():
        return render_template("catalogo.html", categorias=CATEGORIAS)

    @app.get("/products")
    def listar_productos():
        categoria = request.args.get("categoria")
        resultado = list(productos.values())
        if categoria:
            resultado = [p for p in resultado if p["categoria"] == categoria]
        return jsonify(resultado)

    @app.get("/products/<product_id>")
    def obtener_producto(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        return jsonify(producto)

    @app.post("/products")
    def crear_producto():
        datos = request.get_json(silent=True) or {}
        if "nombre" not in datos:
            return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
        product_id = str(uuid.uuid4())
        productos[product_id] = {
            "id": product_id,
            "nombre": datos["nombre"],
            "descripcion": datos.get("descripcion", ""),
            "precio": datos.get("precio", 0),
            "categoria": datos.get("categoria", "Ferretería"),
            "stock": datos.get("stock", 0),
        }
        return jsonify(productos[product_id]), 201

    @app.put("/products/<product_id>")
    def actualizar_producto(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        datos = request.get_json(silent=True) or {}
        for campo in ("nombre", "descripcion", "precio", "categoria", "stock"):
            if campo in datos:
                producto[campo] = datos[campo]
        return jsonify(producto)

    @app.delete("/products/<product_id>")
    def eliminar_producto(product_id):
        if product_id not in productos:
            return jsonify({"error": "Producto no encontrado"}), 404
        del productos[product_id]
        return "", 204

    @app.post("/orders")
    def crear_pedido():
        """Calcula el total de un pedido: {"items": [{"product_id": ..., "cantidad": ...}]}."""
        datos = request.get_json(silent=True) or {}
        items = datos.get("items", [])
        if not items:
            return jsonify({"error": "El pedido no tiene items"}), 400
        detalle = []
        total = 0
        for item in items:
            producto = productos.get(item.get("product_id"))
            if producto is None:
                return jsonify({"error": f"Producto no encontrado: {item.get('product_id')}"}), 404
            cantidad = item.get("cantidad", 1)
            subtotal = producto["precio"] * cantidad
            total += subtotal
            detalle.append({"product_id": producto["id"], "cantidad": cantidad, "subtotal": subtotal})
        return jsonify({"items": detalle, "total": round(total, 2)}), 201

    return app


if __name__ == "__main__":
    create_app().run(port=5000)
