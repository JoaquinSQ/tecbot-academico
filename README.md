# TecBot Académico

Bot de consultas académicas. Actualmente incluye el núcleo de dominio y un
modo consola; el adaptador al canal de mensajería (Telegram, Discord, etc.)
todavía no está conectado.

## Requisitos

- Python 3.11 o superior

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Uso

Modo consola:

```powershell
python -m tecbot.main
# o, si el entorno virtual está activo:
tecbot
```

Escribe una pregunta y TecBot responderá usando `src/tecbot/data/faq.json`.
Para terminar, escribe `salir`, `exit` o `quit`.

## Tests y lint

```powershell
pytest
ruff check .
```

## Estructura

```text
src/tecbot/
├── main.py            # entrypoint (modo consola por ahora)
├── config.py          # carga de variables de entorno
├── bot/
│   ├── commands.py    # comandos y textos de ayuda
│   └── handlers.py    # adapta mensajes a casos de uso
├── services/
│   └── academic.py    # lógica académica (sin dependencias del canal)
└── data/
    └── faq.json       # contenido de ejemplo versionado
```

## Próximos pasos

1. Elegir el canal (Telegram, Discord, WhatsApp o web) y agregar su adaptador.
2. Reemplazar el contenido de ejemplo de `faq.json` por información oficial.
3. Definir si se usará un LLM/RAG o búsqueda sobre datos estructurados.
