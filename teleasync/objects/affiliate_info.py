from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .user import User
    


class AffiliateInfo:
    """Contains information about the affiliate that received a commission via this transaction."""

    def __init__(self, commission_per_mille: int, amount: int, affiliate_user: User | None = None, affiliate_chat: Chat | None = None, nanostar_amount: int | None = None):
        self.commission_per_mille: int = commission_per_mille
        self.amount: int = amount
        self.affiliate_user: User | None = affiliate_user
        self.affiliate_chat: Chat | None = affiliate_chat
        self.nanostar_amount: int | None = nanostar_amount

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
        if self.commission_per_mille is not None:
            result['commission_per_mille'] = _serialize(self.commission_per_mille)
        if self.amount is not None:
            result['amount'] = _serialize(self.amount)
        if self.affiliate_user is not None:
            result['affiliate_user'] = _serialize(self.affiliate_user)
        if self.affiliate_chat is not None:
            result['affiliate_chat'] = _serialize(self.affiliate_chat)
        if self.nanostar_amount is not None:
            result['nanostar_amount'] = _serialize(self.nanostar_amount)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'AffiliateInfo' | None:
        if not data:
            return None
        from .chat import Chat
        from .user import User
        return cls(
            commission_per_mille=data.get('commission_per_mille'),
            amount=data.get('amount'),
            affiliate_user=User.from_dict(data.get('affiliate_user')),
            affiliate_chat=Chat.from_dict(data.get('affiliate_chat')),
            nanostar_amount=data.get('nanostar_amount'),
        )