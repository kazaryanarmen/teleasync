from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .gift import Gift
    


class TransactionPartnerChat:
    """Describes a transaction with a chat."""

    def __init__(self, type: str, chat: Chat, gift: Gift | None = None):
        self.type: str = type
        self.chat: Chat = chat
        self.gift: Gift | None = gift

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
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.gift is not None:
            result['gift'] = _serialize(self.gift)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerChat' | None:
        if not data:
            return None
        from .chat import Chat
        from .gift import Gift
        return cls(
            type=data.get('type'),
            chat=Chat.from_dict(data.get('chat')),
            gift=Gift.from_dict(data.get('gift')),
        )