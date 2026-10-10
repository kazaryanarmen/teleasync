from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatInviteLink:
    """Represents an invite link for a chat."""

    def __init__(self, invite_link: str, creator: User, creates_join_request: bool, is_primary: bool, is_revoked: bool, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None, pending_join_request_count: int | None = None, subscription_period: int | None = None, subscription_price: int | None = None):
        self.invite_link: str = invite_link
        self.creator: User = creator
        self.creates_join_request: bool = creates_join_request
        self.is_primary: bool = is_primary
        self.is_revoked: bool = is_revoked
        self.name: str | None = name
        self.expire_date: int | None = expire_date
        self.member_limit: int | None = member_limit
        self.pending_join_request_count: int | None = pending_join_request_count
        self.subscription_period: int | None = subscription_period
        self.subscription_price: int | None = subscription_price

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
        if self.invite_link is not None:
            result['invite_link'] = _serialize(self.invite_link)
        if self.creator is not None:
            result['creator'] = _serialize(self.creator)
        if self.creates_join_request is not None:
            result['creates_join_request'] = _serialize(self.creates_join_request)
        if self.is_primary is not None:
            result['is_primary'] = _serialize(self.is_primary)
        if self.is_revoked is not None:
            result['is_revoked'] = _serialize(self.is_revoked)
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.expire_date is not None:
            result['expire_date'] = _serialize(self.expire_date)
        if self.member_limit is not None:
            result['member_limit'] = _serialize(self.member_limit)
        if self.pending_join_request_count is not None:
            result['pending_join_request_count'] = _serialize(self.pending_join_request_count)
        if self.subscription_period is not None:
            result['subscription_period'] = _serialize(self.subscription_period)
        if self.subscription_price is not None:
            result['subscription_price'] = _serialize(self.subscription_price)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatInviteLink' | None:
        if not data:
            return None
        from .user import User
        return cls(
            invite_link=data.get('invite_link'),
            creator=User.from_dict(data.get('creator')),
            creates_join_request=data.get('creates_join_request'),
            is_primary=data.get('is_primary'),
            is_revoked=data.get('is_revoked'),
            name=data.get('name'),
            expire_date=data.get('expire_date'),
            member_limit=data.get('member_limit'),
            pending_join_request_count=data.get('pending_join_request_count'),
            subscription_period=data.get('subscription_period'),
            subscription_price=data.get('subscription_price'),
        )