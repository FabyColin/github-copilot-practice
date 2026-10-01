# Guía del instructor

Curso de 1 día (09:00 a 16:50, 7 h 50 min efectivas) sobre GitHub Copilot, con **dos pistas** de ejercicios: **Python** (Flask y pytest) y **JavaScript** (Express, React y Jest). Esta carpeta tiene todo lo necesario para impartirlo.

## Contenido

| Carpeta | Qué contiene |
|---|---|
| `00-setup/` | Checklist previo, día del curso y cierre; solución de problemas |
| `01-fundamentos/` a `09-imagen-a-codigo/` | Guion de cada módulo: tiempos, qué decir, qué demostrar, errores frecuentes |
| `10-mas-alla-del-ide/` | Material de la demo: issue de ejemplo y configuración MCP |
| `11-opcional-revision-pr/` | **Ejercicio opcional** (fuera de la agenda): guion y clave de los defectos |

## Qué pista elegir

Los módulos de teoría, la agenda y los tiempos son iguales. Pregunta al grupo con anticipación (idealmente al inscribirse):

| Si el grupo... | Pista |
|---|---|
| Trabaja con datos, automatización o backend en Python | **Python** |
| Es de desarrollo web o front-end | **JavaScript** (incluye React) |
| Es mixto | La que domine la mayoría; los ejercicios son equivalentes. Mantén la otra como respaldo |

El temario original menciona Jest y React: la pista JavaScript los cumple tal cual y la pista Python es la adaptación.

## Organización del repositorio

```text
docs/                 teoría y enunciados (compartidos; ejercicios en python/ y javascript/)
pistas/python/        src, ejercicios, soluciones
pistas/javascript/    src (API), web (React), ejercicios, soluciones
session-delivery-resources/   esta guía
scripts/build_alumnos.py      genera un repo de alumnos por pista
```

Los repos de alumnos **no se editan a mano**: se regeneran con el script (ver abajo).

## Publicar los repos de alumnos

```bash
python scripts/build_alumnos.py --pista python     --salida ../copilot-fundamentos-alumnos-python     --forzar
python scripts/build_alumnos.py --pista javascript --salida ../copilot-fundamentos-alumnos-react      --forzar
```

Después, en cada carpeta generada: `git add -A`, `git commit` y `git push`. El script conserva `.git`, deja solo la pista elegida, quita `soluciones/` y esta guía, y falla si queda alguna referencia al instructor.

## Agenda

| Horario | Bloque | Min |
|---|---|---|
| 09:00 | 1. Fundamentos | 20 |
| 09:20 | 2. Autocompletado (teoría + 3 tramos + ejercicio completo de 50 min) | 100 |
| 11:00 | Descanso | 10 |
| 11:10 | 3. Chat | 20 |
| 11:30 | 4. Contextualización | 20 |
| 11:50 | 5. Prompting | 15 |
| 12:05 | **Ejercicio 2** | 30 |
| 12:35 | Comida | 50 |
| 13:25 | 6. Comprensión y corrección + **Ejercicio 3** | 40 |
| 14:05 | 7. Agent mode | 20 |
| 14:25 | 8. Pruebas unitarias | 10 |
| 14:35 | Descanso | 10 |
| 14:45 | **Ejercicio 4** | 55 |
| 15:40 | 9. Imagen a código + **Ejercicio 5** | 35 |
| 16:15 | 10. Más allá del IDE (demo) | 25 |
| 16:40 | Cierre | 10 |

Holgura: 10 min antes de las 17:00. El [ejercicio opcional](11-opcional-revision-pr/guion.md) queda fuera de este horario.

## Si vas atrasado

Recorta en este orden:

1. Quita los 3 tramos aislados del módulo 2 y empieza directo en el ejercicio de 50 min (ahorras 30 min).
2. En el Ejercicio 4, omite la mutación manual y limita los casos borde (ahorras 10 min).
3. En el Ejercicio 5, entrega una versión inicial y haz la iteración 2 como demo (ahorras 10 min).
4. El módulo 10 pasa de demo en vivo a mostrar capturas o un PR ya generado (ahorras 15 min).

## Ejercicio opcional

Existe un ejercicio **opcional** de 20 minutos, [Revisa el Pull Request](11-opcional-revision-pr/guion.md), que **no está en la agenda** ni cuenta en la rúbrica. Ofrécelo a quien termine antes o déjalo como práctica posterior; si vas justo de tiempo, ignóralo. La clave de sus tres defectos está en [`clave.md`](11-opcional-revision-pr/clave.md).

## Rúbrica por ejercicio

Cada ejercicio se evalúa en cuatro dimensiones. Puntúa de 0 a 2 (0 = no, 1 = parcial, 2 = sí).

| Dimensión | Qué mirar |
|---|---|
| **Resultado** | Cumple los criterios de aceptación del enunciado |
| **Revisión crítica** | Detectó y corrigió algo que Copilot hizo mal |
| **Comprensión** | Explica el código con sus palabras |
| **Control** | Alcance acotado, revisó diffs, usó el modo correcto |

El criterio más valioso es **Revisión crítica**: un alumno que acepta todo sin cuestionar no aprendió lo esencial aunque las pruebas pasen.

## Soluciones de referencia

| Ejercicio | Python (`pistas/python/soluciones/`) | JavaScript (`pistas/javascript/soluciones/`) |
|---|---|---|
| 1 | `ej1/inventario.py` | `ej1/inventario.js` |
| 2 | `ej2/` (utilidades, instrucciones, prompt file) | `ej2/` (ídem) |
| 3 | `ej3/reporte_ventas.py` y [`bugs.md`](06-comprension-codigo/bugs.md) | `ej3/reporte_ventas.js` y [`bugs.md`](06-comprension-codigo/bugs.md) |
| 4 | `ej4/` (app, descuentos y pruebas; cobertura 100 % de `descuentos.py`) | `ej4/` (app, descuentos y pruebas; cobertura 100 % de `descuentos.js`) |
| 5 | `ej5/` (plantilla Jinja) | `ej5/` (componente React y su prueba) |
| Opcional | `ej-opcional/` (módulo corregido y 15 pruebas estrictas) | `ej-opcional/` (ídem) |

El flujo de CI valida automáticamente las soluciones de los ejercicios 1 y 4 en Python, y de los ejercicios 1, 4 y 5 en JavaScript, y comprueba que los dos repos de alumnos se puedan generar.

## Aviso importante

Copilot y sus modelos cambian rápido. **Ensaya el curso completo 1 o 2 días antes**, revisa que los atajos, nombres de modos y opciones coincidan con la versión actual, y actualiza lo que haya cambiado. Los resultados del agente **no son deterministas**: ten siempre la solución de referencia a mano.
