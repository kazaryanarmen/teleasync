from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    
    from .message_entity import MessageEntity
    


class InlineQueryResultVoice:
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message."""

    def __init__(self, type: str, id: str, voice_url: str, title: str, caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity] | None = None, voice_duration: int | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.type: str = type
        self.id: str = id
        self.voice_url: str = voice_url
        self.title: str = title
        self.caption: str | None = caption
        self.parse_mode: str | None = parse_mode
        self.caption_entities: list[MessageEntity] | None = caption_entities
        self.voice_duration: int | None = voice_duration
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
        if self.voice_url is not None:
            result['voice_url'] = _serialize(self.voice_url)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.caption_entities is not None:
            result['caption_entities'] = _serialize(self.caption_entities)
        if self.voice_duration is not None:
            result['voice_duration'] = _serialize(self.voice_duration)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultVoice' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        from .message_entity import MessageEntity
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            voice_url=data.get('voice_url'),
            title=data.get('title'),
            caption=data.get('caption'),
            parse_mode=data.get('parse_mode'),
            caption_entities=[MessageEntity.from_dict(i) for i in data.get('caption_entities')] if data.get('caption_entities') else None,
            voice_duration=data.get('voice_duration'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
        )