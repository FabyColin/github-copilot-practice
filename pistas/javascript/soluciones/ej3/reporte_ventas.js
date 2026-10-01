/**
 * Reporte de ventas: top de vendedores, ticket promedio por región y total.
 * Solución de referencia del Ejercicio 3 (versión legible y corregida).
 */
const fs = require('fs');

const REGIONES = ['Norte', 'Sur', 'Centro', 'Occidente'];

function leerVentas(ruta) {
  const [, ...lineas] = fs.readFileSync(ruta, 'utf8').split('\n');
  return lineas
    .filter((linea) => linea.trim() !== '')
    .map((linea) => {
      const [fecha, vendedor, region, producto, cantidad, monto] = linea.split(',');
      return { fecha, vendedor, region, producto, cantidad: Number(cantidad), monto: Number(monto) };
    });
}

function totalesPorVendedor(ventas) {
  const totales = {};
  for (const venta of ventas) { // Bug 1 corregido: se procesan TODAS las filas
    totales[venta.vendedor] ??= { monto: 0, ventas: 0 };
    totales[venta.vendedor].monto += venta.monto;
    totales[venta.vendedor].ventas += 1;
  }
  return totales;
}

function ticketPromedioPorRegion(ventas) {
  const acumulado = Object.fromEntries(REGIONES.map((region) => [region, { monto: 0, ventas: 0 }]));
  for (const venta of ventas) {
    acumulado[venta.region].monto += venta.monto;
    acumulado[venta.region].ventas += 1;
  }
  // Bug 3 corregido: sin ventas no hay promedio (antes 0/0 daba NaN en silencio)
  return Object.fromEntries(
    Object.entries(acumulado).map(([region, { monto, ventas: n }]) => [region, n > 0 ? monto / n : null]),
  );
}

function imprimirReporte(ventas) {
  const totales = totalesPorVendedor(ventas);
  // Bug 2 corregido: se ordena por número, no por texto ("9475" > "17841" como cadenas)
  const ranking = Object.entries(totales).sort(([, a], [, b]) => b.monto - a.monto);

  console.log('TOP VENDEDORES');
  ranking.slice(0, 3).forEach(([vendedor, datos], i) => {
    console.log(i + 1, vendedor, datos.monto, datos.ventas);
  });

  console.log('TICKET PROMEDIO POR REGION');
  for (const [region, promedio] of Object.entries(ticketPromedioPorRegion(ventas))) {
    console.log(region, promedio === null ? 'sin ventas' : Math.round(promedio * 100) / 100);
  }

  console.log('TOTAL', Object.values(totales).reduce((suma, datos) => suma + datos.monto, 0));
}

imprimirReporte(leerVentas(process.argv[2]));
