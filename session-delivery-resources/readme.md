# Guía del instructor

Curso de 1 día (09:00 a 16:50, 7 h 50 min efectivas) sobre GitHub Copilot con Python y Flask. Esta carpeta tiene todo lo necesario para impartirlo.

## Contenido

| Carpeta | Qué contiene |
|---|---|
| `00-setup/` | Checklist previo, día del curso y cierre; solución de problemas |
| `01-fundamentos/` a `09-imagen-a-codigo/` | Guion de cada módulo: tiempos, qué decir, qué demostrar, errores frecuentes |
| `10-mas-alla-del-ide/` | Material de la demo: issue de ejemplo y configuración MCP |

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

Holgura: 10 min antes de las 17:00.

## Si vas atrasado

Recorta en este orden:

1. Quita los 3 tramos aislados del módulo 2 y empieza directo en el ejercicio de 50 min (ahorras 30 min).
2. En el Ejercicio 4, omite la mutación manual y limita los casos borde (ahorras 10 min).
3. En el Ejercicio 5, entrega una versión inicial y haz la iteración 2 como demo (ahorras 10 min).
4. El módulo 10 pasa de demo en vivo a mostrar capturas o un PR ya generado (ahorras 15 min).

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

| Ejercicio | Dónde |
|---|---|
| 1 | `soluciones/ej1/inventario.py` |
| 2 | `soluciones/ej2/` |
| 3 | `soluciones/ej3/reporte_ventas.py` y `06-comprension-codigo/bugs.md` |
| 4 | `soluciones/ej4/` (app, descuentos y pruebas; cobertura 100 % de `descuentos.py`) |
| 5 | `soluciones/ej5/` |

El flujo de CI valida automáticamente las soluciones de los ejercicios 1 y 4.

## Aviso importante

Copilot y sus modelos cambian rápido. **Ensaya el curso completo 1 o 2 días antes**, revisa que los atajos, nombres de modos y opciones coincidan con la versión actual, y actualiza lo que haya cambiado. Los resultados del agente **no son deterministas**: ten siempre la solución de referencia a mano.
