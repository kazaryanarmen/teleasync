from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_audio import InputMediaAudio
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockAudio:
    """A block with a music file, corresponding to the HTML tag <audio>."""

    def __init__(self, type: str, audio_: InputMediaAudio, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.audio_: InputMediaAudio = audio_
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
        if self.audio_ is not None:
            result['audio'] = _serialize(self.audio_)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockAudio' | None:
        if not data:
            return None
        from .input_media_audio import InputMediaAudio
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            audio_=InputMediaAudio.from_dict(data.get('audio')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )