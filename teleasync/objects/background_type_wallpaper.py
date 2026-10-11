from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .document import Document
    


class BackgroundTypeWallpaper:
    """The background is a wallpaper in the JPEG format."""

    def __init__(self, type: str, document: Document, dark_theme_dimming: int, is_blurred: bool | None = None, is_moving: bool | None = None):
        self.type: str = type
        self.document: Document = document
        self.dark_theme_dimming: int = dark_theme_dimming
        self.is_blurred: bool | None = is_blurred
        self.is_moving: bool | None = is_moving

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
        if self.document is not None:
            result['document'] = _serialize(self.document)
        if self.dark_theme_dimming is not None:
            result['dark_theme_dimming'] = _serialize(self.dark_theme_dimming)
        if self.is_blurred is not None:
            result['is_blurred'] = _serialize(self.is_blurred)
        if self.is_moving is not None:
            result['is_moving'] = _serialize(self.is_moving)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundTypeWallpaper' | None:
        if not data:
            return None
        from .document import Document
        return cls(
            type=data.get('type'),
            document=Document.from_dict(data.get('document')),
            dark_theme_dimming=data.get('dark_theme_dimming'),
            is_blurred=data.get('is_blurred'),
            is_moving=data.get('is_moving'),
        )