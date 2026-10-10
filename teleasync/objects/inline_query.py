from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    
    from .user import User
    


class InlineQuery:
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results."""

    def __init__(self, id: str, from_: User, query: str, offset: str, chat_type: str | None = None, location: Location | None = None):
        self.id: str = id
        self.from_: User = from_
        self.query: str = query
        self.offset: str = offset
        self.chat_type: str | None = chat_type
        self.location: Location | None = location

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
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.query is not None:
            result['query'] = _serialize(self.query)
        if self.offset is not None:
            result['offset'] = _serialize(self.offset)
        if self.chat_type is not None:
            result['chat_type'] = _serialize(self.chat_type)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQuery' | None:
        if not data:
            return None
        from .location import Location
        from .user import User
        return cls(
            id=data.get('id'),
            from_=User.from_dict(data.get('from')),
            query=data.get('query'),
            offset=data.get('offset'),
            chat_type=data.get('chat_type'),
            location=Location.from_dict(data.get('location')),
        )