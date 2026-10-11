from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_file import InputFile
    


class InputProfilePhotoAnimated:
    """An animated profile photo in the MPEG4 format."""

    def __init__(self, type: str, animation: InputFile | str, main_frame_timestamp: float | None = None):
        self.type: str = type
        self.animation: InputFile | str = animation
        self.main_frame_timestamp: float | None = main_frame_timestamp

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
        if self.animation is not None:
            result['animation'] = _serialize(self.animation)
        if self.main_frame_timestamp is not None:
            result['main_frame_timestamp'] = _serialize(self.main_frame_timestamp)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputProfilePhotoAnimated' | None:
        if not data:
            return None
        from .input_file import InputFile
        return cls(
            type=data.get('type'),
            animation=data.get('animation'),
            main_frame_timestamp=data.get('main_frame_timestamp'),
        )