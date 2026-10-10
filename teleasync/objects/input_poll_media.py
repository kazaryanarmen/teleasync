from __future__ import annotations
from typing import TYPE_CHECKING



class InputPollMedia:
    """This object represents the content of a poll description or a quiz explanation to be sent. It should be one of - InputMediaAnimation - InputMediaAudio - InputMediaDocument - InputMediaLivePhoto - InputMediaLocation - InputMediaPhoto - InputMediaVenue - InputMediaVideo"""

    def __init__(self):
        pass

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputPollMedia' | None:
        if not data:
            return None
        return cls(
        )