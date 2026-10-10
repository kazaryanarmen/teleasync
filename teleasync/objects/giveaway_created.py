from __future__ import annotations
from typing import TYPE_CHECKING



class GiveawayCreated:
    """This object represents a service message about the creation of a scheduled giveaway."""

    def __init__(self, prize_star_count: int | None = None):
        self.prize_star_count: int | None = prize_star_count

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
        if self.prize_star_count is not None:
            result['prize_star_count'] = _serialize(self.prize_star_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'GiveawayCreated' | None:
        if not data:
            return None
        return cls(
            prize_star_count=data.get('prize_star_count'),
        )