from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    


class InputChecklistTask:
    """Describes a task to add to a checklist."""

    def __init__(self, id: int, text: str, parse_mode: str | None = None, text_entities: list[MessageEntity] | None = None):
        self.id: int = id
        self.text: str = text
        self.parse_mode: str | None = parse_mode
        self.text_entities: list[MessageEntity] | None = text_entities

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.text_entities is not None:
            result['text_entities'] = _serialize(self.text_entities)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputChecklistTask' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        return cls(
            id=data.get('id'),
            text=data.get('text'),
            parse_mode=data.get('parse_mode'),
            text_entities=[MessageEntity.from_dict(i1) for i1 in data.get('text_entities')] if data.get('text_entities') else None,
        )