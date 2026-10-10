from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    


class ReplyParameters:
    """Describes reply parameters for the message that is being sent."""

    def __init__(self, message_id: int | None = None, chat_id: int | str | None = None, ephemeral_message_id: int | None = None, allow_sending_without_reply: bool | None = None, quote: str | None = None, quote_parse_mode: str | None = None, quote_entities: list[MessageEntity] | None = None, quote_position: int | None = None, checklist_task_id: int | None = None, poll_option_id: str | None = None):
        self.message_id: int | None = message_id
        self.chat_id: int | str | None = chat_id
        self.ephemeral_message_id: int | None = ephemeral_message_id
        self.allow_sending_without_reply: bool | None = allow_sending_without_reply
        self.quote: str | None = quote
        self.quote_parse_mode: str | None = quote_parse_mode
        self.quote_entities: list[MessageEntity] | None = quote_entities
        self.quote_position: int | None = quote_position
        self.checklist_task_id: int | None = checklist_task_id
        self.poll_option_id: str | None = poll_option_id

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
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.chat_id is not None:
            result['chat_id'] = _serialize(self.chat_id)
        if self.ephemeral_message_id is not None:
            result['ephemeral_message_id'] = _serialize(self.ephemeral_message_id)
        if self.allow_sending_without_reply is not None:
            result['allow_sending_without_reply'] = _serialize(self.allow_sending_without_reply)
        if self.quote is not None:
            result['quote'] = _serialize(self.quote)
        if self.quote_parse_mode is not None:
            result['quote_parse_mode'] = _serialize(self.quote_parse_mode)
        if self.quote_entities is not None:
            result['quote_entities'] = _serialize(self.quote_entities)
        if self.quote_position is not None:
            result['quote_position'] = _serialize(self.quote_position)
        if self.checklist_task_id is not None:
            result['checklist_task_id'] = _serialize(self.checklist_task_id)
        if self.poll_option_id is not None:
            result['poll_option_id'] = _serialize(self.poll_option_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ReplyParameters' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        return cls(
            message_id=data.get('message_id'),
            chat_id=data.get('chat_id'),
            ephemeral_message_id=data.get('ephemeral_message_id'),
            allow_sending_without_reply=data.get('allow_sending_without_reply'),
            quote=data.get('quote'),
            quote_parse_mode=data.get('quote_parse_mode'),
            quote_entities=[MessageEntity.from_dict(i) for i in data.get('quote_entities')] if data.get('quote_entities') else None,
            quote_position=data.get('quote_position'),
            checklist_task_id=data.get('checklist_task_id'),
            poll_option_id=data.get('poll_option_id'),
        )