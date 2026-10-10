from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .business_bot_rights import BusinessBotRights
    
    from .user import User
    


class BusinessConnection:
    """Describes the connection of the bot with a business account."""

    def __init__(self, id: str, user: User, user_chat_id: int, date: int, is_enabled: bool, rights: BusinessBotRights | None = None):
        self.id: str = id
        self.user: User = user
        self.user_chat_id: int = user_chat_id
        self.date: int = date
        self.is_enabled: bool = is_enabled
        self.rights: BusinessBotRights | None = rights

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.user_chat_id is not None:
            result['user_chat_id'] = _serialize(self.user_chat_id)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.is_enabled is not None:
            result['is_enabled'] = _serialize(self.is_enabled)
        if self.rights is not None:
            result['rights'] = _serialize(self.rights)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessConnection' | None:
        if not data:
            return None
        from .business_bot_rights import BusinessBotRights
        from .user import User
        return cls(
            id=data.get('id'),
            user=User.from_dict(data.get('user')),
            user_chat_id=data.get('user_chat_id'),
            date=data.get('date'),
            is_enabled=data.get('is_enabled'),
            rights=BusinessBotRights.from_dict(data.get('rights')),
        )