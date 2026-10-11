from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_button import InlineKeyboardButton
    


class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to the message it belongs to."""

    def __init__(self, inline_keyboard: list[list[InlineKeyboardButton]], force_reply: bool | None = None):
        self.inline_keyboard: list[list[InlineKeyboardButton]] = inline_keyboard
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
        if self.inline_keyboard is not None:
            result['inline_keyboard'] = _serialize(self.inline_keyboard)
        if self.force_reply is not None:
            result['force_reply'] = _serialize(self.force_reply)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineKeyboardMarkup' | None:
        if not data:
            return None
        from .inline_keyboard_button import InlineKeyboardButton
        return cls(
            inline_keyboard=[[InlineKeyboardButton.from_dict(i1) for i1 in i2] for i2 in data.get('inline_keyboard')] if data.get('inline_keyboard') else None,
            force_reply=data.get('force_reply'),
        )