"""
analyze_project.py – Herramienta de análisis estático

Uso:
    python analyze_project.py

Genera:
    analysis_output/diagrams.puml
    analysis_output/project_report.md
    analysis_output/modification_guide.md
    analysis_output/examples/

Requisitos:
    - Python 3.8+
    - graphviz (opcional, para renderizar PUML)
    - PlantUML (opcional)
"""

import ast
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

OUTPUT_DIR = Path("analysis_output")
EXAMPLES_DIR = OUTPUT_DIR / "examples"

EXCLUDE_DIRS = {
    "venv",
    ".env",
    ".tox",
    "__pycache__",
    ".git",
    ".pytest_cache",
}


@dataclass
class FunctionInfo:
    name: str
    args: str
    doc: str = ""


@dataclass
class ClassInfo:
    name: str
    bases: List[str]
    doc: str = ""
    methods: List[FunctionInfo] = field(default_factory=list)


@dataclass
class ModuleInfo:
    path: Path
    imports: List[str] = field(default_factory=list)
    classes: List[ClassInfo] = field(default_factory=list)
    functions: List[FunctionInfo] = field(default_factory=list)


def scan_files(base_path: Path = Path(".")) -> List[Path]:
    """Return all .py files under base_path excluding EXCLUDE_DIRS."""
    py_files = []
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for fname in files:
            if fname.endswith('.py'):
                py_files.append(Path(root) / fname)
    return py_files


def _get_args(node: ast.FunctionDef) -> str:
    args = []
    for arg in node.args.args:
        args.append(arg.arg)
    if node.args.vararg:
        args.append('*' + node.args.vararg.arg)
    if node.args.kwarg:
        args.append('**' + node.args.kwarg.arg)
    defaults = [None] * (len(node.args.args) - len(node.args.defaults)) + node.args.defaults
    parts = []
    for name, default in zip(args, defaults):
        if default is not None:
            parts.append(f"{name}={ast.unparse(default)}")
        else:
            parts.append(name)
    return ', '.join(parts)


def parse_module(path: Path) -> ModuleInfo:
    """Parse a module and extract classes, functions and imports."""
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source, filename=str(path))

    module = ModuleInfo(path=path)
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module.imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                module.imports.append(node.module)
        elif isinstance(node, ast.ClassDef):
            bases = [ast.unparse(base) for base in node.bases]
            methods = []
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef) and not sub.name.startswith('_'):
                    methods.append(FunctionInfo(sub.name, _get_args(sub), ast.get_docstring(sub) or "Sin docstring"))
            module.classes.append(ClassInfo(node.name, bases, ast.get_docstring(node) or "Sin docstring", methods))
        elif isinstance(node, ast.FunctionDef):
            if not node.name.startswith('_'):
                module.functions.append(FunctionInfo(node.name, _get_args(node), ast.get_docstring(node) or "Sin docstring"))
    return module


