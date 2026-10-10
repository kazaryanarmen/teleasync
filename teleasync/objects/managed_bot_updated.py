from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ManagedBotUpdated:
    """This object contains information about the creation, token update, or owner update of a bot that is managed by the current bot."""

    def __init__(self, user: User, bot: User):
        self.user: User = user
        self.bot: User = bot

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
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.bot is not None:
            result['bot'] = _serialize(self.bot)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ManagedBotUpdated' | None:
        if not data:
            return None
        from .user import User
        return cls(
            user=User.from_dict(data.get('user')),
            bot=User.from_dict(data.get('bot')),
        )