from __future__ import annotations
from typing import TYPE_CHECKING



class EncryptedCredentials:
    """Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes."""

    def __init__(self, data: str, hash: str, secret: str):
        self.data: str = data
        self.hash: str = hash
        self.secret: str = secret

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
        if self.hash is not None:
            result['hash'] = _serialize(self.hash)
        if self.secret is not None:
            result['secret'] = _serialize(self.secret)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'EncryptedCredentials' | None:
        if not data:
            return None
        return cls(
            data=data.get('data'),
            hash=data.get('hash'),
            secret=data.get('secret'),
        )