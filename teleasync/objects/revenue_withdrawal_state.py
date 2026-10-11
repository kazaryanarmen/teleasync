from __future__ import annotations
from importlib import import_module


class RevenueWithdrawalState:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "pending": ("revenue_withdrawal_state_pending", "RevenueWithdrawalStatePending"),
        "succeeded": ("revenue_withdrawal_state_succeeded", "RevenueWithdrawalStateSucceeded"),
        "failed": ("revenue_withdrawal_state_failed", "RevenueWithdrawalStateFailed"),
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
