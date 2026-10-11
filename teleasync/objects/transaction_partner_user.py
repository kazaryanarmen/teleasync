from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .affiliate_info import AffiliateInfo
    
    from .gift import Gift
    
    from .paid_media import PaidMedia
    
    from .user import User
    


class TransactionPartnerUser:
    """Describes a transaction with a user."""

    def __init__(self, type: str, transaction_type: str, user: User, affiliate: AffiliateInfo | None = None, invoice_payload: str | None = None, subscription_period: int | None = None, paid_media: list[PaidMedia] | None = None, paid_media_payload: str | None = None, gift: Gift | None = None, premium_subscription_duration: int | None = None):
        self.type: str = type
        self.transaction_type: str = transaction_type
        self.user: User = user
        self.affiliate: AffiliateInfo | None = affiliate
        self.invoice_payload: str | None = invoice_payload
        self.subscription_period: int | None = subscription_period
        self.paid_media: list[PaidMedia] | None = paid_media
        self.paid_media_payload: str | None = paid_media_payload
        self.gift: Gift | None = gift
        self.premium_subscription_duration: int | None = premium_subscription_duration

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
        if self.transaction_type is not None:
            result['transaction_type'] = _serialize(self.transaction_type)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.affiliate is not None:
            result['affiliate'] = _serialize(self.affiliate)
        if self.invoice_payload is not None:
            result['invoice_payload'] = _serialize(self.invoice_payload)
        if self.subscription_period is not None:
            result['subscription_period'] = _serialize(self.subscription_period)
        if self.paid_media is not None:
            result['paid_media'] = _serialize(self.paid_media)
        if self.paid_media_payload is not None:
            result['paid_media_payload'] = _serialize(self.paid_media_payload)
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        if self.premium_subscription_duration is not None:
            result['premium_subscription_duration'] = _serialize(self.premium_subscription_duration)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerUser' | None:
        if not data:
            return None
        from .affiliate_info import AffiliateInfo
        from .gift import Gift
        from .paid_media import PaidMedia
        from .user import User
        return cls(
            type=data.get('type'),
            transaction_type=data.get('transaction_type'),
            user=User.from_dict(data.get('user')),
            affiliate=AffiliateInfo.from_dict(data.get('affiliate')),
            invoice_payload=data.get('invoice_payload'),
            subscription_period=data.get('subscription_period'),
            paid_media=[PaidMedia.from_dict(i1) for i1 in data.get('paid_media')] if data.get('paid_media') else None,
            paid_media_payload=data.get('paid_media_payload'),
            gift=Gift.from_dict(data.get('gift')),
            premium_subscription_duration=data.get('premium_subscription_duration'),
        )