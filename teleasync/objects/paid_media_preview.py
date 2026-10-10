from __future__ import annotations
from typing import TYPE_CHECKING



class PaidMediaPreview:
    """The paid media isn't available before the payment."""

    def __init__(self, type: str, width: int | None = None, height: int | None = None, duration: int | None = None):
        self.type: str = type
        self.width: int | None = width
        self.height: int | None = height
        self.duration: int | None = duration

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
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaPreview' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            width=data.get('width'),
            height=data.get('height'),
            duration=data.get('duration'),
        )