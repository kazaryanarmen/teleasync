from __future__ import annotations
from typing import TYPE_CHECKING



class WebAppInfo:
    """Describes a Web App."""

    def __init__(self, url: str):
        self.url: str = url

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
        if self.url is not None:
            result['url'] = _serialize(self.url)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'WebAppInfo' | None:
        if not data:
            return None
        return cls(
            url=data.get('url'),
        )