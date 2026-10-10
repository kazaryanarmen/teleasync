from __future__ import annotations
from typing import TYPE_CHECKING



class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. It serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:"""

    def __init__(self, url: str, forward_text: str | None = None, bot_username: str | None = None, request_write_access: bool | None = None):
        self.url: str = url
        self.forward_text: str | None = forward_text
        self.bot_username: str | None = bot_username
        self.request_write_access: bool | None = request_write_access

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
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.forward_text is not None:
            result['forward_text'] = _serialize(self.forward_text)
        if self.bot_username is not None:
            result['bot_username'] = _serialize(self.bot_username)
        if self.request_write_access is not None:
            result['request_write_access'] = _serialize(self.request_write_access)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'LoginUrl' | None:
        if not data:
            return None
        return cls(
            url=data.get('url'),
            forward_text=data.get('forward_text'),
            bot_username=data.get('bot_username'),
            request_write_access=data.get('request_write_access'),
        )