from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .inline_keyboard_markup import InlineKeyboardMarkup
    
    from .input_message_content import InputMessageContent
    


class InlineQueryResultLocation:
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location."""

    def __init__(self, type: str, id: str, latitude: float, longitude: float, title: str, horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None, proximity_alert_radius: int | None = None, reply_markup: InlineKeyboardMarkup | None = None, input_message_content: InputMessageContent | None = None, thumbnail_url: str | None = None, thumbnail_width: int | None = None, thumbnail_height: int | None = None):
        self.type: str = type
        self.id: str = id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.title: str = title
        self.horizontal_accuracy: float | None = horizontal_accuracy
        self.live_period: int | None = live_period
        self.heading: int | None = heading
        self.proximity_alert_radius: int | None = proximity_alert_radius
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
        if self.horizontal_accuracy is not None:
            result['horizontal_accuracy'] = _serialize(self.horizontal_accuracy)
        if self.live_period is not None:
            result['live_period'] = _serialize(self.live_period)
        if self.heading is not None:
            result['heading'] = _serialize(self.heading)
        if self.proximity_alert_radius is not None:
            result['proximity_alert_radius'] = _serialize(self.proximity_alert_radius)
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
    def from_dict(cls, data: dict | None) -> 'InlineQueryResultLocation' | None:
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
            horizontal_accuracy=data.get('horizontal_accuracy'),
            live_period=data.get('live_period'),
            heading=data.get('heading'),
            proximity_alert_radius=data.get('proximity_alert_radius'),
            reply_markup=InlineKeyboardMarkup.from_dict(data.get('reply_markup')),
            input_message_content=InputMessageContent.from_dict(data.get('input_message_content')),
            thumbnail_url=data.get('thumbnail_url'),
            thumbnail_width=data.get('thumbnail_width'),
            thumbnail_height=data.get('thumbnail_height'),
        )