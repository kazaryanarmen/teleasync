from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    


class Venue:
    """This object represents a venue."""

    def __init__(self, location: Location, title: str, address: str, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None):
        self.location: Location = location
        self.title: str = title
        self.address: str = address
        self.foursquare_id: str | None = foursquare_id
        self.foursquare_type: str | None = foursquare_type
        self.google_place_id: str | None = google_place_id
        self.google_place_type: str | None = google_place_type

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.address is not None:
            result['address'] = _serialize(self.address)
        if self.foursquare_id is not None:
            result['foursquare_id'] = _serialize(self.foursquare_id)
        if self.foursquare_type is not None:
            result['foursquare_type'] = _serialize(self.foursquare_type)
        if self.google_place_id is not None:
            result['google_place_id'] = _serialize(self.google_place_id)
        if self.google_place_type is not None:
            result['google_place_type'] = _serialize(self.google_place_type)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Venue' | None:
        if not data:
            return None
        from .location import Location
        return cls(
            location=Location.from_dict(data.get('location')),
            title=data.get('title'),
            address=data.get('address'),
            foursquare_id=data.get('foursquare_id'),
            foursquare_type=data.get('foursquare_type'),
            google_place_id=data.get('google_place_id'),
            google_place_type=data.get('google_place_type'),
        )