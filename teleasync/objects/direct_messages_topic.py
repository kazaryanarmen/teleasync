from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class DirectMessagesTopic:
    """Describes a topic of a direct messages chat."""

    def __init__(self, topic_id: int, user: User | None = None):
        self.topic_id: int = topic_id
        self.user: User | None = user

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
        if self.topic_id is not None:
            result['topic_id'] = _serialize(self.topic_id)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'DirectMessagesTopic' | None:
        if not data:
            return None
        from .user import User
        return cls(
            topic_id=data.get('topic_id'),
            user=User.from_dict(data.get('user')),
        )