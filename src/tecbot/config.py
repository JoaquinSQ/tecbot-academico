"""Carga y validación de configuración desde variables de entorno."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Configuración de la aplicación."""

    bot_token: str = ""
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            bot_token=os.getenv("TECBOT_BOT_TOKEN", ""),
            log_level=os.getenv("TECBOT_LOG_LEVEL", "INFO"),
        )
