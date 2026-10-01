# Ejercicio opcional: Revisa el Pull Request (20 min, fuera de la agenda)

**Enunciado:** [`ej-opcional-revision-pr`](../../docs/ejercicios/ej-opcional-revision-pr.md) · **Clave:** [`clave.md`](clave.md)

> **Es opcional.** No cuenta en la agenda (7 h 50 min) ni en la rúbrica. No lo anuncies como parte del programa: ofrécelo a quien termine un ejercicio antes de tiempo o déjalo como tarea posterior.

## Cuándo ofrecerlo

- Un alumno termina el Ejercicio 3, 4 o 5 con 10 minutos o más de sobra.
- Al final del día, como práctica para casa.
- Como reemplazo de la demo del módulo 10 **solo** si el cloud agent o el code review no están disponibles en tu organización.

No lo uses para "rellenar" tiempo del grupo completo: el día ya está lleno.

## Qué ejercita

La contracara del Ejercicio 4. Allí el alumno dirige al agente y revisa sus diffs; aquí revisa un cambio **ya hecho** (como en un PR) que parece sano porque "las pruebas están en verde". Es práctica de revisión crítica, el tema transversal del curso.

## Cómo conducirlo

| Min | Parte | Qué observar |
|---|---|---|
| 0–8 | Revisión propia | ¿Leen la descripción del PR con escepticismo? ¿Ejecutan el código o solo lo leen? |
| 8–15 | Comparar con Copilot | ¿Pidieron la revisión **después** de anotar los suyos? ¿Verifican lo que Copilot afirma? |
| 15–20 | Decidir | ¿Su comentario de revisión es accionable y cortés? |

## Cómo preparar el material

Nada especial: el material ya está en `ejercicios/ej-opcional-revision-pr/` de cada pista. El alumno **no** debe ver la carpeta `soluciones/`: en el repo de alumnos no existe.

Para revisión en un PR real de GitHub, cada alumno necesita poder subir una rama a una copia del repo. Si no es viable, el chat y la acción de revisión del editor bastan.

## Puesta en común (si lo hacen varios)

1. Pregunta qué encontraron **solo ellos** y qué encontró **solo Copilot**.
2. Pregunta por falsos positivos: ¿Copilot reportó algo que no era problema?
3. Cierra con la pregunta 1 del enunciado: ¿qué significa realmente "las pruebas están en verde"?

## Advertencia sobre Copilot code review

Su comportamiento cambia entre versiones y planes. **No prometas** que detectará los tres defectos; puede encontrar algunos, todos o ninguno, y reportar cosas que no son defectos. Eso es parte del aprendizaje. Ensáyalo antes y anota qué suele encontrar.
