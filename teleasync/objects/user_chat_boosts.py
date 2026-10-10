from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat_boost import ChatBoost
    


class UserChatBoosts:
    """This object represents a list of boosts added to a chat by a user."""

    def __init__(self, boosts: list[ChatBoost]):
        self.boosts: list[ChatBoost] = boosts

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
        if self.boosts is not None:
            result['boosts'] = _serialize(self.boosts)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UserChatBoosts' | None:
        if not data:
            return None
        from .chat_boost import ChatBoost
        return cls(
            boosts=[ChatBoost.from_dict(i) for i in data.get('boosts')] if data.get('boosts') else None,
        )