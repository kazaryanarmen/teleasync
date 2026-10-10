from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    
    from .suggested_post_price import SuggestedPostPrice
    


class SuggestedPostApprovalFailed:
    """Describes a service message about the failed approval of a suggested post. Currently, only caused by insufficient user funds at the time of approval."""

    def __init__(self, price: SuggestedPostPrice, suggested_post_message: Message | None = None):
        self.price: SuggestedPostPrice = price
        self.suggested_post_message: Message | None = suggested_post_message

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
        if self.price is not None:
            result['price'] = _serialize(self.price)
        if self.suggested_post_message is not None:
            result['suggested_post_message'] = _serialize(self.suggested_post_message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostApprovalFailed' | None:
        if not data:
            return None
        from .message import Message
        from .suggested_post_price import SuggestedPostPrice
        return cls(
            price=SuggestedPostPrice.from_dict(data.get('price')),
            suggested_post_message=Message.from_dict(data.get('suggested_post_message')),
        )