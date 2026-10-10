from __future__ import annotations
from typing import TYPE_CHECKING



class BotName:
    """This object represents the bot's name."""

    def __init__(self, name: str):
        self.name: str = name

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
        if self.name is not None:
            result['name'] = _serialize(self.name)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotName' | None:
        if not data:
            return None
        return cls(
            name=data.get('name'),
        )