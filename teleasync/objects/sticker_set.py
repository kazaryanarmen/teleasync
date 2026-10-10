from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .photo_size import PhotoSize
    
    from .sticker import Sticker
    


class StickerSet:
    """This object represents a sticker set."""

    def __init__(self, name: str, title: str, sticker_type: str, stickers: list[Sticker], thumbnail: PhotoSize | None = None):
        self.name: str = name
        self.title: str = title
        self.sticker_type: str = sticker_type
        self.stickers: list[Sticker] = stickers
        self.thumbnail: PhotoSize | None = thumbnail

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.sticker_type is not None:
            result['sticker_type'] = _serialize(self.sticker_type)
        if self.stickers is not None:
            result['stickers'] = _serialize(self.stickers)
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StickerSet' | None:
        if not data:
            return None
        from .photo_size import PhotoSize
        from .sticker import Sticker
        return cls(
            name=data.get('name'),
            title=data.get('title'),
            sticker_type=data.get('sticker_type'),
            stickers=[Sticker.from_dict(i) for i in data.get('stickers')] if data.get('stickers') else None,
            thumbnail=PhotoSize.from_dict(data.get('thumbnail')),
        )