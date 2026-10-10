from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class MessageOriginUser:
    """The message was originally sent by a known user."""

    def __init__(self, type: str, date: int, sender_user: User):
        self.type: str = type
        self.date: int = date
        self.sender_user: User = sender_user

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.sender_user is not None:
            result['sender_user'] = _serialize(self.sender_user)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageOriginUser' | None:
        if not data:
            return None
        from .user import User
        return cls(
            type=data.get('type'),
            date=data.get('date'),
            sender_user=User.from_dict(data.get('sender_user')),
        )