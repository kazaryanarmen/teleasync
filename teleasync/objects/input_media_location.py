from __future__ import annotations
from typing import TYPE_CHECKING



class InputMediaLocation:
    """Represents a location to be sent."""

    def __init__(self, type: str, latitude: float, longitude: float, horizontal_accuracy: float | None = None):
        self.type: str = type
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.horizontal_accuracy: float | None = horizontal_accuracy

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
        if self.latitude is not None:
            result['latitude'] = _serialize(self.latitude)
        if self.longitude is not None:
            result['longitude'] = _serialize(self.longitude)
        if self.horizontal_accuracy is not None:
            result['horizontal_accuracy'] = _serialize(self.horizontal_accuracy)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputMediaLocation' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            horizontal_accuracy=data.get('horizontal_accuracy'),
        )