def generate_plantuml(modules: List[ModuleInfo]) -> None:
    """Generate PlantUML diagrams."""
    lines: List[str] = []

    # Class Diagram
    lines.append("@startuml class_diagram")
    for mod in modules:
        package_name = mod.path.parent.as_posix().replace('/', '.')
        lines.append(f"package {package_name} {{")
        for cls in mod.classes:
            lines.append(f"  class {cls.name} {{")
            for method in cls.methods:
                lines.append(f"    +{method.name}()")
            lines.append("  }")
        lines.append("}")
    lines.append("@enduml\n")

    # Package Diagram
    lines.append("@startuml package_diagram")
    modules_map = {mod.path.with_suffix('').as_posix().replace('/', '.'): mod for mod in modules}
    for name in modules_map:
        lines.append(f"package {name} {{}}")
    for mod in modules:
        this_mod = mod.path.with_suffix('').as_posix().replace('/', '.')
        for imp in mod.imports:
            if imp in modules_map:
                lines.append(f"{this_mod} --> {imp}")
    lines.append("@enduml\n")

    # Sequence Diagram (simplified)
    lines.append("@startuml sequence_diagram")
    lines.append("actor User")
    lines.append("participant Bot")
    lines.append("participant Memory")
    lines.append("participant Decision")
    lines.append("User -> Bot: start()")
    lines.append("Bot -> Memory: read_stats()")
    lines.append("Memory --> Bot: stats")
    lines.append("Bot -> Decision: check_shiny()")
    lines.append("Decision --> Bot: result")
    lines.append("alt shiny")
    lines.append("Bot -> User: capture()")
    lines.append("else not shiny")
    lines.append("Bot -> Bot: reset()")
    lines.append("end")
    lines.append("@enduml")

    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(OUTPUT_DIR / "diagrams.puml", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_markdown_report(modules: List[ModuleInfo]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    md_lines = ["# Project Report", "", "## Introducción", "Este reporte fue generado por `analyze_project.py`. Ejecuta `python analyze_project.py` para regenerarlo.", "", "Se generaron los siguientes archivos:", "- `diagrams.puml`", "- `project_report.md`", "- `modification_guide.md`", "- carpeta `examples/`", ""]

    md_lines.append("## Índice")
    md_lines.extend([
        "- [Resumen por módulo](#resumen-por-módulo)",
        "- [Clases Principales](#clases-principales)",
        "- [Funciones Globales](#funciones-globales)",
        "- [Dependencias Externas](#dependencias-externas)",
    ])

    md_lines.append("\n## Resumen por módulo")
    for mod in modules:
        md_lines.append(f"### {mod.path}")
        md_lines.append(f"Clases: {len(mod.classes)} | Funciones: {len(mod.functions)}")
        md_lines.append("")

    md_lines.append("\n## Clases Principales")
    for mod in modules:
        for cls in mod.classes:
            md_lines.append(f"### {cls.name}")
            bases = ", ".join(cls.bases) if cls.bases else "object"
            md_lines.append(f"Firma: `class {cls.name}({bases})`")
            md_lines.append(f"Docstring: {cls.doc.splitlines()[0] if cls.doc else 'Sin docstring'}")
            md_lines.append("")

    md_lines.append("\n## Funciones Globales")
    for mod in modules:
        for func in mod.functions:
            md_lines.append(f"- `{func.name}({func.args})` – {func.doc.splitlines()[0] if func.doc else 'Sin docstring'}")
    md_lines.append("")

    md_lines.append("## Dependencias Externas")
    deps: Dict[str, None] = {}
    for mod in modules:
        for imp in mod.imports:
            if not imp.startswith('modules'):
                deps[imp.split('.')[0]] = None
    if deps:
        for dep in sorted(deps):
            md_lines.append(f"- {dep}")
    else:
        md_lines.append("- Ninguna")

    with open(OUTPUT_DIR / "project_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))


def write_modification_guide(modules: List[ModuleInfo]) -> None:
    lines = ["# Guía de Modificación", "", "## Loop Principal & Lectura de Stats", "El loop principal del bot se encuentra en `modules/main.py` dentro de la función `main_loop()`. Esta función gestiona los estados del juego y consulta `modules.memory.get_game_state()` y otras utilidades para leer la memoria.", "", "La información de cada encuentro Pokémon se registra en `modules/encounter.py`, especialmente en `handle_encounter()` y `log_encounter()`.", "", "## Ejemplo \"Pidgey encontrado\"", "Para añadir un log en consola cuando se encuentre un Pidgey modifica `modules/encounter.py` en la función `handle_encounter()`:", "```python", "if pokemon.species.name == 'Pidgey':", "    print(f'PIDGEY ENCONTRADO!! {pokemon.ivs}')", "```", "", "## Validación de Stats Personalizados", "Puedes implementar límites de IVs/EVs en `modules/pokemon.py` o donde se crean los objetos `Pokemon`. Revisa las clases `Pokemon` y valida los valores al instanciar.", "", "## Inyección de Botón GUI", "La interfaz gráfica se gestiona principalmente en `modules/gui`. Puedes añadir un botón nuevo en los archivos de la GUI y conectar su acción con la lógica de stats utilizando las funciones de `modules.stats`.", ""]
    with open(OUTPUT_DIR / "modification_guide.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_example_scripts() -> None:
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    (EXAMPLES_DIR / "log_stats_example.py").write_text(
        """from modules.encounter import handle_encounter\n\n# Ejemplo de logging\n# Llama a handle_encounter(...) y se imprimirá en consola\n""",
        encoding="utf-8",
    )
    (EXAMPLES_DIR / "filter_ivs_example.py").write_text(
        """def filter_pokemon(pokemon):\n    return pokemon.ivs.sum() > 150\n""",
        encoding="utf-8",
    )
    (EXAMPLES_DIR / "gui_button_example.py").write_text(
        """# Ejemplo de botón en GUI\n# Aquí iría la integración con la GUI existente\n""",
        encoding="utf-8",
    )


def main() -> None:
    print("Escaneando archivos...")
    py_files = scan_files(Path("."))
    print(f"Se encontraron {len(py_files)} archivos Python")
    modules = []
    for path in py_files:
        print(f"Analizando {path}...")
        modules.append(parse_module(path))
    print("Generando PlantUML...")
    generate_plantuml(modules)
    print("Escribiendo reporte Markdown...")
    write_markdown_report(modules)
    write_modification_guide(modules)
    write_example_scripts()
    print("Listo. Archivos generados en analysis_output/")


if __name__ == "__main__":
    main()
