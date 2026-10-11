from __future__ import annotations
from importlib import import_module


class TransactionPartner:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "user": ("transaction_partner_user", "TransactionPartnerUser"),
        "chat": ("transaction_partner_chat", "TransactionPartnerChat"),
        "affiliate_program": ("transaction_partner_affiliate_program", "TransactionPartnerAffiliateProgram"),
        "fragment": ("transaction_partner_fragment", "TransactionPartnerFragment"),
        "telegram_ads": ("transaction_partner_telegram_ads", "TransactionPartnerTelegramAds"),
        "telegram_api": ("transaction_partner_telegram_api", "TransactionPartnerTelegramApi"),
        "other": ("transaction_partner_other", "TransactionPartnerOther"),
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
