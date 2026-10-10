from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user."""

    def __init__(self, traveler: User, watcher: User, distance: int):
        self.traveler: User = traveler
        self.watcher: User = watcher
        self.distance: int = distance

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
        if self.traveler is not None:
            result['traveler'] = _serialize(self.traveler)
        if self.watcher is not None:
            result['watcher'] = _serialize(self.watcher)
        if self.distance is not None:
            result['distance'] = _serialize(self.distance)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ProximityAlertTriggered' | None:
        if not data:
            return None
        from .user import User
        return cls(
            traveler=User.from_dict(data.get('traveler')),
            watcher=User.from_dict(data.get('watcher')),
            distance=data.get('distance'),
        )