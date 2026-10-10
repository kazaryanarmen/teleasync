from __future__ import annotations
from typing import TYPE_CHECKING



class AcceptedGiftTypes:
    """This object describes the types of gifts that can be gifted to a user or a chat."""

    def __init__(self, unlimited_gifts: bool, limited_gifts: bool, unique_gifts: bool, premium_subscription: bool, gifts_from_channels: bool):
        self.unlimited_gifts: bool = unlimited_gifts
        self.limited_gifts: bool = limited_gifts
        self.unique_gifts: bool = unique_gifts
        self.premium_subscription: bool = premium_subscription
        self.gifts_from_channels: bool = gifts_from_channels

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
        if self.unlimited_gifts is not None:
            result['unlimited_gifts'] = _serialize(self.unlimited_gifts)
        if self.limited_gifts is not None:
            result['limited_gifts'] = _serialize(self.limited_gifts)
        if self.unique_gifts is not None:
            result['unique_gifts'] = _serialize(self.unique_gifts)
        if self.premium_subscription is not None:
            result['premium_subscription'] = _serialize(self.premium_subscription)
        if self.gifts_from_channels is not None:
            result['gifts_from_channels'] = _serialize(self.gifts_from_channels)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'AcceptedGiftTypes' | None:
        if not data:
            return None
        return cls(
            unlimited_gifts=data.get('unlimited_gifts'),
            limited_gifts=data.get('limited_gifts'),
            unique_gifts=data.get('unique_gifts'),
            premium_subscription=data.get('premium_subscription'),
            gifts_from_channels=data.get('gifts_from_channels'),
        )