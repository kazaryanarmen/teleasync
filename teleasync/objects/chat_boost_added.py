from __future__ import annotations
from typing import TYPE_CHECKING



class ChatBoostAdded:
    """This object represents a service message about a user boosting a chat."""

    def __init__(self, boost_count: int):
        self.boost_count: int = boost_count

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
        if self.boost_count is not None:
            result['boost_count'] = _serialize(self.boost_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoostAdded' | None:
        if not data:
            return None
        return cls(
            boost_count=data.get('boost_count'),
        )