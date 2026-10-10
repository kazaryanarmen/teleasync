from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .chat_boost import ChatBoost
    


class ChatBoostUpdated:
    """This object represents a boost added to a chat or changed."""

    def __init__(self, chat: Chat, boost: ChatBoost):
        self.chat: Chat = chat
        self.boost: ChatBoost = boost

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
        if self.boost is not None:
            result['boost'] = _serialize(self.boost)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostUpdated' | None:
        if not data:
            return None
        from .chat import Chat
        from .chat_boost import ChatBoost
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            boost=ChatBoost.from_dict(data.get('boost')),
        )