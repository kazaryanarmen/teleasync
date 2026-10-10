from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .chat_boost_source import ChatBoostSource
    


class ChatBoostRemoved:
    """This object represents a boost removed from a chat."""

    def __init__(self, chat: Chat, boost_id: str, remove_date: int, source: ChatBoostSource):
        self.chat: Chat = chat
        self.boost_id: str = boost_id
        self.remove_date: int = remove_date
        self.source: ChatBoostSource = source

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
        if self.boost_id is not None:
            result['boost_id'] = _serialize(self.boost_id)
        if self.remove_date is not None:
            result['remove_date'] = _serialize(self.remove_date)
        if self.source is not None:
            result['source'] = _serialize(self.source)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostRemoved' | None:
        if not data:
            return None
        from .chat import Chat
        from .chat_boost_source import ChatBoostSource
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            boost_id=data.get('boost_id'),
            remove_date=data.get('remove_date'),
            source=ChatBoostSource.from_dict(data.get('source')),
        )