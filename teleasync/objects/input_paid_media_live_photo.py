from __future__ import annotations
from typing import TYPE_CHECKING



class InputPaidMediaLivePhoto:
    """The paid media to send is a live photo."""

    def __init__(self, type: str, media: str, photo_: str):
        self.type: str = type
        self.media: str = media
        self.photo_: str = photo_

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
        if self.media is not None:
            result['media'] = _serialize(self.media)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputPaidMediaLivePhoto' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            media=data.get('media'),
            photo_=data.get('photo'),
        )