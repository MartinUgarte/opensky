"""Primeros tests de la lógica pura. Los vemos en detalle en la clase 4."""

from flights_ingest.transform import filtrar

STATES = [
    ["e8044e", "ARG1234 ", "Argentina"],
    ["a1b2c3", None, "Argentina"],
    ["4ca123", "RYR99   ", "Ireland"],
]


def test_filtra_por_pais() -> None:
    vuelos = filtrar(STATES, "Argentina")
    assert [v["icao24"] for v in vuelos] == ["e8044e", "a1b2c3"]


def test_limpia_callsign_y_acepta_nulos() -> None:
    vuelos = filtrar(STATES, "Argentina")
    assert vuelos[0]["callsign"] == "ARG1234"
    assert vuelos[1]["callsign"] is None


def test_sin_estados_devuelve_lista_vacia() -> None:
    assert filtrar([], "Argentina") == []
