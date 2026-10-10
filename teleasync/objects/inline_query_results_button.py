from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .web_app_info import WebAppInfo
    


class InlineQueryResultsButton:
    """This object represents a button to be shown above inline query results. You must use exactly one of the optional fields."""

    def __init__(self, text: str, web_app: WebAppInfo | None = None, start_parameter: str | None = None):
        self.text: str = text
        self.web_app: WebAppInfo | None = web_app
        self.start_parameter: str | None = start_parameter

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.web_app is not None:
            result['web_app'] = _serialize(self.web_app)
        if self.start_parameter is not None:
            result['start_parameter'] = _serialize(self.start_parameter)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultsButton' | None:
        if not data:
            return None
        from .web_app_info import WebAppInfo
        return cls(
            text=data.get('text'),
            web_app=WebAppInfo.from_dict(data.get('web_app')),
            start_parameter=data.get('start_parameter'),
        )