from __future__ import annotations
from typing import TYPE_CHECKING



class Birthdate:
    """Describes the birthdate of a user."""

    def __init__(self, day: int, month: int, year: int | None = None):
        self.day: int = day
        self.month: int = month
        self.year: int | None = year

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
        if self.day is not None:
            result['day'] = _serialize(self.day)
        if self.month is not None:
            result['month'] = _serialize(self.month)
        if self.year is not None:
            result['year'] = _serialize(self.year)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Birthdate' | None:
        if not data:
            return None
        return cls(
            day=data.get('day'),
            month=data.get('month'),
            year=data.get('year'),
        )