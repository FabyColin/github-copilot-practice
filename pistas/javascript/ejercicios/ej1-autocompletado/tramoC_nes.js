/**
 * Tramo C: Next Edit Suggestions (NES).
 *
 * Instrucciones: activa NES (`github.copilot.nextEditSuggestions.enabled`).
 * Renombra la propiedad "nombre" a "nombreComercial" SOLO en la función `crearProducto`
 * y observa cómo Copilot sugiere el resto de las ediciones relacionadas.
 * Navega entre ellas con Tab y acéptalas una por una, revisando cada una.
 */

function crearProducto(nombre, precio) {
  return { nombre, precio };
}

function mostrarProducto(producto) {
  return `${producto.nombre} - $${producto.precio.toFixed(2)}`;
}

function buscarPorNombre(productos, texto) {
  return productos.filter((p) => p.nombre.toLowerCase().includes(texto.toLowerCase()));
}

function exportarNombres(productos) {
  return productos.map(({ nombre }) => nombre);
}

function ordenarAlfabeticamente(productos) {
  return [...productos].sort((a, b) => a.nombre.localeCompare(b.nombre));
}

module.exports = {
  crearProducto,
  mostrarProducto,
  buscarPorNombre,
  exportarNombres,
  ordenarAlfabeticamente,
};
