from __future__ import annotations
from typing import TYPE_CHECKING



class StoryAreaPosition:
    """Describes the position of a clickable area within a story."""

    def __init__(self, x_percentage: float, y_percentage: float, width_percentage: float, height_percentage: float, rotation_angle: float, corner_radius_percentage: float):
        self.x_percentage: float = x_percentage
        self.y_percentage: float = y_percentage
        self.width_percentage: float = width_percentage
        self.height_percentage: float = height_percentage
        self.rotation_angle: float = rotation_angle
        self.corner_radius_percentage: float = corner_radius_percentage

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
        if self.x_percentage is not None:
            result['x_percentage'] = _serialize(self.x_percentage)
        if self.y_percentage is not None:
            result['y_percentage'] = _serialize(self.y_percentage)
        if self.width_percentage is not None:
            result['width_percentage'] = _serialize(self.width_percentage)
        if self.height_percentage is not None:
            result['height_percentage'] = _serialize(self.height_percentage)
        if self.rotation_angle is not None:
            result['rotation_angle'] = _serialize(self.rotation_angle)
        if self.corner_radius_percentage is not None:
            result['corner_radius_percentage'] = _serialize(self.corner_radius_percentage)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryAreaPosition' | None:
        if not data:
            return None
        return cls(
            x_percentage=data.get('x_percentage'),
            y_percentage=data.get('y_percentage'),
            width_percentage=data.get('width_percentage'),
            height_percentage=data.get('height_percentage'),
            rotation_angle=data.get('rotation_angle'),
            corner_radius_percentage=data.get('corner_radius_percentage'),
        )