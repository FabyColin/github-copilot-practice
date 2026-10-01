/**
 * Para probar el PR en tu máquina (no forma parte del PR).
 *
 *   node ejercicios/ej-opcional-revision-pr/demoApp.js     # http://localhost:5001
 *
 * Reproduce lo que ya existe en el proyecto: una tienda con productos en memoria y
 * POST /products para crear nuevos. Sobre eso se monta el router del PR.
 */
const { randomUUID } = require('node:crypto');
const express = require('express');
const { crearRutasDeStock } = require('./ajusteStock');

function crearApp() {
  const productos = new Map([
    ['p-001', { id: 'p-001', nombre: 'Paracetamol 500 mg', descripcion: 'Caja con 20 tabletas', stock: 40 }],
    ['p-002', { id: 'p-002', nombre: 'Loratadina 10 mg', descripcion: 'Caja con 10 tabletas', stock: 12 }],
  ]);
  const app = express();
  app.use(express.json());

  app.post('/products', (req, res) => {
    const id = randomUUID();
    const { nombre = 'Sin nombre', descripcion = '', stock = 0 } = req.body ?? {};
    productos.set(id, { id, nombre, descripcion, stock });
    res.status(201).json(productos.get(id));
  });

  app.use(crearRutasDeStock(productos));
  return app;
}

if (require.main === module) {
  crearApp().listen(5001, () => console.log('Demo del PR en http://localhost:5001'));
}

module.exports = { crearApp };
