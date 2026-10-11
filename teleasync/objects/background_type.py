from __future__ import annotations
from importlib import import_module


class BackgroundType:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "fill": ("background_type_fill", "BackgroundTypeFill"),
        "wallpaper": ("background_type_wallpaper", "BackgroundTypeWallpaper"),
        "pattern": ("background_type_pattern", "BackgroundTypePattern"),
        "chat_theme": ("background_type_chat_theme", "BackgroundTypeChatTheme"),
    }

    @classmethod
    def from_dict(cls, data: dict | None):
        if not data:
            return None
        entry = cls._SUBTYPES.get(data.get(cls._DISCRIMINATOR))
        if entry is None:
            return data
        module = import_module("." + entry[0], __package__)
        return getattr(module, entry[1]).from_dict(data)
