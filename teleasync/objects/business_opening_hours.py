from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .business_opening_hours_interval import BusinessOpeningHoursInterval
    


class BusinessOpeningHours:
    """Describes the opening hours of a business."""

    def __init__(self, time_zone_name: str, opening_hours: list[BusinessOpeningHoursInterval]):
        self.time_zone_name: str = time_zone_name
        self.opening_hours: list[BusinessOpeningHoursInterval] = opening_hours

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
        if self.time_zone_name is not None:
            result['time_zone_name'] = _serialize(self.time_zone_name)
        if self.opening_hours is not None:
            result['opening_hours'] = _serialize(self.opening_hours)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessOpeningHours' | None:
        if not data:
            return None
        from .business_opening_hours_interval import BusinessOpeningHoursInterval
        return cls(
            time_zone_name=data.get('time_zone_name'),
            opening_hours=[BusinessOpeningHoursInterval.from_dict(i1) for i1 in data.get('opening_hours')] if data.get('opening_hours') else None,
        )