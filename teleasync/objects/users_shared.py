from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .shared_user import SharedUser
    


class UsersShared:
    """This object contains information about the users whose identifiers were shared with the bot using a KeyboardButtonRequestUsers button."""

    def __init__(self, request_id: int, users: list[SharedUser]):
        self.request_id: int = request_id
        self.users: list[SharedUser] = users

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
        if self.users is not None:
            result['users'] = _serialize(self.users)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UsersShared' | None:
        if not data:
            return None
        from .shared_user import SharedUser
        return cls(
            request_id=data.get('request_id'),
            users=[SharedUser.from_dict(i) for i in data.get('users')] if data.get('users') else None,
        )