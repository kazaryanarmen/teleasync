from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_message_button import RichMessageButton
    


class RichTextButton:
    """A button."""

    def __init__(self, type: str, button: RichMessageButton):
        self.type: str = type
        self.button: RichMessageButton = button

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
        if self.button is not None:
            result['button'] = _serialize(self.button)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichTextButton' | None:
        if not data:
            return None
        from .rich_message_button import RichMessageButton
        return cls(
            type=data.get('type'),
            button=RichMessageButton.from_dict(data.get('button')),
        )