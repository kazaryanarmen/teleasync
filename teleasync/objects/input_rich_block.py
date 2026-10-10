from __future__ import annotations
from typing import TYPE_CHECKING



class InputRichBlock:
    """This object represents a block in a rich formatted message to be sent. Currently, it can be any of the following types: - InputRichBlockParagraph - InputRichBlockSectionHeading - InputRichBlockPreformatted - InputRichBlockFooter - InputRichBlockDivider - InputRichBlockMathematicalExpression - InputRichBlockAnchor - InputRichBlockList - InputRichBlockBlockQuotation - InputRichBlockExpandableBlockQuotation - InputRichBlockPullQuotation - InputRichBlockCollage - InputRichBlockSlideshow - InputRichBlockTable - InputRichBlockDetails - InputRichBlockMap - InputRichBlockButtons - InputRichBlockAnimation - InputRichBlockAudio - InputRichBlockDocument - InputRichBlockPhoto - InputRichBlockVideo - InputRichBlockVoiceNote - InputRichBlockThinking"""

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
    def from_dict(cls, data: dict | None) -> 'InputRichBlock' | None:
        if not data:
            return None
        return cls(
        )