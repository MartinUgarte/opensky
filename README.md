# flights-ingest

Proyecto de la Clase 3 (Python para Data Engineering) de la Diplomatura en Cloud Data Engineering, ITBA.

Arrancamos con `script.py`: un script de ingesta que consulta la API de OpenSky y guarda los vuelos
sobre Buenos Aires en un JSON. Durante la clase lo vamos a ir convirtiendo en un proyecto profesional.

## Etapas

Cada etapa es una rama. Se puede saltar a la siguiente con `git checkout <rama>`.

| Rama | Etapa |
|---|---|
| `01-script` | El script inicial |
| `02-uv` | Proyecto uv con dependencias declaradas y lockfile |
| `03-estructura` | Paquete en `src/`, módulos separados y configuración en `.env` |
| `04-typing` | Type hints, TypedDict y docstrings estilo Google; mypy sin errores |
| `05-logging` | Logging configurable y decoradores `@timed` y `@retry` |
| `06-bug-hunt` | La etapa 05 con tres bugs plantados, para cazar con el debugger |
| `main` | La solución final, con un primer test (adelanto de la clase 4) |

## Requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- VS Code con la extensión de Python (recomendado)
