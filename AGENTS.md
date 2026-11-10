# AGENTS.md

TecBot Académico: bot de consultas académicas en Python 3.11+ con layout `src/`.
El canal de mensajería aún no está conectado; el entrypoint actual es un modo consola.

## Comandos

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"

pytest                              # todos los tests
pytest tests/test_academic.py       # un archivo
pytest tests/test_academic.py::test_answer_matches_question  # un test
ruff check .
python -m tecbot.main               # modo consola
```

## Arquitectura

- `src/tecbot/main.py`: único entrypoint; hoy arranca el bucle de consola.
- `src/tecbot/bot/`: adaptación al canal. `handlers.py` recibe texto y devuelve texto; `commands.py` define comandos/ayuda. No poner reglas de negocio aquí.
- `src/tecbot/services/`: lógica de dominio. `academic.py` carga el FAQ y responde; debe poder testearse sin levantar el bot.
- `src/tecbot/data/faq.json`: contenido versionado de ejemplo; se incluye en el paquete vía `package-data`.
- `src/tecbot/config.py`: lee `TECBOT_BOT_TOKEN` y `TECBOT_LOG_LEVEL` desde el entorno. `.env.example` documenta las variables; no commitear `.env`.

## Convenciones y gotchas

- Al agregar un canal (Telegram, Discord, etc.), crear un adaptador que use `BotHandlers` en lugar de duplicar lógica en `main.py`.
- Los tests construyen servicios con archivos FAQ temporales (`tmp_path`); no requieren red ni servicios externos.
- Si se renombra/mueve `data/faq.json`, actualizar `DATA_FILE` en `services/academic.py` y `package-data` en `pyproject.toml`.
- No hay migraciones, base de datos ni codegen todavía.
