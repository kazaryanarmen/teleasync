from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatOwnerChanged:
    """Describes a service message about an ownership change in the chat."""

    def __init__(self, new_owner: User):
        self.new_owner: User = new_owner

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
        if self.new_owner is not None:
            result['new_owner'] = _serialize(self.new_owner)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatOwnerChanged' | None:
        if not data:
            return None
        from .user import User
        return cls(
            new_owner=User.from_dict(data.get('new_owner')),
        )