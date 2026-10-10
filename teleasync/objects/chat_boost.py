from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat_boost_source import ChatBoostSource
    


class ChatBoost:
    """This object contains information about a chat boost."""

    def __init__(self, boost_id: str, add_date: int, expiration_date: int, source: ChatBoostSource):
        self.boost_id: str = boost_id
        self.add_date: int = add_date
        self.expiration_date: int = expiration_date
        self.source: ChatBoostSource = source

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
        if self.boost_id is not None:
            result['boost_id'] = _serialize(self.boost_id)
        if self.add_date is not None:
            result['add_date'] = _serialize(self.add_date)
        if self.expiration_date is not None:
            result['expiration_date'] = _serialize(self.expiration_date)
        if self.source is not None:
            result['source'] = _serialize(self.source)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatBoost' | None:
        if not data:
            return None
        from .chat_boost_source import ChatBoostSource
        return cls(
            boost_id=data.get('boost_id'),
            add_date=data.get('add_date'),
            expiration_date=data.get('expiration_date'),
            source=ChatBoostSource.from_dict(data.get('source')),
        )