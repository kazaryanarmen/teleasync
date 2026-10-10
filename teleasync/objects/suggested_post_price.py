from __future__ import annotations
from typing import TYPE_CHECKING



class SuggestedPostPrice:
    """Describes the price of a suggested post."""

    def __init__(self, currency: str, amount: int):
        self.currency: str = currency
        self.amount: int = amount

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
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostPrice' | None:
        if not data:
            return None
        return cls(
            currency=data.get('currency'),
            amount=data.get('amount'),
        )