# GitHub Copilot: Fundamentos (pista Python)

Material para alumnos del curso de 1 día. Trabajarás con **Python y Flask**, y probarás con **pytest**.

## Qué aprenderás

- Usar sugerencias inline, Next Edit Suggestions y desarrollo guiado por comentarios.
- Trabajar con el chat (Ask, Plan, Agent), slash commands y selección de modelo.
- Dar contexto y reglas a Copilot con variables, custom instructions y prompt files.
- Escribir prompts efectivos e iterar sobre las respuestas.
- Entender y corregir código legacy.
- Delegar cambios multi-archivo al agente con control y revisión humana.
- Generar pruebas con pytest y llevarlas a verde.
- Pasar de un mockup a código.

## Estructura

| Carpeta | Contenido |
|---|---|
| `docs/` | Módulos del curso, enunciados de los ejercicios, agenda y recursos |
| `ejercicios/` | Archivos de arranque de los 5 ejercicios |
| `src/` | Tienda de productos en Flask, proyecto base de varios ejercicios |
| `.devcontainer/` | Entorno listo para Codespaces o Dev Containers |

## Los 5 ejercicios

| # | Ejercicio | Tiempo |
|---|---|---|
| 1 | [Autocompletado](docs/ejercicios/ej1-autocompletado.md): 3 tramos aislados y módulo de inventario | 30 + 50 min |
| 2 | [Chat, contexto y prompting](docs/ejercicios/ej2-chat-contexto-prompting.md) | 30 min |
| 3 | [Rescata el script legacy](docs/ejercicios/ej3-codigo-legacy.md) | 30 min |
| 4 | [Agent mode: descuentos y pruebas en verde](docs/ejercicios/ej4-agent-descuentos.md) | 55 min |
| 5 | [Del mockup a la página](docs/ejercicios/ej5-imagen-a-codigo.md) | 30 min |

Empieza por los [requisitos previos](docs/requisitos.md) y la [agenda](docs/agenda.md).

## Inicio rápido

La opción recomendada es **GitHub Codespaces** (*Code → Codespaces → Create*), que instala todo automáticamente.

En local:

```bash
git clone <url-de-este-repositorio>
cd <carpeta-del-repositorio>
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r src/requirements.txt
pytest src
```

## Licencia

MIT. Consulta [LICENSE](LICENSE).
