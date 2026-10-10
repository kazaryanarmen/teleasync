from __future__ import annotations
from typing import TYPE_CHECKING



class Invoice:
    """This object contains basic information about an invoice."""

    def __init__(self, title: str, description: str, start_parameter: str, currency: str, total_amount: int):
        self.title: str = title
        self.description: str = description
        self.start_parameter: str = start_parameter
        self.currency: str = currency
        self.total_amount: int = total_amount

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.start_parameter is not None:
            result['start_parameter'] = _serialize(self.start_parameter)
        if self.currency is not None:
            result['currency'] = _serialize(self.currency)
        if self.total_amount is not None:
            result['total_amount'] = _serialize(self.total_amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Invoice' | None:
        if not data:
            return None
        return cls(
            title=data.get('title'),
            description=data.get('description'),
            start_parameter=data.get('start_parameter'),
            currency=data.get('currency'),
            total_amount=data.get('total_amount'),
        )