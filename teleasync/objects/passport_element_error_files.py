from __future__ import annotations
from typing import TYPE_CHECKING



class PassportElementErrorFiles:
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."""

    def __init__(self, source: str, type: str, file_hashes: list[str], message: str):
        self.source: str = source
        self.type: str = type
        self.file_hashes: list[str] = file_hashes
        self.message: str = message

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
        if self.source is not None:
            result['source'] = _serialize(self.source)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.file_hashes is not None:
            result['file_hashes'] = _serialize(self.file_hashes)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportElementErrorFiles' | None:
        if not data:
            return None
        return cls(
            source=data.get('source'),
            type=data.get('type'),
            file_hashes=data.get('file_hashes'),
            message=data.get('message'),
        )