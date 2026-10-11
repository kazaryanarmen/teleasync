from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_file import InputFile
    


class InputPaidMediaVideo:
    """The paid media to send is a video."""

    def __init__(self, type: str, media: InputFile | str, thumbnail: InputFile | str | None = None, cover: InputFile | str | None = None, start_timestamp: int | None = None, width: int | None = None, height: int | None = None, duration: int | None = None, supports_streaming: bool | None = None):
        self.type: str = type
        self.media: InputFile | str = media
        self.thumbnail: InputFile | str | None = thumbnail
        self.cover: InputFile | str | None = cover
        self.start_timestamp: int | None = start_timestamp
        self.width: int | None = width
        self.height: int | None = height
        self.duration: int | None = duration
        self.supports_streaming: bool | None = supports_streaming

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
        if self.media is not None:
            result['media'] = _serialize(self.media)
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        if self.cover is not None:
            result['cover'] = _serialize(self.cover)
        if self.start_timestamp is not None:
            result['start_timestamp'] = _serialize(self.start_timestamp)
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.supports_streaming is not None:
            result['supports_streaming'] = _serialize(self.supports_streaming)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputPaidMediaVideo' | None:
        if not data:
            return None
        from .input_file import InputFile
        return cls(
            type=data.get('type'),
            media=data.get('media'),
            thumbnail=data.get('thumbnail'),
            cover=data.get('cover'),
            start_timestamp=data.get('start_timestamp'),
            width=data.get('width'),
            height=data.get('height'),
            duration=data.get('duration'),
            supports_streaming=data.get('supports_streaming'),
        )