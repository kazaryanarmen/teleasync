from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class ChatShared:
    """This object contains information about a chat that was shared with the bot using a KeyboardButtonRequestChat button."""

    def __init__(self, request_id: int, chat_id: int, title: str | None = None, username: str | None = None, photo_: list[PhotoSize] | None = None):
        self.request_id: int = request_id
        self.chat_id: int = chat_id
        self.title: str | None = title
        self.username: str | None = username
        self.photo_: list[PhotoSize] | None = photo_

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
        if self.chat_id is not None:
            result['chat_id'] = _serialize(self.chat_id)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.username is not None:
            result['username'] = _serialize(self.username)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatShared' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            request_id=data.get('request_id'),
            chat_id=data.get('chat_id'),
            title=data.get('title'),
            username=data.get('username'),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
        )