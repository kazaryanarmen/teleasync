from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_rich_block import InputRichBlock
    
    from .input_rich_message_media import InputRichMessageMedia
    


class InputRichMessage:
    """Describes a rich message to be sent. Exactly one of the fields html, markdown, or blocks must be used."""

    def __init__(self, blocks: list[InputRichBlock] | None = None, html: str | None = None, markdown: str | None = None, media: list[InputRichMessageMedia] | None = None, is_rtl: bool | None = None, skip_entity_detection: bool | None = None):
        self.blocks: list[InputRichBlock] | None = blocks
        self.html: str | None = html
        self.markdown: str | None = markdown
        self.media: list[InputRichMessageMedia] | None = media
        self.is_rtl: bool | None = is_rtl
        self.skip_entity_detection: bool | None = skip_entity_detection

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
        if self.blocks is not None:
            result['blocks'] = _serialize(self.blocks)
        if self.html is not None:
            result['html'] = _serialize(self.html)
        if self.markdown is not None:
            result['markdown'] = _serialize(self.markdown)
        if self.media is not None:
            result['media'] = _serialize(self.media)
        if self.is_rtl is not None:
            result['is_rtl'] = _serialize(self.is_rtl)
        if self.skip_entity_detection is not None:
            result['skip_entity_detection'] = _serialize(self.skip_entity_detection)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichMessage' | None:
        if not data:
            return None
        from .input_rich_block import InputRichBlock
        from .input_rich_message_media import InputRichMessageMedia
        return cls(
            blocks=[InputRichBlock.from_dict(i) for i in data.get('blocks')] if data.get('blocks') else None,
            html=data.get('html'),
            markdown=data.get('markdown'),
            media=[InputRichMessageMedia.from_dict(i) for i in data.get('media')] if data.get('media') else None,
            is_rtl=data.get('is_rtl'),
            skip_entity_detection=data.get('skip_entity_detection'),
        )