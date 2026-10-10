from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    


class InputMediaVoiceNote:
    """Represents a voice message file to be sent."""

    def __init__(self, type: str, media: str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, duration: int | None = None):
        self.type: str = type
        self.media: str = media
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.duration: int | None = duration

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
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputMediaVoiceNote' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            media=data.get('media'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i) for i in data.get('caption_entities')] if data.get('caption_entities') else None,
            duration=data.get('duration'),
        )