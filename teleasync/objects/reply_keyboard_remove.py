from __future__ import annotations
from typing import TYPE_CHECKING



class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup). Not supported in channels and for messages sent on behalf of a business account."""

    def __init__(self, remove_keyboard: bool, selective: bool | None = None):
        self.remove_keyboard: bool = remove_keyboard
        self.selective: bool | None = selective

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
        if self.remove_keyboard is not None:
            result['remove_keyboard'] = _serialize(self.remove_keyboard)
        if self.selective is not None:
            result['selective'] = _serialize(self.selective)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ReplyKeyboardRemove' | None:
        if not data:
            return None
        return cls(
            remove_keyboard=data.get('remove_keyboard'),
            selective=data.get('selective'),
        )