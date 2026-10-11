from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_file import InputFile
    
    from .message_entity import MessageEntity
    


class InputMediaLivePhoto:
    """Represents a live photo to be sent."""

    def __init__(self, type: str, media: InputFile | str, photo: InputFile | str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, has_spoiler: bool | None = None):
        self.type: str = type
        self.media: InputFile | str = media
        self.photo: InputFile | str = photo
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.show_caption_above_media: bool | None = show_caption_above_media
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
        if self.photo is not None:
            result['photo'] = _serialize(self.photo)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.show_caption_above_media is not None:
            result['show_caption_above_media'] = _serialize(self.show_caption_above_media)
        if self.has_spoiler is not None:
            result['has_spoiler'] = _serialize(self.has_spoiler)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputMediaLivePhoto' | None:
        if not data:
            return None
        from .input_file import InputFile
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            media=data.get('media'),
            photo=data.get('photo'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i1) for i1 in data.get('caption_entities')] if data.get('caption_entities') else None,
            show_caption_above_media=data.get('show_caption_above_media'),
            has_spoiler=data.get('has_spoiler'),
        )