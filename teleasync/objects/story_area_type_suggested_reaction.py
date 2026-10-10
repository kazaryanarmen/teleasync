from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .reaction_type import ReactionType
    


class StoryAreaTypeSuggestedReaction:
    """Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas."""

    def __init__(self, type: str, reaction_type: ReactionType, is_dark: bool | None = None, is_flipped: bool | None = None):
        self.type: str = type
        self.reaction_type: ReactionType = reaction_type
        self.is_dark: bool | None = is_dark
        self.is_flipped: bool | None = is_flipped

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
        if self.reaction_type is not None:
            result['reaction_type'] = _serialize(self.reaction_type)
        if self.is_dark is not None:
            result['is_dark'] = _serialize(self.is_dark)
        if self.is_flipped is not None:
            result['is_flipped'] = _serialize(self.is_flipped)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryAreaTypeSuggestedReaction' | None:
        if not data:
            return None
        from .reaction_type import ReactionType
        return cls(
            type=data.get('type'),
            reaction_type=ReactionType.from_dict(data.get('reaction_type')),
            is_dark=data.get('is_dark'),
            is_flipped=data.get('is_flipped'),
        )