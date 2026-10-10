from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    
    from .message_entity import MessageEntity
    


class InlineQueryResultMpeg4Gif:
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation."""

    def __init__(self, type: str, id: str, mpeg4_url: str, thumbnail_url: str, mpeg4_width: int | None = None, mpeg4_height: int | None = None, mpeg4_duration: int | None = None, thumbnail_mime_type: str | None = None, title: str | None = None, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.type: str = type
        self.id: str = id
        self.mpeg4_url: str = mpeg4_url
        self.thumbnail_url: str = thumbnail_url
        self.mpeg4_width: int | None = mpeg4_width
        self.mpeg4_height: int | None = mpeg4_height
        self.mpeg4_duration: int | None = mpeg4_duration
        self.thumbnail_mime_type: str | None = thumbnail_mime_type
        self.title: str | None = title
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.show_caption_above_media: bool | None = show_caption_above_media
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup
        self.input_message_content: InputMessageContent | None = input_message_content

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.mpeg4_url is not None:
            result['mpeg4_url'] = _serialize(self.mpeg4_url)
        if self.thumbnail_url is not None:
            result['thumbnail_url'] = _serialize(self.thumbnail_url)
        if self.mpeg4_width is not None:
            result['mpeg4_width'] = _serialize(self.mpeg4_width)
        if self.mpeg4_height is not None:
            result['mpeg4_height'] = _serialize(self.mpeg4_height)
        if self.mpeg4_duration is not None:
            result['mpeg4_duration'] = _serialize(self.mpeg4_duration)
        if self.thumbnail_mime_type is not None:
            result['thumbnail_mime_type'] = _serialize(self.thumbnail_mime_type)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.show_caption_above_media is not None:
            result['show_caption_above_media'] = _serialize(self.show_caption_above_media)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultMpeg4Gif' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            mpeg4_url=data.get('mpeg4_url'),
            thumbnail_url=data.get('thumbnail_url'),
            mpeg4_width=data.get('mpeg4_width'),
            mpeg4_height=data.get('mpeg4_height'),
            mpeg4_duration=data.get('mpeg4_duration'),
            thumbnail_mime_type=data.get('thumbnail_mime_type'),
            title=data.get('title'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i) for i in data.get('caption_entities')] if data.get('caption_entities') else None,
            show_caption_above_media=data.get('show_caption_above_media'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
        )