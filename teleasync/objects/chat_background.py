from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .background_type import BackgroundType
    


class ChatBackground:
    """This object represents a chat background."""

    def __init__(self, type: BackgroundType):
        self.type: BackgroundType = type

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
    def from_dict(cls, data: dict | None) -> 'ChatBackground' | None:
        if not data:
            return None
        from .background_type import BackgroundType
        return cls(
            type=BackgroundType.from_dict(data.get('type')),
        )