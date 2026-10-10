from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .encrypted_credentials import EncryptedCredentials
    
    from .encrypted_passport_element import EncryptedPassportElement
    


class PassportData:
    """Describes Telegram Passport data shared with the bot by the user."""

    def __init__(self, data: list[EncryptedPassportElement], credentials: EncryptedCredentials):
        self.data: list[EncryptedPassportElement] = data
        self.credentials: EncryptedCredentials = credentials

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
        if self.data is not None:
            result['data'] = _serialize(self.data)
        if self.credentials is not None:
            result['credentials'] = _serialize(self.credentials)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PassportData' | None:
        if not data:
            return None
        from .encrypted_credentials import EncryptedCredentials
        from .encrypted_passport_element import EncryptedPassportElement
        return cls(
            data=[EncryptedPassportElement.from_dict(i) for i in data.get('data')] if data.get('data') else None,
            credentials=EncryptedCredentials.from_dict(data.get('credentials')),
        )