from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .keyboard_button import KeyboardButton
    


class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples). Not supported in channels and for messages sent on behalf of a business account."""

    def __init__(self, keyboard: list[KeyboardButton], is_persistent: bool | None = None, resize_keyboard: bool | None = None, one_time_keyboard: bool | None = None, input_field_placeholder: str | None = None, selective: bool | None = None, force_reply: bool | None = None):
        self.keyboard: list[KeyboardButton] = keyboard
        self.is_persistent: bool | None = is_persistent
        self.resize_keyboard: bool | None = resize_keyboard
        self.one_time_keyboard: bool | None = one_time_keyboard
        self.input_field_placeholder: str | None = input_field_placeholder
        self.selective: bool | None = selective
        self.force_reply: bool | None = force_reply

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
        if self.keyboard is not None:
            result['keyboard'] = _serialize(self.keyboard)
        if self.is_persistent is not None:
            result['is_persistent'] = _serialize(self.is_persistent)
        if self.resize_keyboard is not None:
            result['resize_keyboard'] = _serialize(self.resize_keyboard)
        if self.one_time_keyboard is not None:
            result['one_time_keyboard'] = _serialize(self.one_time_keyboard)
        if self.input_field_placeholder is not None:
            result['input_field_placeholder'] = _serialize(self.input_field_placeholder)
        if self.selective is not None:
            result['selective'] = _serialize(self.selective)
        if self.force_reply is not None:
            result['force_reply'] = _serialize(self.force_reply)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ReplyKeyboardMarkup' | None:
        if not data:
            return None
        from .keyboard_button import KeyboardButton
        return cls(
            keyboard=[KeyboardButton.from_dict(i) for i in data.get('keyboard')] if data.get('keyboard') else None,
            is_persistent=data.get('is_persistent'),
            resize_keyboard=data.get('resize_keyboard'),
            one_time_keyboard=data.get('one_time_keyboard'),
            input_field_placeholder=data.get('input_field_placeholder'),
            selective=data.get('selective'),
            force_reply=data.get('force_reply'),
        )