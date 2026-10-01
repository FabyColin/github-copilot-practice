/** Pruebas de validación del cierre del Ejercicio 1 (vienen incluidas; no las modifiques). */
const { Inventario } = require('./inventario');

const HOY = new Date('2026-10-01');

let inv;

beforeEach(() => {
  inv = new Inventario();
  inv.agregar({ sku: 'A1', nombre: 'Paracetamol 500 mg', stock: 120, precio: 45.0, caducidad: new Date('2027-06-30') });
  inv.agregar({ sku: 'B2', nombre: 'Amoxicilina 500 mg', stock: 3, precio: 129.5, caducidad: new Date('2026-11-15') });
  inv.agregar({ sku: 'C3', nombre: 'Vitamina C 1 g', stock: 0, precio: 89.0, caducidad: new Date('2026-10-20') });
  inv.agregar({ sku: 'D4', nombre: 'Jarabe para la tos', stock: 5, precio: 70.0, caducidad: new Date('2026-09-15') });
});

test('agregar un SKU duplicado lanza error', () => {
  expect(() =>
    inv.agregar({ sku: 'A1', nombre: 'Otro', stock: 1, precio: 1.0, caducidad: HOY }),
  ).toThrow();
});

test('eliminar quita el producto', () => {
  inv.eliminar('A1');
  expect(inv.buscar('paracetamol')).toEqual([]);
});

test('eliminar un SKU inexistente lanza error', () => {
  expect(() => inv.eliminar('ZZZ')).toThrow();
});

test('buscar ignora mayúsculas y minúsculas', () => {
  expect(inv.buscar('VITAMINA').map((p) => p.sku)).toEqual(['C3']);
});

test('stockBajo devuelve los productos bajo el umbral', () => {
  expect(inv.stockBajo(5).map((p) => p.sku).sort()).toEqual(['B2', 'C3']);
});

test('proximosACaducar incluye vencidos y ordena por fecha', () => {
  // Límite: 1-oct + 60 días = 30-nov. D4 ya venció; C3 y B2 vencen dentro del plazo; A1 no.
  expect(inv.proximosACaducar(60, HOY).map((p) => p.sku)).toEqual(['D4', 'C3', 'B2']);
});

test('proximosACaducar con un plazo corto', () => {
  expect(inv.proximosACaducar(30, HOY).map((p) => p.sku)).toEqual(['D4', 'C3']);
});

test('reporte incluye totales y valor del inventario', () => {
  const reporte = inv.reporte();
  expect(reporte.productos).toBe(4);
  expect(reporte.unidades).toBe(128);
  expect(reporte.valorTotal).toBeCloseTo(120 * 45.0 + 3 * 129.5 + 5 * 70.0);
});
