from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ManagedBotCreated:
    """This object contains information about the bot that was created to be managed by the current bot."""

    def __init__(self, bot: User):
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
        if self.bot is not None:
            result['bot'] = _serialize(self.bot)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ManagedBotCreated' | None:
        if not data:
            return None
        from .user import User
        return cls(
            bot=User.from_dict(data.get('bot')),
        )