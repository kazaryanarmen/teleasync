from __future__ import annotations
from typing import TYPE_CHECKING



class LabeledPrice:
    """This object represents a portion of the price for goods or services."""

    def __init__(self, label: str, amount: int):
        self.label: str = label
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
        if self.label is not None:
            result['label'] = _serialize(self.label)
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'LabeledPrice' | None:
        if not data:
            return None
        return cls(
            label=data.get('label'),
            amount=data.get('amount'),
        )