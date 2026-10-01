# Setup y checklists

## 1 semana antes

- [ ] Confirma la **pista** del grupo (Python o JavaScript) y comparte el repo de alumnos correspondiente.

- [ ] Confirma que **todos los alumnos** tienen licencia de Copilot activa (individual o de organización).
- [ ] Envía [`docs/requisitos.md`](../../docs/requisitos.md) y pide que ejecuten la verificación de 5 minutos.
- [ ] Verifica que la organización permita **Codespaces**, el **cloud agent** y **MCP** (políticas de Copilot a nivel organización).
- [ ] Si usarás el cloud agent en la demo: confirma que está habilitado en el repositorio.
- [ ] Revisa las cuotas del plan (medidor en github.com/settings/copilot).

## 2 días antes: ensayo completo

- [ ] Haz **todos** los ejercicios siguiendo los enunciados. Cronométralos.
- [ ] Verifica atajos y nombres de modos contra la versión actual de VS Code y Copilot.
- [ ] Revisa que `/explain`, `/fix`, `/tests` y `/doc` funcionen.
- [ ] Comprueba que la imagen se adjunta al chat con el modelo elegido.
- [ ] Guarda **capturas o video** de cada demo como respaldo.

## 1 día antes: demo del módulo 10

- [ ] Crea el issue de `10-mas-alla-del-ide/issue-demo.md` en tu repositorio de demo.
- [ ] **Asígnalo a Copilot con anticipación** (la tarea tarda varios minutos y consume solicitudes premium) y deja el PR listo para revisar.
- [ ] Prepara un segundo PR con un cambio pequeño para mostrar **Copilot code review**.
- [ ] Copia `mcp.json.ejemplo` a `.vscode/mcp.json` **en tu máquina** y comprueba que el servidor aparece.

## El día del curso

- [ ] Llega 30 minutos antes. Abre el repo en VS Code o Codespaces.
- [ ] Pista Python: `pytest pistas/python/src` (debe dar `2 passed`) y `python pistas/python/src/app.py`.
- [ ] Pista JavaScript: en `pistas/javascript`, `npm install`, `npm test` (debe dar `3 passed`) y `npm start`.
- [ ] Verifica que el chat responde y que el modo Agent está disponible.
- [ ] Ten abiertas las soluciones de referencia en otra ventana.
- [ ] Verifica que **no** exista un `.github/copilot-instructions.md` en el repo del alumno (se crea en el Ejercicio 2).
- [ ] Proyector, volumen y zoom de la fuente en 150 % o más.

## Al terminar

- [ ] Elimina los Codespaces de demo.
- [ ] Desasigna el issue demo del cloud agent y cierra los PR de demo.
- [ ] Elimina `.vscode/mcp.json` de tu máquina si fue solo para la demo.
- [ ] Recoge feedback y actualiza el material.

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| No aparecen sugerencias inline | Licencia inactiva o extensión sin sesión | Cerrar sesión y volver a iniciar en GitHub desde VS Code |
| No existe el modo Agent | Versión antigua o política de la organización | Actualizar VS Code; revisar políticas de Copilot |
| Falta el modelo X | Plan o política de la organización | Usar otro modelo; avisar al administrador |
| `/tests` o `/fix` no responden como se espera | Falta selección o archivo activo | Seleccionar el código primero |
| NES no sugiere nada | Opción desactivada | `github.copilot.nextEditSuggestions.enabled` |
| `pytest` no encuentra `app` | Se ejecuta fuera de `src/` | `cd src && pytest` |
| `ModuleNotFoundError: flask` | Falta el entorno virtual | Activarlo e instalar `src/requirements.txt` |
| `Cannot find module 'express'` (JS) | No se instalaron dependencias | `npm install` en la carpeta de la pista |
| `npm test` dice que no hay pruebas (JS) | Se ejecutó fuera de la carpeta de la pista | Entrar a `pistas/javascript` (o a la raíz del repo de alumnos) |
| `npm run dev` carga pero no hay datos (JS) | La API no está corriendo | Abrir otra terminal con `npm start` |
| Falla `Unexpected token '<'` en Jest (JS) | Archivo `.jsx` fuera de `web/` | Las pruebas de React van en `web/` |
| El agente tarda o se atora | Tarea muy grande o servicio saturado | Reducir el alcance o pasar a la solución de referencia |
| El prompt file no aparece con `/` | Ruta o extensión incorrecta | Debe ser `.github/prompts/<nombre>.prompt.md` |
