from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_animation import InputMediaAnimation
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockAnimation:
    """A block with an animation, corresponding to the HTML tag <video>."""

    def __init__(self, type: str, animation: InputMediaAnimation, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.animation: InputMediaAnimation = animation
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
        if self.animation is not None:
            result['animation'] = _serialize(self.animation)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockAnimation' | None:
        if not data:
            return None
        from .input_media_animation import InputMediaAnimation
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            animation=InputMediaAnimation.from_dict(data.get('animation')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )