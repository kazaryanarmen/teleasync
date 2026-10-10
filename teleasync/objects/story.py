from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class Story:
    """This object represents a story."""

    def __init__(self, chat: Chat, id: int):
        self.chat: Chat = chat
        self.id: int = id

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
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.id is not None:
            result['id'] = _serialize(self.id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Story' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            id=data.get('id'),
        )