from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    


class SharedUser:
    """This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUsers button."""

    def __init__(self, user_id: int, first_name: str | None = None, last_name: str | None = None, username: str | None = None, photo_: list[PhotoSize] | None = None):
        self.user_id: int = user_id
        self.first_name: str | None = first_name
        self.last_name: str | None = last_name
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
        if self.user_id is not None:
            result['user_id'] = _serialize(self.user_id)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.username is not None:
            result['username'] = _serialize(self.username)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SharedUser' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        return cls(
            user_id=data.get('user_id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            username=data.get('username'),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
        )