from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_block_table_cell import RichBlockTableCell
    
    from .rich_text import RichText
    


class InputRichBlockTable:
    """A table, corresponding to the HTML tag <table>."""

    def __init__(self, type: str, cells: list[RichBlockTableCell], is_bordered: bool | None = None, is_striped: bool | None = None, is_compact: bool | None = None, caption: RichText | None = None):
        self.type: str = type
        self.cells: list[RichBlockTableCell] = cells
        self.is_bordered: bool | None = is_bordered
        self.is_striped: bool | None = is_striped
        self.is_compact: bool | None = is_compact
        self.caption: RichText | None = caption

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
        if self.cells is not None:
            result['cells'] = _serialize(self.cells)
        if self.is_bordered is not None:
            result['is_bordered'] = _serialize(self.is_bordered)
        if self.is_striped is not None:
            result['is_striped'] = _serialize(self.is_striped)
        if self.is_compact is not None:
            result['is_compact'] = _serialize(self.is_compact)
        if self.caption is not None:
            result['caption'] = _serialize(self.caption)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockTable' | None:
        if not data:
            return None
        from .rich_block_table_cell import RichBlockTableCell
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            cells=[RichBlockTableCell.from_dict(i) for i in data.get('cells')] if data.get('cells') else None,
            is_bordered=data.get('is_bordered'),
            is_striped=data.get('is_striped'),
            is_compact=data.get('is_compact'),
            caption=RichText.from_dict(data.get('caption')),
        )