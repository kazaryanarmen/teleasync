from __future__ import annotations
from typing import TYPE_CHECKING



class InputContactMessageContent:
    """Represents the content of a contact message to be sent as the result of an inline query."""

    def __init__(self, phone_number: str, first_name: str, last_name: str | None = None, vcard: str | None = None):
        self.phone_number: str = phone_number
        self.first_name: str = first_name
        self.last_name: str | None = last_name
        self.vcard: str | None = vcard

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
        if self.phone_number is not None:
            result['phone_number'] = _serialize(self.phone_number)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.vcard is not None:
            result['vcard'] = _serialize(self.vcard)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputContactMessageContent' | None:
        if not data:
            return None
        return cls(
            phone_number=data.get('phone_number'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            vcard=data.get('vcard'),
        )