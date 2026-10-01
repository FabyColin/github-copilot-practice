/** Pruebas de validación del cierre del Ejercicio 1 (vienen incluidas; no las modifiques). */
const { Inventario } = require('./inventario');

let inv;

beforeEach(() => {
  inv = new Inventario();
  inv.agregar({ sku: 'A1', nombre: 'Martillo', stock: 40, precio: 190.0 });
  inv.agregar({ sku: 'B2', nombre: 'Taladro', stock: 3, precio: 1500.0 });
  inv.agregar({ sku: 'C3', nombre: 'Cinta aislante', stock: 0, precio: 30.0 });
});

test('agregar un SKU duplicado lanza error', () => {
  expect(() => inv.agregar({ sku: 'A1', nombre: 'Otro', stock: 1, precio: 1.0 })).toThrow();
});

test('eliminar quita el producto', () => {
  inv.eliminar('A1');
  expect(inv.buscar('martillo')).toEqual([]);
});

test('eliminar un SKU inexistente lanza error', () => {
  expect(() => inv.eliminar('ZZZ')).toThrow();
});

test('buscar ignora mayúsculas y minúsculas', () => {
  expect(inv.buscar('CINTA').map((p) => p.sku)).toEqual(['C3']);
});

test('stockBajo devuelve los productos bajo el umbral', () => {
  expect(inv.stockBajo(5).map((p) => p.sku).sort()).toEqual(['B2', 'C3']);
});

test('reporte incluye totales y valor del inventario', () => {
  const reporte = inv.reporte();
  expect(reporte.productos).toBe(3);
  expect(reporte.unidades).toBe(43);
  expect(reporte.valorTotal).toBeCloseTo(40 * 190.0 + 3 * 1500.0);
});
