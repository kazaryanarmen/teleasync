from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class LivePhoto:
    """This object represents a live photo."""

    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int, photo: list[PhotoSize] | None = None, mime_type: str | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.photo: list[PhotoSize] | None = photo
        self.mime_type: str | None = mime_type
        self.file_size: int | None = file_size

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
        if self.file_id is not None:
            result['file_id'] = _serialize(self.file_id)
        if self.file_unique_id is not None:
            result['file_unique_id'] = _serialize(self.file_unique_id)
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.photo is not None:
            result['photo'] = _serialize(self.photo)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'LivePhoto' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            width=data.get('width'),
            height=data.get('height'),
            duration=data.get('duration'),
            photo=[PhotoSize.from_dict(i1) for i1 in data.get('photo')] if data.get('photo') else None,
            mime_type=data.get('mime_type'),
            file_size=data.get('file_size'),
        )