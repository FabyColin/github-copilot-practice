# Pistas: Python o JavaScript

El curso tiene dos pistas con los mismos objetivos, tiempos y estructura. Elige la que prefiera tu grupo; los módulos de teoría son iguales para ambas.

| | Pista Python | Pista JavaScript |
|---|---|---|
| **Backend** | Flask | Express |
| **Interfaz (ejercicio 5)** | Plantilla Jinja con HTML, CSS y JS | Componente React (Vite) |
| **Pruebas** | pytest, pytest-cov | Jest, supertest, React Testing Library |
| **Entorno** | Python 3.12 | Node.js 20 o superior |
| **Instalación** | `pip install -r src/requirements.txt` | `npm install` |
| **Correr la API** | `python src/app.py` (puerto 5000) | `npm start` (puerto 5000) |
| **Correr las pruebas** | `pytest src` | `npm test` |

## Equivalencias de archivos

Los módulos de teoría usan ejemplos de la pista Python. En la pista JavaScript, el equivalente es:

| Python | JavaScript |
|---|---|
| `src/app.py` | `src/app.js` |
| `src/descuentos.py` | `src/descuentos.js` |
| `src/tests/test_app.py` | `src/tests/app.test.js` |
| `src/templates/catalogo.html` | `web/Catalogo.jsx` |
| `ejercicios/ej1-autocompletado/inventario.py` | `ejercicios/ej1-autocompletado/inventario.js` |
| `pytest`, `/tests` con pytest | `jest`, `/tests` con Jest |
| `requirements.txt` | `package.json` |

## Rutas de los enunciados

Las rutas de los enunciados (`src/`, `ejercicios/`, `web/`) son **relativas a la carpeta de la pista** (`pistas/python/` o `pistas/javascript/` en el repositorio del instructor; la raíz del repositorio de alumnos).

## Qué es distinto en el Ejercicio 3

En Python, el bug de la división entre cero detiene el programa con un error. En JavaScript, `0 / 0` da `NaN` y el programa sigue: los **tres** bugs son silenciosos. Es una diferencia real del lenguaje y hace el ejercicio más exigente para quien lo verifica.
