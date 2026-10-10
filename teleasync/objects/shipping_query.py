from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .shipping_address import ShippingAddress
    
    from .user import User
    


class ShippingQuery:
    """This object contains information about an incoming shipping query."""

    def __init__(self, id: str, from_: User, invoice_payload: str, shipping_address: ShippingAddress):
        self.id: str = id
        self.from_: User = from_
        self.invoice_payload: str = invoice_payload
        self.shipping_address: ShippingAddress = shipping_address

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
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.invoice_payload is not None:
            result['invoice_payload'] = _serialize(self.invoice_payload)
        if self.shipping_address is not None:
            result['shipping_address'] = _serialize(self.shipping_address)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ShippingQuery' | None:
        if not data:
            return None
        from .shipping_address import ShippingAddress
        from .user import User
        return cls(
            id=data.get('id'),
            from_=User.from_dict(data.get('from')),
            invoice_payload=data.get('invoice_payload'),
            shipping_address=ShippingAddress.from_dict(data.get('shipping_address')),
        )