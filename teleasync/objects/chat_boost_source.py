from __future__ import annotations
from typing import TYPE_CHECKING



class ChatBoostSource:
    """This object describes the source of a chat boost. It can be one of - ChatBoostSourcePremium - ChatBoostSourceGiftCode - ChatBoostSourceGiveaway"""

    def __init__(self):
        pass

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostSource' | None:
        if not data:
            return None
        return cls(
        )