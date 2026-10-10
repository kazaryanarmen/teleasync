from __future__ import annotations
from typing import TYPE_CHECKING



class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat."""

    def __init__(self, type: str, chat_id: int | str):
        self.type: str = type
        self.chat_id: int | str = chat_id

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.chat_id is not None:
            result['chat_id'] = _serialize(self.chat_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotCommandScopeChatAdministrators' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            chat_id=data.get('chat_id'),
        )