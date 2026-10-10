from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    
    from .user import User
    


class ChosenInlineResult:
    """Represents a result of an inline query that was chosen by the user and sent to their chat partner. Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates."""

    def __init__(self, result_id: str, from_: User, query: str, location: Location | None = None, inline_message_id: str | None = None):
        self.result_id: str = result_id
        self.from_: User = from_
        self.query: str = query
        self.location: Location | None = location
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
        if self.result_id is not None:
            result['result_id'] = _serialize(self.result_id)
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.query is not None:
            result['query'] = _serialize(self.query)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.inline_message_id is not None:
            result['inline_message_id'] = _serialize(self.inline_message_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChosenInlineResult' | None:
        if not data:
            return None
        from .location import Location
        from .user import User
        return cls(
            result_id=data.get('result_id'),
            from_=User.from_dict(data.get('from')),
            query=data.get('query'),
            location=Location.from_dict(data.get('location')),
            inline_message_id=data.get('inline_message_id'),
        )