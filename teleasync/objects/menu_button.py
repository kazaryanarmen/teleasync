from __future__ import annotations
from typing import TYPE_CHECKING



class MenuButton:
    """This object describes the bot's menu button in a private chat. It should be one of - MenuButtonCommands - MenuButtonWebApp - MenuButtonDefault If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands."""

    def __init__(self):
        pass

    def to_dict(self) -> dict:
        def _serialize(v):
            if hasattr(v, 'to_dict'):
                return v.to_dict()
            elif isinstance(v, list):
                return [_serialize(i) for i in v]
            elif isinstance(v, dict):
                return {k: _serialize(val) for k, val in v.items()}
            return v
        result = {}
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MenuButton' | None:
        if not data:
            return None
        return cls(
        )