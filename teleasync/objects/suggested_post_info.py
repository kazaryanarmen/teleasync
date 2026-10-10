from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .suggested_post_price import SuggestedPostPrice
    


class SuggestedPostInfo:
    """Contains information about a suggested post."""

    def __init__(self, state: str, price: SuggestedPostPrice | None = None, send_date: int | None = None):
        self.state: str = state
        self.price: SuggestedPostPrice | None = price
        self.send_date: int | None = send_date

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
        if self.state is not None:
            result['state'] = _serialize(self.state)
        if self.price is not None:
            result['price'] = _serialize(self.price)
        if self.send_date is not None:
            result['send_date'] = _serialize(self.send_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostInfo' | None:
        if not data:
            return None
        from .suggested_post_price import SuggestedPostPrice
        return cls(
            state=data.get('state'),
            price=SuggestedPostPrice.from_dict(data.get('price')),
            send_date=data.get('send_date'),
        )