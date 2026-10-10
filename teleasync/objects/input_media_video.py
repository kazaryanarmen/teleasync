from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    


class InputMediaVideo:
    """Represents a video to be sent."""

    def __init__(self, type: str, media: str, thumbnail: str | None = None, cover: str | None = None, start_timestamp: int | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, width: int | None = None, height: int | None = None, duration: int | None = None, supports_streaming: bool | None = None, has_spoiler: bool | None = None):
        self.type: str = type
        self.media: str = media
        self.thumbnail: str | None = thumbnail
        self.cover: str | None = cover
        self.start_timestamp: int | None = start_timestamp
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.show_caption_above_media: bool | None = show_caption_above_media
        self.width: int | None = width
        self.height: int | None = height
        self.duration: int | None = duration
        self.supports_streaming: bool | None = supports_streaming
        self.has_spoiler: bool | None = has_spoiler

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
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.show_caption_above_media is not None:
            result['show_caption_above_media'] = _serialize(self.show_caption_above_media)
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.supports_streaming is not None:
            result['supports_streaming'] = _serialize(self.supports_streaming)
        if self.has_spoiler is not None:
            result['has_spoiler'] = _serialize(self.has_spoiler)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputMediaVideo' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            media=data.get('media'),
            thumbnail=data.get('thumbnail'),
            cover=data.get('cover'),
            start_timestamp=data.get('start_timestamp'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i) for i in data.get('caption_entities')] if data.get('caption_entities') else None,
            show_caption_above_media=data.get('show_caption_above_media'),
            width=data.get('width'),
            height=data.get('height'),
            duration=data.get('duration'),
            supports_streaming=data.get('supports_streaming'),
            has_spoiler=data.get('has_spoiler'),
        )