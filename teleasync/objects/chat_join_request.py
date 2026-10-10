from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .chat_invite_link import ChatInviteLink
    
    from .user import User
    


class ChatJoinRequest:
    """Represents a join request sent to a chat."""

    def __init__(self, chat: Chat, from_: User, user_chat_id: int, date: int, bio: str | None = None, invite_link: ChatInviteLink | None = None, query_id: str | None = None):
        self.chat: Chat = chat
        self.from_: User = from_
        self.user_chat_id: int = user_chat_id
        self.date: int = date
        self.bio: str | None = bio
        self.invite_link: ChatInviteLink | None = invite_link
        self.query_id: str | None = query_id

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
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.user_chat_id is not None:
            result['user_chat_id'] = _serialize(self.user_chat_id)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.bio is not None:
            result['bio'] = _serialize(self.bio)
        if self.invite_link is not None:
            result['invite_link'] = _serialize(self.invite_link)
        if self.query_id is not None:
            result['query_id'] = _serialize(self.query_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatJoinRequest' | None:
        if not data:
            return None
        from .chat import Chat
        from .chat_invite_link import ChatInviteLink
        from .user import User
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            from_=User.from_dict(data.get('from')),
            user_chat_id=data.get('user_chat_id'),
            date=data.get('date'),
            bio=data.get('bio'),
            invite_link=ChatInviteLink.from_dict(data.get('invite_link')),
            query_id=data.get('query_id'),
        )