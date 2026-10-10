from __future__ import annotations
from typing import TYPE_CHECKING



class ResponseParameters:
    """Describes why a request was unsuccessful."""

    def __init__(self, migrate_to_chat_id: int | None = None, retry_after: int | None = None):
        self.migrate_to_chat_id: int | None = migrate_to_chat_id
        self.retry_after: int | None = retry_after

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
        if self.migrate_to_chat_id is not None:
            result['migrate_to_chat_id'] = _serialize(self.migrate_to_chat_id)
        if self.retry_after is not None:
            result['retry_after'] = _serialize(self.retry_after)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ResponseParameters' | None:
        if not data:
            return None
        return cls(
            migrate_to_chat_id=data.get('migrate_to_chat_id'),
            retry_after=data.get('retry_after'),
        )