from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_document import InputMediaDocument
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockDocument:
    """A block with a general file, corresponding to the custom HTML tag <tg-document>."""

    def __init__(self, type: str, document: InputMediaDocument, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.document: InputMediaDocument = document
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
        if self.document is not None:
            result['document'] = _serialize(self.document)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockDocument' | None:
        if not data:
            return None
        from .input_media_document import InputMediaDocument
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            document=InputMediaDocument.from_dict(data.get('document')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )