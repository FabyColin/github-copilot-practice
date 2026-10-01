/**
 * Tienda de productos: API REST en Express (proyecto base del curso).
 * Los datos viven en memoria y se reinician al arrancar la aplicación.
 */
const { randomUUID } = require('node:crypto');
const express = require('express');

const CATEGORIAS = [
  'Electricidad',
  'Jardín y exteriores',
  'Herramientas manuales',
  'Ferretería',
  'Madera y construcción',
  'Pintura y acabados',
  'Plomería',
  'Herramientas eléctricas',
  'Almacenamiento y organización',
];

function productosIniciales() {
  const semilla = [
    ['p-001', 'Martillo de acero', 'Martillo 16 oz con mango antideslizante', 189.9, 'Herramientas manuales', 40],
    ['p-002', 'Taladro inalámbrico', 'Taladro 20V con dos baterías', 1499.0, 'Herramientas eléctricas', 12],
    ['p-003', 'Cinta aislante', 'Rollo de 18 m, color negro', 29.5, 'Electricidad', 200],
    ['p-004', 'Pintura vinílica blanca', 'Cubeta de 19 litros', 1250.0, 'Pintura y acabados', 18],
    ['p-005', 'Manguera de jardín', 'Manguera reforzada de 25 m', 349.0, 'Jardín y exteriores', 25],
    ['p-006', 'Llave mezcladora', 'Llave monomando cromada', 899.0, 'Plomería', 9],
  ];
  return new Map(
    semilla.map(([id, nombre, descripcion, precio, categoria, stock]) => [
      id,
      { id, nombre, descripcion, precio, categoria, stock },
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
      categoria: datos.categoria ?? 'Ferretería',
      stock: datos.stock ?? 0,
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
    for (const campo of ['nombre', 'descripcion', 'precio', 'categoria', 'stock']) {
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
