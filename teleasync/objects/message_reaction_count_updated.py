from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .reaction_count import ReactionCount
    


class MessageReactionCountUpdated:
    """This object represents reaction changes on a message with anonymous reactions."""

    def __init__(self, chat: Chat, message_id: int, date: int, reactions: list[ReactionCount]):
        self.chat: Chat = chat
        self.message_id: int = message_id
        self.date: int = date
        self.reactions: list[ReactionCount] = reactions

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
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.reactions is not None:
            result['reactions'] = _serialize(self.reactions)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageReactionCountUpdated' | None:
        if not data:
            return None
        from .chat import Chat
        from .reaction_count import ReactionCount
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            message_id=data.get('message_id'),
            date=data.get('date'),
            reactions=[ReactionCount.from_dict(i1) for i1 in data.get('reactions')] if data.get('reactions') else None,
        )