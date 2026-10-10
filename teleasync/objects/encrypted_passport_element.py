from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .passport_file import PassportFile
    


class EncryptedPassportElement:
    """Describes documents or other Telegram Passport elements shared with the bot by the user."""

    def __init__(self, type: str, hash: str, data: str | None = None, phone_number: str | None = None, email: str | None = None, files: list[PassportFile] | None = None, front_side: PassportFile | None = None, reverse_side: PassportFile | None = None, selfie: PassportFile | None = None, translation: list[PassportFile] | None = None):
        self.type: str = type
        self.hash: str = hash
        self.data: str | None = data
        self.phone_number: str | None = phone_number
        self.email: str | None = email
        self.files: list[PassportFile] | None = files
        self.front_side: PassportFile | None = front_side
        self.reverse_side: PassportFile | None = reverse_side
        self.selfie: PassportFile | None = selfie
        self.translation: list[PassportFile] | None = translation

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
        if self.hash is not None:
            result['hash'] = _serialize(self.hash)
        if self.data is not None:
            result['data'] = _serialize(self.data)
        if self.phone_number is not None:
            result['phone_number'] = _serialize(self.phone_number)
        if self.email is not None:
            result['email'] = _serialize(self.email)
        if self.files is not None:
            result['files'] = _serialize(self.files)
        if self.front_side is not None:
            result['front_side'] = _serialize(self.front_side)
        if self.reverse_side is not None:
            result['reverse_side'] = _serialize(self.reverse_side)
        if self.selfie is not None:
            result['selfie'] = _serialize(self.selfie)
        if self.translation is not None:
            result['translation'] = _serialize(self.translation)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'EncryptedPassportElement' | None:
        if not data:
            return None
        from .passport_file import PassportFile
        return cls(
            type=data.get('type'),
            hash=data.get('hash'),
            data=data.get('data'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            files=[PassportFile.from_dict(i) for i in data.get('files')] if data.get('files') else None,
            front_side=PassportFile.from_dict(data.get('front_side')),
            reverse_side=PassportFile.from_dict(data.get('reverse_side')),
            selfie=PassportFile.from_dict(data.get('selfie')),
            translation=[PassportFile.from_dict(i) for i in data.get('translation')] if data.get('translation') else None,
        )