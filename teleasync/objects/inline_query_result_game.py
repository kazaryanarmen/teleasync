from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    


class InlineQueryResultGame:
    """Represents a Game."""

    def __init__(self, type: str, id: str, game_short_name: str, reply_markup: InlineKeyboardMarkup | None = None):
        self.type: str = type
        self.id: str = id
        self.game_short_name: str = game_short_name
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.game_short_name is not None:
            result['game_short_name'] = _serialize(self.game_short_name)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultGame' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            game_short_name=data.get('game_short_name'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
        )