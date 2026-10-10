from __future__ import annotations
from typing import TYPE_CHECKING



class PassportElementError:
    """This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of: - PassportElementErrorDataField - PassportElementErrorFrontSide - PassportElementErrorReverseSide - PassportElementErrorSelfie - PassportElementErrorFile - PassportElementErrorFiles - PassportElementErrorTranslationFile - PassportElementErrorTranslationFiles - PassportElementErrorUnspecified"""

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
    def from_dict(cls, data: dict | None) -> 'PassportElementError' | None:
        if not data:
            return None
        return cls(
        )