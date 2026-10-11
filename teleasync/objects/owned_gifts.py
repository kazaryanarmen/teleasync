from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .owned_gift import OwnedGift
    


class OwnedGifts:
    """Contains the list of gifts received and owned by a user or a chat."""

    def __init__(self, total_count: int, gifts: list[OwnedGift], next_offset: str | None = None):
        self.total_count: int = total_count
        self.gifts: list[OwnedGift] = gifts
        self.next_offset: str | None = next_offset

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
        if self.total_count is not None:
            result['total_count'] = _serialize(self.total_count)
        if self.gifts is not None:
            result['gifts'] = _serialize(self.gifts)
        if self.next_offset is not None:
            result['next_offset'] = _serialize(self.next_offset)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'OwnedGifts' | None:
        if not data:
            return None
        from .owned_gift import OwnedGift
        return cls(
            total_count=data.get('total_count'),
            gifts=[OwnedGift.from_dict(i1) for i1 in data.get('gifts')] if data.get('gifts') else None,
            next_offset=data.get('next_offset'),
        )