from __future__ import annotations
from typing import TYPE_CHECKING



class ReactionTypeCustomEmoji:
    """The reaction is based on a custom emoji."""

    def __init__(self, type: str, custom_emoji_id: str):
        self.type: str = type
        self.custom_emoji_id: str = custom_emoji_id

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
        if self.custom_emoji_id is not None:
            result['custom_emoji_id'] = _serialize(self.custom_emoji_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ReactionTypeCustomEmoji' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            custom_emoji_id=data.get('custom_emoji_id'),
        )