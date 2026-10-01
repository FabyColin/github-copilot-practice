const express = require('express');
const request = require('supertest');
const { crearRutasDeStock } = require('./ajusteStock');

function crearApp() {
  const productos = new Map([
    ['p-001', { id: 'p-001', nombre: 'Paracetamol 500 mg', descripcion: 'Caja con 20 tabletas', stock: 40 }],
  ]);
  const app = express();
  app.use(express.json());
  app.use(crearRutasDeStock(productos));
  return app;
}

test('ajusta el stock', () => {
  request(crearApp())
    .post('/products/p-001/stock')
    .send({ delta: 5 })
    .then((respuesta) => {
      expect(respuesta.status).toBe(200);
    });
});

test('muestra la ficha del producto', async () => {
  const respuesta = await request(crearApp()).get('/products/p-001/ficha');
  expect(respuesta).toBeDefined();
});

test('producto inexistente devuelve 404', async () => {
  const respuesta = await request(crearApp()).post('/products/zzz/stock').send({ delta: 1 });
  expect(respuesta.status).toBe(404);
});
