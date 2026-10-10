from __future__ import annotations
from typing import TYPE_CHECKING



class WebAppData:
    """Describes data sent from a Web App to the bot."""

    def __init__(self, data: str, button_text: str):
        self.data: str = data
        self.button_text: str = button_text

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
        if self.data is not None:
            result['data'] = _serialize(self.data)
        if self.button_text is not None:
            result['button_text'] = _serialize(self.button_text)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'WebAppData' | None:
        if not data:
            return None
        return cls(
            data=data.get('data'),
            button_text=data.get('button_text'),
        )