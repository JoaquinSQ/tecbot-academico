import json
from pathlib import Path

from tecbot.bot.handlers import BotHandlers
from tecbot.services.academic import AcademicService


def make_handlers(tmp_path: Path) -> BotHandlers:
    data_file = tmp_path / "faq.json"
    data_file.write_text(json.dumps([], ensure_ascii=False), encoding="utf-8")
    return BotHandlers(AcademicService(data_file))


def test_start_returns_welcome_and_help(tmp_path: Path) -> None:
    response = make_handlers(tmp_path).handle("/start")

    assert "TecBot Académico" in response
    assert "/ayuda" in response


def test_regular_message_is_delegated_to_academic_service(tmp_path: Path) -> None:
    response = make_handlers(tmp_path).handle("cualquier consulta")

    assert "No tengo una respuesta" in response
