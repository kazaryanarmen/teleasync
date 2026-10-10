from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .unique_gift_backdrop_colors import UniqueGiftBackdropColors
    


class UniqueGiftBackdrop:
    """This object describes the backdrop of a unique gift."""

    def __init__(self, name: str, colors: UniqueGiftBackdropColors, rarity_per_mille: int):
        self.name: str = name
        self.colors: UniqueGiftBackdropColors = colors
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
        if self.colors is not None:
            result['colors'] = _serialize(self.colors)
        if self.rarity_per_mille is not None:
            result['rarity_per_mille'] = _serialize(self.rarity_per_mille)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGiftBackdrop' | None:
        if not data:
            return None
        from .unique_gift_backdrop_colors import UniqueGiftBackdropColors
        return cls(
            name=data.get('name'),
            colors=UniqueGiftBackdropColors.from_dict(data.get('colors')),
            rarity_per_mille=data.get('rarity_per_mille'),
        )