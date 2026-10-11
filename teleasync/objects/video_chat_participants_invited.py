from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat."""

    def __init__(self, users: list[User]):
        self.users: list[User] = users

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
        if self.users is not None:
            result['users'] = _serialize(self.users)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'VideoChatParticipantsInvited' | None:
        if not data:
            return None
        from .user import User
        return cls(
            users=[User.from_dict(i1) for i1 in data.get('users')] if data.get('users') else None,
        )