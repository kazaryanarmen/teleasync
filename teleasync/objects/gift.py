from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .gift_background import GiftBackground
    
    from .sticker import Sticker
    


class Gift:
    """This object represents a gift that can be sent by the bot."""

    def __init__(self, id: str, sticker: Sticker, star_count: int, upgrade_star_count: int | None = None, is_premium: bool | None = None, has_colors: bool | None = None, total_count: int | None = None, remaining_count: int | None = None, personal_total_count: int | None = None, personal_remaining_count: int | None = None, background: GiftBackground | None = None, unique_gift_variant_count: int | None = None, publisher_chat: Chat | None = None):
        self.id: str = id
        self.sticker: Sticker = sticker
        self.star_count: int = star_count
        self.upgrade_star_count: int | None = upgrade_star_count
        self.is_premium: bool | None = is_premium
        self.has_colors: bool | None = has_colors
        self.total_count: int | None = total_count
        self.remaining_count: int | None = remaining_count
        self.personal_total_count: int | None = personal_total_count
        self.personal_remaining_count: int | None = personal_remaining_count
        self.background: GiftBackground | None = background
        self.unique_gift_variant_count: int | None = unique_gift_variant_count
        self.publisher_chat: Chat | None = publisher_chat

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.sticker is not None:
            result['sticker'] = _serialize(self.sticker)
        if self.star_count is not None:
            result['star_count'] = _serialize(self.star_count)
        if self.upgrade_star_count is not None:
            result['upgrade_star_count'] = _serialize(self.upgrade_star_count)
        if self.is_premium is not None:
            result['is_premium'] = _serialize(self.is_premium)
        if self.has_colors is not None:
            result['has_colors'] = _serialize(self.has_colors)
        if self.total_count is not None:
            result['total_count'] = _serialize(self.total_count)
        if self.remaining_count is not None:
            result['remaining_count'] = _serialize(self.remaining_count)
        if self.personal_total_count is not None:
            result['personal_total_count'] = _serialize(self.personal_total_count)
        if self.personal_remaining_count is not None:
            result['personal_remaining_count'] = _serialize(self.personal_remaining_count)
        if self.background is not None:
            result['background'] = _serialize(self.background)
        if self.unique_gift_variant_count is not None:
            result['unique_gift_variant_count'] = _serialize(self.unique_gift_variant_count)
        if self.publisher_chat is not None:
            result['publisher_chat'] = _serialize(self.publisher_chat)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Gift' | None:
        if not data:
            return None
        from .chat import Chat
        from .gift_background import GiftBackground
        from .sticker import Sticker
        return cls(
            id=data.get('id'),
            sticker=Sticker.from_dict(data.get('sticker')),
            star_count=data.get('star_count'),
            upgrade_star_count=data.get('upgrade_star_count'),
            is_premium=data.get('is_premium'),
            has_colors=data.get('has_colors'),
            total_count=data.get('total_count'),
            remaining_count=data.get('remaining_count'),
            personal_total_count=data.get('personal_total_count'),
            personal_remaining_count=data.get('personal_remaining_count'),
            background=GiftBackground.from_dict(data.get('background')),
            unique_gift_variant_count=data.get('unique_gift_variant_count'),
            publisher_chat=Chat.from_dict(data.get('publisher_chat')),
        )