from __future__ import annotations
from typing import TYPE_CHECKING



class LocationAddress:
    """Describes the physical address of a location."""

    def __init__(self, country_code: str, state: str | None = None, city: str | None = None, street: str | None = None):
        self.country_code: str = country_code
        self.state: str | None = state
        self.city: str | None = city
        self.street: str | None = street

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
        if self.country_code is not None:
            result['country_code'] = _serialize(self.country_code)
        if self.state is not None:
            result['state'] = _serialize(self.state)
        if self.city is not None:
            result['city'] = _serialize(self.city)
        if self.street is not None:
            result['street'] = _serialize(self.street)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'LocationAddress' | None:
        if not data:
            return None
        return cls(
            country_code=data.get('country_code'),
            state=data.get('state'),
            city=data.get('city'),
            street=data.get('street'),
        )