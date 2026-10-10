from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    


class BusinessLocation:
    """Contains information about the location of a Telegram Business account."""

    def __init__(self, address: str, location: Location | None = None):
        self.address: str = address
        self.location: Location | None = location

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
        if self.address is not None:
            result['address'] = _serialize(self.address)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessLocation' | None:
        if not data:
            return None
        from .location import Location
        return cls(
            address=data.get('address'),
            location=Location.from_dict(data.get('location')),
        )