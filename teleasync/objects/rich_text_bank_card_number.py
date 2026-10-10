from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .rich_text import RichText
    


class RichTextBankCardNumber:
    """A text with a bank card number."""

    def __init__(self, type: str, text: RichText, bank_card_number: str):
        self.type: str = type
        self.text: RichText = text
        self.bank_card_number: str = bank_card_number

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
        if self.text is not None:
            result['text'] = _serialize(self.text)
        if self.bank_card_number is not None:
            result['bank_card_number'] = _serialize(self.bank_card_number)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichTextBankCardNumber' | None:
        if not data:
            return None
        from .rich_text import RichText
        return cls(
            type=data.get('type'),
            text=RichText.from_dict(data.get('text')),
            bank_card_number=data.get('bank_card_number'),
        )