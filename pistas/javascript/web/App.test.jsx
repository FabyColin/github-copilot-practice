import { render, screen } from '@testing-library/react';
import App from './App';

beforeEach(() => {
  // Si la app consulta la API, evita llamadas reales durante la prueba.
  global.fetch = jest.fn(() => new Promise(() => {}));
});

test('muestra el nombre de la tienda', () => {
  render(<App />);
  expect(screen.getByText(/FerreMax/)).toBeInTheDocument();
});
