from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class PaidMediaPhoto:
    """The paid media is a photo."""

    def __init__(self, type: str, photo: list[PhotoSize]):
        self.type: str = type
        self.photo: list[PhotoSize] = photo

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
        if self.photo is not None:
            result['photo'] = _serialize(self.photo)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaPhoto' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            type=data.get('type'),
            photo=[PhotoSize.from_dict(i1) for i1 in data.get('photo')] if data.get('photo') else None,
        )