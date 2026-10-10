from __future__ import annotations
from typing import TYPE_CHECKING



class InputStoryContentPhoto:
    """Describes a photo to post as a story."""

    def __init__(self, type: str, photo_: str):
        self.type: str = type
        self.photo_: str = photo_

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
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputStoryContentPhoto' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            photo_=data.get('photo'),
        )