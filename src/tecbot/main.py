"""Entrypoint de TecBot Académico.

Por ahora expone un modo consola para probar el núcleo sin conectar un canal
de mensajería. El adaptador del canal debe construirse sobre ``BotHandlers``.
"""

from __future__ import annotations

import logging
import sys

from tecbot.bot.handlers import BotHandlers
from tecbot.config import Settings
from tecbot.services.academic import AcademicService

EXIT_WORDS = {"salir", "exit", "quit"}


def build_handlers(settings: Settings) -> BotHandlers:
    """Construye los handlers con sus dependencias."""
    return BotHandlers(AcademicService())


def run_cli(handlers: BotHandlers) -> None:
    """Bucle de consola: lee preguntas y escribe respuestas."""
    print("TecBot Académico (modo consola). Escribe 'salir' para terminar.")
    for line in sys.stdin:
        text = line.strip()
        if text.lower() in EXIT_WORDS:
            break
        if text:
            print(handlers.handle(text))


def main() -> None:
    settings = Settings.from_env()
    logging.basicConfig(level=settings.log_level)
    run_cli(build_handlers(settings))


if __name__ == "__main__":
    main()
