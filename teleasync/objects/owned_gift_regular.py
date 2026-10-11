from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .gift import Gift
    
    from .message_entity import MessageEntity
    
    from .user import User
    


class OwnedGiftRegular:
    """Describes a regular gift owned by a user or a chat."""

    def __init__(self, type: str, gift: Gift, send_date: int, owned_gift_id: str | None = None, sender_user: User | None = None, text: str | None = None, entities: list[MessageEntity] | None = None, is_private: bool | None = None, is_saved: bool | None = None, can_be_upgraded: bool | None = None, was_refunded: bool | None = None, convert_star_count: int | None = None, prepaid_upgrade_star_count: int | None = None, is_upgrade_separate: bool | None = None, unique_gift_number: int | None = None):
        self.type: str = type
        self.gift: Gift = gift
        self.send_date: int = send_date
        self.owned_gift_id: str | None = owned_gift_id
        self.sender_user: User | None = sender_user
        self.text: str | None = text
        self.entities: list[MessageEntity] | None = entities
        self.is_private: bool | None = is_private
        self.is_saved: bool | None = is_saved
        self.can_be_upgraded: bool | None = can_be_upgraded
        self.was_refunded: bool | None = was_refunded
        self.convert_star_count: int | None = convert_star_count
        self.prepaid_upgrade_star_count: int | None = prepaid_upgrade_star_count
        self.is_upgrade_separate: bool | None = is_upgrade_separate
        self.unique_gift_number: int | None = unique_gift_number

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.is_private is not None:
            result['is_private'] = _serialize(self.is_private)
        if self.is_saved is not None:
            result['is_saved'] = _serialize(self.is_saved)
        if self.can_be_upgraded is not None:
            result['can_be_upgraded'] = _serialize(self.can_be_upgraded)
        if self.was_refunded is not None:
            result['was_refunded'] = _serialize(self.was_refunded)
        if self.convert_star_count is not None:
            result['convert_star_count'] = _serialize(self.convert_star_count)
        if self.prepaid_upgrade_star_count is not None:
            result['prepaid_upgrade_star_count'] = _serialize(self.prepaid_upgrade_star_count)
        if self.is_upgrade_separate is not None:
            result['is_upgrade_separate'] = _serialize(self.is_upgrade_separate)
        if self.unique_gift_number is not None:
            result['unique_gift_number'] = _serialize(self.unique_gift_number)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'OwnedGiftRegular' | None:
        if not data:
            return None
        from .gift import Gift
        from .message_entity import MessageEntity
        from .user import User
        return cls(
            type=data.get('type'),
            gift=Gift.from_dict(data.get('gift')),
            send_date=data.get('send_date'),
            owned_gift_id=data.get('owned_gift_id'),
            sender_user=User.from_dict(data.get('sender_user')),
            text=data.get('text'),
            entities=[MessageEntity.from_dict(i1) for i1 in data.get('entities')] if data.get('entities') else None,
            is_private=data.get('is_private'),
            is_saved=data.get('is_saved'),
            can_be_upgraded=data.get('can_be_upgraded'),
            was_refunded=data.get('was_refunded'),
            convert_star_count=data.get('convert_star_count'),
            prepaid_upgrade_star_count=data.get('prepaid_upgrade_star_count'),
            is_upgrade_separate=data.get('is_upgrade_separate'),
            unique_gift_number=data.get('unique_gift_number'),
        )