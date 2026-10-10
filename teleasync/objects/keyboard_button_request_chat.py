from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat_administrator_rights import ChatAdministratorRights
    


class KeyboardButtonRequestChat:
    """This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. More about requesting chats: https://core.telegram.org/bots/features#chat-and-user-selection."""

    def __init__(self, request_id: int, chat_is_channel: bool, chat_is_forum: bool | None = None, chat_has_username: bool | None = None, chat_is_created: bool | None = None, user_administrator_rights: ChatAdministratorRights | None = None, bot_administrator_rights: ChatAdministratorRights | None = None, bot_is_member: bool | None = None, request_title: bool | None = None, request_username: bool | None = None, request_photo: bool | None = None):
        self.request_id: int = request_id
        self.chat_is_channel: bool = chat_is_channel
        self.chat_is_forum: bool | None = chat_is_forum
        self.chat_has_username: bool | None = chat_has_username
        self.chat_is_created: bool | None = chat_is_created
        self.user_administrator_rights: ChatAdministratorRights | None = user_administrator_rights
        self.bot_administrator_rights: ChatAdministratorRights | None = bot_administrator_rights
        self.bot_is_member: bool | None = bot_is_member
        self.request_title: bool | None = request_title
        self.request_username: bool | None = request_username
        self.request_photo: bool | None = request_photo

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
        if self.request_id is not None:
            result['request_id'] = _serialize(self.request_id)
        if self.chat_is_channel is not None:
            result['chat_is_channel'] = _serialize(self.chat_is_channel)
        if self.chat_is_forum is not None:
            result['chat_is_forum'] = _serialize(self.chat_is_forum)
        if self.chat_has_username is not None:
            result['chat_has_username'] = _serialize(self.chat_has_username)
        if self.chat_is_created is not None:
            result['chat_is_created'] = _serialize(self.chat_is_created)
        if self.user_administrator_rights is not None:
            result['user_administrator_rights'] = _serialize(self.user_administrator_rights)
        if self.bot_administrator_rights is not None:
            result['bot_administrator_rights'] = _serialize(self.bot_administrator_rights)
        if self.bot_is_member is not None:
            result['bot_is_member'] = _serialize(self.bot_is_member)
        if self.request_title is not None:
            result['request_title'] = _serialize(self.request_title)
        if self.request_username is not None:
            result['request_username'] = _serialize(self.request_username)
        if self.request_photo is not None:
            result['request_photo'] = _serialize(self.request_photo)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'KeyboardButtonRequestChat' | None:
        if not data:
            return None
        from .chat_administrator_rights import ChatAdministratorRights
        return cls(
            request_id=data.get('request_id'),
            chat_is_channel=data.get('chat_is_channel'),
            chat_is_forum=data.get('chat_is_forum'),
            chat_has_username=data.get('chat_has_username'),
            chat_is_created=data.get('chat_is_created'),
            user_administrator_rights=ChatAdministratorRights.from_dict(data.get('user_administrator_rights')),
            bot_administrator_rights=ChatAdministratorRights.from_dict(data.get('bot_administrator_rights')),
            bot_is_member=data.get('bot_is_member'),
            request_title=data.get('request_title'),
            request_username=data.get('request_username'),
            request_photo=data.get('request_photo'),
        )