from __future__ import annotations
from importlib import import_module


class ChatMember:
    """Union-тип. from_dict возвращает нужный подтип по полю 'status'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "status"
    _SUBTYPES = {
        "creator": ("chat_member_owner", "ChatMemberOwner"),
        "administrator": ("chat_member_administrator", "ChatMemberAdministrator"),
        "member": ("chat_member_member", "ChatMemberMember"),
        "restricted": ("chat_member_restricted", "ChatMemberRestricted"),
        "left": ("chat_member_left", "ChatMemberLeft"),
        "kicked": ("chat_member_banned", "ChatMemberBanned"),
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
