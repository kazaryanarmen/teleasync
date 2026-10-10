from __future__ import annotations
from typing import TYPE_CHECKING



class Chat:
    """This object represents a chat."""

    def __init__(self, id: int, type: str, title: str | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, is_forum: bool | None = None, is_direct_messages: bool | None = None):
        self.id: int = id
        self.type: str = type
        self.title: str | None = title
        self.username: str | None = username
        self.first_name: str | None = first_name
        self.last_name: str | None = last_name
        self.is_forum: bool | None = is_forum
        self.is_direct_messages: bool | None = is_direct_messages

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.username is not None:
            result['username'] = _serialize(self.username)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.is_forum is not None:
            result['is_forum'] = _serialize(self.is_forum)
        if self.is_direct_messages is not None:
            result['is_direct_messages'] = _serialize(self.is_direct_messages)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Chat' | None:
        if not data:
            return None
        return cls(
            id=data.get('id'),
            type=data.get('type'),
            title=data.get('title'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            is_forum=data.get('is_forum'),
            is_direct_messages=data.get('is_direct_messages'),
        )