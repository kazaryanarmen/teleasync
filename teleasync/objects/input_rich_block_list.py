from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_rich_block_list_item import InputRichBlockListItem
    


class InputRichBlockList:
    """A list of blocks, corresponding to the HTML tag <ul> or <ol> with multiple nested tags <li>."""

    def __init__(self, type: str, items: list[InputRichBlockListItem]):
        self.type: str = type
        self.items: list[InputRichBlockListItem] = items

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
        if self.items is not None:
            result['items'] = _serialize(self.items)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockList' | None:
        if not data:
            return None
        from .input_rich_block_list_item import InputRichBlockListItem
        return cls(
            type=data.get('type'),
            items=[InputRichBlockListItem.from_dict(i) for i in data.get('items')] if data.get('items') else None,
        )