"""Para probar el PR en tu máquina (no forma parte del PR).

    python demo_app.py        # http://localhost:5001

Reproduce lo que ya existe en el proyecto: una tienda con productos en memoria y
POST /products para crear nuevos. Sobre eso se registran las rutas del PR.
"""
import uuid

from flask import Flask, jsonify, request

from ajuste_stock import registrar_rutas


def crear_app():
    app = Flask(__name__)
    productos = {
        "p-001": {"id": "p-001", "nombre": "Paracetamol 500 mg", "descripcion": "Caja con 20 tabletas", "stock": 40},
        "p-002": {"id": "p-002", "nombre": "Loratadina 10 mg", "descripcion": "Caja con 10 tabletas", "stock": 12},
    }

    @app.post("/products")
    def crear_producto():
        datos = request.get_json(silent=True) or {}
        product_id = str(uuid.uuid4())
        productos[product_id] = {
            "id": product_id,
            "nombre": datos.get("nombre", "Sin nombre"),
            "descripcion": datos.get("descripcion", ""),
            "stock": datos.get("stock", 0),
        }
        return jsonify(productos[product_id]), 201

    registrar_rutas(app, productos)
    return app


if __name__ == "__main__":
    crear_app().run(port=5001)
