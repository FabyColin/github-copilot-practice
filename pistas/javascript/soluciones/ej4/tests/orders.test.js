const request = require('supertest');
const { createApp } = require('../app');

const pedido = (items, cupon) => request(createApp()).post('/orders').send({ items, ...(cupon && { cupon }) });

test('pedido sin descuento', async () => {
  const r = await pedido([{ product_id: 'p-001', cantidad: 2 }]);
  expect(r.status).toBe(201);
  expect(r.body.total).toBe(379.8);
});

test('pedido con descuento por volumen', async () => {
  const r = await pedido([{ product_id: 'p-003', cantidad: 10 }]); // 295.00 con 5 %
  expect(r.body.total).toBe(280.25);
});

test('pedido con cupón', async () => {
  const r = await pedido([{ product_id: 'p-002', cantidad: 1 }], 'BIENVENIDA10');
  expect(r.body.total).toBe(1349.1);
});

test('cupón vencido devuelve 400', async () => {
  const r = await pedido([{ product_id: 'p-002', cantidad: 1 }], 'VENCIDO20');
  expect(r.status).toBe(400);
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
