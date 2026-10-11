from __future__ import annotations
from importlib import import_module


class ReactionType:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "emoji": ("reaction_type_emoji", "ReactionTypeEmoji"),
        "custom_emoji": ("reaction_type_custom_emoji", "ReactionTypeCustomEmoji"),
        "paid": ("reaction_type_paid", "ReactionTypePaid"),
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
