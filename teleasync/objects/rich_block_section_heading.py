from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichBlockSectionHeading:
    """A section heading, corresponding to the HTML tags <h1>, <h2>, <h3>, <h4>, <h5>, or <h6>."""

    def __init__(self, type: str, text: RichText, size: int):
        self.type: str = type
        self.text: RichText = text
        self.size: int = size

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
        if self.size is not None:
            result['size'] = _serialize(self.size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockSectionHeading' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            text=RichText.from_dict(data.get('text')),
            size=data.get('size'),
        )