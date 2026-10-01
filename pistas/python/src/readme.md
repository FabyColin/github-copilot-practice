# Farmacia Demo (proyecto base)

API REST en Flask con datos ficticios en memoria. Es el proyecto que se usa en los ejercicios 2, 4 y 5.

> Los productos, precios y reglas son **ficticios y didácticos**. No representan precios ni requisitos regulatorios reales.

## Ejecutar

```bash
cd src
pip install -r requirements.txt
python app.py          # http://localhost:5000
pytest                 # pruebas
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/products` | Lista productos (filtro opcional `?categoria=`) |
| GET | `/products/<id>` | Detalle de un producto |
| POST | `/products` | Crea un producto (`nombre` obligatorio) |
| PUT | `/products/<id>` | Actualiza campos |
| DELETE | `/products/<id>` | Elimina |
| POST | `/orders` | Calcula el total de un pedido |

Cada producto tiene `id`, `nombre`, `descripcion`, `precio`, `categoria`, `stock` y `requiere_receta` (verdadero para medicamentos que se venden solo con receta, como los antibióticos).
