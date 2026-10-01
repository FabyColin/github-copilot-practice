const {
  CuponInvalido,
  calcularTotal,
  descuentoPorCupon,
  descuentoPorVolumen,
} = require('../descuentos');

describe('descuentoPorVolumen', () => {
  test.each([
    [0, 0],
    [4, 0],
    [5, 0.05],
    [9, 0.05],
    [10, 0.1],
    [500, 0.1],
  ])('%i unidades -> %f', (unidades, esperado) => {
    expect(descuentoPorVolumen(unidades)).toBe(esperado);
  });
});

describe('descuentoPorCupon', () => {
  test('cupón válido sin importar mayúsculas', () => {
    expect(descuentoPorCupon('salud10')).toBe(0.1);
  });

  test('sin cupón', () => {
    expect(descuentoPorCupon(null)).toBe(0);
    expect(descuentoPorCupon('')).toBe(0);
  });

  test('cupón inexistente', () => {
    expect(() => descuentoPorCupon('NOEXISTE')).toThrow(CuponInvalido);
  });

  test('cupón vencido', () => {
    expect(() => descuentoPorCupon('VENCIDO20')).toThrow(CuponInvalido);
  });

  test('cupón válido en su último día', () => {
    expect(descuentoPorCupon('VENCIDO20', new Date('2020-01-01'))).toBe(0.2);
  });
});

describe('calcularTotal', () => {
  test('los descuentos se acumulan', () => {
    const resultado = calcularTotal(1000, 5, 'SALUD10'); // 5 % + 10 %
    expect(resultado.porcentaje_descuento).toBeCloseTo(0.15);
    expect(resultado.total).toBe(850);
  });

  test('el descuento tiene un tope del 20 %', () => {
    const resultado = calcularTotal(1000, 10, 'ADULTOMAYOR15'); // 10 % + 15 % = 25 %, se recorta a 20 %
    expect(resultado.porcentaje_descuento).toBe(0.2);
    expect(resultado.total).toBe(800);
  });

  test('en el tope exacto no se recorta', () => {
    expect(calcularTotal(1000, 10, 'SALUD10').porcentaje_descuento).toBeCloseTo(0.2);
  });

  test.each([
    [-1, 1],
    [100, -1],
  ])('valores negativos (%i, %i) lanzan error', (subtotal, unidades) => {
    expect(() => calcularTotal(subtotal, unidades)).toThrow(RangeError);
  });

  test('subtotal cero', () => {
    expect(calcularTotal(0, 0).total).toBe(0);
  });
});
