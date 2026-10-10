from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class VideoNote:
    """This object represents a video message."""

    def __init__(self, file_id: str, file_unique_id: str, length: int, duration: int, thumbnail: PhotoSize | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.length: int = length
        self.duration: int = duration
        self.thumbnail: PhotoSize | None = thumbnail
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
        if self.length is not None:
            result['length'] = _serialize(self.length)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'VideoNote' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            length=data.get('length'),
            duration=data.get('duration'),
            thumbnail=PhotoSize.from_dict(data.get('thumbnail')),
            file_size=data.get('file_size'),
        )