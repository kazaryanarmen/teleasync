from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    


class InlineQueryResultArticle:
    """Represents a link to an article or web page."""

    def __init__(self, type: str, id: str, title: str, input_message_content: InputMessageContent, reply_markup: InlineKeyboardMarkup | None = None, url: str | None = None, description: str | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None):
        self.type: str = type
        self.id: str = id
        self.title: str = title
        self.input_message_content: InputMessageContent = input_message_content
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup
        self.url: str | None = url
        self.description: str | None = description
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
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.thumbnail_url is not None:
            result['thumbnail_url'] = _serialize(self.thumbnail_url)
        if self.thumbnail_width is not None:
            result['thumbnail_width'] = _serialize(self.thumbnail_width)
        if self.thumbnail_height is not None:
            result['thumbnail_height'] = _serialize(self.thumbnail_height)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultArticle' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            title=data.get('title'),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            url=data.get('url'),
            description=data.get('description'),
            thumbnail_url=data.get('thumbnail_url'),
            thumbnail_width=data.get('thumbnail_width'),
            thumbnail_height=data.get('thumbnail_height'),
        )