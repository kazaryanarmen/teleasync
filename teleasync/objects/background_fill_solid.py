from __future__ import annotations
from typing import TYPE_CHECKING



class BackgroundFillSolid:
    """The background is filled using the selected color."""

    def __init__(self, type: str, color: int):
        self.type: str = type
        self.color: int = color

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
        if self.color is not None:
            result['color'] = _serialize(self.color)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundFillSolid' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            color=data.get('color'),
        )