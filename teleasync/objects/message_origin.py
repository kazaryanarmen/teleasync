from __future__ import annotations
from importlib import import_module


class MessageOrigin:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "user": ("message_origin_user", "MessageOriginUser"),
        "hidden_user": ("message_origin_hidden_user", "MessageOriginHiddenUser"),
        "chat": ("message_origin_chat", "MessageOriginChat"),
        "channel": ("message_origin_channel", "MessageOriginChannel"),
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
