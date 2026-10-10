from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    


class TextQuote:
    """This object contains information about the quoted part of a message that is replied to by the given message."""

    def __init__(self, text: str, position: int, entities: list[MessageEntity] | None = None, is_manual: bool | None = None):
        self.text: str = text
        self.position: int = position
        self.entities: list[MessageEntity] | None = entities
        self.is_manual: bool | None = is_manual

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
        if self.position is not None:
            result['position'] = _serialize(self.position)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.is_manual is not None:
            result['is_manual'] = _serialize(self.is_manual)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TextQuote' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        return cls(
            text=data.get('text'),
            position=data.get('position'),
            entities=[MessageEntity.from_dict(i) for i in data.get('entities')] if data.get('entities') else None,
            is_manual=data.get('is_manual'),
        )