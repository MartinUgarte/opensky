"""Configuración del pipeline, leída de variables de entorno."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

DEFAULT_URL = "https://opensky-network.org/api"
DEFAULT_BBOX = "-35.0,-59.0,-34.0,-58.0"  # lamin,lomin,lamax,lomax: Buenos Aires


@dataclass(frozen=True)
class Settings:
    """Configuración inmutable de una corrida.

    Attributes:
        base_url: URL base de la API de OpenSky.
        bbox: Bounding box como "lamin,lomin,lamax,lomax".
        pais: País de origen de los vuelos a conservar.
        output_dir: Carpeta donde se escriben los JSON.
        log_level: Nivel mínimo de logging.
    """

    base_url: str
    bbox: str
    pais: str
    output_dir: str
    log_level: str


def load_settings() -> Settings:
    """Lee la configuración del entorno, cargando el archivo .env si existe.

    Returns:
        La configuración de la corrida, con defaults para lo que no esté definido.
    """
    load_dotenv()
    return Settings(
        base_url=os.getenv("OPENSKY_URL", DEFAULT_URL),
        bbox=os.getenv("BBOX", DEFAULT_BBOX),
        pais=os.getenv("PAIS", "Argentina"),
        output_dir=os.getenv("OUTPUT_DIR", "data/bronze"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
