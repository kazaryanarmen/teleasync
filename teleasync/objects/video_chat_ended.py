from __future__ import annotations
from typing import TYPE_CHECKING



class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat."""

    def __init__(self, duration: int):
        self.duration: int = duration

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
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'VideoChatEnded' | None:
        if not data:
            return None
        return cls(
            duration=data.get('duration'),
        )