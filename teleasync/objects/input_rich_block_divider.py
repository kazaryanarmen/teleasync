from __future__ import annotations
from typing import TYPE_CHECKING



class InputRichBlockDivider:
    """A divider, corresponding to the HTML tag <hr/>."""

    def __init__(self, type: str):
        self.type: str = type

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockDivider' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
        )