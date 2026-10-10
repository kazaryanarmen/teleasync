from __future__ import annotations
from typing import TYPE_CHECKING



class PreparedInlineMessage:
    """Describes an inline message to be sent by a user of a Mini App."""

    def __init__(self, id: str, expiration_date: int):
        self.id: str = id
        self.expiration_date: int = expiration_date

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
        if self.expiration_date is not None:
            result['expiration_date'] = _serialize(self.expiration_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PreparedInlineMessage' | None:
        if not data:
            return None
        return cls(
            id=data.get('id'),
            expiration_date=data.get('expiration_date'),
        )