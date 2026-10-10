from __future__ import annotations
from typing import TYPE_CHECKING



class ShippingAddress:
    """This object represents a shipping address."""

    def __init__(self, country_code: str, state: str, city: str, street_line1: str, street_line2: str, post_code: str):
        self.country_code: str = country_code
        self.state: str = state
        self.city: str = city
        self.street_line1: str = street_line1
        self.street_line2: str = street_line2
        self.post_code: str = post_code

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
        if self.country_code is not None:
            result['country_code'] = _serialize(self.country_code)
        if self.state is not None:
            result['state'] = _serialize(self.state)
        if self.city is not None:
            result['city'] = _serialize(self.city)
        if self.street_line1 is not None:
            result['street_line1'] = _serialize(self.street_line1)
        if self.street_line2 is not None:
            result['street_line2'] = _serialize(self.street_line2)
        if self.post_code is not None:
            result['post_code'] = _serialize(self.post_code)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ShippingAddress' | None:
        if not data:
            return None
        return cls(
            country_code=data.get('country_code'),
            state=data.get('state'),
            city=data.get('city'),
            street_line1=data.get('street_line1'),
            street_line2=data.get('street_line2'),
            post_code=data.get('post_code'),
        )