from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class TransactionPartnerAffiliateProgram:
    """Describes the affiliate program that issued the affiliate commission received via this transaction."""

    def __init__(self, type: str, commission_per_mille: int, sponsor_user: User | None = None):
        self.type: str = type
        self.commission_per_mille: int = commission_per_mille
        self.sponsor_user: User | None = sponsor_user

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
        if self.commission_per_mille is not None:
            result['commission_per_mille'] = _serialize(self.commission_per_mille)
        if self.sponsor_user is not None:
            result['sponsor_user'] = _serialize(self.sponsor_user)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerAffiliateProgram' | None:
        if not data:
            return None
        from .user import User
        return cls(
            type=data.get('type'),
            commission_per_mille=data.get('commission_per_mille'),
            sponsor_user=User.from_dict(data.get('sponsor_user')),
        )