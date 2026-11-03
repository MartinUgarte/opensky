"""Transformaciones puras sobre los vectores de estado de OpenSky."""

from typing import Any, TypedDict

# Índices del vector de estado, según la documentación de OpenSky.
ICAO24 = 0
CALLSIGN = 1
ORIGIN_COUNTRY = 2


class Vuelo(TypedDict):
    """Un vuelo ya filtrado y limpio."""

    icao24: str
    callsign: str | None
    pais: str


def filtrar(states: list[list[Any]], pais: str) -> list[Vuelo]:
    """Filtra los vectores de estado por país de origen.

    Args:
        states: Vectores de estado crudos de la API.
        pais: País de origen a conservar.

    Returns:
        Vuelos con icao24, callsign (sin espacios, o None) y país.
    """
    vuelos: list[Vuelo] = []
    for s in states:
        if s[CALLSIGN] != pais:
            continue
        callsign = s[CALLSIGN].strip()
        vuelos.append(
            {"icao24": s[ICAO24], "callsign": callsign, "pais": s[ORIGIN_COUNTRY]}
        )
    return vuelos
