from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .web_app_info import WebAppInfo
    


class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App."""

    def __init__(self, type: str, text: str, web_app: WebAppInfo):
        self.type: str = type
        self.text: str = text
        self.web_app: WebAppInfo = web_app

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.web_app is not None:
            result['web_app'] = _serialize(self.web_app)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MenuButtonWebApp' | None:
        if not data:
            return None
        from .web_app_info import WebAppInfo
        return cls(
            type=data.get('type'),
            text=data.get('text'),
            web_app=WebAppInfo.from_dict(data.get('web_app')),
        )