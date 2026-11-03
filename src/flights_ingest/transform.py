# Índices del vector de estado, según la documentación de OpenSky.
ICAO24 = 0
CALLSIGN = 1
ORIGIN_COUNTRY = 2


def filtrar(states, pais):
    vuelos = []
    for s in states:
        if s[ORIGIN_COUNTRY] == pais:
            vuelos.append(
                {
                    "icao24": s[ICAO24],
                    "callsign": s[CALLSIGN].strip(),
                    "pais": s[ORIGIN_COUNTRY],
                }
            )
    return vuelos
