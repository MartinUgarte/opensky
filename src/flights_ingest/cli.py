"""Entry point: orquesta configuración, consulta, transformación y escritura."""

import json
import logging
from datetime import UTC, datetime
from pathlib import Path

from flights_ingest.client import fetch_states, parse_bbox
from flights_ingest.config import load_settings
from flights_ingest.decorators import timed
from flights_ingest.transform import Vuelo, filtrar

logger = logging.getLogger(__name__)


@timed
def escribir_json(vuelos: list[Vuelo], output_dir: str) -> Path:
    """Escribe los vuelos en un JSON nuevo, con timestamp en el nombre.

    Args:
        vuelos: Vuelos a escribir.
        output_dir: Carpeta de destino; se crea si no existe.

    Returns:
        La ruta del archivo escrito.
    """
    destino = Path(output_dir)
    destino.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    path = destino / f"vuelos_{ts}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(vuelos, f, ensure_ascii=False, indent=2)
    return path


def main() -> None:
    """Corre el pipeline completo: consulta, filtra y escribe."""
    settings = load_settings()
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    states = fetch_states(settings.base_url, parse_bbox(settings.bbox))
    if states is None:
        logger.warning("La API no devolvió estados para el bbox %s", settings.bbox)
        states = []
    vuelos = filtrar(states, settings.pais)
    path = escribir_json(vuelos, settings.output_dir)
    logger.info("Escribí %d vuelos en %s", len(vuelos), path)
