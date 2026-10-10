from __future__ import annotations
from typing import TYPE_CHECKING



class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode. Not supported in channels and for messages sent on behalf of a user account."""

    def __init__(self, force_reply: bool, input_field_placeholder: str | None = None, selective: bool | None = None):
        self.force_reply: bool = force_reply
        self.input_field_placeholder: str | None = input_field_placeholder
        self.selective: bool | None = selective

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
        if self.force_reply is not None:
            result['force_reply'] = _serialize(self.force_reply)
        if self.input_field_placeholder is not None:
            result['input_field_placeholder'] = _serialize(self.input_field_placeholder)
        if self.selective is not None:
            result['selective'] = _serialize(self.selective)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ForceReply' | None:
        if not data:
            return None
        return cls(
            force_reply=data.get('force_reply'),
            input_field_placeholder=data.get('input_field_placeholder'),
            selective=data.get('selective'),
        )