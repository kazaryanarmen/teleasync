from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .link_preview_options import LinkPreviewOptions
    
    from .message_entity import MessageEntity
    


class InputTextMessageContent:
    """Represents the content of a text message to be sent as the result of an inline query."""

    def __init__(self, message_text: str, parse_mode: str | None = None, entities: list[MessageEntity] | None = None, link_preview_options: LinkPreviewOptions | None = None):
        self.message_text: str = message_text
        self.parse_mode: str | None = parse_mode
        self.entities: list[MessageEntity] | None = entities
        self.link_preview_options: LinkPreviewOptions | None = link_preview_options

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
        if self.message_text is not None:
            result['message_text'] = _serialize(self.message_text)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.link_preview_options is not None:
            result['link_preview_options'] = _serialize(self.link_preview_options)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputTextMessageContent' | None:
        if not data:
            return None
        from .link_preview_options import LinkPreviewOptions
        from .message_entity import MessageEntity
        return cls(
            message_text=data.get('message_text'),
            parse_mode=data.get('parse_mode'),
            entities=[MessageEntity.from_dict(i1) for i1 in data.get('entities')] if data.get('entities') else None,
            link_preview_options=LinkPreviewOptions.from_dict(data.get('link_preview_options')),
        )