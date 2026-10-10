from __future__ import annotations
from typing import TYPE_CHECKING



class InputStoryContent:
    """This object describes the content of a story to post. Currently, it can be one of - InputStoryContentPhoto - InputStoryContentVideo"""

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
    def from_dict(cls, data: dict | None) -> 'InputStoryContent' | None:
        if not data:
            return None
        return cls(
        )