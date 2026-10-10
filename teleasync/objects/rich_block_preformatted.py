from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichBlockPreformatted:
    """A preformatted text block, corresponding to the nested HTML tags <pre> and <code>."""

    def __init__(self, type: str, text: RichText, language: str | None = None):
        self.type: str = type
        self.text: RichText = text
        self.language: str | None = language

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
        if self.language is not None:
            result['language'] = _serialize(self.language)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockPreformatted' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            text=RichText.from_dict(data.get('text')),
            language=data.get('language'),
        )