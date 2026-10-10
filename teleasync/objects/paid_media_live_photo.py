from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .live_photo import LivePhoto
    


class PaidMediaLivePhoto:
    """The paid media is a live photo."""

    def __init__(self, type: str, live_photo: LivePhoto):
        self.type: str = type
        self.live_photo: LivePhoto = live_photo

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
        if self.live_photo is not None:
            result['live_photo'] = _serialize(self.live_photo)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaLivePhoto' | None:
        if not data:
            return None
        from .live_photo import LivePhoto
        return cls(
            type=data.get('type'),
            live_photo=LivePhoto.from_dict(data.get('live_photo')),
        )