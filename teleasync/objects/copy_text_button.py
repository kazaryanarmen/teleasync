from __future__ import annotations
from typing import TYPE_CHECKING



class CopyTextButton:
    """This object represents an inline keyboard button that copies specified text to the clipboard."""

    def __init__(self, text: str):
        self.text: str = text

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'CopyTextButton' | None:
        if not data:
            return None
        return cls(
            text=data.get('text'),
        )