from __future__ import annotations
from importlib import import_module


class BackgroundFill:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "solid": ("background_fill_solid", "BackgroundFillSolid"),
        "gradient": ("background_fill_gradient", "BackgroundFillGradient"),
        "freeform_gradient": ("background_fill_freeform_gradient", "BackgroundFillFreeformGradient"),
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
