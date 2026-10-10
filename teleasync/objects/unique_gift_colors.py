from __future__ import annotations
from typing import TYPE_CHECKING



class UniqueGiftColors:
    """This object contains information about the color scheme for a user's name, message replies and link previews based on a unique gift."""

    def __init__(self, model_custom_emoji_id: str, symbol_custom_emoji_id: str, light_theme_main_color: int, light_theme_other_colors: list[int], dark_theme_main_color: int, dark_theme_other_colors: list[int]):
        self.model_custom_emoji_id: str = model_custom_emoji_id
        self.symbol_custom_emoji_id: str = symbol_custom_emoji_id
        self.light_theme_main_color: int = light_theme_main_color
        self.light_theme_other_colors: list[int] = light_theme_other_colors
        self.dark_theme_main_color: int = dark_theme_main_color
        self.dark_theme_other_colors: list[int] = dark_theme_other_colors

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
        if self.model_custom_emoji_id is not None:
            result['model_custom_emoji_id'] = _serialize(self.model_custom_emoji_id)
        if self.symbol_custom_emoji_id is not None:
            result['symbol_custom_emoji_id'] = _serialize(self.symbol_custom_emoji_id)
        if self.light_theme_main_color is not None:
            result['light_theme_main_color'] = _serialize(self.light_theme_main_color)
        if self.light_theme_other_colors is not None:
            result['light_theme_other_colors'] = _serialize(self.light_theme_other_colors)
        if self.dark_theme_main_color is not None:
            result['dark_theme_main_color'] = _serialize(self.dark_theme_main_color)
        if self.dark_theme_other_colors is not None:
            result['dark_theme_other_colors'] = _serialize(self.dark_theme_other_colors)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGiftColors' | None:
        if not data:
            return None
        return cls(
            model_custom_emoji_id=data.get('model_custom_emoji_id'),
            symbol_custom_emoji_id=data.get('symbol_custom_emoji_id'),
            light_theme_main_color=data.get('light_theme_main_color'),
            light_theme_other_colors=data.get('light_theme_other_colors'),
            dark_theme_main_color=data.get('dark_theme_main_color'),
            dark_theme_other_colors=data.get('dark_theme_other_colors'),
        )