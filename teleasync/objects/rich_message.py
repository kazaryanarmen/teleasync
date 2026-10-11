from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block import RichBlock
    


class RichMessage:
    """Rich formatted message."""

    def __init__(self, blocks: list[RichBlock], is_rtl: bool | None = None):
        self.blocks: list[RichBlock] = blocks
        self.is_rtl: bool | None = is_rtl

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
        if self.blocks is not None:
            result['blocks'] = _serialize(self.blocks)
        if self.is_rtl is not None:
            result['is_rtl'] = _serialize(self.is_rtl)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichMessage' | None:
        if not data:
            return None
        from .rich_block import RichBlock
        return cls(
            blocks=[RichBlock.from_dict(i1) for i1 in data.get('blocks')] if data.get('blocks') else None,
            is_rtl=data.get('is_rtl'),
        )