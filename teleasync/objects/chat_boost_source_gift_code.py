from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatBoostSourceGiftCode:
    """The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription."""

    def __init__(self, source: str, user: User):
        self.source: str = source
        self.user: User = user

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
        if self.source is not None:
            result['source'] = _serialize(self.source)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostSourceGiftCode' | None:
        if not data:
            return None
        from .user import User
        return cls(
            source=data.get('source'),
            user=User.from_dict(data.get('user')),
        )