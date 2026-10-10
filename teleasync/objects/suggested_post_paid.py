from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    
    from .star_amount import StarAmount
    


class SuggestedPostPaid:
    """Describes a service message about a successful payment for a suggested post."""

    def __init__(self, currency: str, suggested_post_message: Message | None = None, amount: int | None = None, star_amount: StarAmount | None = None):
        self.currency: str = currency
        self.suggested_post_message: Message | None = suggested_post_message
        self.amount: int | None = amount
        self.star_amount: StarAmount | None = star_amount

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
        if self.currency is not None:
            result['currency'] = _serialize(self.currency)
        if self.suggested_post_message is not None:
            result['suggested_post_message'] = _serialize(self.suggested_post_message)
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        if self.star_amount is not None:
            result['star_amount'] = _serialize(self.star_amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostPaid' | None:
        if not data:
            return None
        from .message import Message
        from .star_amount import StarAmount
        return cls(
            currency=data.get('currency'),
            suggested_post_message=Message.from_dict(data.get('suggested_post_message')),
            amount=data.get('amount'),
            star_amount=StarAmount.from_dict(data.get('star_amount')),
        )