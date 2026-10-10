from __future__ import annotations
from typing import TYPE_CHECKING



class BusinessOpeningHoursInterval:
    """Describes an interval of time during which a business is open."""

    def __init__(self, opening_minute: int, closing_minute: int):
        self.opening_minute: int = opening_minute
        self.closing_minute: int = closing_minute

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
        if self.opening_minute is not None:
            result['opening_minute'] = _serialize(self.opening_minute)
        if self.closing_minute is not None:
            result['closing_minute'] = _serialize(self.closing_minute)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessOpeningHoursInterval' | None:
        if not data:
            return None
        return cls(
            opening_minute=data.get('opening_minute'),
            closing_minute=data.get('closing_minute'),
        )