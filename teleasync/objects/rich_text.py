from __future__ import annotations
from typing import TYPE_CHECKING



class RichText:
    """This object represents a rich formatted text. Currently, it can be either a String for plain text, an Array of RichText, or any of the following types: - RichTextBold - RichTextItalic - RichTextUnderline - RichTextStrikethrough - RichTextSpoiler - RichTextDateTime - RichTextTextMention - RichTextSubscript - RichTextSuperscript - RichTextMarked - RichTextCode - RichTextCustomEmoji - RichTextMathematicalExpression - RichTextUrl - RichTextEmailAddress - RichTextPhoneNumber - RichTextBankCardNumber - RichTextMention - RichTextHashtag - RichTextCashtag - RichTextBotCommand - RichTextButton - RichTextAnchor - RichTextAnchorLink - RichTextReference - RichTextReferenceLink"""

    def __init__(self):
        pass

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'RichText' | None:
        if not data:
            return None
        return cls(
        )