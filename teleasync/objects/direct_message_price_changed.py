from __future__ import annotations
from typing import TYPE_CHECKING



class DirectMessagePriceChanged:
    """Describes a service message about a change in the price of direct messages sent to a channel chat."""

    def __init__(self, are_direct_messages_enabled: bool, direct_message_star_count: int | None = None):
        self.are_direct_messages_enabled: bool = are_direct_messages_enabled
        self.direct_message_star_count: int | None = direct_message_star_count

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
        if self.are_direct_messages_enabled is not None:
            result['are_direct_messages_enabled'] = _serialize(self.are_direct_messages_enabled)
        if self.direct_message_star_count is not None:
            result['direct_message_star_count'] = _serialize(self.direct_message_star_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'DirectMessagePriceChanged' | None:
        if not data:
            return None
        return cls(
            are_direct_messages_enabled=data.get('are_direct_messages_enabled'),
            direct_message_star_count=data.get('direct_message_star_count'),
        )