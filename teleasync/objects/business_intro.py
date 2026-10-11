from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .sticker import Sticker
    


class BusinessIntro:
    """Contains information about the start page settings of a Telegram Business account."""

    def __init__(self, title: str | None = None, message: str | None = None, sticker: Sticker | None = None):
        self.title: str | None = title
        self.message: str | None = message
        self.sticker: Sticker | None = sticker

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.message is not None:
            result['message'] = _serialize(self.message)
        if self.sticker is not None:
            result['sticker'] = _serialize(self.sticker)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessIntro' | None:
        if not data:
            return None
        from .sticker import Sticker
        return cls(
            title=data.get('title'),
            message=data.get('message'),
            sticker=Sticker.from_dict(data.get('sticker')),
        )