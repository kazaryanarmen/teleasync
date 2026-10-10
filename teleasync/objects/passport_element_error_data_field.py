from __future__ import annotations
from typing import TYPE_CHECKING



class PassportElementErrorDataField:
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."""

    def __init__(self, source: str, type: str, field_name: str, data_hash: str, message: str):
        self.source: str = source
        self.type: str = type
        self.field_name: str = field_name
        self.data_hash: str = data_hash
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
        if self.field_name is not None:
            result['field_name'] = _serialize(self.field_name)
        if self.data_hash is not None:
            result['data_hash'] = _serialize(self.data_hash)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportElementErrorDataField' | None:
        if not data:
            return None
        return cls(
            source=data.get('source'),
            type=data.get('type'),
            field_name=data.get('field_name'),
            data_hash=data.get('data_hash'),
            message=data.get('message'),
        )