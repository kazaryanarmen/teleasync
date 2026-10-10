from __future__ import annotations
from typing import TYPE_CHECKING



class MaskPosition:
    """This object describes the position on faces where a mask should be placed by default."""

    def __init__(self, point: str, x_shift: float, y_shift: float, scale: float):
        self.point: str = point
        self.x_shift: float = x_shift
        self.y_shift: float = y_shift
        self.scale: float = scale

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
        if self.point is not None:
            result['point'] = _serialize(self.point)
        if self.x_shift is not None:
            result['x_shift'] = _serialize(self.x_shift)
        if self.y_shift is not None:
            result['y_shift'] = _serialize(self.y_shift)
        if self.scale is not None:
            result['scale'] = _serialize(self.scale)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MaskPosition' | None:
        if not data:
            return None
        return cls(
            point=data.get('point'),
            x_shift=data.get('x_shift'),
            y_shift=data.get('y_shift'),
            scale=data.get('scale'),
        )