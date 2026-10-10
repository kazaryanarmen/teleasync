from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .order_info import OrderInfo
    


class SuccessfulPayment:
    """This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control."""

    def __init__(self, currency: str, total_amount: int, invoice_payload: str, telegram_payment_charge_id: str, provider_payment_charge_id: str, subscription_expiration_date: int | None = None, is_recurring: bool | None = None, is_first_recurring: bool | None = None, shipping_option_id: str | None = None, order_info: OrderInfo | None = None):
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.telegram_payment_charge_id: str = telegram_payment_charge_id
        self.provider_payment_charge_id: str = provider_payment_charge_id
        self.subscription_expiration_date: int | None = subscription_expiration_date
        self.is_recurring: bool | None = is_recurring
        self.is_first_recurring: bool | None = is_first_recurring
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
        if self.currency is not None:
            result['currency'] = _serialize(self.currency)
        if self.total_amount is not None:
            result['total_amount'] = _serialize(self.total_amount)
        if self.invoice_payload is not None:
            result['invoice_payload'] = _serialize(self.invoice_payload)
        if self.telegram_payment_charge_id is not None:
            result['telegram_payment_charge_id'] = _serialize(self.telegram_payment_charge_id)
        if self.provider_payment_charge_id is not None:
            result['provider_payment_charge_id'] = _serialize(self.provider_payment_charge_id)
        if self.subscription_expiration_date is not None:
            result['subscription_expiration_date'] = _serialize(self.subscription_expiration_date)
        if self.is_recurring is not None:
            result['is_recurring'] = _serialize(self.is_recurring)
        if self.is_first_recurring is not None:
            result['is_first_recurring'] = _serialize(self.is_first_recurring)
        if self.shipping_option_id is not None:
            result['shipping_option_id'] = _serialize(self.shipping_option_id)
        if self.order_info is not None:
            result['order_info'] = _serialize(self.order_info)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuccessfulPayment' | None:
        if not data:
            return None
        from .order_info import OrderInfo
        return cls(
            currency=data.get('currency'),
            total_amount=data.get('total_amount'),
            invoice_payload=data.get('invoice_payload'),
            telegram_payment_charge_id=data.get('telegram_payment_charge_id'),
            provider_payment_charge_id=data.get('provider_payment_charge_id'),
            subscription_expiration_date=data.get('subscription_expiration_date'),
            is_recurring=data.get('is_recurring'),
            is_first_recurring=data.get('is_first_recurring'),
            shipping_option_id=data.get('shipping_option_id'),
            order_info=OrderInfo.from_dict(data.get('order_info')),
        )