from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .message_entity import MessageEntity
    
    from .user import User
    


class ChecklistTask:
    """Describes a task in a checklist."""

    def __init__(self, id: int, text: str, text_entities: list[MessageEntity] | None = None, completed_by_user: User | None = None, completed_by_chat: Chat | None = None, completion_date: int | None = None):
        self.id: int = id
        self.text: str = text
        self.text_entities: list[MessageEntity] | None = text_entities
        self.completed_by_user: User | None = completed_by_user
        self.completed_by_chat: Chat | None = completed_by_chat
        self.completion_date: int | None = completion_date

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
        if self.text_entities is not None:
            result['text_entities'] = _serialize(self.text_entities)
        if self.completed_by_user is not None:
            result['completed_by_user'] = _serialize(self.completed_by_user)
        if self.completed_by_chat is not None:
            result['completed_by_chat'] = _serialize(self.completed_by_chat)
        if self.completion_date is not None:
            result['completion_date'] = _serialize(self.completion_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChecklistTask' | None:
        if not data:
            return None
        from .chat import Chat
        from .message_entity import MessageEntity
        from .user import User
        return cls(
            id=data.get('id'),
            text=data.get('text'),
            text_entities=[MessageEntity.from_dict(i) for i in data.get('text_entities')] if data.get('text_entities') else None,
            completed_by_user=User.from_dict(data.get('completed_by_user')),
            completed_by_chat=Chat.from_dict(data.get('completed_by_chat')),
            completion_date=data.get('completion_date'),
        )