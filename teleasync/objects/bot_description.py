from __future__ import annotations
from typing import TYPE_CHECKING



class BotDescription:
    """This object represents the bot's description."""

    def __init__(self, description: str):
        self.description: str = description

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
        if self.description is not None:
            result['description'] = _serialize(self.description)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotDescription' | None:
        if not data:
            return None
        return cls(
            description=data.get('description'),
        )