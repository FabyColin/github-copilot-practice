# Requisitos previos

Completa esta lista **antes del curso**. Si tienes problemas, avisa al instructor con anticipación.

## Cuentas

- [ ] Cuenta de GitHub.
- [ ] Licencia activa de GitHub Copilot (individual u otorgada por tu organización). Verifica en [github.com/settings/copilot](https://github.com/settings/copilot).

## Software (si no usarás Codespaces)

- [ ] [Visual Studio Code](https://code.visualstudio.com/) en su versión estable más reciente.
- [ ] Extensiones **GitHub Copilot** y **GitHub Copilot Chat** (y **GitHub Pull Requests** para la demo final).
- [ ] Python 3.12 o superior.
- [ ] Git.

## Verificación (5 minutos)

```bash
git clone <url-del-repositorio>
cd copilot-fundamentos-curso
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r src/requirements.txt
pytest src
```

Debes ver `2 passed`. Después, en VS Code:

- [ ] Escribe un comentario en un archivo `.py` y comprueba que aparece texto gris de sugerencia.
- [ ] Abre el chat de Copilot (`Ctrl+Alt+I`) y escribe un mensaje.

!!! tip "Alternativa recomendada"
    Usa **GitHub Codespaces** (*Code → Codespaces → Create codespace on main*). El entorno queda configurado automáticamente por `.devcontainer/`.

## Política de uso

Trabajaremos con código de ejemplo. **No pegues código, datos ni credenciales de clientes** en el chat durante el curso.
