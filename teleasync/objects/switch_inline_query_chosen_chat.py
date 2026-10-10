from __future__ import annotations
from typing import TYPE_CHECKING



class SwitchInlineQueryChosenChat:
    """This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query."""

    def __init__(self, query: str | None = None, allow_user_chats: bool | None = None, allow_bot_chats: bool | None = None, allow_group_chats: bool | None = None, allow_channel_chats: bool | None = None):
        self.query: str | None = query
        self.allow_user_chats: bool | None = allow_user_chats
        self.allow_bot_chats: bool | None = allow_bot_chats
        self.allow_group_chats: bool | None = allow_group_chats
        self.allow_channel_chats: bool | None = allow_channel_chats

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
        if self.query is not None:
            result['query'] = _serialize(self.query)
        if self.allow_user_chats is not None:
            result['allow_user_chats'] = _serialize(self.allow_user_chats)
        if self.allow_bot_chats is not None:
            result['allow_bot_chats'] = _serialize(self.allow_bot_chats)
        if self.allow_group_chats is not None:
            result['allow_group_chats'] = _serialize(self.allow_group_chats)
        if self.allow_channel_chats is not None:
            result['allow_channel_chats'] = _serialize(self.allow_channel_chats)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SwitchInlineQueryChosenChat' | None:
        if not data:
            return None
        return cls(
            query=data.get('query'),
            allow_user_chats=data.get('allow_user_chats'),
            allow_bot_chats=data.get('allow_bot_chats'),
            allow_group_chats=data.get('allow_group_chats'),
            allow_channel_chats=data.get('allow_channel_chats'),
        )