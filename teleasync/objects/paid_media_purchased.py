from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class PaidMediaPurchased:
    """This object contains information about a paid media purchase."""

    def __init__(self, from_: User, paid_media_payload: str):
        self.from_: User = from_
        self.paid_media_payload: str = paid_media_payload

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
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.paid_media_payload is not None:
            result['paid_media_payload'] = _serialize(self.paid_media_payload)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaPurchased' | None:
        if not data:
            return None
        from .user import User
        return cls(
            from_=User.from_dict(data.get('from')),
            paid_media_payload=data.get('paid_media_payload'),
        )