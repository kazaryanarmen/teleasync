from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .transaction_partner import TransactionPartner
    


class StarTransaction:
    """Describes a Telegram Star transaction. Note that if the buyer initiates a chargeback with the payment provider from whom they acquired Stars (e.g., Apple, Google) following this transaction, the refunded Stars will be deducted from the bot's balance. This is outside of Telegram's control."""

    def __init__(self, id: str, amount: int, date: int, nanostar_amount: int | None = None, source: TransactionPartner | None = None, receiver: TransactionPartner | None = None):
        self.id: str = id
        self.amount: int = amount
        self.date: int = date
        self.nanostar_amount: int | None = nanostar_amount
        self.source: TransactionPartner | None = source
        self.receiver: TransactionPartner | None = receiver

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
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.nanostar_amount is not None:
            result['nanostar_amount'] = _serialize(self.nanostar_amount)
        if self.source is not None:
            result['source'] = _serialize(self.source)
        if self.receiver is not None:
            result['receiver'] = _serialize(self.receiver)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StarTransaction' | None:
        if not data:
            return None
        from .transaction_partner import TransactionPartner
        return cls(
            id=data.get('id'),
            amount=data.get('amount'),
            date=data.get('date'),
            nanostar_amount=data.get('nanostar_amount'),
            source=TransactionPartner.from_dict(data.get('source')),
            receiver=TransactionPartner.from_dict(data.get('receiver')),
        )