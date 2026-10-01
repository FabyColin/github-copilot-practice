/**
 * Farmacia Demo: API REST en Express (proyecto base del curso).
 * Los datos son ficticios y viven en memoria: se reinician al arrancar la aplicación.
 */
const { randomUUID } = require('node:crypto');
const express = require('express');

const CATEGORIAS = [
  'Analgésicos y antiinflamatorios',
  'Antibióticos',
  'Alergias y respiratorio',
  'Aparato digestivo',
  'Vitaminas y suplementos',
  'Cuidado personal e higiene',
  'Material de curación',
  'Bebé y maternidad',
  'Dispositivos médicos',
];

function productosIniciales() {
  // [id, nombre, descripción, precio, categoría, stock, requiereReceta]
  const semilla = [
    ['p-001', 'Paracetamol 500 mg', 'Caja con 20 tabletas', 45.0, 'Analgésicos y antiinflamatorios', 120, false],
    ['p-002', 'Amoxicilina 500 mg', 'Caja con 12 cápsulas', 129.5, 'Antibióticos', 30, true],
    ['p-003', 'Vitamina C 1 g', 'Tubo con 10 tabletas efervescentes', 89.0, 'Vitaminas y suplementos', 60, false],
    ['p-004', 'Gel antibacterial 500 ml', 'Frasco con dosificador', 62.0, 'Cuidado personal e higiene', 80, false],
    ['p-005', 'Termómetro digital', 'Lectura en 10 segundos', 149.0, 'Dispositivos médicos', 25, false],
    ['p-006', 'Loratadina 10 mg', 'Caja con 10 tabletas', 58.0, 'Alergias y respiratorio', 40, false],
  ];
  return new Map(
    semilla.map(([id, nombre, descripcion, precio, categoria, stock, requiere_receta]) => [
      id,
      { id, nombre, descripcion, precio, categoria, stock, requiere_receta },
    ]),
  );
}

function createApp() {
  const app = express();
  app.use(express.json());
  const productos = productosIniciales();

  app.get('/products', (req, res) => {
    const { categoria } = req.query;
    let resultado = [...productos.values()];
    if (categoria) {
      resultado = resultado.filter((p) => p.categoria === categoria);
    }
    res.json(resultado);
  });

  app.get('/products/:id', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).json({ error: 'Producto no encontrado' });
    }
    return res.json(producto);
  });

  app.post('/products', (req, res) => {
    const datos = req.body ?? {};
    if (!('nombre' in datos)) {
      return res.status(400).json({ error: "El campo 'nombre' es obligatorio" });
    }
    const id = randomUUID();
    const producto = {
      id,
      nombre: datos.nombre,
      descripcion: datos.descripcion ?? '',
      precio: datos.precio ?? 0,
      categoria: datos.categoria ?? 'Cuidado personal e higiene',
      stock: datos.stock ?? 0,
      requiere_receta: datos.requiere_receta ?? false,
    };
    productos.set(id, producto);
    return res.status(201).json(producto);
  });

  app.put('/products/:id', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).json({ error: 'Producto no encontrado' });
    }
    const datos = req.body ?? {};
    for (const campo of ['nombre', 'descripcion', 'precio', 'categoria', 'stock', 'requiere_receta']) {
      if (campo in datos) {
        producto[campo] = datos[campo];
      }
    }
    return res.json(producto);
  });

  app.delete('/products/:id', (req, res) => {
    if (!productos.delete(req.params.id)) {
      return res.status(404).json({ error: 'Producto no encontrado' });
    }
    return res.status(204).send();
  });

  // Calcula el total de un pedido: { items: [{ product_id, cantidad }] }
  app.post('/orders', (req, res) => {
    const items = req.body?.items ?? [];
    if (items.length === 0) {
      return res.status(400).json({ error: 'El pedido no tiene items' });
    }
    const detalle = [];
    let total = 0;
    for (const item of items) {
      const producto = productos.get(item.product_id);
      if (!producto) {
        return res.status(404).json({ error: `Producto no encontrado: ${item.product_id}` });
      }
      const cantidad = item.cantidad ?? 1;
      const subtotal = producto.precio * cantidad;
      total += subtotal;
      detalle.push({ product_id: producto.id, cantidad, subtotal });
    }
    return res.status(201).json({ items: detalle, total: Math.round(total * 100) / 100 });
  });

  return app;
}

module.exports = { createApp, CATEGORIAS };
