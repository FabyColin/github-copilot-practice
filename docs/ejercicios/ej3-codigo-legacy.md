# Ejercicio 3: Rescata el script legacy

**Módulo:** [6. Comprensión y corrección](../modulos/06-comprension-y-correccion.md) · **Tiempo:** 30 min
**Carpeta:** `ejercicios/ej3-codigo-legacy/`

## Escenario

Heredaste `reporte_ventas.py`: nadie lo documentó, usa nombres de una letra y el equipo dice que "a veces falla". Se ejecuta así:

```bash
cd ejercicios/ej3-codigo-legacy
python reporte_ventas.py ventas.csv
```

Debe mostrar el **top 3 de vendedores**, el **ticket promedio por región** y el **total de ventas**.

## Parte 1: entender (10 min)

Usando Copilot (**sin leer primero el código por tu cuenta**):

1. En modo Ask: "Resume qué hace este script, sus entradas y sus salidas."
2. Selecciona la función `f` y usa `/explain`.
3. Pide nombres descriptivos para `f`, `d`, `r`, `t`, `g`, `s`, `k`.
4. Con `#codebase`: "¿Qué columnas del CSV usa el script y en qué posición?"

**Entregable:** un párrafo (3 a 5 líneas) con tu explicación del script, escrito **con tus palabras**.

## Parte 2: diagnosticar y corregir (15 min)

El script tiene **3 bugs**. Algunos son silenciosos: el programa no falla, pero los números salen mal.

1. Ejecútalo y revisa la salida. ¿Algo falla? ¿Algo parece raro?
2. Para cada problema, usa el reporte de bug del módulo 6 (esperado / obtenido / reproducción).
3. Pide a Copilot **la causa** antes de la corrección.
4. Aplica el arreglo y **verifica ejecutando de nuevo**.

!!! tip "Pista de verificación"
    Calcula a mano el total de las ventas de `Marta` en `ventas.csv` y compáralo con lo que muestra el reporte.

## Parte 3: dejarlo mejor (5 min)

Pide a Copilot que refactorice el script con nombres descriptivos y funciones pequeñas, **sin cambiar el resultado**. Verifica que la salida coincide con la de tu versión corregida.

## Criterios de aceptación

- [ ] El script corre sin errores.
- [ ] Los números coinciden con tus cálculos manuales.
- [ ] Para cada bug anotaste: **qué fallaba, por qué y cómo lo detectaste**.
- [ ] Puedes explicar cada corrección sin mirar la respuesta de Copilot.

## Preguntas de cierre

1. ¿Qué bug fue el más difícil de detectar? ¿Por qué?
2. ¿Hubo algún "arreglo" de Copilot que ocultaba el problema en lugar de resolverlo?

---

*Solución de referencia y explicación de los bugs: `session-delivery-resources/06-comprension-codigo/` y `soluciones/ej3/` (solo para el instructor).*
