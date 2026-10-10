from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    


class InlineQueryResultVenue:
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue."""

    def __init__(self, type: str, id: str, latitude: float, longitude: float, title: str, address: str, foursquare_id: str | None = None, foursquare_type: str | None = None, google_place_id: str | None = None, google_place_type: str | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None):
        self.type: str = type
        self.id: str = id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.title: str = title
        self.address: str = address
        self.foursquare_id: str | None = foursquare_id
        self.foursquare_type: str | None = foursquare_type
        self.google_place_id: str | None = google_place_id
        self.google_place_type: str | None = google_place_type
        self.reply_markup: InlineKeyboardMarkup | None = reply_markup
        self.input_message_content: InputMessageContent | None = input_message_content
        self.thumbnail_url: str | None = thumbnail_url
        self.thumbnail_width: int | None = thumbnail_width
        self.thumbnail_height: int | None = thumbnail_height

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.latitude is not None:
            result['latitude'] = _serialize(self.latitude)
        if self.longitude is not None:
            result['longitude'] = _serialize(self.longitude)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.address is not None:
            result['address'] = _serialize(self.address)
        if self.foursquare_id is not None:
            result['foursquare_id'] = _serialize(self.foursquare_id)
        if self.foursquare_type is not None:
            result['foursquare_type'] = _serialize(self.foursquare_type)
        if self.google_place_id is not None:
            result['google_place_id'] = _serialize(self.google_place_id)
        if self.google_place_type is not None:
            result['google_place_type'] = _serialize(self.google_place_type)
        if self.reply_markup is not None:
            result['reply_markup'] = _serialize(self.reply_markup)
        if self.input_message_content is not None:
            result['input_message_content'] = _serialize(self.input_message_content)
        if self.thumbnail_url is not None:
            result['thumbnail_url'] = _serialize(self.thumbnail_url)
        if self.thumbnail_width is not None:
            result['thumbnail_width'] = _serialize(self.thumbnail_width)
        if self.thumbnail_height is not None:
            result['thumbnail_height'] = _serialize(self.thumbnail_height)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultVenue' | None:
        if not data:
            return None
        from .inline_keyboard_markup import InlineKeyboardMarkup
        from .input_message_content import InputMessageContent
        return cls(
            type=data.get('type'),
            id=data.get('id'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            title=data.get('title'),
            address=data.get('address'),
            foursquare_id=data.get('foursquare_id'),
            foursquare_type=data.get('foursquare_type'),
            google_place_id=data.get('google_place_id'),
            google_place_type=data.get('google_place_type'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
            thumbnail_url=data.get('thumbnail_url'),
            thumbnail_width=data.get('thumbnail_width'),
            thumbnail_height=data.get('thumbnail_height'),
        )