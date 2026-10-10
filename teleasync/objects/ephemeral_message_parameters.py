from __future__ import annotations
from typing import TYPE_CHECKING



class EphemeralMessageParameters:
    """Auto-generated Telegram object: EphemeralMessageParameters"""

    def __init__(self, receiver_user_id: int, callback_query_id: str | None = None, replace_callback_query_message: bool | None = None):
        self.receiver_user_id: int = receiver_user_id
        self.callback_query_id: str | None = callback_query_id
        self.replace_callback_query_message: bool | None = replace_callback_query_message

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
        if self.receiver_user_id is not None:
            result['receiver_user_id'] = _serialize(self.receiver_user_id)
        if self.callback_query_id is not None:
            result['callback_query_id'] = _serialize(self.callback_query_id)
        if self.replace_callback_query_message is not None:
            result['replace_callback_query_message'] = _serialize(self.replace_callback_query_message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'EphemeralMessageParameters' | None:
        if not data:
            return None
        return cls(
            receiver_user_id=data.get('receiver_user_id'),
            callback_query_id=data.get('callback_query_id'),
            replace_callback_query_message=data.get('replace_callback_query_message'),
        )