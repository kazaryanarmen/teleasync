from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    


class InlineQueryResultCachedSticker:
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker."""

    def __init__(self, type: str, id: str, sticker_file_id: str, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.type: str = type
        self.id: str = id
        self.sticker_file_id: str = sticker_file_id
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
        if self.sticker_file_id is not None:
            result['sticker_file_id'] = _serialize(self.sticker_file_id)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultCachedSticker' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            sticker_file_id=data.get('sticker_file_id'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
        )