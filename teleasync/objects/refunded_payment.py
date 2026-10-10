from __future__ import annotations
from typing import TYPE_CHECKING



class RefundedPayment:
    """This object contains basic information about a refunded payment."""

    def __init__(self, currency: str, total_amount: int, invoice_payload: str, telegram_payment_charge_id: str, provider_payment_charge_id: str | None = None):
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.telegram_payment_charge_id: str = telegram_payment_charge_id
        self.provider_payment_charge_id: str | None = provider_payment_charge_id

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RefundedPayment' | None:
        if not data:
            return None
        return cls(
            currency=data.get('currency'),
            total_amount=data.get('total_amount'),
            invoice_payload=data.get('invoice_payload'),
            telegram_payment_charge_id=data.get('telegram_payment_charge_id'),
            provider_payment_charge_id=data.get('provider_payment_charge_id'),
        )