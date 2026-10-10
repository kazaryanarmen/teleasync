from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    
    from .rich_block_caption import RichBlockCaption
    


class RichBlockPhoto:
    """A block with a photo, corresponding to the HTML tag <img>."""

    def __init__(self, type: str, photo_: list[PhotoSize], has_spoiler: bool | None = None, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.photo_: list[PhotoSize] = photo_
        self.has_spoiler: bool | None = has_spoiler
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
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.has_spoiler is not None:
            result['has_spoiler'] = _serialize(self.has_spoiler)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockPhoto' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
            has_spoiler=data.get('has_spoiler'),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )