from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class MessageGenerationStopped:
    """This object describes an update about a user stopping message generation."""

    def __init__(self, chat: Chat, draft_id: int, message_thread_id: int | None = None):
        self.chat: Chat = chat
        self.draft_id: int = draft_id
        self.message_thread_id: int | None = message_thread_id

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
        if self.draft_id is not None:
            result['draft_id'] = _serialize(self.draft_id)
        if self.message_thread_id is not None:
            result['message_thread_id'] = _serialize(self.message_thread_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageGenerationStopped' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            draft_id=data.get('draft_id'),
            message_thread_id=data.get('message_thread_id'),
        )