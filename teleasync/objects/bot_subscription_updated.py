from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class BotSubscriptionUpdated:
    """This object contains information about changes to a user payment subscription toward the current bot."""

    def __init__(self, user: User, invoice_payload: str, state: str):
        self.user: User = user
        self.invoice_payload: str = invoice_payload
        self.state: str = state

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
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.invoice_payload is not None:
            result['invoice_payload'] = _serialize(self.invoice_payload)
        if self.state is not None:
            result['state'] = _serialize(self.state)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BotSubscriptionUpdated' | None:
        if not data:
            return None
        from .user import User
        return cls(
            user=User.from_dict(data.get('user')),
            invoice_payload=data.get('invoice_payload'),
            state=data.get('state'),
        )