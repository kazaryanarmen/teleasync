from __future__ import annotations
from typing import TYPE_CHECKING



class TransactionPartnerTelegramApi:
    """Describes a transaction with payment for paid broadcasting."""

    def __init__(self, type: str, request_count: int):
        self.type: str = type
        self.request_count: int = request_count

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
        if self.request_count is not None:
            result['request_count'] = _serialize(self.request_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerTelegramApi' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            request_count=data.get('request_count'),
        )