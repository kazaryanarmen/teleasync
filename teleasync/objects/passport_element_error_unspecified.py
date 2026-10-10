from __future__ import annotations
from typing import TYPE_CHECKING



class PassportElementErrorUnspecified:
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added."""

    def __init__(self, source: str, type: str, element_hash: str, message: str):
        self.source: str = source
        self.type: str = type
        self.element_hash: str = element_hash
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
        if self.element_hash is not None:
            result['element_hash'] = _serialize(self.element_hash)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportElementErrorUnspecified' | None:
        if not data:
            return None
        return cls(
            source=data.get('source'),
            type=data.get('type'),
            element_hash=data.get('element_hash'),
            message=data.get('message'),
        )