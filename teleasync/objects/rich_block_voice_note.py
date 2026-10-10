from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block_caption import RichBlockCaption
    
    from .voice import Voice
    


class RichBlockVoiceNote:
    """A block with a voice note, corresponding to the HTML tag <audio>."""

    def __init__(self, type: str, voice_note: Voice, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.voice_note: Voice = voice_note
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
        if self.voice_note is not None:
            result['voice_note'] = _serialize(self.voice_note)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichBlockVoiceNote' | None:
        if not data:
            return None
        from .rich_block_caption import RichBlockCaption
        from .voice import Voice
        return cls(
            type=data.get('type'),
            voice_note=Voice.from_dict(data.get('voice_note')),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )