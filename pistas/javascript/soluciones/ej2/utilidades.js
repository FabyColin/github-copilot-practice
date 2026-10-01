/** Utilidades de la tienda (solución de referencia del Ejercicio 2). */

/**
 * Devuelve el valor del inventario (precio x stock) agrupado por categoría.
 * @param {{categoria: string, precio: number, stock: number}[]} productos
 * @returns {Record<string, number>}
 */
function valorInventarioPorCategoria(productos) {
  const valores = {};
  for (const { categoria, precio, stock } of productos) {
    valores[categoria] = (valores[categoria] ?? 0) + precio * stock;
  }
  return valores;
}

/**
 * Convierte un texto en un slug para URL: minúsculas, sin símbolos, con guiones.
 * @param {string} texto
 * @returns {string}
 */
function crearSlug(texto) {
  return texto
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-');
}

/**
 * Promedio móvil de ventana fija; solo se calculan ventanas completas.
 * @param {number[]} valores
 * @param {number} ventana
 * @returns {number[]}
 */
function promedioMovil(valores, ventana) {
  if (ventana <= 0) {
    throw new RangeError('La ventana debe ser mayor que cero');
  }
  const resultado = [];
  for (let i = 0; i + ventana <= valores.length; i += 1) {
    const suma = valores.slice(i, i + ventana).reduce((a, b) => a + b, 0);
    resultado.push(suma / ventana);
  }
  return resultado;
}

/**
 * Aplica un descuento porcentual (0 a 100) a un precio.
 * @param {number} precio
 * @param {number} porcentaje
 * @returns {number}
 */
function precioConDescuento(precio, porcentaje) {
  return precio - (precio * porcentaje) / 100;
}

module.exports = { valorInventarioPorCategoria, crearSlug, promedioMovil, precioConDescuento };
