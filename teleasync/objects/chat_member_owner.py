from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges."""

    def __init__(self, status: str, user: User, is_anonymous: bool, custom_title: str | None = None):
        self.status: str = status
        self.user: User = user
        self.is_anonymous: bool = is_anonymous
        self.custom_title: str | None = custom_title

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
        if self.is_anonymous is not None:
            result['is_anonymous'] = _serialize(self.is_anonymous)
        if self.custom_title is not None:
            result['custom_title'] = _serialize(self.custom_title)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatMemberOwner' | None:
        if not data:
            return None
        from .user import User
        return cls(
            status=data.get('status'),
            user=User.from_dict(data.get('user')),
            is_anonymous=data.get('is_anonymous'),
            custom_title=data.get('custom_title'),
        )