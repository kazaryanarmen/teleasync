from __future__ import annotations
from typing import TYPE_CHECKING



class UserRating:
    """This object describes the rating of a user based on their Telegram Star spendings."""

    def __init__(self, level: int, rating: int, current_level_rating: int, next_level_rating: int | None = None):
        self.level: int = level
        self.rating: int = rating
        self.current_level_rating: int = current_level_rating
        self.next_level_rating: int | None = next_level_rating

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
        if self.level is not None:
            result['level'] = _serialize(self.level)
        if self.rating is not None:
            result['rating'] = _serialize(self.rating)
        if self.current_level_rating is not None:
            result['current_level_rating'] = _serialize(self.current_level_rating)
        if self.next_level_rating is not None:
            result['next_level_rating'] = _serialize(self.next_level_rating)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UserRating' | None:
        if not data:
            return None
        return cls(
            level=data.get('level'),
            rating=data.get('rating'),
            current_level_rating=data.get('current_level_rating'),
            next_level_rating=data.get('next_level_rating'),
        )