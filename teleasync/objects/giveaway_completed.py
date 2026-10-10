from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    


class GiveawayCompleted:
    """This object represents a service message about the completion of a giveaway without public winners."""

    def __init__(self, winner_count: int, unclaimed_prize_count: int | None = None, giveaway_message: Message | None = None, is_star_giveaway: bool | None = None):
        self.winner_count: int = winner_count
        self.unclaimed_prize_count: int | None = unclaimed_prize_count
        self.giveaway_message: Message | None = giveaway_message
        self.is_star_giveaway: bool | None = is_star_giveaway

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
        if self.winner_count is not None:
            result['winner_count'] = _serialize(self.winner_count)
        if self.unclaimed_prize_count is not None:
            result['unclaimed_prize_count'] = _serialize(self.unclaimed_prize_count)
        if self.giveaway_message is not None:
            result['giveaway_message'] = _serialize(self.giveaway_message)
        if self.is_star_giveaway is not None:
            result['is_star_giveaway'] = _serialize(self.is_star_giveaway)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'GiveawayCompleted' | None:
        if not data:
            return None
        from .message import Message
        return cls(
            winner_count=data.get('winner_count'),
            unclaimed_prize_count=data.get('unclaimed_prize_count'),
            giveaway_message=Message.from_dict(data.get('giveaway_message')),
            is_star_giveaway=data.get('is_star_giveaway'),
        )