from __future__ import annotations
from typing import TYPE_CHECKING



class LinkPreviewOptions:
    """Describes the options used for link preview generation."""

    def __init__(self, is_disabled: bool | None = None, url: str | None = None, prefer_small_media: bool | None = None, prefer_large_media: bool | None = None, show_above_text: bool | None = None):
        self.is_disabled: bool | None = is_disabled
        self.url: str | None = url
        self.prefer_small_media: bool | None = prefer_small_media
        self.prefer_large_media: bool | None = prefer_large_media
        self.show_above_text: bool | None = show_above_text

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
        if self.is_disabled is not None:
            result['is_disabled'] = _serialize(self.is_disabled)
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.prefer_small_media is not None:
            result['prefer_small_media'] = _serialize(self.prefer_small_media)
        if self.prefer_large_media is not None:
            result['prefer_large_media'] = _serialize(self.prefer_large_media)
        if self.show_above_text is not None:
            result['show_above_text'] = _serialize(self.show_above_text)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'LinkPreviewOptions' | None:
        if not data:
            return None
        return cls(
            is_disabled=data.get('is_disabled'),
            url=data.get('url'),
            prefer_small_media=data.get('prefer_small_media'),
            prefer_large_media=data.get('prefer_large_media'),
            show_above_text=data.get('show_above_text'),
        )