"""Genera la presentación Derevo del curso, una por pista.

Requiere el skill derevo-presentation (plantilla y constructor) y python-pptx:

    pip install python-pptx
    set DEREVO_SKILL_DIR=<ruta a la carpeta del skill derevo-presentation>
    python presentacion/build_deck.py --pista python
    python presentacion/build_deck.py --pista javascript

La salida queda en presentacion/salida/ (ignorada por git: cada archivo pesa unos 18 MB).
"""
import argparse
import os
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--pista", required=True, choices=["python", "javascript"])
ARGS = ap.parse_args()
PISTA = ARGS.pista

SKILL = os.environ.get("DEREVO_SKILL_DIR")
if not SKILL or not os.path.isdir(SKILL):
    sys.exit("Define DEREVO_SKILL_DIR con la carpeta del skill derevo-presentation.")
sys.path.insert(0, os.path.join(SKILL, "src"))
from derevo_builder import assemble_deck  # noqa: E402

OUT_DIR = str(Path(__file__).resolve().parent / "salida")
os.makedirs(OUT_DIR, exist_ok=True)


def beat(label, headline, icon, items):
    return {"label": label, "headline": headline, "icon": icon,
            "items": [{"icon": i, "text": t} if i else {"text": t} for i, t in items]}


content = [
    # ---------- Apertura ----------
    {"type": "story", "pattern_hint": "journey",
     "title": "Agenda del día: de un Tab al agente.",
     "subtitle": "Cinco bloques, cada uno con práctica guiada.",
     "beats": [
         beat("09:00", "Base", "bolt",
              [(None, "Fundamentos"), (None, "Autocompletado"), (None, "Ejercicio 1")]),
         beat("11:10", "Chat", "brain",
              [(None, "Modos y contexto"), (None, "Prompting"), (None, "Ejercicio 2")]),
         beat("13:25", "Código", "target",
              [(None, "Código legacy"), (None, "Corregir bugs"), (None, "Ejercicio 3")]),
         beat("14:05", "Agent", "settings",
              [(None, "Plan y diffs"), (None, "Pruebas en verde"), (None, "Ejercicio 4")]),
         beat("15:40", "Imagen", "layers",
              [(None, "Mockup a página"), (None, "Cloud agent, MCP"), (None, "Ejercicio 5")]),
     ],
     "cta": "Práctica total: 3 h 45 min. Todo el material está en el repositorio del curso."},
    {"type": "big_number",
     "title": "Un día, mucha práctica.",
     "subtitle": "Más manos al teclado que diapositivas.",
     "stats": [
         {"value": "10", "label": "módulos", "description": "del autocompletado al cloud agent"},
         {"value": "5", "label": "ejercicios", "description": "en Python y Flask"},
         {"value": "3 h 45", "label": "de práctica", "description": "guiada por el instructor"},
     ]},

    # ---------- 1. Fundamentos ----------
    {"type": "story",
     "title": "Copilot vive en el IDE, en github.com y en la CLI.",
     "subtitle": "Hoy trabajaremos casi todo el tiempo en VS Code.",
     "beats": [
         beat("IDE", "Tu editor", "bolt",
              [("check", "Autocompletado"), ("brain", "Chat y modo Agent"), ("settings", "Ediciones multi-archivo")]),
         beat("GITHUB.COM", "En la plataforma", "users",
              [("target", "Chat web"), ("layers", "Cloud agent sobre issues"), ("circle_check", "Code review en PR")]),
         beat("CLI", "En la terminal", "settings",
              [("question", "Preguntas rápidas"), ("bolt", "Tareas desde la línea de comandos"),
               ("arrow_right", "Delegar al cloud agent")]),
     ]},
    {"type": "story", "pattern_hint": "comparison",
     "title": "Qué consume créditos y qué no.",
     "subtitle": "Las cuotas cambian: verifica tu plan en la página oficial.",
     "beats": [
         beat("COMPLETIONS", "Sugerencias mientras escribes", "bolt",
              [("check", "Ghost text y NES"), ("circle_check", "Normalmente sin consumo premium en planes de pago"),
               ("clock", "Se usan todo el día")]),
         beat("CHAT Y AGENTES", "Cada interacción cuenta", "alert",
              [("alert", "Los modelos potentes pueden contar más"), ("layers", "El cloud agent consume por tarea"),
               ("target", "Elige el modo y el modelo según la tarea")]),
     ],
     "cta": "Revisa tu medidor en github.com/settings/copilot."},
    {"type": "quote",
     "title": "La regla de oro del curso.",
     "quote": "Si no puedes explicar lo que hace una sugerencia, no la aceptes.",
     "author": "Copilot propone, tú decides",
     "author_role": "Tú eres el autor del código",
     "cta": "No pegues código, datos ni credenciales de clientes en el chat."},

    # ---------- 2. Autocompletado ----------
    {"type": "process_flow",
     "title": "Cuatro teclas para dominar el ghost text.",
     "subtitle": "En macOS cambia Ctrl por Cmd y Alt por Option.",
     "steps": [
         {"headline": "Tab", "description": "Aceptar la sugerencia", "icon": "check"},
         {"headline": "Esc", "description": "Descartarla", "icon": "x"},
         {"headline": "Alt + ]", "description": "Siguiente alternativa (Alt + [ la anterior)", "icon": "arrow_right"},
         {"headline": "Ctrl + Der.", "description": "Aceptar solo una palabra", "icon": "bolt"},
     ]},
    {"type": "story",
     "title": "Tres técnicas de autocompletado.",
     "subtitle": "Cada una se practica con un ejercicio aislado de 10 minutos.",
     "beats": [
         beat("TRAMO A", "Ghost text", "bolt",
              [("check", "Escribe la firma"), ("check", "Acepta, descarta o edita"), ("alert", "Prueba casos raros")]),
         beat("TRAMO B", "Por comentarios", "brain",
              [("target", "Comentario preciso"), ("arrow_right", "Copilot propone el cómo"),
               ("check", "Si falla, mejora el comentario")]),
         beat("TRAMO C", "Next Edit (NES)", "layers",
              [("arrow_right", "Predice tu siguiente cambio"), ("layers", "Ideal para refactors en cascada"),
               ("alert", "Revisa cada edición")]),
     ]},
    {"type": "timeline",
     "title": "Ejercicio 1: construye un inventario con Tab.",
     "subtitle": "Sin chat: solo autocompletado, comentarios y NES.",
     "phases": [
         {"number": "A", "title": "Ghost text", "duration": "10 min",
          "items": ["Cuatro funciones", "Anota lo que rechazas"]},
         {"number": "B", "title": "Comentarios", "duration": "10 min",
          "items": ["Filtrar y ordenar", "Mejora el comentario"]},
         {"number": "C", "title": "NES", "duration": "10 min",
          "items": ["Renombra un campo", "Busca lo que NES no vio"]},
         {"number": "50", "title": "Inventario", "duration": "50 min",
          "items": ["Clase completa", "6 pruebas en verde"]},
     ]},

    # ---------- 3. Chat ----------
    {"type": "story", "pattern_hint": "comparison",
     "title": "Chat en panel o inline chat.",
     "subtitle": "La misma IA, dos formas de usarla.",
     "beats": [
         beat("PANEL", "Conversaciones amplias", "users",
              [("question", "Preguntas de diseño"), ("layers", "Varios archivos"), ("clock", "Diálogo largo")]),
         beat("INLINE (CTRL+I)", "Cambios puntuales", "bolt",
              [("target", "Sobre una selección"), ("check", "Diff directo en el editor"),
               ("arrow_right", "Rápido y acotado")]),
     ]},
    {"type": "story",
     "title": "Ask entiende, Plan decide, Agent ejecuta.",
     "subtitle": "Elige el modo según el riesgo de la tarea.",
     "beats": [
         beat("ASK", "Solo responde", "question",
              [("brain", "Entender y explorar"), ("check", "Cero riesgo para tus archivos")]),
         beat("PLAN", "Propone primero", "target",
              [("layers", "Plan paso a paso"), ("circle_check", "Lo revisas y ajustas")]),
         beat("AGENT", "Edita y ejecuta", "settings",
              [("bolt", "Varios archivos y terminal"), ("alert", "Con tu aprobación")]),
     ]},
    {"type": "process_flow",
     "title": "Slash commands que usarás todo el día.",
     "subtitle": "Selecciona el código primero.",
     "steps": [
         {"headline": "/explain", "description": "Explica el código seleccionado", "icon": "brain"},
         {"headline": "/fix", "description": "Propone una corrección", "icon": "settings"},
         {"headline": "/tests", "description": "Genera pruebas", "icon": "check"},
         {"headline": "/doc", "description": "Documenta el código", "icon": "layers"},
     ]},

    # ---------- 4. Contextualización ----------
    {"type": "process_flow",
     "title": "Variables de contexto para Copilot.",
     "subtitle": "Menos contexto y más relevante supera a mucho y desordenado.",
     "steps": [
         {"headline": "#file", "description": "Un archivo específico", "icon": "layers"},
         {"headline": "#selection", "description": "El texto seleccionado", "icon": "target"},
         {"headline": "#codebase", "description": "Búsqueda en todo el proyecto", "icon": "database"},
     ]},
    {"type": "story", "pattern_hint": "comparison",
     "title": "Reglas del proyecto y prompts reutilizables.",
     "subtitle": "Dos archivos que convierten buenas prácticas en hábito.",
     "beats": [
         beat("SIEMPRE ACTIVAS", "copilot-instructions.md", "settings",
              [("check", "Se aplica a todo el proyecto"), ("target", "Reglas cortas y verificables"),
               ("x", "Evita 'escribe buen código'")]),
         beat("BAJO DEMANDA", "Archivos .prompt.md", "bolt",
              [("arrow_right", "Se invocan con /nombre"), ("layers", "Tareas repetibles del equipo"),
               ("check", "Ej.: revisar un endpoint")]),
     ],
     "cta": "Ruta: .github/copilot-instructions.md y .github/prompts/"},

    # ---------- 5. Prompting ----------
    {"type": "process_flow",
     "title": "Anatomía de un buen prompt.",
     "subtitle": "Cuatro piezas que eliminan las adivinanzas.",
     "steps": [
         {"label": "1", "headline": "Contexto", "description": "¿Dónde estamos?", "icon": "database"},
         {"label": "2", "headline": "Intención", "description": "¿Qué quiero lograr?", "icon": "target"},
         {"label": "3", "headline": "Restricciones", "description": "¿Qué límites hay?", "icon": "alert"},
         {"label": "4", "headline": "Ejemplo", "description": "¿Cómo se ve lo correcto?", "icon": "check"},
     ]},
    {"type": "story", "pattern_hint": "comparison",
     "title": "Del prompt vago al prompt que funciona.",
     "subtitle": "Mismo objetivo, resultados muy distintos.",
     "beats": [
         beat("ANTES", "hazme validaciones", "x",
              [("question", "El modelo adivina"), ("alert", "Cambios impredecibles")]),
         beat("DESPUÉS", "Validación precisa de POST", "circle_check",
              [("target", "Campos y rangos definidos"), ("alert", "Responde 400 con el motivo"),
               ("x", "Sin dependencias nuevas")]),
     ]},
    {"type": "story",
     "title": "Antipatrones y cómo corregirlos.",
     "subtitle": "Acota el alcance e itera en lugar de empezar de cero.",
     "beats": [
         beat("VAGO", "Sin contexto", "question",
              [("arrow_right", "Agrega contexto, intención y restricciones")]),
         beat("TODO JUNTO", "Cambios enormes", "layers",
              [("arrow_right", "Divide en pasos pequeños y revisables")]),
         beat("SIN LÍMITES", "Alcance abierto", "alert",
              [("arrow_right", "Di qué archivos sí y cuáles no")]),
     ],
     "cta": "Si casi sirve: señala lo que está bien y corrige solo lo que falla."},
    {"type": "timeline",
     "title": "Ejercicio 2: configura tu copiloto.",
     "subtitle": "Treinta minutos entre chat, contexto y prompting.",
     "phases": [
         {"number": "01", "title": "Chat y modelos", "duration": "8 min",
          "items": ["Inline y slash", "Compara modelos"]},
         {"number": "02", "title": "Contexto", "duration": "10 min",
          "items": ["copilot-instructions.md", "Un prompt file propio"]},
         {"number": "03", "title": "Prompts", "duration": "12 min",
          "items": ["Reescríbelo completo", "Itera sin reiniciar"]},
     ]},

    # ---------- 6. Comprensión y corrección ----------
    {"type": "process_flow",
     "title": "Cómo entender código que no escribiste.",
     "subtitle": "De lo general a lo particular, y siempre verificando.",
     "steps": [
         {"label": "1", "headline": "Panorama", "description": "Resume entradas y salidas", "icon": "layers"},
         {"label": "2", "headline": "Detalle", "description": "/explain por bloques", "icon": "brain"},
         {"label": "3", "headline": "Dependencias", "description": "#codebase: ¿quién lo llama?", "icon": "database"},
         {"label": "4", "headline": "Verificar", "description": "Ejecuta y compara", "icon": "check"},
     ]},
    {"type": "timeline",
     "title": "Ejercicio 3: rescata el script legacy.",
     "subtitle": "Tres bugs, y alguno no lanza error.",
     "phases": [
         {"number": "01", "title": "Entender", "duration": "10 min",
          "items": ["Sin leer el código antes", "Explicación con tus palabras"]},
         {"number": "02", "title": "Corregir", "duration": "15 min",
          "items": ["Pide la causa primero", "Verifica a mano los totales"]},
         {"number": "03", "title": "Refactor", "duration": "5 min",
          "items": ["Nombres descriptivos", "Mismo resultado"]},
     ]},

    # ---------- 7. Agent mode ----------
    {"type": "process_flow",
     "title": "Agent mode: tú sigues al mando.",
     "subtitle": "Un ciclo corto, con revisión humana en cada paso.",
     "steps": [
         {"label": "1", "headline": "Planear", "description": "Modo Plan y ajustes", "icon": "target"},
         {"label": "2", "headline": "Ejecutar", "description": "Aprueba cada comando", "icon": "bolt"},
         {"label": "3", "headline": "Revisar", "description": "Diff por archivo", "icon": "layers"},
         {"label": "4", "headline": "Deshacer", "description": "Undo o checkpoint", "icon": "clock"},
     ]},
    {"type": "story", "pattern_hint": "comparison",
     "title": "Limita el alcance antes de ejecutar.",
     "subtitle": "El alcance lo defines tú, de forma explícita.",
     "beats": [
         beat("SIN LÍMITES", "El agente decide", "x",
              [("alert", "Toca archivos que no esperabas"), ("question", "Diffs difíciles de revisar")]),
         beat("CON ALCANCE", "Tú decides", "circle_check",
              [("check", "Solo modifica app.py y crea descuentos.py"), ("x", "No cambies las pruebas existentes"),
               ("target", "Haz commit antes de empezar")]),
     ],
     "cta": "Si se desvía, detén la sesión y reformula."},

    # ---------- 8. Pruebas ----------
    {"type": "process_flow",
     "title": "Pruebas en verde, sin trampas.",
     "subtitle": "Pytest es nuestro equivalente a Jest.",
     "steps": [
         {"label": "1", "headline": "/tests", "description": "Genera y lee las pruebas", "icon": "check"},
         {"label": "2", "headline": "Ejecutar", "description": "Itera hasta el verde", "icon": "bolt"},
         {"label": "3", "headline": "Casos borde", "description": "Límites, inválidos, fechas", "icon": "alert"},
         {"label": "4", "headline": "Mutación", "description": "Rompe el código a propósito", "icon": "target"},
     ]},
    {"type": "big_number",
     "title": "La cobertura mide líneas, no calidad.",
     "subtitle": "Una prueba sin assert da 100% y no verifica nada.",
     "stats": [
         {"value": "85", "unit": "%", "label": "cobertura mínima",
          "description": "en descuentos.py, y además la prueba de mutación debe fallar"},
     ]},
    {"type": "timeline",
     "title": "Ejercicio 4: descuentos con el agente.",
     "subtitle": "Plan, ejecución controlada y pruebas en verde.",
     "phases": [
         {"number": "01", "title": "Planear", "duration": "10 min",
          "items": ["Modo Plan con las reglas", "Ajusta antes de ejecutar"]},
         {"number": "02", "title": "Agent", "duration": "20 min",
          "items": ["Lee cada comando", "Prueba Undo y checkpoint"]},
         {"number": "03", "title": "Pruebas", "duration": "25 min",
          "items": ["/tests y casos borde", "Cobertura y mutación"]},
     ]},

    # ---------- 9. Imagen a código ----------
    {"type": "process_flow",
     "title": "Del mockup a la página.",
     "subtitle": "Usa un modelo con visión y describe el comportamiento.",
     "steps": [
         {"label": "1", "headline": "Adjuntar", "description": "Arrastra el mockup al chat", "icon": "layers"},
         {"label": "2", "headline": "Describir", "description": "Datos, filtros, restricciones", "icon": "target"},
         {"label": "3", "headline": "Comparar", "description": "Anota 3 diferencias", "icon": "question"},
         {"label": "4", "headline": "Iterar", "description": "Correcciones concretas", "icon": "arrow_right"},
     ]},
    {"type": "timeline",
     "title": "Ejercicio 5: catálogo de FerreMax.",
     "subtitle": "Una página Flask que consume la API de productos.",
     "phases": [
         {"number": "01", "title": "Primera versión", "duration": "10 min",
          "items": ["Prompt completo", "Ruta /catalogo"]},
         {"number": "02", "title": "Iterar", "duration": "15 min",
          "items": ["Diferencias visuales", "Estado vacío o responsivo"]},
         {"number": "03", "title": "Revisión", "duration": "5 min",
          "items": ["¿Escapa el HTML?", "Teclado y errores de API"]},
     ]},

    # ---------- 10. Más allá del IDE ----------
    {"type": "process_flow",
     "title": "Cloud agent: de un issue a un Pull Request.",
     "subtitle": "Demo del instructor.",
     "steps": [
         {"label": "1", "headline": "Issue claro", "description": "Contexto y criterios", "icon": "target"},
         {"label": "2", "headline": "Asignar", "description": "A Copilot", "icon": "users"},
         {"label": "3", "headline": "Pull Request", "description": "Rama, código y pruebas", "icon": "layers"},
         {"label": "4", "headline": "Revisar", "description": "@copilot para pedir ajustes", "icon": "check"},
     ]},
    {"type": "story",
     "title": "Code review y MCP: más alcance, misma revisión.",
     "subtitle": "Más alcance, con las mismas reglas de revisión humana.",
     "beats": [
         beat("CLOUD AGENT", "Issue claro, PR útil", "layers",
              [("clock", "Tarda varios minutos"), ("dollar", "Consume solicitudes premium")]),
         beat("CODE REVIEW", "Primera revisión", "circle_check",
              [("check", "Detecta bugs y riesgos"), ("users", "No sustituye a una persona")]),
         beat("MCP", "Conecta servicios", "database",
              [("bolt", "Documentación, datos, servicios"), ("alert", "Instala solo fuentes de confianza")]),
     ]},

    {"type": "process_flow",
     "title": "Opcional: revisa un PR con ojo crítico.",
     "subtitle": "OPCIONAL · 20 min · fuera de la agenda. Para quien termine antes o quiera practicar después.",
     "steps": [
         {"label": "1", "headline": "Revisa tú", "description": "Lee, ejecuta y anota hallazgos", "icon": "target"},
         {"label": "2", "headline": "Compara", "description": "Pide la revisión a Copilot", "icon": "brain"},
         {"label": "3", "headline": "Decide", "description": "Aprobar o pedir cambios", "icon": "circle_check"},
     ],
     "cta": "\u00bfLas pruebas est\u00e1n en verde? Compru\u00e9balo: no todas las pruebas protegen algo."},

    # ---------- Cierre ----------
    {"type": "story",
     "title": "Tres ideas para llevarte.",
     "subtitle": "Lo que hace la diferencia entre usar Copilot y usarlo bien.",
     "beats": [
         beat("REVISA", "Tú eres el autor", "circle_check",
              [("check", "Lee antes de aceptar"), ("check", "Ejecuta y prueba")]),
         beat("ACOTA", "Alcance explícito", "target",
              [("check", "Contexto, intención y restricciones"), ("check", "Pasos pequeños")]),
         beat("ITERA", "Mejora, no reinicies", "arrow_right",
              [("check", "Señala qué está bien y qué falla"), ("check", "Pide la causa, no solo el parche")]),
     ]},
]

