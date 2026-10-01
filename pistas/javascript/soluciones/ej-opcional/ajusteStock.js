/** Ajuste de stock y ficha de producto (versión corregida tras la revisión). */
const express = require('express');

const ESCAPES = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
const escapar = (valor) => String(valor).replace(/[&<>"']/g, (c) => ESCAPES[c]);

function crearRutasDeStock(productos) {
  const router = express.Router();

  router.post('/products/:id/stock', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).json({ error: 'Producto no encontrado' });
    }

    const delta = req.body?.delta;
    // Defecto 1: antes no se validaba nada ("5" se concatenaba como texto); ahora solo un entero distinto de cero
    if (!Number.isInteger(delta) || delta === 0) {
      return res.status(400).json({ error: "'delta' debe ser un entero distinto de cero" });
    }
    if (producto.stock + delta < 0) {
      return res.status(409).json({ error: 'El stock no puede quedar negativo' });
    }

    producto.stock += delta;
    return res.json(producto);
  });

  router.get('/products/:id/ficha', (req, res) => {
    const producto = productos.get(req.params.id);
    if (!producto) {
      return res.status(404).send('Producto no encontrado');
    }
    // Defecto 2: los datos del producto se escapan antes de insertarlos en el HTML
    return res.send(
      `<h1>${escapar(producto.nombre)}</h1><p>${escapar(producto.descripcion)}</p><p>Stock disponible: ${escapar(producto.stock)}</p>`,
    );
  });

  return router;
}

module.exports = { crearRutasDeStock };
