from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_photo import InputMediaPhoto
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockPhoto:
    """A block with a photo, corresponding to the HTML tag <img>."""

    def __init__(self, type: str, photo: InputMediaPhoto, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.photo: InputMediaPhoto = photo
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
        if self.photo is not None:
            result['photo'] = _serialize(self.photo)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockPhoto' | None:
        if not data:
            return None
        from .input_media_photo import InputMediaPhoto
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            photo=InputMediaPhoto.from_dict(data.get('photo')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )