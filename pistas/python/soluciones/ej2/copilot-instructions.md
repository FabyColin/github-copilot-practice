# Instrucciones para GitHub Copilot en este proyecto

## Contexto
Este proyecto es una API REST de una tienda de productos hecha con Flask y probada con pytest.

## Estilo de código
- Python 3.12. Type hints obligatorios en funciones nuevas.
- Docstrings en español, de una línea cuando sea suficiente.
- Nombres de variables y funciones en español y en `snake_case`.
- Sin dependencias nuevas a menos que se pidan explícitamente.

## Seguridad y calidad
- Valida siempre la entrada del usuario en los endpoints.
- Nunca dejes secretos ni contraseñas en el código.
- No uses `debug=True` fuera de desarrollo local.

## Pruebas
- Toda función nueva lleva pruebas con pytest en `src/tests/`.
- Cubre al menos un caso borde por función.
