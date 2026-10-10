from __future__ import annotations
from typing import TYPE_CHECKING



class BackgroundTypeChatTheme:
    """The background is taken directly from a built-in chat theme."""

    def __init__(self, type: str, theme_name: str):
        self.type: str = type
        self.theme_name: str = theme_name

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
        if self.theme_name is not None:
            result['theme_name'] = _serialize(self.theme_name)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BackgroundTypeChatTheme' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            theme_name=data.get('theme_name'),
        )