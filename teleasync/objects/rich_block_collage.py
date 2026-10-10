from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block import RichBlock
    
    from .rich_block_caption import RichBlockCaption
    


class RichBlockCollage:
    """A collage, corresponding to the custom HTML tag <tg-collage>."""

    def __init__(self, type: str, blocks: list[RichBlock], caption: RichBlockCaption | None = None):
        self.type: str = type
        self.blocks: list[RichBlock] = blocks
        self.caption: RichBlockCaption | None = caption

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
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockCollage' | None:
        if not data:
            return None
        from .rich_block import RichBlock
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            blocks=[RichBlock.from_dict(i) for i in data.get('blocks')] if data.get('blocks') else None,
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )