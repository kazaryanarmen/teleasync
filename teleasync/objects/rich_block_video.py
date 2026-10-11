from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block_caption import RichBlockCaption
    
    from .video import Video
    


class RichBlockVideo:
    """A block with a video, corresponding to the HTML tag <video>."""

    def __init__(self, type: str, video: Video, has_spoiler: bool | None = None, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.video: Video = video
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
        if self.video is not None:
            result['video'] = _serialize(self.video)
        if self.has_spoiler is not None:
            result['has_spoiler'] = _serialize(self.has_spoiler)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockVideo' | None:
        if not data:
            return None
        from .rich_block_caption import RichBlockCaption
        from .video import Video
        return cls(
            type=data.get('type'),
            video=Video.from_dict(data.get('video')),
            has_spoiler=data.get('has_spoiler'),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )