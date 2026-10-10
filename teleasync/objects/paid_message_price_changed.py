from __future__ import annotations
from typing import TYPE_CHECKING



class PaidMessagePriceChanged:
    """Describes a service message about a change in the price of paid messages within a chat."""

    def __init__(self, paid_message_star_count: int):
        self.paid_message_star_count: int = paid_message_star_count

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
        if self.paid_message_star_count is not None:
            result['paid_message_star_count'] = _serialize(self.paid_message_star_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMessagePriceChanged' | None:
        if not data:
            return None
        return cls(
            paid_message_star_count=data.get('paid_message_star_count'),
        )