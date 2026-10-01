# Módulo 9: Imagen a código (5 min) y Ejercicio 5 (30 min)

**Material:** [`docs/modulos/09-imagen-a-codigo.md`](../../docs/modulos/09-imagen-a-codigo.md) · **Ejercicio:** [`ej5`](../../docs/ejercicios/ej5-imagen-a-codigo.md)

## Teoría (5 min)

- Modelo con visión, adjuntar imagen, describir **comportamiento** además del aspecto.
- Aclara que el temario menciona React y aquí se genera una plantilla Jinja con Flask.

## Ejercicio 5 (30 min)

| Parte | Min | Qué observar |
|---|---|---|
| 1. Primera versión | 10 | Prompt con contexto, intención y restricciones |
| 2. Comparar e iterar | 15 | 3 diferencias concretas; 2 iteraciones |
| 3. Revisión de calidad | 5 | XSS, teclado/accesibilidad, errores de API |

## Qué revisar

- ¿Inserta datos con `innerHTML` sin escapar? Es la falla de seguridad más común. La solución de referencia usa `textContent`.
- ¿Agregó librerías externas pese a la restricción?
- ¿Modificó endpoints de `/products`?

## Comparación sugerida (3 min)

Muestra `soluciones/ej5/templates/catalogo.html` junto al resultado de un alumno y compara: estados vacíos, escape de HTML, responsividad.

Para probar la solución:

```bash
mkdir /tmp/ej5 && cp -r src/. /tmp/ej5/
cp soluciones/ej5/app.py /tmp/ej5/ && cp soluciones/ej5/templates/catalogo.html /tmp/ej5/templates/
cd /tmp/ej5 && python app.py   # http://localhost:5000/catalogo
```

## Errores frecuentes

| Error | Qué decir |
|---|---|
| El modelo elegido no admite imágenes | Cambiar a un modelo con visión |
| "Se ve igual" sin comparar | Anotar 3 diferencias concretas |
| Resultado perfecto a la primera | Pedir revisar accesibilidad y estados de error |
