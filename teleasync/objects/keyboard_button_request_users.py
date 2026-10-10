from __future__ import annotations
from typing import TYPE_CHECKING



class KeyboardButtonRequestUsers:
    """This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. More about requesting users: https://core.telegram.org/bots/features#chat-and-user-selection"""

    def __init__(self, request_id: int, user_is_bot: bool | None = None, user_is_premium: bool | None = None, max_quantity: int | None = None, request_name: bool | None = None, request_username: bool | None = None, request_photo: bool | None = None):
        self.request_id: int = request_id
        self.user_is_bot: bool | None = user_is_bot
        self.user_is_premium: bool | None = user_is_premium
        self.max_quantity: int | None = max_quantity
        self.request_name: bool | None = request_name
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
        if self.user_is_bot is not None:
            result['user_is_bot'] = _serialize(self.user_is_bot)
        if self.user_is_premium is not None:
            result['user_is_premium'] = _serialize(self.user_is_premium)
        if self.max_quantity is not None:
            result['max_quantity'] = _serialize(self.max_quantity)
        if self.request_name is not None:
            result['request_name'] = _serialize(self.request_name)
        if self.request_username is not None:
            result['request_username'] = _serialize(self.request_username)
        if self.request_photo is not None:
            result['request_photo'] = _serialize(self.request_photo)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'KeyboardButtonRequestUsers' | None:
        if not data:
            return None
        return cls(
            request_id=data.get('request_id'),
            user_is_bot=data.get('user_is_bot'),
            user_is_premium=data.get('user_is_premium'),
            max_quantity=data.get('max_quantity'),
            request_name=data.get('request_name'),
            request_username=data.get('request_username'),
            request_photo=data.get('request_photo'),
        )