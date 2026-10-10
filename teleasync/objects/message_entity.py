from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc."""

    def __init__(self, type: str, offset: int, length: int, url: str | None = None, user: User | None = None, language: str | None = None, custom_emoji_id: str | None = None, unix_time: int | None = None, date_time_format: str | None = None):
        self.type: str = type
        self.offset: int = offset
        self.length: int = length
        self.url: str | None = url
        self.user: User | None = user
        self.language: str | None = language
        self.custom_emoji_id: str | None = custom_emoji_id
        self.unix_time: int | None = unix_time
        self.date_time_format: str | None = date_time_format

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
        if self.offset is not None:
            result['offset'] = _serialize(self.offset)
        if self.length is not None:
            result['length'] = _serialize(self.length)
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.language is not None:
            result['language'] = _serialize(self.language)
        if self.custom_emoji_id is not None:
            result['custom_emoji_id'] = _serialize(self.custom_emoji_id)
        if self.unix_time is not None:
            result['unix_time'] = _serialize(self.unix_time)
        if self.date_time_format is not None:
            result['date_time_format'] = _serialize(self.date_time_format)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'MessageEntity' | None:
        if not data:
            return None
        from .user import User
        return cls(
            type=data.get('type'),
            offset=data.get('offset'),
            length=data.get('length'),
            url=data.get('url'),
            user=User.from_dict(data.get('user')),
            language=data.get('language'),
            custom_emoji_id=data.get('custom_emoji_id'),
            unix_time=data.get('unix_time'),
            date_time_format=data.get('date_time_format'),
        )