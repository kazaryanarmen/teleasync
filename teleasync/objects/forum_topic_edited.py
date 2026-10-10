from __future__ import annotations
from typing import TYPE_CHECKING



class ForumTopicEdited:
    """This object represents a service message about an edited forum topic."""

    def __init__(self, name: str | None = None, icon_custom_emoji_id: str | None = None):
        self.name: str | None = name
        self.icon_custom_emoji_id: str | None = icon_custom_emoji_id

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
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.icon_custom_emoji_id is not None:
            result['icon_custom_emoji_id'] = _serialize(self.icon_custom_emoji_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ForumTopicEdited' | None:
        if not data:
            return None
        return cls(
            name=data.get('name'),
            icon_custom_emoji_id=data.get('icon_custom_emoji_id'),
        )