from __future__ import annotations
from typing import TYPE_CHECKING



class BackgroundFillGradient:
    """The background is a gradient fill."""

    def __init__(self, type: str, top_color: int, bottom_color: int, rotation_angle: int):
        self.type: str = type
        self.top_color: int = top_color
        self.bottom_color: int = bottom_color
        self.rotation_angle: int = rotation_angle

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
        if self.top_color is not None:
            result['top_color'] = _serialize(self.top_color)
        if self.bottom_color is not None:
            result['bottom_color'] = _serialize(self.bottom_color)
        if self.rotation_angle is not None:
            result['rotation_angle'] = _serialize(self.rotation_angle)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundFillGradient' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            top_color=data.get('top_color'),
            bottom_color=data.get('bottom_color'),
            rotation_angle=data.get('rotation_angle'),
        )