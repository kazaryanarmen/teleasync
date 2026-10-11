from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .paid_media import PaidMedia
    


class PaidMediaInfo:
    """Describes the paid media added to a message."""

    def __init__(self, star_count: int, paid_media: list[PaidMedia]):
        self.star_count: int = star_count
        self.paid_media: list[PaidMedia] = paid_media

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
        if self.star_count is not None:
            result['star_count'] = _serialize(self.star_count)
        if self.paid_media is not None:
            result['paid_media'] = _serialize(self.paid_media)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PaidMediaInfo' | None:
        if not data:
            return None
        from .paid_media import PaidMedia
        return cls(
            star_count=data.get('star_count'),
            paid_media=[PaidMedia.from_dict(i1) for i1 in data.get('paid_media')] if data.get('paid_media') else None,
        )