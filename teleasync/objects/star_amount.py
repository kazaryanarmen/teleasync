from __future__ import annotations
from typing import TYPE_CHECKING



class StarAmount:
    """Describes an amount of Telegram Stars."""

    def __init__(self, amount: int, nanostar_amount: int | None = None):
        self.amount: int = amount
        self.nanostar_amount: int | None = nanostar_amount

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
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        if self.nanostar_amount is not None:
            result['nanostar_amount'] = _serialize(self.nanostar_amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StarAmount' | None:
        if not data:
            return None
        return cls(
            amount=data.get('amount'),
            nanostar_amount=data.get('nanostar_amount'),
        )