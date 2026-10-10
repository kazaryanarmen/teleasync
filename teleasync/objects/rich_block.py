from __future__ import annotations
from typing import TYPE_CHECKING



class RichBlock:
    """This object represents a block in a rich formatted message. Currently, it can be any of the following types: - RichBlockParagraph - RichBlockSectionHeading - RichBlockPreformatted - RichBlockFooter - RichBlockDivider - RichBlockMathematicalExpression - RichBlockAnchor - RichBlockList - RichBlockBlockQuotation - RichBlockExpandableBlockQuotation - RichBlockPullQuotation - RichBlockCollage - RichBlockSlideshow - RichBlockTable - RichBlockDetails - RichBlockMap - RichBlockButtons - RichBlockAnimation - RichBlockAudio - RichBlockDocument - RichBlockPhoto - RichBlockVideo - RichBlockVoiceNote - RichBlockThinking"""

    def __init__(self):
        pass

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlock' | None:
        if not data:
            return None
        return cls(
        )