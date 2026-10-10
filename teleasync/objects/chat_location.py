from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    


class ChatLocation:
    """Represents a location to which a chat is connected."""

    def __init__(self, location: Location, address: str):
        self.location: Location = location
        self.address: str = address

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
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.address is not None:
            result['address'] = _serialize(self.address)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatLocation' | None:
        if not data:
            return None
        from .location import Location
        return cls(
            location=Location.from_dict(data.get('location')),
            address=data.get('address'),
        )