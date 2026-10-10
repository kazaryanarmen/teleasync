from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class BotAccessSettings:
    """This object describes the access settings of a bot."""

    def __init__(self, is_access_restricted: bool, added_users: list[User] | None = None):
        self.is_access_restricted: bool = is_access_restricted
        self.added_users: list[User] | None = added_users

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
        if self.is_access_restricted is not None:
            result['is_access_restricted'] = _serialize(self.is_access_restricted)
        if self.added_users is not None:
            result['added_users'] = _serialize(self.added_users)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotAccessSettings' | None:
        if not data:
            return None
        from .user import User
        return cls(
            is_access_restricted=data.get('is_access_restricted'),
            added_users=[User.from_dict(i) for i in data.get('added_users')] if data.get('added_users') else None,
        )