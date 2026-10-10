from __future__ import annotations
from typing import TYPE_CHECKING



class RevenueWithdrawalStateSucceeded:
    """The withdrawal succeeded."""

    def __init__(self, type: str, date: int, url: str):
        self.type: str = type
        self.date: int = date
        self.url: str = url

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.url is not None:
            result['url'] = _serialize(self.url)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RevenueWithdrawalStateSucceeded' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            date=data.get('date'),
            url=data.get('url'),
        )