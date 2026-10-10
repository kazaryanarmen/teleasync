from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_video import InputMediaVideo
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockVideo:
    """A block with a video, corresponding to the HTML tag <video>."""

    def __init__(self, type: str, video_: InputMediaVideo, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.video_: InputMediaVideo = video_
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
        if self.video_ is not None:
            result['video'] = _serialize(self.video_)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockVideo' | None:
        if not data:
            return None
        from .input_media_video import InputMediaVideo
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            video_=InputMediaVideo.from_dict(data.get('video')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )