from __future__ import annotations
from typing import TYPE_CHECKING



class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""

    def __init__(self, file_id: str, file_unique_id: str, file_size: int | None = None, file_path: str | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.file_size: int | None = file_size
        self.file_path: str | None = file_path

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
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        if self.file_path is not None:
            result['file_path'] = _serialize(self.file_path)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'File' | None:
        if not data:
            return None
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            file_size=data.get('file_size'),
            file_path=data.get('file_path'),
        )