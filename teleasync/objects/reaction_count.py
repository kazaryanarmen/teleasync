from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .reaction_type import ReactionType
    


class ReactionCount:
    """Represents a reaction added to a message along with the number of times it was added."""

    def __init__(self, type: ReactionType, total_count: int):
        self.type: ReactionType = type
        self.total_count: int = total_count

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
        if self.total_count is not None:
            result['total_count'] = _serialize(self.total_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ReactionCount' | None:
        if not data:
            return None
        from .reaction_type import ReactionType
        return cls(
            type=ReactionType.from_dict(data.get('type')),
            total_count=data.get('total_count'),
        )