from __future__ import annotations
from typing import TYPE_CHECKING



class ForumTopic:
    """This object represents a forum topic."""

    def __init__(self, message_thread_id: int, name: str, icon_color: int, icon_custom_emoji_id: str | None = None, is_name_implicit: bool | None = None):
        self.message_thread_id: int = message_thread_id
        self.name: str = name
        self.icon_color: int = icon_color
        self.icon_custom_emoji_id: str | None = icon_custom_emoji_id
        self.is_name_implicit: bool | None = is_name_implicit

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
        if self.message_thread_id is not None:
            result['message_thread_id'] = _serialize(self.message_thread_id)
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.icon_color is not None:
            result['icon_color'] = _serialize(self.icon_color)
        if self.icon_custom_emoji_id is not None:
            result['icon_custom_emoji_id'] = _serialize(self.icon_custom_emoji_id)
        if self.is_name_implicit is not None:
            result['is_name_implicit'] = _serialize(self.is_name_implicit)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ForumTopic' | None:
        if not data:
            return None
        return cls(
            message_thread_id=data.get('message_thread_id'),
            name=data.get('name'),
            icon_color=data.get('icon_color'),
            icon_custom_emoji_id=data.get('icon_custom_emoji_id'),
            is_name_implicit=data.get('is_name_implicit'),
        )