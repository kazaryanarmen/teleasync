from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_media_animation import InputMediaAnimation
    
    from .input_media_audio import InputMediaAudio
    
    from .input_media_document import InputMediaDocument
    
    from .input_media_photo import InputMediaPhoto
    
    from .input_media_video import InputMediaVideo
    
    from .input_media_voice_note import InputMediaVoiceNote
    


class InputRichMessageMedia:
    """Describes a media element embedded in an outgoing rich message."""

    def __init__(self, id: str, media: InputMediaAudio | InputMediaVideo | InputMediaVoiceNote | InputMediaDocument | InputMediaAnimation | InputMediaPhoto):
        self.id: str = id
        self.media: InputMediaAudio | InputMediaVideo | InputMediaVoiceNote | InputMediaDocument | InputMediaAnimation | InputMediaPhoto = media

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.media is not None:
            result['media'] = _serialize(self.media)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichMessageMedia' | None:
        if not data:
            return None
        from .input_media_animation import InputMediaAnimation
        from .input_media_audio import InputMediaAudio
        from .input_media_document import InputMediaDocument
        from .input_media_photo import InputMediaPhoto
        from .input_media_video import InputMediaVideo
        from .input_media_voice_note import InputMediaVoiceNote
        return cls(
            id=data.get('id'),
            media=InputMediaAnimation.from_dict(data.get('media')),
        )