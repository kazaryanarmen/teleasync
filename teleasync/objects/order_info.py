from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .shipping_address import ShippingAddress
    


class OrderInfo:
    """This object represents information about an order."""

    def __init__(self, name: str | None = None, phone_number: str | None = None, email: str | None = None, shipping_address: ShippingAddress | None = None):
        self.name: str | None = name
        self.phone_number: str | None = phone_number
        self.email: str | None = email
        self.shipping_address: ShippingAddress | None = shipping_address

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
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.phone_number is not None:
            result['phone_number'] = _serialize(self.phone_number)
        if self.email is not None:
            result['email'] = _serialize(self.email)
        if self.shipping_address is not None:
            result['shipping_address'] = _serialize(self.shipping_address)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'OrderInfo' | None:
        if not data:
            return None
        from .shipping_address import ShippingAddress
        return cls(
            name=data.get('name'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            shipping_address=ShippingAddress.from_dict(data.get('shipping_address')),
        )