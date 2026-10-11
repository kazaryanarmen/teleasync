from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block import RichBlock
    
    from .rich_text import RichText
    


class RichBlockBlockQuotation:
    """A block quotation, corresponding to the HTML tag <blockquote>."""

    def __init__(self, type: str, blocks: list[RichBlock], credit: RichText | None = None):
        self.type: str = type
        self.blocks: list[RichBlock] = blocks
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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.blocks is not None:
            result['blocks'] = _serialize(self.blocks)
        if self.credit is not None:
            result['credit'] = _serialize(self.credit)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockBlockQuotation' | None:
        if not data:
            return None
        from .rich_block import RichBlock
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            blocks=[RichBlock.from_dict(i1) for i1 in data.get('blocks')] if data.get('blocks') else None,
            credit=RichText.from_dict(data.get('credit')),
        )