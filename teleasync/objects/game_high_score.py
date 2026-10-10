from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class GameHighScore:
    """This object represents one row of the high scores table for a game."""

    def __init__(self, position: int, user: User, score: int):
        self.position: int = position
        self.user: User = user
        self.score: int = score

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
        if self.position is not None:
            result['position'] = _serialize(self.position)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.score is not None:
            result['score'] = _serialize(self.score)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'GameHighScore' | None:
        if not data:
            return None
        from .user import User
        return cls(
            position=data.get('position'),
            user=User.from_dict(data.get('user')),
            score=data.get('score'),
        )