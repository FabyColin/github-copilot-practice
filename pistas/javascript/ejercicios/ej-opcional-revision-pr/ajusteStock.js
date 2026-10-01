/**
 * Ajuste de stock y ficha de producto.
 *
 * Agrega dos rutas a la API de la tienda:
 *   POST /products/:id/stock   suma o resta unidades al stock de un producto
 *   GET  /products/:id/ficha   muestra una ficha HTML del producto
 */
const express = require('express');

function crearRutasDeStock(productos) {
  const router = express.Router();

  router.post('/products/:id/stock', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).json({ error: 'Producto no encontrado' });
    }
    producto.stock += req.body.delta;
    return res.json(producto);
  });

  router.get('/products/:id/ficha', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).send('Producto no encontrado');
    }
    return res.send(
      `<h1>${producto.nombre}</h1><p>${producto.descripcion}</p><p>Stock disponible: ${producto.stock}</p>`,
    );
  });

  return router;
}

module.exports = { crearRutasDeStock };
