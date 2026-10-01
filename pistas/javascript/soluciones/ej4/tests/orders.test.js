const request = require('supertest');
const { createApp } = require('../app');

const pedido = (items, { cupon, receta } = {}) =>
  request(createApp())
    .post('/orders')
    .send({ items, ...(cupon && { cupon }), ...(receta !== undefined && { receta }) });

test('pedido sin descuento', async () => {
  const r = await pedido([{ product_id: 'p-001', cantidad: 2 }]);
  expect(r.status).toBe(201);
  expect(r.body.total).toBe(90);
});

test('pedido con descuento por volumen', async () => {
  const r = await pedido([{ product_id: 'p-001', cantidad: 5 }]); // 225.00 con 5 %
  expect(r.body.total).toBe(213.75);
});

test('pedido con cupón', async () => {
  const r = await pedido([{ product_id: 'p-005', cantidad: 1 }], { cupon: 'SALUD10' });
  expect(r.body.total).toBe(134.1);
});

test('pedido con tope de descuento', async () => {
  const r = await pedido([{ product_id: 'p-001', cantidad: 10 }], { cupon: 'ADULTOMAYOR15' }); // 450.00, tope 20 %
  expect(r.body.total).toBe(360);
});

test('cupón vencido devuelve 400', async () => {
  const r = await pedido([{ product_id: 'p-003', cantidad: 1 }], { cupon: 'VENCIDO20' });
  expect(r.status).toBe(400);
});

test('medicamento con receta sin folio devuelve 400', async () => {
  const r = await pedido([{ product_id: 'p-002', cantidad: 1 }]);
  expect(r.status).toBe(400);
  expect(r.body.error.toLowerCase()).toContain('receta');
});

test.each([[''], ['   '], [12345], [null]])('folio de receta inválido (%p) devuelve 400', async (receta) => {
  const r = await pedido([{ product_id: 'p-002', cantidad: 1 }], { receta });
  expect(r.status).toBe(400);
});

test('medicamento con receta y folio se acepta', async () => {
  const r = await pedido([{ product_id: 'p-002', cantidad: 1 }], { receta: 'RX-2026-0001' });
  expect(r.status).toBe(201);
  expect(r.body.total).toBe(129.5);
});

test('producto sin receta no exige folio', async () => {
  expect((await pedido([{ product_id: 'p-001', cantidad: 1 }])).status).toBe(201);
});

test('cantidad negativa devuelve 400', async () => {
  expect((await pedido([{ product_id: 'p-001', cantidad: -3 }])).status).toBe(400);
});

test('cantidad no entera devuelve 400', async () => {
  expect((await pedido([{ product_id: 'p-001', cantidad: '2' }])).status).toBe(400);
});

test('producto inexistente devuelve 404', async () => {
  expect((await pedido([{ product_id: 'zzz', cantidad: 1 }])).status).toBe(404);
});

test('pedido vacío devuelve 400', async () => {
  expect((await pedido([])).status).toBe(400);
});
