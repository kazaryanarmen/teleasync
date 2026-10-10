from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    
    from .suggested_post_price import SuggestedPostPrice
    


class SuggestedPostApproved:
    """Describes a service message about the approval of a suggested post."""

    def __init__(self, send_date: int, suggested_post_message: Message | None = None, price: SuggestedPostPrice | None = None):
        self.send_date: int = send_date
        self.suggested_post_message: Message | None = suggested_post_message
        self.price: SuggestedPostPrice | None = price

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
        if self.send_date is not None:
            result['send_date'] = _serialize(self.send_date)
        if self.suggested_post_message is not None:
            result['suggested_post_message'] = _serialize(self.suggested_post_message)
        if self.price is not None:
            result['price'] = _serialize(self.price)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostApproved' | None:
        if not data:
            return None
        from .message import Message
        from .suggested_post_price import SuggestedPostPrice
        return cls(
            send_date=data.get('send_date'),
            suggested_post_message=Message.from_dict(data.get('suggested_post_message')),
            price=SuggestedPostPrice.from_dict(data.get('price')),
        )