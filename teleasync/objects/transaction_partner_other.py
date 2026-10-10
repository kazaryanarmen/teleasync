from __future__ import annotations
from typing import TYPE_CHECKING



class TransactionPartnerOther:
    """Describes a transaction with an unknown source or recipient."""

    def __init__(self, type: str):
        self.type: str = type

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerOther' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
        )