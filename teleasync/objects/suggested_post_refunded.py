from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    


class SuggestedPostRefunded:
    """Describes a service message about a payment refund for a suggested post."""

    def __init__(self, reason: str, suggested_post_message: Message | None = None):
        self.reason: str = reason
        self.suggested_post_message: Message | None = suggested_post_message

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
        if self.reason is not None:
            result['reason'] = _serialize(self.reason)
        if self.suggested_post_message is not None:
            result['suggested_post_message'] = _serialize(self.suggested_post_message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'SuggestedPostRefunded' | None:
        if not data:
            return None
        from .message import Message
        return cls(
            reason=data.get('reason'),
            suggested_post_message=Message.from_dict(data.get('suggested_post_message')),
        )