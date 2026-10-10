from __future__ import annotations
from typing import TYPE_CHECKING



class StoryAreaType:
    """Describes the type of a clickable area on a story. Currently, it can be one of - StoryAreaTypeLocation - StoryAreaTypeSuggestedReaction - StoryAreaTypeLink - StoryAreaTypeWeather - StoryAreaTypeUniqueGift"""

    def __init__(self):
        pass

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryAreaType' | None:
        if not data:
            return None
        return cls(
        )