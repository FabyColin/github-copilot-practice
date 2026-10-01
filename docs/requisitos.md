# Requisitos previos

Completa esta lista **antes del curso**. Si tienes problemas, avisa al instructor con anticipación. Revisa la pestaña de tu pista (Python o JavaScript); ver [Pistas](pistas.md).

## Cuentas

- [ ] Cuenta de GitHub.
- [ ] Licencia activa de GitHub Copilot (individual u otorgada por tu organización). Verifica en [github.com/settings/copilot](https://github.com/settings/copilot).

## Software (si no usarás Codespaces)

- [ ] [Visual Studio Code](https://code.visualstudio.com/) en su versión estable más reciente.
- [ ] Extensiones **GitHub Copilot** y **GitHub Copilot Chat** (y **GitHub Pull Requests** para la demo final).
- [ ] Git.

=== "Python"

    - [ ] Python 3.12 o superior.

=== "JavaScript"

    - [ ] [Node.js](https://nodejs.org) 20 o superior (incluye `npm`).

## Verificación (5 minutos)

=== "Python"

    ```bash
    git clone <url-del-repositorio>
    cd <carpeta-del-repositorio>
    python -m venv .venv
    # Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
    pip install -r src/requirements.txt
    pytest src
    ```

    Debes ver `2 passed`.

=== "JavaScript"

    ```bash
    git clone <url-del-repositorio>
    cd <carpeta-del-repositorio>
    npm install
    npm test
    ```

    Debes ver `Tests: 3 passed`.

Después, en VS Code:

- [ ] Escribe un comentario en un archivo de código y comprueba que aparece texto gris de sugerencia.
- [ ] Abre el chat de Copilot (`Ctrl+Alt+I`) y escribe un mensaje.

!!! tip "Alternativa recomendada"
    Usa **GitHub Codespaces** (*Code → Codespaces → Create codespace on main*). El entorno queda configurado automáticamente por `.devcontainer/`.

## Política de uso

Trabajaremos con código y datos de ejemplo (una farmacia ficticia). **No pegues código, datos ni credenciales de clientes** en el chat durante el curso, y **nunca datos de pacientes, recetas ni folios reales**.
