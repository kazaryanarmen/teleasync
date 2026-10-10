from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    


class SuggestedPostDeclined:
    """Describes a service message about the rejection of a suggested post."""

    def __init__(self, suggested_post_message: Message | None = None, comment: str | None = None):
        self.suggested_post_message: Message | None = suggested_post_message
        self.comment: str | None = comment

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
        if self.suggested_post_message is not None:
            result['suggested_post_message'] = _serialize(self.suggested_post_message)
        if self.comment is not None:
            result['comment'] = _serialize(self.comment)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostDeclined' | None:
        if not data:
            return None
        from .message import Message
        return cls(
            suggested_post_message=Message.from_dict(data.get('suggested_post_message')),
            comment=data.get('comment'),
        )