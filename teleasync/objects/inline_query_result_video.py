from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    
    from .message_entity import MessageEntity
    


class InlineQueryResultVideo:
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video."""

    def __init__(self, type: str, id: str, video_url: str, mime_type: str, thumbnail_url: str, title: str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, show_caption_above_media: bool | None = None, video_width: int | None = None, video_height: int | None = None, video_duration: int | None = None, description: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.type: str = type
        self.id: str = id
        self.video_url: str = video_url
        self.mime_type: str = mime_type
        self.thumbnail_url: str = thumbnail_url
        self.title: str = title
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.show_caption_above_media: bool | None = show_caption_above_media
        self.video_width: int | None = video_width
        self.video_height: int | None = video_height
        self.video_duration: int | None = video_duration
        self.description: str | None = description
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
        if self.video_url is not None:
            result['video_url'] = _serialize(self.video_url)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.thumbnail_url is not None:
            result['thumbnail_url'] = _serialize(self.thumbnail_url)
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
        if self.video_width is not None:
            result['video_width'] = _serialize(self.video_width)
        if self.video_height is not None:
            result['video_height'] = _serialize(self.video_height)
        if self.video_duration is not None:
            result['video_duration'] = _serialize(self.video_duration)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultVideo' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            video_url=data.get('video_url'),
            mime_type=data.get('mime_type'),
            thumbnail_url=data.get('thumbnail_url'),
            title=data.get('title'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i1) for i1 in data.get('caption_entities')] if data.get('caption_entities') else None,
            show_caption_above_media=data.get('show_caption_above_media'),
            video_width=data.get('video_width'),
            video_height=data.get('video_height'),
            video_duration=data.get('video_duration'),
            description=data.get('description'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
        )