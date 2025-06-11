import csv
from pathlib import Path

CSV_FILE = Path("encounters.csv")
CSV_COLUMNS = [
    "fecha_hora",
    "especie",
    "género",
    "nivel",
    "naturaleza",
    "habilidad",
    "hp",
    "atk",
    "def",
    "spatk",
    "spdef",
    "spd",
    "shiny_value",
    "es_shiny",
    "atrapado",
]


def registrar_encuentro(data: dict) -> None:
    """Append an encounter entry to encounters.csv."""
    write_header = not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerow(data)
