from __future__ import annotations
from typing import TYPE_CHECKING



class KeyboardButtonRequestManagedBot:
    """This object defines the parameters for the creation of a managed bot. Information about the created bot will be shared with the bot using the update managed_bot and a Message with the field managed_bot_created."""

    def __init__(self, request_id: int, suggested_name: str | None = None, suggested_username: str | None = None):
        self.request_id: int = request_id
        self.suggested_name: str | None = suggested_name
        self.suggested_username: str | None = suggested_username

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
        if self.request_id is not None:
            result['request_id'] = _serialize(self.request_id)
        if self.suggested_name is not None:
            result['suggested_name'] = _serialize(self.suggested_name)
        if self.suggested_username is not None:
            result['suggested_username'] = _serialize(self.suggested_username)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'KeyboardButtonRequestManagedBot' | None:
        if not data:
            return None
        return cls(
            request_id=data.get('request_id'),
            suggested_name=data.get('suggested_name'),
            suggested_username=data.get('suggested_username'),
        )