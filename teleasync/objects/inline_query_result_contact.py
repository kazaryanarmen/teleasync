from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    


class InlineQueryResultContact:
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact."""

    def __init__(self, type: str, id: str, phone_number: str, first_name: str, last_name: str | None = None, vcard: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None):
        self.type: str = type
        self.id: str = id
        self.phone_number: str = phone_number
        self.first_name: str = first_name
        self.last_name: str | None = last_name
        self.vcard: str | None = vcard
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
        if self.phone_number is not None:
            result['phone_number'] = _serialize(self.phone_number)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.vcard is not None:
            result['vcard'] = _serialize(self.vcard)
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
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultContact' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            phone_number=data.get('phone_number'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            vcard=data.get('vcard'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
            thumbnail_url=data.get('thumbnail_url'),
            thumbnail_width=data.get('thumbnail_width'),
            thumbnail_height=data.get('thumbnail_height'),
        )