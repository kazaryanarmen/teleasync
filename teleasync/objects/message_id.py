from __future__ import annotations
from typing import TYPE_CHECKING



class MessageId:
    """This object represents a unique message identifier."""

    def __init__(self, message_id: int):
        self.message_id: int = message_id

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
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageId' | None:
        if not data:
            return None
        return cls(
            message_id=data.get('message_id'),
        )