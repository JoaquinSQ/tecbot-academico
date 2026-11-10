"""Servicio académico: responde consultas a partir del FAQ versionado."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "faq.json"

EMPTY_MESSAGE = "Escribe una pregunta sobre temas académicos."
FALLBACK_MESSAGE = (
    "No tengo una respuesta para eso todavía. Intenta con otra pregunta."
)


@dataclass(frozen=True)
class FaqEntry:
    question: str
    answer: str


class AcademicService:
    """Carga el FAQ y busca la respuesta más adecuada."""

    def __init__(self, data_file: Path | None = None) -> None:
        self._data_file = data_file or DATA_FILE
        self._entries = self._load()

    def _load(self) -> list[FaqEntry]:
        with self._data_file.open(encoding="utf-8") as file:
            raw = json.load(file)
        return [FaqEntry(**item) for item in raw]

    def answer(self, message: str) -> str:
        normalized = message.strip().lower()
        if not normalized:
            return EMPTY_MESSAGE

        for entry in self._entries:
            question = entry.question.lower()
            if normalized in question or question in normalized:
                return entry.answer

        return FALLBACK_MESSAGE
