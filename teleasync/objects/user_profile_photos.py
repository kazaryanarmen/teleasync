from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class UserProfilePhotos:
    """This object represent a user's profile pictures."""

    def __init__(self, total_count: int, photos: list[PhotoSize]):
        self.total_count: int = total_count
        self.photos: list[PhotoSize] = photos

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
        if self.total_count is not None:
            result['total_count'] = _serialize(self.total_count)
        if self.photos is not None:
            result['photos'] = _serialize(self.photos)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UserProfilePhotos' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            total_count=data.get('total_count'),
            photos=[PhotoSize.from_dict(i) for i in data.get('photos')] if data.get('photos') else None,
        )