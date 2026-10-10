from __future__ import annotations
from typing import TYPE_CHECKING



class PassportElementErrorFrontSide:
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes."""

    def __init__(self, source: str, type: str, file_hash: str, message: str):
        self.source: str = source
        self.type: str = type
        self.file_hash: str = file_hash
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
        if self.file_hash is not None:
            result['file_hash'] = _serialize(self.file_hash)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportElementErrorFrontSide' | None:
        if not data:
            return None
        return cls(
            source=data.get('source'),
            type=data.get('type'),
            file_hash=data.get('file_hash'),
            message=data.get('message'),
        )