from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .mask_position import MaskPosition
    


class InputSticker:
    """This object describes a sticker to be added to a sticker set."""

    def __init__(self, sticker_: str, format: str, emoji_list: list[str], mask_position: MaskPosition | None = None, keywords: list[str] | None = None):
        self.sticker_: str = sticker_
        self.format: str = format
        self.emoji_list: list[str] = emoji_list
        self.mask_position: MaskPosition | None = mask_position
        self.keywords: list[str] | None = keywords

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
        if self.sticker_ is not None:
            result['sticker'] = _serialize(self.sticker_)
        if self.format is not None:
            result['format'] = _serialize(self.format)
        if self.emoji_list is not None:
            result['emoji_list'] = _serialize(self.emoji_list)
        if self.mask_position is not None:
            result['mask_position'] = _serialize(self.mask_position)
        if self.keywords is not None:
            result['keywords'] = _serialize(self.keywords)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputSticker' | None:
        if not data:
            return None
        from .mask_position import MaskPosition
        return cls(
            sticker_=data.get('sticker'),
            format=data.get('format'),
            emoji_list=data.get('emoji_list'),
            mask_position=MaskPosition.from_dict(data.get('mask_position')),
            keywords=data.get('keywords'),
        )