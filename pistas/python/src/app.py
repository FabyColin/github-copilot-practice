"""Farmacia Demo: API REST en Flask (proyecto base del curso).

Los datos son ficticios y viven en memoria: se reinician al arrancar la aplicación.
"""
import uuid

from flask import Flask, jsonify, request

CATEGORIAS = [
    "Analgésicos y antiinflamatorios",
    "Antibióticos",
    "Alergias y respiratorio",
    "Aparato digestivo",
    "Vitaminas y suplementos",
    "Cuidado personal e higiene",
    "Material de curación",
    "Bebé y maternidad",
    "Dispositivos médicos",
]


def _productos_iniciales():
    # (id, nombre, descripción, precio, categoría, stock, requiere_receta)
    semilla = [
        ("p-001", "Paracetamol 500 mg", "Caja con 20 tabletas", 45.00, "Analgésicos y antiinflamatorios", 120, False),
        ("p-002", "Amoxicilina 500 mg", "Caja con 12 cápsulas", 129.50, "Antibióticos", 30, True),
        ("p-003", "Vitamina C 1 g", "Tubo con 10 tabletas efervescentes", 89.00, "Vitaminas y suplementos", 60, False),
        ("p-004", "Gel antibacterial 500 ml", "Frasco con dosificador", 62.00, "Cuidado personal e higiene", 80, False),
        ("p-005", "Termómetro digital", "Lectura en 10 segundos", 149.00, "Dispositivos médicos", 25, False),
        ("p-006", "Loratadina 10 mg", "Caja con 10 tabletas", 58.00, "Alergias y respiratorio", 40, False),
    ]
    return {
        pid: {
            "id": pid,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "categoria": categoria,
            "stock": stock,
            "requiere_receta": requiere_receta,
        }
        for pid, nombre, descripcion, precio, categoria, stock, requiere_receta in semilla
    }


def create_app():
    app = Flask(__name__)
    productos = _productos_iniciales()

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
            "categoria": datos.get("categoria", "Cuidado personal e higiene"),
            "stock": datos.get("stock", 0),
            "requiere_receta": datos.get("requiere_receta", False),
        }
        return jsonify(productos[product_id]), 201

    @app.put("/products/<product_id>")
    def actualizar_producto(product_id):
        producto = productos.get(product_id)
        if producto is None:
            return jsonify({"error": "Producto no encontrado"}), 404
        datos = request.get_json(silent=True) or {}
        for campo in ("nombre", "descripcion", "precio", "categoria", "stock", "requiere_receta"):
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
