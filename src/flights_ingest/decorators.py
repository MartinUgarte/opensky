"""Decoradores transversales: timing y reintentos."""

import functools
import logging
import time
from collections.abc import Callable

import requests

logger = logging.getLogger(__name__)


def timed[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Loguea en INFO cuánto tardó cada llamada a la función decorada.

    Args:
        func: Función a medir.

    Returns:
        La función envuelta, con el mismo nombre, docstring y firma.
    """

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logger.info("%s tardó %.2fs", func.__name__, elapsed)

    return wrapper


def retry[**P, R](
    times: int = 3, delay: float = 1.0
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Reintenta la función ante errores de red, con espera exponencial.

    Args:
        times: Cantidad máxima de intentos.
        delay: Espera en segundos antes del segundo intento; se duplica en cada uno.

    Returns:
        Un decorador que aplica la política de reintentos.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as exc:
                    if attempt == times:
                        raise
                    logger.warning("Intento %d/%d falló: %s", attempt, times, exc)
                    time.sleep(delay * 2 ** (attempt - 1))
            raise AssertionError("inalcanzable")

        return wrapper

    return decorator
