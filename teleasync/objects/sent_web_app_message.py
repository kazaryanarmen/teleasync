from __future__ import annotations
from typing import TYPE_CHECKING



class SentWebAppMessage:
    """Describes an inline message sent by a Web App on behalf of a user."""

    def __init__(self, inline_message_id: str | None = None):
        self.inline_message_id: str | None = inline_message_id

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
        if self.inline_message_id is not None:
            result['inline_message_id'] = _serialize(self.inline_message_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SentWebAppMessage' | None:
        if not data:
            return None
        return cls(
            inline_message_id=data.get('inline_message_id'),
        )