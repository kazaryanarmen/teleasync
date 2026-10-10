from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files)."""

    def __init__(self, file_id: str, file_unique_id: str, thumbnail: PhotoSize | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.thumbnail: PhotoSize | None = thumbnail
        self.file_name: str | None = file_name
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
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        if self.file_name is not None:
            result['file_name'] = _serialize(self.file_name)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Document' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            thumbnail=PhotoSize.from_dict(data.get('thumbnail')),
            file_name=data.get('file_name'),
            mime_type=data.get('mime_type'),
            file_size=data.get('file_size'),
        )