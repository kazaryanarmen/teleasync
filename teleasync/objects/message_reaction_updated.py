from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .reaction_type import ReactionType
    
    from .user import User
    


class MessageReactionUpdated:
    """This object represents a change of a reaction on a message performed by a user."""

    def __init__(self, chat: Chat, message_id: int, date: int, old_reaction: list[ReactionType], new_reaction: list[ReactionType], user: User | None = None, actor_chat: Chat | None = None):
        self.chat: Chat = chat
        self.message_id: int = message_id
        self.date: int = date
        self.old_reaction: list[ReactionType] = old_reaction
        self.new_reaction: list[ReactionType] = new_reaction
        self.user: User | None = user
        self.actor_chat: Chat | None = actor_chat

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
        if self.old_reaction is not None:
            result['old_reaction'] = _serialize(self.old_reaction)
        if self.new_reaction is not None:
            result['new_reaction'] = _serialize(self.new_reaction)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.actor_chat is not None:
            result['actor_chat'] = _serialize(self.actor_chat)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageReactionUpdated' | None:
        if not data:
            return None
        from .chat import Chat
        from .reaction_type import ReactionType
        from .user import User
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            message_id=data.get('message_id'),
            date=data.get('date'),
            old_reaction=[ReactionType.from_dict(i) for i in data.get('old_reaction')] if data.get('old_reaction') else None,
            new_reaction=[ReactionType.from_dict(i) for i in data.get('new_reaction')] if data.get('new_reaction') else None,
            user=User.from_dict(data.get('user')),
            actor_chat=Chat.from_dict(data.get('actor_chat')),
        )