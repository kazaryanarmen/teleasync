from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichBlockTableCell:
    """Cell in a table."""

    def __init__(self, align: str, valign: str, text: RichText | None = None, is_header: bool | None = None, colspan: int | None = None, rowspan: int | None = None):
        self.align: str = align
        self.valign: str = valign
        self.text: RichText | None = text
        self.is_header: bool | None = is_header
        self.colspan: int | None = colspan
        self.rowspan: int | None = rowspan

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
        if self.align is not None:
            result['align'] = _serialize(self.align)
        if self.valign is not None:
            result['valign'] = _serialize(self.valign)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.is_header is not None:
            result['is_header'] = _serialize(self.is_header)
        if self.colspan is not None:
            result['colspan'] = _serialize(self.colspan)
        if self.rowspan is not None:
            result['rowspan'] = _serialize(self.rowspan)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockTableCell' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            align=data.get('align'),
            valign=data.get('valign'),
            text=RichText.from_dict(data.get('text')),
            is_header=data.get('is_header'),
            colspan=data.get('colspan'),
            rowspan=data.get('rowspan'),
        )