from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class MessageOriginChat:
    """The message was originally sent on behalf of a chat to a group chat."""

    def __init__(self, type: str, date: int, sender_chat: Chat, author_signature: str | None = None):
        self.type: str = type
        self.date: int = date
        self.sender_chat: Chat = sender_chat
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
        if self.sender_chat is not None:
            result['sender_chat'] = _serialize(self.sender_chat)
        if self.author_signature is not None:
            result['author_signature'] = _serialize(self.author_signature)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageOriginChat' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            type=data.get('type'),
            date=data.get('date'),
            sender_chat=Chat.from_dict(data.get('sender_chat')),
            author_signature=data.get('author_signature'),
        )