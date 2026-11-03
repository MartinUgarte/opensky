import os
from dataclasses import dataclass

from dotenv import load_dotenv

DEFAULT_URL = "https://opensky-network.org/api"
DEFAULT_BBOX = "-35.0,-59.0,-34.0,-58.0"  # lamin,lomin,lamax,lomax: Buenos Aires


@dataclass(frozen=True)
class Settings:
    base_url: str
    bbox: str
    pais: str
    output_dir: str
    log_level: str


def load_settings():
    load_dotenv()  # lee .env si existe
    return Settings(
        base_url=os.getenv("OPENSKY_URL", DEFAULT_URL),
        bbox=os.getenv("BBOX", DEFAULT_BBOX),
        pais=os.getenv("PAIS", "Argentina"),
        output_dir=os.getenv("OUTPUT_DIR", "data/bronze"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
