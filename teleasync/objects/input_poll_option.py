from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_poll_option_media import InputPollOptionMedia
    
    from .message_entity import MessageEntity
    


class InputPollOption:
    """This object contains information about one answer option in a poll to be sent."""

    def __init__(self, text: str, text_parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None, media: InputPollOptionMedia | None = None):
        self.text: str = text
        self.text_parse_mode: str | None = text_parse_mode
        self.text_entities: list[MessageEntity] | None = text_entities
        self.media: InputPollOptionMedia | None = media

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.text_parse_mode is not None:
            result['text_parse_mode'] = _serialize(self.text_parse_mode)
        if self.text_entities is not None:
            result['text_entities'] = _serialize(self.text_entities)
        if self.media is not None:
            result['media'] = _serialize(self.media)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputPollOption' | None:
        if not data:
            return None
        from .input_poll_option_media import InputPollOptionMedia
        from .message_entity import MessageEntity
        return cls(
            text=data.get('text'),
            text_parse_mode=data.get('text_parse_mode'),
            text_entities=[MessageEntity.from_dict(i1) for i1 in data.get('text_entities')] if data.get('text_entities') else None,
            media=InputPollOptionMedia.from_dict(data.get('media')),
        )