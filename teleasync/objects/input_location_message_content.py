from __future__ import annotations
from typing import TYPE_CHECKING



class InputLocationMessageContent:
    """Represents the content of a location message to be sent as the result of an inline query."""

    def __init__(self, latitude: float, longitude: float, horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None):
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.horizontal_accuracy: float | None = horizontal_accuracy
        self.live_period: int | None = live_period
        self.heading: int | None = heading
        self.proximity_alert_radius: int | None = proximity_alert_radius

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
        if self.latitude is not None:
            result['latitude'] = _serialize(self.latitude)
        if self.longitude is not None:
            result['longitude'] = _serialize(self.longitude)
        if self.horizontal_accuracy is not None:
            result['horizontal_accuracy'] = _serialize(self.horizontal_accuracy)
        if self.live_period is not None:
            result['live_period'] = _serialize(self.live_period)
        if self.heading is not None:
            result['heading'] = _serialize(self.heading)
        if self.proximity_alert_radius is not None:
            result['proximity_alert_radius'] = _serialize(self.proximity_alert_radius)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputLocationMessageContent' | None:
        if not data:
            return None
        return cls(
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            horizontal_accuracy=data.get('horizontal_accuracy'),
            live_period=data.get('live_period'),
            heading=data.get('heading'),
            proximity_alert_radius=data.get('proximity_alert_radius'),
        )