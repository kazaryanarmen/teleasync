from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .keyboard_button_poll_type import KeyboardButtonPollType
    
    from .keyboard_button_request_chat import KeyboardButtonRequestChat
    
    from .keyboard_button_request_managed_bot import KeyboardButtonRequestManagedBot
    
    from .keyboard_button_request_users import KeyboardButtonRequestUsers
    
    from .web_app_info import WebAppInfo
    


class KeyboardButton:
    """This object represents one button of the reply keyboard. At most one of the fields other than text, icon_custom_emoji_id, and style must be used to specify the type of the button. For simple text buttons, String can be used instead of this object to specify the button text."""

    def __init__(self, text: str, icon_custom_emoji_id: str | None = None, style: str | None = None, request_users: KeyboardButtonRequestUsers | None = None, request_chat: KeyboardButtonRequestChat | None = None, request_managed_bot: KeyboardButtonRequestManagedBot | None = None, request_contact: bool | None = None, request_location: bool | None = None, request_poll: KeyboardButtonPollType | None = None, web_app: WebAppInfo | None = None):
        self.text: str = text
        self.icon_custom_emoji_id: str | None = icon_custom_emoji_id
        self.style: str | None = style
        self.request_users: KeyboardButtonRequestUsers | None = request_users
        self.request_chat: KeyboardButtonRequestChat | None = request_chat
        self.request_managed_bot: KeyboardButtonRequestManagedBot | None = request_managed_bot
        self.request_contact: bool | None = request_contact
        self.request_location: bool | None = request_location
        self.request_poll: KeyboardButtonPollType | None = request_poll
        self.web_app: WebAppInfo | None = web_app

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
        if self.icon_custom_emoji_id is not None:
            result['icon_custom_emoji_id'] = _serialize(self.icon_custom_emoji_id)
        if self.style is not None:
            result['style'] = _serialize(self.style)
        if self.request_users is not None:
            result['request_users'] = _serialize(self.request_users)
        if self.request_chat is not None:
            result['request_chat'] = _serialize(self.request_chat)
        if self.request_managed_bot is not None:
            result['request_managed_bot'] = _serialize(self.request_managed_bot)
        if self.request_contact is not None:
            result['request_contact'] = _serialize(self.request_contact)
        if self.request_location is not None:
            result['request_location'] = _serialize(self.request_location)
        if self.request_poll is not None:
            result['request_poll'] = _serialize(self.request_poll)
        if self.web_app is not None:
            result['web_app'] = _serialize(self.web_app)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'KeyboardButton' | None:
        if not data:
            return None
        from .keyboard_button_poll_type import KeyboardButtonPollType
        from .keyboard_button_request_chat import KeyboardButtonRequestChat
        from .keyboard_button_request_managed_bot import KeyboardButtonRequestManagedBot
        from .keyboard_button_request_users import KeyboardButtonRequestUsers
        from .web_app_info import WebAppInfo
        return cls(
            text=data.get('text'),
            icon_custom_emoji_id=data.get('icon_custom_emoji_id'),
            style=data.get('style'),
            request_users=KeyboardButtonRequestUsers.from_dict(data.get('request_users')),
            request_chat=KeyboardButtonRequestChat.from_dict(data.get('request_chat')),
            request_managed_bot=KeyboardButtonRequestManagedBot.from_dict(data.get('request_managed_bot')),
            request_contact=data.get('request_contact'),
            request_location=data.get('request_location'),
            request_poll=KeyboardButtonPollType.from_dict(data.get('request_poll')),
            web_app=WebAppInfo.from_dict(data.get('web_app')),
        )