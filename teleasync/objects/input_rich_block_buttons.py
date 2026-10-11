from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_message_button import RichMessageButton
    


class InputRichBlockButtons:
    """A block containing a list of buttons that are shown in one row, corresponding to the custom HTML tag <tg-button-row>."""

    def __init__(self, type: str, buttons: list[RichMessageButton], align: str | None = None):
        self.type: str = type
        self.buttons: list[RichMessageButton] = buttons
        self.align: str | None = align

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
        if self.buttons is not None:
            result['buttons'] = _serialize(self.buttons)
        if self.align is not None:
            result['align'] = _serialize(self.align)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockButtons' | None:
        if not data:
            return None
        from .rich_message_button import RichMessageButton
        return cls(
            type=data.get('type'),
            buttons=[RichMessageButton.from_dict(i1) for i1 in data.get('buttons')] if data.get('buttons') else None,
            align=data.get('align'),
        )