from __future__ import annotations
from typing import TYPE_CHECKING



class PreparedKeyboardButton:
    """Describes a keyboard button to be used by a user of a Mini App."""

    def __init__(self, id: str):
        self.id: str = id

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PreparedKeyboardButton' | None:
        if not data:
            return None
        return cls(
            id=data.get('id'),
        )