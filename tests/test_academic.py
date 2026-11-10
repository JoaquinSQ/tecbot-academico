import json
from pathlib import Path

from tecbot.services.academic import FALLBACK_MESSAGE, AcademicService


def make_service(tmp_path: Path, entries: list[dict[str, str]]) -> AcademicService:
    data_file = tmp_path / "faq.json"
    data_file.write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    return AcademicService(data_file)


def test_answer_matches_question(tmp_path: Path) -> None:
    service = make_service(
        tmp_path,
        [{"question": "¿Cómo me inscribo?", "answer": "En el portal."}],
    )

    assert service.answer("¿cómo me inscribo?") == "En el portal."


def test_answer_returns_fallback_for_unknown_question(tmp_path: Path) -> None:
    service = make_service(
        tmp_path,
        [{"question": "¿Cómo me inscribo?", "answer": "En el portal."}],
    )

    assert service.answer("horario de biblioteca") == FALLBACK_MESSAGE
