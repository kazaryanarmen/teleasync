from __future__ import annotations
from typing import TYPE_CHECKING



class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat."""

    def __init__(self, start_date: int):
        self.start_date: int = start_date

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
        if self.start_date is not None:
            result['start_date'] = _serialize(self.start_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'VideoChatScheduled' | None:
        if not data:
            return None
        return cls(
            start_date=data.get('start_date'),
        )