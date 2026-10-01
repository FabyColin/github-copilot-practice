/** Pruebas mínimas de la base. En el Ejercicio 4 el alumno las amplía con /tests. */
const request = require('supertest');
const { createApp } = require('../app');

describe('API de productos', () => {
  test('lista los productos', async () => {
    const respuesta = await request(createApp()).get('/products');
    expect(respuesta.status).toBe(200);
    expect(respuesta.body).toHaveLength(6);
  });

  test('producto inexistente devuelve 404', async () => {
    const respuesta = await request(createApp()).get('/products/no-existe');
    expect(respuesta.status).toBe(404);
  });
});
