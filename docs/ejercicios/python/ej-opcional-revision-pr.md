# Ejercicio opcional: Revisa el Pull Request (Python)

!!! info "Este ejercicio es OPCIONAL"
    **No forma parte de la agenda del día** ni se evalúa. Es para quien termine un ejercicio antes de tiempo o quiera practicar después del curso. Si vas justo de tiempo, sáltalo sin pendiente.

**Tiempo:** 20 min · **Módulos relacionados:** [10. Más allá del IDE](../../modulos/10-mas-alla-del-ide.md) y [8. Pruebas unitarias](../../modulos/08-pruebas-unitarias.md)
**Carpeta:** `ejercicios/ej-opcional-revision-pr/`

## Escenario

Un compañero abrió el **PR #42** y te pide aprobarlo hoy. Dice que las pruebas están en verde y que el cambio es pequeño. Parte del código lo generó una herramienta de IA. **Tu trabajo es revisarlo como lo harías antes de hacer merge.**

Lee primero `DESCRIPCION_DEL_PR.md`. El cambio está en `ajuste_stock.py` y sus pruebas en `test_ajuste_stock.py`.

!!! warning "Regla"
    En las partes 1 y 2 **no corrijas el código**: solo revisa y anota. Corregir es la parte 3.

## Parte 1: revisa por tu cuenta (8 min)

1. Lee la descripción del PR y el código.
2. Ejecuta las pruebas:

    ```bash
    cd ejercicios/ej-opcional-revision-pr
    pytest -q
    ```

3. Prueba el cambio de verdad con la app de demostración (`python demo_app.py`, puerto 5001) y `curl` o el navegador.
4. Anota cada hallazgo con: **qué**, **dónde**, **gravedad** (alta, media, baja) y **cómo lo comprobaste**.

??? tip "Pistas (ábrelas solo si te atoras)"
    - ¿Qué pasa si `delta` no es un número, o no viene?
    - ¿Qué impide que el stock quede en negativo?
    - ¿De dónde salen los datos que se pintan en la ficha? ¿Quién puede escribirlos?
    - Si el código estuviera roto, ¿las pruebas fallarían? Léelas con calma.

## Parte 2: compara con Copilot (7 min)

Pide una revisión a Copilot **después** de haber anotado tus hallazgos. Elige una:

- **Chat:** modo Ask con `#file:ajuste_stock.py` y `#file:test_ajuste_stock.py`. Pide: "Revisa este cambio como lo haría un revisor de seguridad y calidad. Lista problemas con gravedad y cómo reproducirlos."
- **Code review en el editor:** si tu versión de VS Code lo ofrece, usa la acción de revisión de Copilot en el panel de control de código fuente o sobre una selección.
- **Code review en un PR real:** si tienes una copia del repositorio donde puedas subir una rama, crea un PR y agrega a Copilot como revisor.

Después compara:

| | Tus hallazgos | Hallazgos de Copilot |
|---|---|---|
| ¿Qué encontró cada uno? | | |
| ¿Qué encontró solo uno de los dos? | | |
| ¿Hubo falsos positivos (reportes que no son problemas)? | | |
| ¿Verificaste los hallazgos de Copilot ejecutando algo? | | |

## Parte 3: decide (5 min)

1. Escribe tu decisión (**aprobar**, **aprobar con cambios** o **pedir cambios**) y un comentario de revisión de 3 a 5 líneas dirigido a quien abrió el PR.
2. Si te alcanza el tiempo, pide al agente que corrija **un** hallazgo y escribe una prueba que habría fallado con el código original.

## Criterios de aceptación

- [ ] Tu lista de hallazgos incluye gravedad y evidencia, no solo opiniones.
- [ ] Comprobaste al menos un hallazgo **ejecutando** código.
- [ ] Comparaste tu revisión con la de Copilot e identificaste al menos una diferencia.
- [ ] Tu decisión está justificada.

## Preguntas de cierre

1. ¿Qué te hizo desconfiar (o confiar de más) de "las pruebas están en verde"?
2. ¿Qué encontró Copilot que tú no, y al revés?
3. ¿Qué cambiarías en el proceso de tu equipo para que un cambio generado con IA se revise mejor?
