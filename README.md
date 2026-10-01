# GitHub Copilot: Fundamentos (curso de 1 día)

Curso práctico de 8 horas para aprender a trabajar con GitHub Copilot en el flujo de desarrollo diario, desde el autocompletado hasta el modo Agent, usando **Python y Flask**.

## Qué aprenderás

- Usar sugerencias inline, Next Edit Suggestions y desarrollo guiado por comentarios.
- Trabajar con el chat (Ask, Plan, Agent), slash commands y selección de modelo.
- Dar contexto y reglas a Copilot con variables, custom instructions y prompt files.
- Escribir prompts efectivos e iterar sobre las respuestas.
- Entender y corregir código legacy.
- Delegar cambios multi-archivo al agente con control y revisión humana.
- Generar pruebas con pytest y llevarlas a verde.
- Pasar de un mockup a código.
- Conocer el cloud agent, Copilot code review y MCP (demo del instructor).

## Cómo está organizado el repositorio

| Carpeta | Contenido |
|---|---|
| `docs/` | Sitio del curso (MkDocs): módulos, ejercicios, agenda y recursos |
| `ejercicios/` | Archivos de arranque de los 5 ejercicios |
| `soluciones/` | Soluciones de referencia (para el instructor) |
| `src/` | Tienda de productos en Flask, proyecto base de varios ejercicios |
| `session-delivery-resources/` | Guía del instructor: guion por módulo, setup y rúbrica |
| `.devcontainer/` | Entorno listo para Codespaces o Dev Containers |

## Los 5 ejercicios

| # | Ejercicio | Módulos | Tiempo |
|---|---|---|---|
| 1 | Autocompletado: 3 tramos aislados + módulo de inventario | 2 | 30 + 50 min |
| 2 | Chat, contexto y prompting | 3, 4, 5 | 30 min |
| 3 | Rescata el script legacy | 6 | 30 min |
| 4 | Agent mode: descuentos y pruebas en verde | 7, 8 | 55 min |
| 5 | Del mockup a la página | 9 | 30 min |

## Inicio rápido

La opción recomendada es **GitHub Codespaces** (botón *Code → Codespaces → Create*), que instala todo automáticamente.

En local:

```bash
git clone <url-de-este-repositorio>
cd copilot-fundamentos-curso
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r src/requirements.txt -r requirements.txt
pytest src
```

Para ver la documentación como sitio web:

```bash
mkdocs serve
```

## Para el instructor

Empieza por [`session-delivery-resources/readme.md`](session-delivery-resources/readme.md). Las soluciones están en `soluciones/` y el CI las valida en cada cambio.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
