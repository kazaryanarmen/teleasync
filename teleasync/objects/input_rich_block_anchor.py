from __future__ import annotations
from typing import TYPE_CHECKING



class InputRichBlockAnchor:
    """A block with an anchor, corresponding to the HTML tag <a> with the attribute name."""

    def __init__(self, type: str, name: str):
        self.type: str = type
        self.name: str = name

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
        if self.name is not None:
            result['name'] = _serialize(self.name)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockAnchor' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            name=data.get('name'),
        )