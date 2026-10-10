from __future__ import annotations
from typing import TYPE_CHECKING



class PassportFile:
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB."""

    def __init__(self, file_id: str, file_unique_id: str, file_size: int, file_date: int):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.file_size: int = file_size
        self.file_date: int = file_date

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
        if self.file_date is not None:
            result['file_date'] = _serialize(self.file_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportFile' | None:
        if not data:
            return None
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            file_size=data.get('file_size'),
            file_date=data.get('file_date'),
        )