from __future__ import annotations
from typing import TYPE_CHECKING



class InputStoryContentVideo:
    """Describes a video to post as a story."""

    def __init__(self, type: str, video_: str, duration: float | None = None, cover_frame_timestamp: float | None = None, is_animation: bool | None = None):
        self.type: str = type
        self.video_: str = video_
        self.duration: float | None = duration
        self.cover_frame_timestamp: float | None = cover_frame_timestamp
        self.is_animation: bool | None = is_animation

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
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.cover_frame_timestamp is not None:
            result['cover_frame_timestamp'] = _serialize(self.cover_frame_timestamp)
        if self.is_animation is not None:
            result['is_animation'] = _serialize(self.is_animation)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputStoryContentVideo' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            video_=data.get('video'),
            duration=data.get('duration'),
            cover_frame_timestamp=data.get('cover_frame_timestamp'),
            is_animation=data.get('is_animation'),
        )