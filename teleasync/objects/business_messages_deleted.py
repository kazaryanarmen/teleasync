from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class BusinessMessagesDeleted:
    """This object is received when messages are deleted from a connected business account."""

    def __init__(self, business_connection_id: str, chat: Chat, message_ids: list[int]):
        self.business_connection_id: str = business_connection_id
        self.chat: Chat = chat
        self.message_ids: list[int] = message_ids

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
        if self.business_connection_id is not None:
            result['business_connection_id'] = _serialize(self.business_connection_id)
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.message_ids is not None:
            result['message_ids'] = _serialize(self.message_ids)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessMessagesDeleted' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            business_connection_id=data.get('business_connection_id'),
            chat=Chat.from_dict(data.get('chat')),
            message_ids=data.get('message_ids'),
        )