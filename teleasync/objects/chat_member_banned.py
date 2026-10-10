from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."""

    def __init__(self, status: str, user: User, until_date: int):
        self.status: str = status
        self.user: User = user
        self.until_date: int = until_date

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
        if self.status is not None:
            result['status'] = _serialize(self.status)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.until_date is not None:
            result['until_date'] = _serialize(self.until_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatMemberBanned' | None:
        if not data:
            return None
        from .user import User
        return cls(
            status=data.get('status'),
            user=User.from_dict(data.get('user')),
            until_date=data.get('until_date'),
        )