from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatBoostSourceGiveaway:
    """The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and prize_star_count / 500 times for one year for Telegram Star giveaways."""

    def __init__(self, source: str, giveaway_message_id: int, user: User | None = None, prize_star_count: int | None = None, is_unclaimed: bool | None = None):
        self.source: str = source
        self.giveaway_message_id: int = giveaway_message_id
        self.user: User | None = user
        self.prize_star_count: int | None = prize_star_count
        self.is_unclaimed: bool | None = is_unclaimed

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
        if self.giveaway_message_id is not None:
            result['giveaway_message_id'] = _serialize(self.giveaway_message_id)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.prize_star_count is not None:
            result['prize_star_count'] = _serialize(self.prize_star_count)
        if self.is_unclaimed is not None:
            result['is_unclaimed'] = _serialize(self.is_unclaimed)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostSourceGiveaway' | None:
        if not data:
            return None
        from .user import User
        return cls(
            source=data.get('source'),
            giveaway_message_id=data.get('giveaway_message_id'),
            user=User.from_dict(data.get('user')),
            prize_star_count=data.get('prize_star_count'),
            is_unclaimed=data.get('is_unclaimed'),
        )