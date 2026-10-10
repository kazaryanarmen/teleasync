from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .unique_gift import UniqueGift
    
    from .user import User
    


class OwnedGiftUnique:
    """Describes a unique gift received and owned by a user or a chat."""

    def __init__(self, type: str, gift: UniqueGift, send_date: int, owned_gift_id: str | None = None, sender_user: User | None = None, is_saved: bool | None = None, can_be_transferred: bool | None = None, transfer_star_count: int | None = None, next_transfer_date: int | None = None):
        self.type: str = type
        self.gift: UniqueGift = gift
        self.send_date: int = send_date
        self.owned_gift_id: str | None = owned_gift_id
        self.sender_user: User | None = sender_user
        self.is_saved: bool | None = is_saved
        self.can_be_transferred: bool | None = can_be_transferred
        self.transfer_star_count: int | None = transfer_star_count
        self.next_transfer_date: int | None = next_transfer_date

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
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        if self.send_date is not None:
            result['send_date'] = _serialize(self.send_date)
        if self.owned_gift_id is not None:
            result['owned_gift_id'] = _serialize(self.owned_gift_id)
        if self.sender_user is not None:
            result['sender_user'] = _serialize(self.sender_user)
        if self.is_saved is not None:
            result['is_saved'] = _serialize(self.is_saved)
        if self.can_be_transferred is not None:
            result['can_be_transferred'] = _serialize(self.can_be_transferred)
        if self.transfer_star_count is not None:
            result['transfer_star_count'] = _serialize(self.transfer_star_count)
        if self.next_transfer_date is not None:
            result['next_transfer_date'] = _serialize(self.next_transfer_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'OwnedGiftUnique' | None:
        if not data:
            return None
        from .unique_gift import UniqueGift
        from .user import User
        return cls(
            type=data.get('type'),
            gift=UniqueGift.from_dict(data.get('gift')),
            send_date=data.get('send_date'),
            owned_gift_id=data.get('owned_gift_id'),
            sender_user=User.from_dict(data.get('sender_user')),
            is_saved=data.get('is_saved'),
            can_be_transferred=data.get('can_be_transferred'),
            transfer_star_count=data.get('transfer_star_count'),
            next_transfer_date=data.get('next_transfer_date'),
        )