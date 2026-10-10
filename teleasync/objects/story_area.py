from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .story_area_position import StoryAreaPosition
    
    from .story_area_type import StoryAreaType
    


class StoryArea:
    """Describes a clickable area on a story media."""

    def __init__(self, position: StoryAreaPosition, type: StoryAreaType):
        self.position: StoryAreaPosition = position
        self.type: StoryAreaType = type

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
        if self.position is not None:
            result['position'] = _serialize(self.position)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryArea' | None:
        if not data:
            return None
        from .story_area_position import StoryAreaPosition
        from .story_area_type import StoryAreaType
        return cls(
            position=StoryAreaPosition.from_dict(data.get('position')),
            type=StoryAreaType.from_dict(data.get('type')),
        )