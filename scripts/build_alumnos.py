#!/usr/bin/env python3
"""Genera el repositorio de alumnos de una pista a partir del repositorio del instructor.

Uso:
    python scripts/build_alumnos.py --pista python     --salida ../copilot-fundamentos-alumnos-python
    python scripts/build_alumnos.py --pista javascript --salida ../copilot-fundamentos-alumnos-react

Qué hace:
  * Toma el contenido de pistas/<pista>/ y lo deja en la raíz (src/, ejercicios/, web/...).
  * Excluye soluciones/, session-delivery-resources/, scripts/ y la otra pista.
  * Copia la documentación, deja solo los enunciados de la pista y los aplana en docs/ejercicios/.
  * Deja en los documentos solo la pestaña de la pista y convierte los avisos de MkDocs a citas
    legibles en GitHub.
  * Verifica que no quede ninguna referencia a material del instructor.

Solo usa la biblioteca estándar de Python.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PISTAS = {"python": "Python", "javascript": "JavaScript"}
IGNORAR = {"soluciones", "node_modules", "__pycache__", ".pytest_cache", "dist", "coverage", ".venv", "venv", ".git"}
TEXTO = {".py", ".js", ".jsx", ".md", ".json", ".html", ".css", ".cjs", ".txt", ".csv", ".yml", ".yaml"}
PROHIBIDO = ("soluciones/", "session-delivery", "solo para el instructor")
TIPO_AVISO = {"note": "Nota", "tip": "Consejo", "warning": "Atención", "danger": "Peligro", "info": "Información"}


# ---------- transformaciones de Markdown ----------
def filtrar_pestanas(texto: str, pista: str) -> str:
    """Conserva solo la pestaña `=== "Titulo"` cuyo título empieza con el nombre de la pista."""
    nombre = PISTAS[pista]
    lineas = texto.split("\n")
    salida: list[str] = []
    i = 0
    while i < len(lineas):
        if re.match(r'^=== ".+"\s*$', lineas[i]):
            elegido: list[str] = []
            while i < len(lineas) and re.match(r'^=== ".+"\s*$', lineas[i]):
                titulo = re.match(r'^=== "(.+)"\s*$', lineas[i]).group(1)
                i += 1
                bloque: list[str] = []
                while i < len(lineas) and (lineas[i].startswith("    ") or lineas[i].strip() == ""):
                    bloque.append(lineas[i][4:] if lineas[i].startswith("    ") else "")
                    i += 1
                while bloque and bloque[-1] == "":
                    bloque.pop()
                if titulo.startswith(nombre):
                    elegido = bloque
                # saltar líneas vacías entre pestañas contiguas
                j = i
                while j < len(lineas) and lineas[j].strip() == "":
                    j += 1
                if j < len(lineas) and re.match(r'^=== ".+"\s*$', lineas[j]):
                    i = j
            salida.extend(elegido)
            salida.append("")
        else:
            salida.append(lineas[i])
            i += 1
    return "\n".join(salida)


def convertir_avisos(texto: str) -> str:
    """`!!! tip "Titulo"` (o `??? tip`) + cuerpo con sangría -> cita de Markdown (se ve bien en GitHub)."""
    lineas = texto.split("\n")
    salida: list[str] = []
    i = 0
    while i < len(lineas):
        m = re.match(r'^(!!!|\?\?\?\+?) (\w+)(?: "(.*)")?\s*$', lineas[i])
        if not m:
            salida.append(lineas[i])
            i += 1
            continue
        marcador, tipo, titulo = m.group(1), m.group(2), m.group(3)
        i += 1
        cuerpo: list[str] = []
        while i < len(lineas) and (lineas[i].startswith("    ") or lineas[i].strip() == ""):
            cuerpo.append(lineas[i][4:] if lineas[i].startswith("    ") else "")
            i += 1
        while cuerpo and cuerpo[-1] == "":
            cuerpo.pop()
        encabezado = titulo or TIPO_AVISO.get(tipo, tipo.capitalize())
        if marcador.startswith("???"):  # desplegable: se conserva oculto con <details>
            salida.append(f"<details>\n<summary><b>{encabezado}</b></summary>\n")
            salida.extend(cuerpo)
            salida.append("\n</details>")
        else:
            salida.append(f"> **{encabezado}**")
            salida.append(">")
            salida.extend(("> " + c).rstrip() for c in cuerpo)
        salida.append("")
    return "\n".join(salida)


def limpiar_instructor(texto: str) -> str:
    texto = re.sub(r"\n---\n\n\*Soluci[^\n]*\*\n*$", "\n", texto)  # pie de solución en los ejercicios
    texto = re.sub(r"^Ejemplo( completo)? en `soluciones/[^`]*`\.\n\n", "", texto, flags=re.M)
    texto = re.sub(r" Ejemplo en `session-delivery-resources/[^`]*`\.", "", texto)
    texto = re.sub(
        r"Archivo de ejemplo en `session-delivery-resources/[^`]*`; se copia a `\.vscode/mcp\.json` para la demo\.",
        "El instructor lo agrega en `.vscode/mcp.json` para la demo.",
        texto,
    )
    return texto


def procesar_md(texto: str, pista: str, aplanado: bool) -> str:
    texto = texto.replace("\r\n", "\n")
    texto = filtrar_pestanas(texto, pista)
    texto = convertir_avisos(texto)
    texto = limpiar_instructor(texto)
    if aplanado:  # docs/ejercicios/<pista>/ejN.md -> docs/ejercicios/ejN.md
        texto = texto.replace("](../../modulos/", "](../modulos/").replace("](../../assets/", "](../assets/")
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.rstrip("\n") + "\n"


# ---------- copia ----------
def copiar_arbol(origen: Path, destino: Path) -> None:
    for item in origen.iterdir():
        if item.name in IGNORAR:
            continue
        objetivo = destino / item.name
        if item.is_dir():
            objetivo.mkdir(parents=True, exist_ok=True)
            copiar_arbol(item, objetivo)
        else:
            shutil.copy2(item, objetivo)


def escribir(ruta: Path, texto: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8", newline="\n")


def construir(pista: str, salida: Path, forzar: bool) -> None:
    origen = RAIZ / "pistas" / pista
    if not origen.is_dir():
        sys.exit(f"No existe la pista: {origen}")

    if salida.exists() and any(p.name != ".git" for p in salida.iterdir()):
        if not forzar:
            sys.exit(f"{salida} no está vacío. Usa --forzar para reemplazar su contenido (se conserva .git).")
        for p in salida.iterdir():
            if p.name == ".git":
                continue
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    salida.mkdir(parents=True, exist_ok=True)

    # 1. Código de la pista en la raíz (sin soluciones)
    copiar_arbol(origen, salida)
    for ruta in salida.rglob("*"):  # las rutas de docs cambian al aplanar
        if ruta.is_file() and ruta.suffix in TEXTO:
            texto = ruta.read_text(encoding="utf-8")
            nuevo = texto.replace(f"docs/ejercicios/{pista}/", "docs/ejercicios/")
            if nuevo != texto:
                escribir(ruta, nuevo)

    # 2. Documentación
    docs_src, docs_dst = RAIZ / "docs", salida / "docs"
    for carpeta in ("modulos",):
        for md in (docs_src / carpeta).glob("*.md"):
            escribir(docs_dst / carpeta / md.name, procesar_md(md.read_text(encoding="utf-8"), pista, False))
    for nombre in ("index.md", "agenda.md", "requisitos.md", "recursos.md", "pistas.md"):
        escribir(docs_dst / nombre, procesar_md((docs_src / nombre).read_text(encoding="utf-8"), pista, False))
    for md in (docs_src / "ejercicios" / pista).glob("*.md"):
        escribir(docs_dst / "ejercicios" / md.name, procesar_md(md.read_text(encoding="utf-8"), pista, True))
    shutil.copytree(docs_src / "assets", docs_dst / "assets")

    # 3. Plantillas de la pista (README, entorno, CI) y archivos comunes
    copiar_arbol(RAIZ / "scripts" / "plantillas" / pista, salida)
    for comun in ("LICENSE", "SECURITY.md", "SUPPORT.md"):
        shutil.copy2(RAIZ / comun, salida / comun)

    # 4. Verificación: nada del instructor debe haberse colado
    problemas = []
    for ruta in salida.rglob("*"):
        if ruta.is_file() and ruta.suffix in TEXTO and ".git" not in ruta.parts:
            texto = ruta.read_text(encoding="utf-8", errors="ignore")
            for palabra in PROHIBIDO:
                if palabra in texto:
                    problemas.append(f"{ruta.relative_to(salida)}: contiene '{palabra}'")
    if (salida / "soluciones").exists() or (salida / "session-delivery-resources").exists():
        problemas.append("quedó una carpeta del instructor")
    if problemas:
        print("Referencias al instructor que no se pudieron limpiar:", *problemas, sep="\n  - ")
        sys.exit(1)

    archivos = sum(1 for p in salida.rglob("*") if p.is_file() and ".git" not in p.parts)
    print(f"Repo de alumnos ({PISTAS[pista]}) generado en {salida}: {archivos} archivos")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pista", required=True, choices=sorted(PISTAS))
    ap.add_argument("--salida", required=True, type=Path)
    ap.add_argument("--forzar", action="store_true", help="reemplaza el contenido de la carpeta de salida (conserva .git)")
    args = ap.parse_args()
    construir(args.pista, args.salida.resolve(), args.forzar)


if __name__ == "__main__":
    main()
