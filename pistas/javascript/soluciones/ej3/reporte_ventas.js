/**
 * Reporte de ventas: top de vendedores, ticket promedio por sucursal y total.
 * Solución de referencia del Ejercicio 3 (versión legible y corregida).
 */
const fs = require('fs');

const SUCURSALES = ['Norte', 'Sur', 'Centro', 'Occidente'];

function leerVentas(ruta) {
  const [, ...lineas] = fs.readFileSync(ruta, 'utf8').split('\n');
  return lineas
    .filter((linea) => linea.trim() !== '')
    .map((linea) => {
      const [fecha, vendedor, sucursal, producto, cantidad, monto] = linea.split(',');
      return { fecha, vendedor, sucursal, producto, cantidad: Number(cantidad), monto: Number(monto) };
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

function ticketPromedioPorSucursal(ventas) {
  const acumulado = Object.fromEntries(SUCURSALES.map((sucursal) => [sucursal, { monto: 0, ventas: 0 }]));
  for (const venta of ventas) {
    acumulado[venta.sucursal].monto += venta.monto;
    acumulado[venta.sucursal].ventas += 1;
  }
  // Bug 3 corregido: sin ventas no hay promedio (antes 0/0 daba NaN en silencio)
  return Object.fromEntries(
    Object.entries(acumulado).map(([sucursal, { monto, ventas: n }]) => [sucursal, n > 0 ? monto / n : null]),
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

  console.log('TICKET PROMEDIO POR SUCURSAL');
  for (const [sucursal, promedio] of Object.entries(ticketPromedioPorSucursal(ventas))) {
    console.log(sucursal, promedio === null ? 'sin ventas' : Math.round(promedio * 100) / 100);
  }

  console.log('TOTAL', Object.values(totales).reduce((suma, datos) => suma + datos.monto, 0));
}

imprimirReporte(leerVentas(process.argv[2]));
