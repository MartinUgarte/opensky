import json
from datetime import UTC, datetime
from pathlib import Path

from flights_ingest.client import fetch_states, parse_bbox
from flights_ingest.config import load_settings
from flights_ingest.transform import filtrar


def escribir_json(vuelos, output_dir):
    destino = Path(output_dir)
    destino.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    path = destino / f"vuelos_{ts}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(vuelos, f, ensure_ascii=False, indent=2)
    return path


def main():
    settings = load_settings()
    states = fetch_states(settings.base_url, parse_bbox(settings.bbox))
    vuelos = filtrar(states, settings.pais)
    path = escribir_json(vuelos, settings.output_dir)
    print("Escribí", len(vuelos), "vuelos en", path)
