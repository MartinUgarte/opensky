"""Cliente de la API de OpenSky: todo el I/O de red vive acá."""

from typing import Any

import requests

BBox = dict[str, float]


def parse_bbox(raw: str) -> BBox:
    """Convierte un bounding box en texto a los parámetros que espera la API.

    Args:
        raw: Bounding box como "lamin,lomin,lamax,lomax".

    Returns:
        Diccionario con las claves lamin, lomin, lamax y lomax.

    Raises:
        ValueError: Si el texto no tiene cuatro números separados por comas.
    """
    lamin, lomin, lamax, lomax = (float(x) for x in raw.split(","))
    return {"lamin": lamin, "lomin": lomin, "lamax": lamax, "lomax": lomax}


def fetch_states(base_url: str, bbox: BBox) -> list[list[Any]] | None:
    """Consulta los vectores de estado de los aviones dentro de un bounding box.

    Args:
        base_url: URL base de la API de OpenSky.
        bbox: Bounding box en el formato de parse_bbox.

    Returns:
        Los vectores de estado crudos, o None si no hay vuelos en el área.

    Raises:
        requests.HTTPError: Si la API responde con un error.
    """
    resp = requests.get(f"{base_url}/states/all", params=bbox, timeout=10)
    resp.raise_for_status()
    states: list[list[Any]] | None = resp.json()["states"]
    return states
