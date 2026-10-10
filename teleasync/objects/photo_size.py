from __future__ import annotations
from typing import TYPE_CHECKING



class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail."""

    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
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
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PhotoSize' | None:
        if not data:
            return None
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            width=data.get('width'),
            height=data.get('height'),
            file_size=data.get('file_size'),
        )