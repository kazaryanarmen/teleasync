from __future__ import annotations
from typing import TYPE_CHECKING



class Voice:
    """This object represents a voice note."""

    def __init__(self, file_id: str, file_unique_id: str, duration: int, mime_type: str | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.duration: int = duration
        self.mime_type: str | None = mime_type
        self.file_size: int | None = file_size

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
        if self.file_id is not None:
            result['file_id'] = _serialize(self.file_id)
        if self.file_unique_id is not None:
            result['file_unique_id'] = _serialize(self.file_unique_id)
        if self.duration is not None:
            result['duration'] = _serialize(self.duration)
        if self.mime_type is not None:
            result['mime_type'] = _serialize(self.mime_type)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Voice' | None:
        if not data:
            return None
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            duration=data.get('duration'),
            mime_type=data.get('mime_type'),
            file_size=data.get('file_size'),
        )