from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .message_entity import MessageEntity
    
    from .poll_media import PollMedia
    
    from .user import User
    


class PollOption:
    """This object contains information about one answer option in a poll."""

    def __init__(self, persistent_id: str, text: str, voter_count: int, text_entities: list[MessageEntity] | None = None, media: PollMedia | None = None, added_by_user: User | None = None, added_by_chat: Chat | None = None, addition_date: int | None = None):
        self.persistent_id: str = persistent_id
        self.text: str = text
        self.voter_count: int = voter_count
        self.text_entities: list[MessageEntity] | None = text_entities
        self.media: PollMedia | None = media
        self.added_by_user: User | None = added_by_user
        self.added_by_chat: Chat | None = added_by_chat
        self.addition_date: int | None = addition_date

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
        if self.persistent_id is not None:
            result['persistent_id'] = _serialize(self.persistent_id)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.voter_count is not None:
            result['voter_count'] = _serialize(self.voter_count)
        if self.text_entities is not None:
            result['text_entities'] = _serialize(self.text_entities)
        if self.media is not None:
            result['media'] = _serialize(self.media)
        if self.added_by_user is not None:
            result['added_by_user'] = _serialize(self.added_by_user)
        if self.added_by_chat is not None:
            result['added_by_chat'] = _serialize(self.added_by_chat)
        if self.addition_date is not None:
            result['addition_date'] = _serialize(self.addition_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PollOption' | None:
        if not data:
            return None
        from .chat import Chat
        from .message_entity import MessageEntity
        from .poll_media import PollMedia
        from .user import User
        return cls(
            persistent_id=data.get('persistent_id'),
            text=data.get('text'),
            voter_count=data.get('voter_count'),
            text_entities=[MessageEntity.from_dict(i) for i in data.get('text_entities')] if data.get('text_entities') else None,
            media=PollMedia.from_dict(data.get('media')),
            added_by_user=User.from_dict(data.get('added_by_user')),
            added_by_chat=Chat.from_dict(data.get('added_by_chat')),
            addition_date=data.get('addition_date'),
        )