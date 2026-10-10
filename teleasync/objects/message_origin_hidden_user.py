from __future__ import annotations
from typing import TYPE_CHECKING



class MessageOriginHiddenUser:
    """The message was originally sent by an unknown user."""

    def __init__(self, type: str, date: int, sender_user_name: str):
        self.type: str = type
        self.date: int = date
        self.sender_user_name: str = sender_user_name

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
        if self.sender_user_name is not None:
            result['sender_user_name'] = _serialize(self.sender_user_name)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageOriginHiddenUser' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            date=data.get('date'),
            sender_user_name=data.get('sender_user_name'),
        )