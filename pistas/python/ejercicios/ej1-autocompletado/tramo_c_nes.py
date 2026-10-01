"""Tramo C: Next Edit Suggestions (NES).

Instrucciones: activa NES (`github.copilot.nextEditSuggestions.enabled`).
Renombra el campo "nombre" a "titulo" SOLO en la función `crear_producto`
y observa cómo Copilot sugiere el resto de las ediciones relacionadas.
Navega entre ellas con Tab y acéptalas una por una, revisando cada una.
"""


def crear_producto(nombre, precio):
    return {"nombre": nombre, "precio": precio}


def mostrar_producto(producto):
    return f"{producto['nombre']} - ${producto['precio']:.2f}"


def buscar_por_nombre(productos, texto):
    return [p for p in productos if texto.lower() in p["nombre"].lower()]


def exportar_nombres(productos):
    return [p["nombre"] for p in productos]


def ordenar_alfabeticamente(productos):
    return sorted(productos, key=lambda p: p["nombre"])
