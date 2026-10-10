from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .location import Location
    
    from .rich_block_caption import RichBlockCaption
    


class InputRichBlockMap:
    """A block with a map, corresponding to the custom HTML tag <tg-map>. The map's width and height must not exceed 10000 in total. The width and height ratio must be at most 20."""

    def __init__(self, type: str, location: Location, zoom: int | None = None, width: int | None = None, height: int | None = None, caption: RichBlockCaption | None = None):
        self.type: str = type
        self.location: Location = location
        self.zoom: int | None = zoom
        self.width: int | None = width
        self.height: int | None = height
        self.caption: RichBlockCaption | None = caption

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
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.zoom is not None:
            result['zoom'] = _serialize(self.zoom)
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockMap' | None:
        if not data:
            return None
        from .location import Location
        from .rich_block_caption import RichBlockCaption
        return cls(
            type=data.get('type'),
            location=Location.from_dict(data.get('location')),
            zoom=data.get('zoom'),
            width=data.get('width'),
            height=data.get('height'),
            caption=RichBlockCaption.from_dict(data.get('caption')),
        )