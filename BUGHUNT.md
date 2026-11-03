# Bug hunt

Esta rama tiene **tres bugs** plantados. Encontralos usando `breakpoint()`, `python -m pdb`
o el debugger de VS Code. **Regla: prohibido usar print.**

Para cada bug anotá: en qué línea está, qué valor tenía la variable cuando lo encontraste
y cómo lo arreglaste.

## Pistas

1. Corré `uv run flights-ingest` y mirá el log final. ¿Te parece razonable el número?
2. Cambiá el `BBOX` del `.env` a un rectángulo en el medio del océano, por ejemplo
   `BBOX=-50.0,-30.0,-49.0,-29.0`, y volvé a correr.
3. Uno de los bugs aparece recién cuando arreglás otro.

Bonus: ¿cuál de los tres hubiera atrapado `uv run mypy src/`?

## Para debuggear

    uv run python -m pdb -m flights_ingest   # post-mortem si explota

En VS Code: elegí el intérprete de `.venv` y usá la configuración "flights-ingest" de `.vscode/launch.json`.
