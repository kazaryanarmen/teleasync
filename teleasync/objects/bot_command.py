from __future__ import annotations
from typing import TYPE_CHECKING



class BotCommand:
    """This object represents a bot command."""

    def __init__(self, command: str, description: str, is_ephemeral: bool | None = None):
        self.command: str = command
        self.description: str = description
        self.is_ephemeral: bool | None = is_ephemeral

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
        if self.command is not None:
            result['command'] = _serialize(self.command)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.is_ephemeral is not None:
            result['is_ephemeral'] = _serialize(self.is_ephemeral)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotCommand' | None:
        if not data:
            return None
        return cls(
            command=data.get('command'),
            description=data.get('description'),
            is_ephemeral=data.get('is_ephemeral'),
        )