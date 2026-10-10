from __future__ import annotations
from typing import TYPE_CHECKING



class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings."""

    def __init__(self, message_auto_delete_time: int):
        self.message_auto_delete_time: int = message_auto_delete_time

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
        if self.message_auto_delete_time is not None:
            result['message_auto_delete_time'] = _serialize(self.message_auto_delete_time)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageAutoDeleteTimerChanged' | None:
        if not data:
            return None
        return cls(
            message_auto_delete_time=data.get('message_auto_delete_time'),
        )