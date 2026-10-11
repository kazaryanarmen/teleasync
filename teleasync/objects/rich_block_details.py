from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block import RichBlock
    
    from .rich_text import RichText
    


class RichBlockDetails:
    """An expandable block for details disclosure, corresponding to the HTML tag <details>."""

    def __init__(self, type: str, summary: RichText, blocks: list[RichBlock], is_open: bool | None = None):
        self.type: str = type
        self.summary: RichText = summary
        self.blocks: list[RichBlock] = blocks
        self.is_open: bool | None = is_open

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
        if self.summary is not None:
            result['summary'] = _serialize(self.summary)
        if self.blocks is not None:
            result['blocks'] = _serialize(self.blocks)
        if self.is_open is not None:
            result['is_open'] = _serialize(self.is_open)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockDetails' | None:
        if not data:
            return None
        from .rich_block import RichBlock
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            summary=RichText.from_dict(data.get('summary')),
            blocks=[RichBlock.from_dict(i1) for i1 in data.get('blocks')] if data.get('blocks') else None,
            is_open=data.get('is_open'),
        )