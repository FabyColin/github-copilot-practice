# GitHub Copilot: Fundamentos (curso de 1 día) · repositorio del instructor

Curso práctico de 8 horas para aprender a trabajar con GitHub Copilot en el flujo de desarrollo diario, desde el autocompletado hasta el modo Agent. Tiene **dos pistas** de ejercicios equivalentes:

| Pista | Stack | Pruebas | Repo de alumnos |
|---|---|---|---|
| **Python** | Flask | pytest | `copilot-fundamentos-alumnos-python` |
| **JavaScript** | Express y React (Vite) | Jest | `copilot-fundamentos-alumnos-react` |

Este repositorio es la **fuente única**: contiene la teoría, las dos pistas, las soluciones y la guía del instructor. Los repos de alumnos se generan desde aquí con un script y **no se editan a mano**.

## Caso de práctica

Todos los ejercicios usan **Farmacia Demo**, un caso ficticio con medicamentos, existencias, caducidades, recetas y descuentos. Los datos y reglas son didácticos; no representan precios ni requisitos regulatorios reales.

## Qué aprenderás

- Usar sugerencias inline, Next Edit Suggestions y desarrollo guiado por comentarios.
- Trabajar con el chat (Ask, Plan, Agent), slash commands y selección de modelo.
- Dar contexto y reglas a Copilot con variables, custom instructions y prompt files.
- Escribir prompts efectivos e iterar sobre las respuestas.
- Entender y corregir código legacy.
- Delegar cambios multi-archivo al agente con control y revisión humana.
- Generar pruebas y llevarlas a verde.
- Pasar de un mockup a código.
- Conocer el cloud agent, Copilot code review y MCP (demo del instructor).

## Organización

```text
docs/                         Teoría (compartida) y enunciados: ejercicios/python y ejercicios/javascript
pistas/
  python/                     src (Flask), ejercicios, soluciones
  javascript/                 src (Express), web (React), ejercicios, soluciones
session-delivery-resources/   Guía del instructor: guion por módulo, setup, rúbrica, bugs sembrados
scripts/
  build_alumnos.py            Genera el repo de alumnos de una pista
  plantillas/                 README, entorno y CI de cada repo de alumnos
.devcontainer/                Entorno del instructor (Python y Node)
```

## Los 5 ejercicios (mismos objetivos y tiempos en ambas pistas)

| # | Ejercicio | Módulos | Tiempo |
|---|---|---|---|
| 1 | Autocompletado: 3 tramos aislados + módulo de inventario | 2 | 30 + 50 min |
| 2 | Chat, contexto y prompting | 3, 4, 5 | 30 min |
| 3 | Rescata el script legacy | 6 | 30 min |
| 4 | Agent mode: descuentos y pruebas en verde | 7, 8 | 55 min |
| 5 | Del mockup al código (plantilla Jinja / componente React) | 9 | 30 min |
| *Opcional* | *Revisa el Pull Request (fuera de la agenda)* | *8, 10* | *20 min* |

## Inicio rápido (instructor)

Opción recomendada: **GitHub Codespaces** con el devcontainer del repo (instala Python y Node).

Pista Python:

```bash
pip install -r pistas/python/src/requirements.txt
pytest pistas/python/src
```

Pista JavaScript:

```bash
cd pistas/javascript
npm install
npm test
```

Documentación como sitio web:

```bash
pip install -r requirements.txt
mkdocs serve
```

## Publicar los repos de alumnos

```bash
python scripts/build_alumnos.py --pista python     --salida ../copilot-fundamentos-alumnos-python --forzar
python scripts/build_alumnos.py --pista javascript --salida ../copilot-fundamentos-alumnos-react  --forzar
```

El script deja solo la pista elegida en la raíz, quita `soluciones/` y la guía del instructor, filtra las pestañas Python/JavaScript de los documentos y falla si queda alguna referencia al material del instructor. Después haz `git add -A`, `git commit` y `git push` en cada carpeta generada (se conserva su `.git`).

## Para el instructor

Empieza por [`session-delivery-resources/readme.md`](session-delivery-resources/readme.md). El CI valida las soluciones de ambas pistas y que los dos repos de alumnos se puedan generar.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
# copilot-fundamentos-curso
