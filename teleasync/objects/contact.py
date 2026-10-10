from __future__ import annotations
from typing import TYPE_CHECKING



class Contact:
    """This object represents a phone contact."""

    def __init__(self, phone_number: str, first_name: str, last_name: str | None = None, user_id: int | None = None, vcard: str | None = None):
        self.phone_number: str = phone_number
        self.first_name: str = first_name
        self.last_name: str | None = last_name
        self.user_id: int | None = user_id
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
        if self.user_id is not None:
            result['user_id'] = _serialize(self.user_id)
        if self.vcard is not None:
            result['vcard'] = _serialize(self.vcard)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Contact' | None:
        if not data:
            return None
        return cls(
            phone_number=data.get('phone_number'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            user_id=data.get('user_id'),
            vcard=data.get('vcard'),
        )