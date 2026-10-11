from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .background_fill import BackgroundFill
    
    from .document import Document
    


class BackgroundTypePattern:
    """The background is a .PNG or .TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user."""

    def __init__(self, type: str, document: Document, fill: BackgroundFill, intensity: int, is_inverted: bool | None = None, is_moving: bool | None = None):
        self.type: str = type
        self.document: Document = document
        self.fill: BackgroundFill = fill
        self.intensity: int = intensity
        self.is_inverted: bool | None = is_inverted
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
        if self.fill is not None:
            result['fill'] = _serialize(self.fill)
        if self.intensity is not None:
            result['intensity'] = _serialize(self.intensity)
        if self.is_inverted is not None:
            result['is_inverted'] = _serialize(self.is_inverted)
        if self.is_moving is not None:
            result['is_moving'] = _serialize(self.is_moving)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundTypePattern' | None:
        if not data:
            return None
        from .background_fill import BackgroundFill
        from .document import Document
        return cls(
            type=data.get('type'),
            document=Document.from_dict(data.get('document')),
            fill=BackgroundFill.from_dict(data.get('fill')),
            intensity=data.get('intensity'),
            is_inverted=data.get('is_inverted'),
            is_moving=data.get('is_moving'),
        )