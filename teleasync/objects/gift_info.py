from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .gift import Gift
    
    from .message_entity import MessageEntity
    


class GiftInfo:
    """Describes a service message about a regular gift that was sent or received."""

    def __init__(self, gift: Gift, owned_gift_id: str | None = None, convert_star_count: int | None = None, prepaid_upgrade_star_count: int | None = None, is_upgrade_separate: bool | None = None, can_be_upgraded: bool | None = None, text: str | None = None, entities: list[MessageEntity] | None = None, is_private: bool | None = None, unique_gift_number: int | None = None):
        self.gift: Gift = gift
        self.owned_gift_id: str | None = owned_gift_id
        self.convert_star_count: int | None = convert_star_count
        self.prepaid_upgrade_star_count: int | None = prepaid_upgrade_star_count
        self.is_upgrade_separate: bool | None = is_upgrade_separate
        self.can_be_upgraded: bool | None = can_be_upgraded
        self.text: str | None = text
        self.entities: list[MessageEntity] | None = entities
        self.is_private: bool | None = is_private
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
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        if self.owned_gift_id is not None:
            result['owned_gift_id'] = _serialize(self.owned_gift_id)
        if self.convert_star_count is not None:
            result['convert_star_count'] = _serialize(self.convert_star_count)
        if self.prepaid_upgrade_star_count is not None:
            result['prepaid_upgrade_star_count'] = _serialize(self.prepaid_upgrade_star_count)
        if self.is_upgrade_separate is not None:
            result['is_upgrade_separate'] = _serialize(self.is_upgrade_separate)
        if self.can_be_upgraded is not None:
            result['can_be_upgraded'] = _serialize(self.can_be_upgraded)
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.entities is not None:
            result['entities'] = _serialize(self.entities)
        if self.is_private is not None:
            result['is_private'] = _serialize(self.is_private)
        if self.unique_gift_number is not None:
            result['unique_gift_number'] = _serialize(self.unique_gift_number)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'GiftInfo' | None:
        if not data:
            return None
        from .gift import Gift
        from .message_entity import MessageEntity
        return cls(
            gift=Gift.from_dict(data.get('gift')),
            owned_gift_id=data.get('owned_gift_id'),
            convert_star_count=data.get('convert_star_count'),
            prepaid_upgrade_star_count=data.get('prepaid_upgrade_star_count'),
            is_upgrade_separate=data.get('is_upgrade_separate'),
            can_be_upgraded=data.get('can_be_upgraded'),
            text=data.get('text'),
            entities=[MessageEntity.from_dict(i) for i in data.get('entities')] if data.get('entities') else None,
            is_private=data.get('is_private'),
            unique_gift_number=data.get('unique_gift_number'),
        )