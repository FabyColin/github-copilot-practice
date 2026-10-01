/**
 * Reglas de descuento por volumen y cupones (solución de referencia del Ejercicio 4).
 * Datos y reglas ficticios, con fines didácticos.
 */

const DESCUENTO_MAXIMO = 0.2;

// Descuento por piezas totales del pedido: [mínimo de piezas, porcentaje]
const ESCALAS_VOLUMEN = [
  [10, 0.1],
  [5, 0.05],
];

const CUPONES = {
  SALUD10: { porcentaje: 0.1, vence: new Date('2099-12-31') },
  ADULTOMAYOR15: { porcentaje: 0.15, vence: new Date('2099-12-31') },
  VENCIDO20: { porcentaje: 0.2, vence: new Date('2020-01-01') },
};

class CuponInvalido extends Error {
  constructor(mensaje) {
    super(mensaje);
    this.name = 'CuponInvalido';
  }
}

const redondear = (valor) => Math.round(valor * 100) / 100;

function descuentoPorVolumen(unidades) {
  const escala = ESCALAS_VOLUMEN.find(([minimo]) => unidades >= minimo);
  return escala ? escala[1] : 0;
}

function descuentoPorCupon(codigo, hoy = new Date()) {
  if (!codigo) {
    return 0;
  }
  const cupon = CUPONES[String(codigo).toUpperCase()];
  if (!cupon) {
    throw new CuponInvalido(`El cupón ${codigo} no existe`);
  }
  if (cupon.vence < hoy) {
    throw new CuponInvalido(`El cupón ${codigo} está vencido`);
  }
  return cupon.porcentaje;
}

/** Combina descuento por volumen y por cupón, con un tope del 20 %. */
function calcularTotal(subtotal, unidades, codigo = null, hoy = new Date()) {
  if (subtotal < 0 || unidades < 0) {
    throw new RangeError('El subtotal y las unidades no pueden ser negativos');
  }
  const porcentaje = Math.min(
    descuentoPorVolumen(unidades) + descuentoPorCupon(codigo, hoy),
    DESCUENTO_MAXIMO,
  );
  const descuento = redondear(subtotal * porcentaje);
  return {
    subtotal: redondear(subtotal),
    descuento,
    porcentaje_descuento: porcentaje,
    total: redondear(subtotal - descuento),
  };
}

module.exports = { CuponInvalido, descuentoPorVolumen, descuentoPorCupon, calcularTotal, DESCUENTO_MAXIMO };
