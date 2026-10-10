from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_rich_block import InputRichBlock
    


class InputRichBlockListItem:
    """An item of a list to be sent."""

    def __init__(self, blocks: list[InputRichBlock], has_checkbox: bool | None = None, is_checked: bool | None = None, value: int | None = None, type: str | None = None):
        self.blocks: list[InputRichBlock] = blocks
        self.has_checkbox: bool | None = has_checkbox
        self.is_checked: bool | None = is_checked
        self.value: int | None = value
        self.type: str | None = type

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
        if self.has_checkbox is not None:
            result['has_checkbox'] = _serialize(self.has_checkbox)
        if self.is_checked is not None:
            result['is_checked'] = _serialize(self.is_checked)
        if self.value is not None:
            result['value'] = _serialize(self.value)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockListItem' | None:
        if not data:
            return None
        from .input_rich_block import InputRichBlock
        return cls(
            blocks=[InputRichBlock.from_dict(i) for i in data.get('blocks')] if data.get('blocks') else None,
            has_checkbox=data.get('has_checkbox'),
            is_checked=data.get('is_checked'),
            value=data.get('value'),
            type=data.get('type'),
        )