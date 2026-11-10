"""Handlers agnósticos del canal: texto de entrada -> texto de salida."""

from __future__ import annotations

from tecbot.bot.commands import HELP_TEXT
from tecbot.services.academic import AcademicService

WELCOME_TEXT = (
    "Hola, soy TecBot Académico. Pregúntame sobre trámites, materias o servicios."
)

START_COMMANDS = {"/start", "/ayuda", "/help"}


class BotHandlers:
    """Punto único de entrada para los mensajes del usuario."""

    def __init__(self, academic: AcademicService) -> None:
        self._academic = academic

    def handle(self, text: str) -> str:
        normalized = text.strip().lower()
        if normalized in START_COMMANDS:
            return f"{WELCOME_TEXT}\n\n{HELP_TEXT}"
        return self._academic.answer(text)
