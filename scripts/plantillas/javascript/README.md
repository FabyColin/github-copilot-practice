# GitHub Copilot: Fundamentos (pista JavaScript y React)

Material para alumnos del curso de 1 día. Trabajarás con **Express y React (Vite)**, y probarás con **Jest**.

## Qué aprenderás

- Usar sugerencias inline, Next Edit Suggestions y desarrollo guiado por comentarios.
- Trabajar con el chat (Ask, Plan, Agent), slash commands y selección de modelo.
- Dar contexto y reglas a Copilot con variables, custom instructions y prompt files.
- Escribir prompts efectivos e iterar sobre las respuestas.
- Entender y corregir código legacy.
- Delegar cambios multi-archivo al agente con control y revisión humana.
- Generar pruebas con Jest y llevarlas a verde.
- Generar un componente React a partir de un mockup.

## Estructura

| Carpeta | Contenido |
|---|---|
| `docs/` | Módulos del curso, enunciados de los ejercicios, agenda y recursos |
| `ejercicios/` | Archivos de arranque de los 5 ejercicios |
| `src/` | API de la tienda en Express y sus pruebas |
| `web/` | Interfaz en React (se completa en el Ejercicio 5) |
| `.devcontainer/` | Entorno listo para Codespaces o Dev Containers |

## Los 5 ejercicios

| # | Ejercicio | Tiempo |
|---|---|---|
| 1 | [Autocompletado](docs/ejercicios/ej1-autocompletado.md): 3 tramos aislados y módulo de inventario | 30 + 50 min |
| 2 | [Chat, contexto y prompting](docs/ejercicios/ej2-chat-contexto-prompting.md) | 30 min |
| 3 | [Rescata el script legacy](docs/ejercicios/ej3-codigo-legacy.md) | 30 min |
| 4 | [Agent mode: descuentos y pruebas en verde](docs/ejercicios/ej4-agent-descuentos.md) | 55 min |
| 5 | [Del mockup a un componente React](docs/ejercicios/ej5-imagen-a-codigo.md) | 30 min |

**Opcional:** [Revisa el Pull Request](docs/ejercicios/ej-opcional-revision-pr.md) (20 min). No está en la agenda; es para quien termine antes o quiera practicar después.

Empieza por los [requisitos previos](docs/requisitos.md) y la [agenda](docs/agenda.md).

## Inicio rápido

La opción recomendada es **GitHub Codespaces** (*Code → Codespaces → Create*), que instala todo automáticamente.

En local (Node.js 20 o superior):

```bash
git clone <url-de-este-repositorio>
cd <carpeta-del-repositorio>
npm install
npm test          # pruebas de la API y de React
npm start         # API en http://localhost:5000
npm run dev       # interfaz en http://localhost:5173
```

## Licencia

MIT. Consulta [LICENSE](LICENSE).
