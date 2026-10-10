from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .star_transaction import StarTransaction
    


class StarTransactions:
    """Contains a list of Telegram Star transactions."""

    def __init__(self, transactions: list[StarTransaction]):
        self.transactions: list[StarTransaction] = transactions

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
        if self.transactions is not None:
            result['transactions'] = _serialize(self.transactions)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StarTransactions' | None:
        if not data:
            return None
        from .star_transaction import StarTransaction
        return cls(
            transactions=[StarTransaction.from_dict(i) for i in data.get('transactions')] if data.get('transactions') else None,
        )