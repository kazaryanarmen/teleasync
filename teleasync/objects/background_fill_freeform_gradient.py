from __future__ import annotations
from typing import TYPE_CHECKING



class BackgroundFillFreeformGradient:
    """The background is a freeform gradient that rotates after every message in the chat."""

    def __init__(self, type: str, colors: list[int]):
        self.type: str = type
        self.colors: list[int] = colors

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
        if self.colors is not None:
            result['colors'] = _serialize(self.colors)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundFillFreeformGradient' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            colors=data.get('colors'),
        )