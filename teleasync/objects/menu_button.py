from __future__ import annotations
from importlib import import_module


class MenuButton:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "commands": ("menu_button_commands", "MenuButtonCommands"),
        "web_app": ("menu_button_web_app", "MenuButtonWebApp"),
        "default": ("menu_button_default", "MenuButtonDefault"),
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
