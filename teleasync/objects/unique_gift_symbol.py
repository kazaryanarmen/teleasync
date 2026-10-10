from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .sticker import Sticker
    


class UniqueGiftSymbol:
    """This object describes the symbol shown on the pattern of a unique gift."""

    def __init__(self, name: str, sticker_: Sticker, rarity_per_mille: int):
        self.name: str = name
        self.sticker_: Sticker = sticker_
        self.rarity_per_mille: int = rarity_per_mille

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
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.sticker_ is not None:
            result['sticker'] = _serialize(self.sticker_)
        if self.rarity_per_mille is not None:
            result['rarity_per_mille'] = _serialize(self.rarity_per_mille)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGiftSymbol' | None:
        if not data:
            return None
        from .sticker import Sticker
        return cls(
            name=data.get('name'),
            sticker_=Sticker.from_dict(data.get('sticker')),
            rarity_per_mille=data.get('rarity_per_mille'),
        )