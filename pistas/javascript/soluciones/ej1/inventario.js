/** Solución de referencia del Ejercicio 1. */
class Inventario {
  #productos = new Map();

  agregar(producto) {
    if (this.#productos.has(producto.sku)) {
      throw new Error(`El SKU ${producto.sku} ya existe`);
    }
    this.#productos.set(producto.sku, { ...producto });
  }

  eliminar(sku) {
    if (!this.#productos.delete(sku)) {
      throw new Error(`El SKU ${sku} no existe`);
    }
  }

  buscar(texto) {
    const t = texto.toLowerCase();
    return [...this.#productos.values()].filter((p) => p.nombre.toLowerCase().includes(t));
  }

  stockBajo(umbral) {
    return [...this.#productos.values()].filter((p) => p.stock < umbral);
  }

  reporte() {
    const productos = [...this.#productos.values()];
    return {
      productos: productos.length,
      unidades: productos.reduce((suma, p) => suma + p.stock, 0),
      valorTotal: productos.reduce((suma, p) => suma + p.stock * p.precio, 0),
    };
  }
}

module.exports = { Inventario };
