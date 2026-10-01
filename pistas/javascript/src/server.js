const { createApp } = require('./app');

const PUERTO = process.env.PORT || 5000;

createApp().listen(PUERTO, () => {
  console.log(`API de la tienda en http://localhost:${PUERTO}`);
});
