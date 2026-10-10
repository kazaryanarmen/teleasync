from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .maybe_inaccessible_message import MaybeInaccessibleMessage
    
    from .message_entity import MessageEntity
    


class PollOptionDeleted:
    """Describes a service message about an option deleted from a poll."""

    def __init__(self, option_persistent_id: str, option_text: str, poll_message: MaybeInaccessibleMessage | None = None, option_text_entities: list[MessageEntity] | None = None):
        self.option_persistent_id: str = option_persistent_id
        self.option_text: str = option_text
        self.poll_message: MaybeInaccessibleMessage | None = poll_message
        self.option_text_entities: list[MessageEntity] | None = option_text_entities

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
        if self.option_persistent_id is not None:
            result['option_persistent_id'] = _serialize(self.option_persistent_id)
        if self.option_text is not None:
            result['option_text'] = _serialize(self.option_text)
        if self.poll_message is not None:
            result['poll_message'] = _serialize(self.poll_message)
        if self.option_text_entities is not None:
            result['option_text_entities'] = _serialize(self.option_text_entities)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PollOptionDeleted' | None:
        if not data:
            return None
        from .maybe_inaccessible_message import MaybeInaccessibleMessage
        from .message_entity import MessageEntity
        return cls(
            option_persistent_id=data.get('option_persistent_id'),
            option_text=data.get('option_text'),
            poll_message=MaybeInaccessibleMessage.from_dict(data.get('poll_message')),
            option_text_entities=[MessageEntity.from_dict(i) for i in data.get('option_text_entities')] if data.get('option_text_entities') else None,
        )