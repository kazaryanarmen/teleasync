from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .maybe_inaccessible_message import MaybeInaccessibleMessage
    
    from .user import User
    


class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present."""

    def __init__(self, id: str, from_: User, chat_instance: str, message: MaybeInaccessibleMessage | None = None, inline_message_id: str | None = None, data: str | None = None, game_short_name: str | None = None):
        self.id: str = id
        self.from_: User = from_
        self.chat_instance: str = chat_instance
        self.message: MaybeInaccessibleMessage | None = message
        self.inline_message_id: str | None = inline_message_id
        self.data: str | None = data
        self.game_short_name: str | None = game_short_name

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
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.chat_instance is not None:
            result['chat_instance'] = _serialize(self.chat_instance)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        if self.inline_message_id is not None:
            result['inline_message_id'] = _serialize(self.inline_message_id)
        if self.data is not None:
            result['data'] = _serialize(self.data)
        if self.game_short_name is not None:
            result['game_short_name'] = _serialize(self.game_short_name)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'CallbackQuery' | None:
        if not data:
            return None
        from .maybe_inaccessible_message import MaybeInaccessibleMessage
        from .user import User
        return cls(
            id=data.get('id'),
            from_=User.from_dict(data.get('from')),
            chat_instance=data.get('chat_instance'),
            message=MaybeInaccessibleMessage.from_dict(data.get('message')),
            inline_message_id=data.get('inline_message_id'),
            data=data.get('data'),
            game_short_name=data.get('game_short_name'),
        )