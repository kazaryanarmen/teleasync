from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichTextDateTime:
    """Formatted date and time."""

    def __init__(self, type: str, text: RichText, unix_time: int, date_time_format: str):
        self.type: str = type
        self.text: RichText = text
        self.unix_time: int = unix_time
        self.date_time_format: str = date_time_format

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.unix_time is not None:
            result['unix_time'] = _serialize(self.unix_time)
        if self.date_time_format is not None:
            result['date_time_format'] = _serialize(self.date_time_format)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichTextDateTime' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            text=RichText.from_dict(data.get('text')),
            unix_time=data.get('unix_time'),
            date_time_format=data.get('date_time_format'),
        )