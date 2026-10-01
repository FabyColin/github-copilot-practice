import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Catalogo from './Catalogo';

const PRODUCTOS = [
  { id: 'p-001', nombre: 'Paracetamol 500 mg', categoria: 'Analgésicos y antiinflamatorios', precio: 45, requiere_receta: false },
  { id: 'p-002', nombre: 'Amoxicilina 500 mg', categoria: 'Antibióticos', precio: 129.5, requiere_receta: true },
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
  expect(await screen.findByText('Paracetamol 500 mg')).toBeInTheDocument();
  expect(screen.getByText('Amoxicilina 500 mg')).toBeInTheDocument();
});

test('marca solo los productos que requieren receta', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Paracetamol 500 mg');
  expect(screen.getAllByText('Requiere receta')).toHaveLength(1);
});

test('la búsqueda filtra por nombre', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Paracetamol 500 mg');
  await userEvent.type(screen.getByLabelText('Buscar producto'), 'amoxi');
  expect(screen.queryByText('Paracetamol 500 mg')).not.toBeInTheDocument();
  expect(screen.getByText('Amoxicilina 500 mg')).toBeInTheDocument();
});

test('muestra un estado vacío cuando nada coincide', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Paracetamol 500 mg');
  await userEvent.type(screen.getByLabelText('Buscar producto'), 'zzz');
  expect(screen.getByText(/No encontramos productos/)).toBeInTheDocument();
});

test('cambiar la categoría vuelve a consultar la API con el filtro', async () => {
  simularApi({ ok: true, json: async () => PRODUCTOS });
  render(<Catalogo />);
  await screen.findByText('Paracetamol 500 mg');
  await userEvent.selectOptions(screen.getByLabelText('Categoría'), 'Antibióticos');
  await waitFor(() => expect(global.fetch).toHaveBeenLastCalledWith('/products?categoria=Antibi%C3%B3ticos'));
});

test('muestra un mensaje si la API falla', async () => {
  simularApi({ ok: false, status: 500, json: async () => ({}) });
  render(<Catalogo />);
  expect(await screen.findByRole('alert')).toHaveTextContent(/No pudimos cargar/);
});
