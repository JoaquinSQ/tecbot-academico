"""Comandos y textos de ayuda del bot."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    name: str
    description: str


COMMANDS = (
    Command("/start", "Inicia la conversación con TecBot."),
    Command("/ayuda", "Muestra los comandos disponibles."),
)

HELP_TEXT = "\n".join(f"{command.name} - {command.description}" for command in COMMANDS)
