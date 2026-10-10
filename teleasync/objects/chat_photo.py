from __future__ import annotations
from typing import TYPE_CHECKING



class ChatPhoto:
    """This object represents a chat photo."""

    def __init__(self, small_file_id: str, small_file_unique_id: str, big_file_id: str, big_file_unique_id: str):
        self.small_file_id: str = small_file_id
        self.small_file_unique_id: str = small_file_unique_id
        self.big_file_id: str = big_file_id
        self.big_file_unique_id: str = big_file_unique_id

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
        if self.small_file_id is not None:
            result['small_file_id'] = _serialize(self.small_file_id)
        if self.small_file_unique_id is not None:
            result['small_file_unique_id'] = _serialize(self.small_file_unique_id)
        if self.big_file_id is not None:
            result['big_file_id'] = _serialize(self.big_file_id)
        if self.big_file_unique_id is not None:
            result['big_file_unique_id'] = _serialize(self.big_file_unique_id)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatPhoto' | None:
        if not data:
            return None
        return cls(
            small_file_id=data.get('small_file_id'),
            small_file_unique_id=data.get('small_file_unique_id'),
            big_file_id=data.get('big_file_id'),
            big_file_unique_id=data.get('big_file_unique_id'),
        )