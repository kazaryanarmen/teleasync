from __future__ import annotations
from typing import TYPE_CHECKING



class BotShortDescription:
    """This object represents the bot's short description."""

    def __init__(self, short_description: str):
        self.short_description: str = short_description

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
        if self.short_description is not None:
            result['short_description'] = _serialize(self.short_description)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotShortDescription' | None:
        if not data:
            return None
        return cls(
            short_description=data.get('short_description'),
        )