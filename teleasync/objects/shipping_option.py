from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .labeled_price import LabeledPrice
    


class ShippingOption:
    """This object represents one shipping option."""

    def __init__(self, id: str, title: str, prices: list[LabeledPrice]):
        self.id: str = id
        self.title: str = title
        self.prices: list[LabeledPrice] = prices

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.prices is not None:
            result['prices'] = _serialize(self.prices)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ShippingOption' | None:
        if not data:
            return None
        from .labeled_price import LabeledPrice
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            prices=[LabeledPrice.from_dict(i1) for i1 in data.get('prices')] if data.get('prices') else None,
        )