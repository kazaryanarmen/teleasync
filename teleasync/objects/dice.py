from __future__ import annotations
from typing import TYPE_CHECKING



class Dice:
    """This object represents an animated emoji that displays a random value."""

    def __init__(self, emoji: str, value: int):
        self.emoji: str = emoji
        self.value: int = value

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
        if self.emoji is not None:
            result['emoji'] = _serialize(self.emoji)
        if self.value is not None:
            result['value'] = _serialize(self.value)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Dice' | None:
        if not data:
            return None
        return cls(
            emoji=data.get('emoji'),
            value=data.get('value'),
        )