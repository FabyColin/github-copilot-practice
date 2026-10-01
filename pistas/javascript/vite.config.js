import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// En desarrollo, las llamadas a la API se envían al servidor Express (npm start, puerto 5000).
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/products': 'http://localhost:5000',
      '/orders': 'http://localhost:5000',
    },
  },
});
