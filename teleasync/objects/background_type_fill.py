from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .background_fill import BackgroundFill
    


class BackgroundTypeFill:
    """The background is automatically filled based on the selected colors."""

    def __init__(self, type: str, fill: BackgroundFill, dark_theme_dimming: int):
        self.type: str = type
        self.fill: BackgroundFill = fill
        self.dark_theme_dimming: int = dark_theme_dimming

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
        if self.fill is not None:
            result['fill'] = _serialize(self.fill)
        if self.dark_theme_dimming is not None:
            result['dark_theme_dimming'] = _serialize(self.dark_theme_dimming)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundTypeFill' | None:
        if not data:
            return None
        from .background_fill import BackgroundFill
        return cls(
            type=data.get('type'),
            fill=BackgroundFill.from_dict(data.get('fill')),
            dark_theme_dimming=data.get('dark_theme_dimming'),
        )