from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .video import Video
    


class PaidMediaVideo:
    """The paid media is a video."""

    def __init__(self, type: str, video_: Video):
        self.type: str = type
        self.video_: Video = video_

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
        if self.video_ is not None:
            result['video'] = _serialize(self.video_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaVideo' | None:
        if not data:
            return None
        from .video import Video
        return cls(
            type=data.get('type'),
            video_=Video.from_dict(data.get('video')),
        )