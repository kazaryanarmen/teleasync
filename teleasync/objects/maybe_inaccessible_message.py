from __future__ import annotations


class MaybeInaccessibleMessage:
    """Union: Message или InaccessibleMessage (если date == 0)."""

    @classmethod
    def from_dict(cls, data: dict | None):
        if not data:
            return None
        if data.get("date") == 0:
            from .inaccessible_message import InaccessibleMessage
            return InaccessibleMessage.from_dict(data)
        from .message import Message
        return Message.from_dict(data)