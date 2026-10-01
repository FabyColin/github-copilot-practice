/** Pruebas que sí verifican algo (corrigen el Defecto 3). */
const express = require('express');
const request = require('supertest');
const { crearRutasDeStock } = require('./ajusteStock');

const XSS = '<script>alert(1)</script>';

function crearEntorno() {
  const productos = new Map([
    ['p-001', { id: 'p-001', nombre: 'Martillo de acero', descripcion: 'Martillo 16 oz', stock: 40 }],
    ['p-xss', { id: 'p-xss', nombre: XSS, descripcion: '<b onclick=x>', stock: 1 }],
  ]);
  const app = express();
  app.use(express.json());
  app.use(crearRutasDeStock(productos));
  return { app, productos };
}

describe('POST /products/:id/stock', () => {
  test('suma stock', async () => {
    const { app, productos } = crearEntorno();
    const r = await request(app).post('/products/p-001/stock').send({ delta: 5 });
    expect(r.status).toBe(200);
    expect(r.body.stock).toBe(45);
    expect(productos.get('p-001').stock).toBe(45);
  });

  test('resta stock', async () => {
    const { app } = crearEntorno();
    const r = await request(app).post('/products/p-001/stock').send({ delta: -40 });
    expect(r.body.stock).toBe(0);
  });

  test.each([['abc'], ['5'], [1.5], [null], [true], [0], [[]], [{}]])(
    'delta inválido (%p) devuelve 400 y no modifica el stock',
    async (delta) => {
      const { app, productos } = crearEntorno();
      const r = await request(app).post('/products/p-001/stock').send({ delta });
      expect(r.status).toBe(400);
      expect(productos.get('p-001').stock).toBe(40);
    },
  );

  test('sin delta ni cuerpo devuelve 400', async () => {
    const { app } = crearEntorno();
    expect((await request(app).post('/products/p-001/stock').send({})).status).toBe(400);
    expect((await request(app).post('/products/p-001/stock')).status).toBe(400);
  });

  test('el stock no puede quedar negativo', async () => {
    const { app, productos } = crearEntorno();
    const r = await request(app).post('/products/p-001/stock').send({ delta: -41 });
    expect(r.status).toBe(409);
    expect(productos.get('p-001').stock).toBe(40);
  });

  test('producto inexistente devuelve 404', async () => {
    const { app } = crearEntorno();
    expect((await request(app).post('/products/zzz/stock').send({ delta: 1 })).status).toBe(404);
    expect((await request(app).get('/products/zzz/ficha')).status).toBe(404);
  });
});

describe('GET /products/:id/ficha', () => {
  test('muestra los datos del producto', async () => {
    const { app } = crearEntorno();
    const r = await request(app).get('/products/p-001/ficha');
    expect(r.status).toBe(200);
    expect(r.text).toContain('<h1>Martillo de acero</h1>');
    expect(r.text).toContain('Stock disponible: 40');
  });

  test('escapa el HTML malicioso', async () => {
    const { app } = crearEntorno();
    const r = await request(app).get('/products/p-xss/ficha');
    expect(r.text).not.toContain('<script>');
    expect(r.text).toContain('&lt;script&gt;');
    expect(r.text).not.toContain('<b onclick');
  });
});
