from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .audio import Audio
    


class UserProfileAudios:
    """This object represents the audios displayed on a user's profile."""

    def __init__(self, total_count: int, audios: list[Audio]):
        self.total_count: int = total_count
        self.audios: list[Audio] = audios

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
        if self.total_count is not None:
            result['total_count'] = _serialize(self.total_count)
        if self.audios is not None:
            result['audios'] = _serialize(self.audios)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UserProfileAudios' | None:
        if not data:
            return None
        from .audio import Audio
        return cls(
            total_count=data.get('total_count'),
            audios=[Audio.from_dict(i) for i in data.get('audios')] if data.get('audios') else None,
        )