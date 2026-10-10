from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_rich_message import InputRichMessage
    


class InputRichMessageContent:
    """Represents the content of a rich message to be sent as the result of an inline query."""

    def __init__(self, rich_message: InputRichMessage):
        self.rich_message: InputRichMessage = rich_message

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
        if self.rich_message is not None:
            result['rich_message'] = _serialize(self.rich_message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichMessageContent' | None:
        if not data:
            return None
        from .input_rich_message import InputRichMessage
        return cls(
            rich_message=InputRichMessage.from_dict(data.get('rich_message')),
        )