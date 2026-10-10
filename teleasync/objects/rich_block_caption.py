from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichBlockCaption:
    """Caption of a rich formatted block."""

    def __init__(self, text: RichText, credit: RichText | None = None):
        self.text: RichText = text
        self.credit: RichText | None = credit

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
        if self.credit is not None:
            result['credit'] = _serialize(self.credit)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockCaption' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            text=RichText.from_dict(data.get('text')),
            credit=RichText.from_dict(data.get('credit')),
        )