# Textos que cambian según la pista (el resto del deck es común)
TEXTOS_JS = {
    "Pytest es nuestro equivalente a Jest.": "Jest para la API y React Testing Library para los componentes.",
    "en descuentos.py, y además la prueba de mutación debe fallar": "en descuentos.js, y además la prueba de mutación debe fallar",
    "Del mockup a la página.": "Del mockup al componente.",
    "Ejercicio 5: catálogo de FerreMax.": "Ejercicio 5: catálogo en React.",
    "Una página Flask que consume la API de productos.": "Un componente React que consume la API de productos.",
    "Ruta /catalogo": "Componente Catalogo",
    "¿Escapa el HTML?": "¿Pinta con JSX?",
}


def aplicar_textos(obj, reemplazos):
    if isinstance(obj, str):
        return reemplazos.get(obj, obj)
    if isinstance(obj, list):
        return [aplicar_textos(x, reemplazos) for x in obj]
    if isinstance(obj, dict):
        return {k: aplicar_textos(v, reemplazos) for k, v in obj.items()}
    return obj


if PISTA == "javascript":
    content = aplicar_textos(content, TEXTOS_JS)

PISTA_TXT = "Pista Python" if PISTA == "python" else "Pista JavaScript y React"
REPO = "copilot-fundamentos-alumnos-python" if PISTA == "python" else "copilot-fundamentos-alumnos-react"

brief = {
    "project_cover": {
        "project_title": "GitHub Copilot: Fundamentos",
        "eyebrow": f"Curso de 1 día · {PISTA_TXT}",
        "subtitle": "Autocompletado · Chat · Agent mode · Pruebas · Cloud agent",
        "deck_date": "Octubre 2026",
        "owner": "Derevo · Capacitación",
        "theme": "dark",
    },
    "content_slides": content,
    "closing": {
        "type": "pill_band",
        "title": "Gracias. Ahora, a practicar.",
        "subtitle": "Material y ejercicios",
        "body": "Cada ejercicio tiene su carpeta en el repositorio del curso.\nRevisa, acota e itera: Copilot propone, tú decides.",
        "cta": f"Repositorio del curso: {REPO}",
        "cta_color": "dark",
    },
}

assemble_deck(
    template_path=os.path.join(SKILL, "template", "Derevo_Master_Template.pptx"),
    output_path=os.path.join(OUT_DIR, f"Copilot_Fundamentos_Derevo_{PISTA}.pptx"),
    brief=brief,
)
