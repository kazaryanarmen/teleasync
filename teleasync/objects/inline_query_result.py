from __future__ import annotations
from typing import TYPE_CHECKING



class InlineQueryResult:
    """This object represents one result of an inline query. Telegram clients currently support results of the following 20 types: - InlineQueryResultCachedAudio - InlineQueryResultCachedDocument - InlineQueryResultCachedGif - InlineQueryResultCachedMpeg4Gif - InlineQueryResultCachedPhoto - InlineQueryResultCachedSticker - InlineQueryResultCachedVideo - InlineQueryResultCachedVoice - InlineQueryResultArticle - InlineQueryResultAudio - InlineQueryResultContact - InlineQueryResultGame - InlineQueryResultDocument - InlineQueryResultGif - InlineQueryResultLocation - InlineQueryResultMpeg4Gif - InlineQueryResultPhoto - InlineQueryResultVenue - InlineQueryResultVideo - InlineQueryResultVoice Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public."""

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
    def from_dict(cls, data: dict | None) -> 'InlineQueryResult' | None:
        if not data:
            return None
        return cls(
        )