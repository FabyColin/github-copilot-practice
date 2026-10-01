import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Catalogo from './Catalogo';

const PRODUCTOS = [
  { id: 'p-001', nombre: 'Martillo de acero', categoria: 'Herramientas manuales', precio: 189.9 },
  { id: 'p-002', nombre: 'Taladro inalámbrico', categoria: 'Herramientas eléctricas', precio: 1499 },
];

function simularApi(respuesta) {
  global.fetch = jest.fn().mockResolvedValue(respuesta);
}

afterEach(() => {
  jest.resetAllMocks();
});

test('muestra los productos recibidos de la API', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  expect(await screen.findByText('Martillo de acero')).toBeInTheDocument();
  expect(screen.getByText('Taladro inalámbrico')).toBeInTheDocument();
});

test('la búsqueda filtra por nombre', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Martillo de acero');
  await userEvent.type(screen.getByLabelText('Buscar producto'), 'taladro');
  expect(screen.queryByText('Martillo de acero')).not.toBeInTheDocument();
  expect(screen.getByText('Taladro inalámbrico')).toBeInTheDocument();
});

test('muestra un estado vacío cuando nada coincide', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Martillo de acero');
  await userEvent.type(screen.getByLabelText('Buscar producto'), 'zzz');
  expect(screen.getByText(/No encontramos productos/)).toBeInTheDocument();
});

test('cambiar la categoría vuelve a consultar la API con el filtro', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Martillo de acero');
  await userEvent.selectOptions(screen.getByLabelText('Categoría'), 'Plomería');
  await waitFor(() => expect(global.fetch).toHaveBeenLastCalledWith('/products?categoria=Plomer%C3%ADa'));
});

test('muestra un mensaje si la API falla', async () => {
  simularApi({ ok: false, status: 500, json: async () => ({}) });
  render(<Catalogo />);
  expect(await screen.findByRole('alert')).toHaveTextContent(/No pudimos cargar/);
});
