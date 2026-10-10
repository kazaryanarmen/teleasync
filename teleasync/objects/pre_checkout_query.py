from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .order_info import OrderInfo
    
    from .user import User
    


class PreCheckoutQuery:
    """This object contains information about an incoming pre-checkout query."""

    def __init__(self, id: str, from_: User, currency: str, total_amount: int, invoice_payload: str, shipping_option_id: str | None = None, order_info: OrderInfo | None = None):
        self.id: str = id
        self.from_: User = from_
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.shipping_option_id: str | None = shipping_option_id
        self.order_info: OrderInfo | None = order_info

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
        if self.currency is not None:
            result['currency'] = _serialize(self.currency)
        if self.total_amount is not None:
            result['total_amount'] = _serialize(self.total_amount)
        if self.invoice_payload is not None:
            result['invoice_payload'] = _serialize(self.invoice_payload)
        if self.shipping_option_id is not None:
            result['shipping_option_id'] = _serialize(self.shipping_option_id)
        if self.order_info is not None:
            result['order_info'] = _serialize(self.order_info)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PreCheckoutQuery' | None:
        if not data:
            return None
        from .order_info import OrderInfo
        from .user import User
        return cls(
            id=data.get('id'),
            from_=User.from_dict(data.get('from')),
            currency=data.get('currency'),
            total_amount=data.get('total_amount'),
            invoice_payload=data.get('invoice_payload'),
            shipping_option_id=data.get('shipping_option_id'),
            order_info=OrderInfo.from_dict(data.get('order_info')),
        )