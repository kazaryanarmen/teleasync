from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    
    from .unique_gift import UniqueGift
    


class UniqueGiftInfo:
    """Describes a service message about a unique gift that was sent or received."""

    def __init__(self, gift: UniqueGift, origin: str, text: str | None = None, entities: list[MessageEntity] | None = None, is_private: bool | None = None, last_resale_currency: str | None = None, last_resale_amount: int | None = None, owned_gift_id: str | None = None, transfer_star_count: int | None = None, next_transfer_date: int | None = None):
        self.gift: UniqueGift = gift
        self.origin: str = origin
        self.text: str | None = text
        self.entities: list[MessageEntity] | None = entities
        self.is_private: bool | None = is_private
        self.last_resale_currency: str | None = last_resale_currency
        self.last_resale_amount: int | None = last_resale_amount
        self.owned_gift_id: str | None = owned_gift_id
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
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        if self.origin is not None:
            result['origin'] = _serialize(self.origin)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.is_private is not None:
            result['is_private'] = _serialize(self.is_private)
        if self.last_resale_currency is not None:
            result['last_resale_currency'] = _serialize(self.last_resale_currency)
        if self.last_resale_amount is not None:
            result['last_resale_amount'] = _serialize(self.last_resale_amount)
        if self.owned_gift_id is not None:
            result['owned_gift_id'] = _serialize(self.owned_gift_id)
        if self.transfer_star_count is not None:
            result['transfer_star_count'] = _serialize(self.transfer_star_count)
        if self.next_transfer_date is not None:
            result['next_transfer_date'] = _serialize(self.next_transfer_date)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGiftInfo' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        from .unique_gift import UniqueGift
        return cls(
            gift=UniqueGift.from_dict(data.get('gift')),
            origin=data.get('origin'),
            text=data.get('text'),
            entities=[MessageEntity.from_dict(i1) for i1 in data.get('entities')] if data.get('entities') else None,
            is_private=data.get('is_private'),
            last_resale_currency=data.get('last_resale_currency'),
            last_resale_amount=data.get('last_resale_amount'),
            owned_gift_id=data.get('owned_gift_id'),
            transfer_star_count=data.get('transfer_star_count'),
            next_transfer_date=data.get('next_transfer_date'),
        )