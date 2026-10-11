from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    
    from .message_entity import MessageEntity
    


class InlineQueryResultDocument:
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method."""

    def __init__(self, type: str, id: str, title: str, document_url: str, mime_type: str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, description: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None):
        self.type: str = type
        self.id: str = id
        self.title: str = title
        self.document_url: str = document_url
        self.mime_type: str = mime_type
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.description: str | None = description
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup
        self.input_message_content: InputMessageContent | None = input_message_content
        self.thumbnail_url: str | None = thumbnail_url
        self.thumbnail_width: int | None = thumbnail_width
        self.thumbnail_height: int | None = thumbnail_height

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.document_url is not None:
            result['document_url'] = _serialize(self.document_url)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        if self.thumbnail_url is not None:
            result['thumbnail_url'] = _serialize(self.thumbnail_url)
        if self.thumbnail_width is not None:
            result['thumbnail_width'] = _serialize(self.thumbnail_width)
        if self.thumbnail_height is not None:
            result['thumbnail_height'] = _serialize(self.thumbnail_height)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultDocument' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            title=data.get('title'),
            document_url=data.get('document_url'),
            mime_type=data.get('mime_type'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i1) for i1 in data.get('caption_entities')] if data.get('caption_entities') else None,
            description=data.get('description'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
            thumbnail_url=data.get('thumbnail_url'),
            thumbnail_width=data.get('thumbnail_width'),
            thumbnail_height=data.get('thumbnail_height'),
        )