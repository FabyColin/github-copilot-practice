"""Utilidades de la tienda (solución de referencia del Ejercicio 2)."""
import re


def valor_inventario_por_categoria(productos: list[dict]) -> dict[str, float]:
    """Devuelve el valor del inventario (precio x stock) agrupado por categoría."""
    valores: dict[str, float] = {}
    for producto in productos:
        categoria = producto["categoria"]
        valores[categoria] = valores.get(categoria, 0) + producto["precio"] * producto["stock"]
    return valores


def crear_slug(texto: str) -> str:
    """Convierte un texto en un slug para URL: minúsculas, sin símbolos, con guiones."""
    texto = texto.strip().lower()
    texto = re.sub(r"[^a-z0-9\s-]", "", texto)
    return re.sub(r"\s+", "-", texto)


def promedio_movil(valores: list[float], ventana: int) -> list[float]:
    """Promedio móvil de ventana fija; solo se calculan ventanas completas."""
    if ventana <= 0:
        raise ValueError("La ventana debe ser mayor que cero")
    return [
        sum(valores[i : i + ventana]) / ventana
        for i in range(len(valores) - ventana + 1)
    ]


def precio_con_descuento(precio: float, porcentaje: float) -> float:
    """Aplica un descuento porcentual (0 a 100) a un precio."""
    return precio - precio * porcentaje / 100
