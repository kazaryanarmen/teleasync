from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .user import User
    


class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll."""

    def __init__(self, poll_id: str, option_ids: list[int], option_persistent_ids: list[str], voter_chat: Chat | None = None, user: User | None = None):
        self.poll_id: str = poll_id
        self.option_ids: list[int] = option_ids
        self.option_persistent_ids: list[str] = option_persistent_ids
        self.voter_chat: Chat | None = voter_chat
        self.user: User | None = user

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
        if self.poll_id is not None:
            result['poll_id'] = _serialize(self.poll_id)
        if self.option_ids is not None:
            result['option_ids'] = _serialize(self.option_ids)
        if self.option_persistent_ids is not None:
            result['option_persistent_ids'] = _serialize(self.option_persistent_ids)
        if self.voter_chat is not None:
            result['voter_chat'] = _serialize(self.voter_chat)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PollAnswer' | None:
        if not data:
            return None
        from .chat import Chat
        from .user import User
        return cls(
            poll_id=data.get('poll_id'),
            option_ids=data.get('option_ids'),
            option_persistent_ids=data.get('option_persistent_ids'),
            voter_chat=Chat.from_dict(data.get('voter_chat')),
            user=User.from_dict(data.get('user')),
        )