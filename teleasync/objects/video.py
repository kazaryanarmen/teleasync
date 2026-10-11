from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    
    from .video_quality import VideoQuality
    


class Video:
    """This object represents a video file."""

    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, duration: int, thumbnail: PhotoSize | None = None, cover: list[PhotoSize] | None = None, start_timestamp: int | None = None, qualities: list[VideoQuality] | None = None, file_name: str | None = None, mime_type: str | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumbnail: PhotoSize | None = thumbnail
        self.cover: list[PhotoSize] | None = cover
        self.start_timestamp: int | None = start_timestamp
        self.qualities: list[VideoQuality] | None = qualities
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
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        if self.cover is not None:
            result['cover'] = _serialize(self.cover)
        if self.start_timestamp is not None:
            result['start_timestamp'] = _serialize(self.start_timestamp)
        if self.qualities is not None:
            result['qualities'] = _serialize(self.qualities)
        if self.file_name is not None:
            result['file_name'] = _serialize(self.file_name)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Video' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        from .video_quality import VideoQuality
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            width=data.get('width'),
            height=data.get('height'),
            duration=data.get('duration'),
            thumbnail=PhotoSize.from_dict(data.get('thumbnail')),
            cover=[PhotoSize.from_dict(i1) for i1 in data.get('cover')] if data.get('cover') else None,
            start_timestamp=data.get('start_timestamp'),
            qualities=[VideoQuality.from_dict(i1) for i1 in data.get('qualities')] if data.get('qualities') else None,
            file_name=data.get('file_name'),
            mime_type=data.get('mime_type'),
            file_size=data.get('file_size'),
        )