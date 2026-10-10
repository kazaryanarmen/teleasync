from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .gift import Gift
    


class Gifts:
    """This object represent a list of gifts."""

    def __init__(self, gifts: list[Gift]):
        self.gifts: list[Gift] = gifts

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
        if self.gifts is not None:
            result['gifts'] = _serialize(self.gifts)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Gifts' | None:
        if not data:
            return None
        from .gift import Gift
        return cls(
            gifts=[Gift.from_dict(i) for i in data.get('gifts')] if data.get('gifts') else None,
        )