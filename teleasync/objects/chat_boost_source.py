from __future__ import annotations
from importlib import import_module


class ChatBoostSource:
    """Union-тип. from_dict возвращает нужный подтип по полю 'source'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "source"
    _SUBTYPES = {
        "premium": ("chat_boost_source_premium", "ChatBoostSourcePremium"),
        "gift_code": ("chat_boost_source_gift_code", "ChatBoostSourceGiftCode"),
        "giveaway": ("chat_boost_source_giveaway", "ChatBoostSourceGiveaway"),
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
