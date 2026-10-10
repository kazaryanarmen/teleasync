from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichTextUrl:
    """A text with a link."""

    def __init__(self, type: str, text: RichText, url: str):
        self.type: str = type
        self.text: RichText = text
        self.url: str = url

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
        if self.url is not None:
            result['url'] = _serialize(self.url)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichTextUrl' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            text=RichText.from_dict(data.get('text')),
            url=data.get('url'),
        )