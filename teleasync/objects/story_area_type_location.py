from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location_address import LocationAddress
    


class StoryAreaTypeLocation:
    """Describes a story area pointing to a location. Currently, a story can have up to 10 location areas."""

    def __init__(self, type: str, latitude: float, longitude: float, address: LocationAddress | None = None):
        self.type: str = type
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.address: LocationAddress | None = address

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.latitude is not None:
            result['latitude'] = _serialize(self.latitude)
        if self.longitude is not None:
            result['longitude'] = _serialize(self.longitude)
        if self.address is not None:
            result['address'] = _serialize(self.address)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryAreaTypeLocation' | None:
        if not data:
            return None
        from .location_address import LocationAddress
        return cls(
            type=data.get('type'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            address=LocationAddress.from_dict(data.get('address')),
        )