from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class MessageOriginChannel:
    """The message was originally sent to a channel chat."""

    def __init__(self, type: str, date: int, chat: Chat, message_id: int, author_signature: str | None = None):
        self.type: str = type
        self.date: int = date
        self.chat: Chat = chat
        self.message_id: int = message_id
        self.author_signature: str | None = author_signature

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
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.author_signature is not None:
            result['author_signature'] = _serialize(self.author_signature)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageOriginChannel' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            type=data.get('type'),
            date=data.get('date'),
            chat=Chat.from_dict(data.get('chat')),
            message_id=data.get('message_id'),
            author_signature=data.get('author_signature'),
        )