from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class PaidMediaPhoto:
    """The paid media is a photo."""

    def __init__(self, type: str, photo_: list[PhotoSize]):
        self.type: str = type
        self.photo_: list[PhotoSize] = photo_

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
    def from_dict(cls, data: dict | None) -> 'PaidMediaPhoto' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            type=data.get('type'),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
        )