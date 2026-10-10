from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .animation import Animation
    
    from .audio import Audio
    
    from .document import Document
    
    from .link import Link
    
    from .live_photo import LivePhoto
    
    from .location import Location
    
    from .photo_size import PhotoSize
    
    from .sticker import Sticker
    
    from .venue import Venue
    
    from .video import Video
    


class PollMedia:
    """At most one of the optional fields can be present in any given object."""

    def __init__(self, animation_: Animation | None = None, audio_: Audio | None = None, document_: Document | None = None, link: Link | None = None, live_photo: LivePhoto | None = None, location: Location | None = None, photo_: list[PhotoSize] | None = None, sticker_: Sticker | None = None, venue: Venue | None = None, video_: Video | None = None):
        self.animation_: Animation | None = animation_
        self.audio_: Audio | None = audio_
        self.document_: Document | None = document_
        self.link: Link | None = link
        self.live_photo: LivePhoto | None = live_photo
        self.location: Location | None = location
        self.photo_: list[PhotoSize] | None = photo_
        self.sticker_: Sticker | None = sticker_
        self.venue: Venue | None = venue
        self.video_: Video | None = video_

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
        if self.animation_ is not None:
            result['animation'] = _serialize(self.animation_)
        if self.audio_ is not None:
            result['audio'] = _serialize(self.audio_)
        if self.document_ is not None:
            result['document'] = _serialize(self.document_)
        if self.link is not None:
            result['link'] = _serialize(self.link)
        if self.live_photo is not None:
            result['live_photo'] = _serialize(self.live_photo)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.sticker_ is not None:
            result['sticker'] = _serialize(self.sticker_)
        if self.venue is not None:
            result['venue'] = _serialize(self.venue)
        if self.video_ is not None:
            result['video'] = _serialize(self.video_)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'PollMedia' | None:
        if not data:
            return None
        from .animation import Animation
        from .audio import Audio
        from .document import Document
        from .link import Link
        from .live_photo import LivePhoto
        from .location import Location
        from .photo_size import PhotoSize
        from .sticker import Sticker
        from .venue import Venue
        from .video import Video
        return cls(
            animation_=Animation.from_dict(data.get('animation')),
            audio_=Audio.from_dict(data.get('audio')),
            document_=Document.from_dict(data.get('document')),
            link=Link.from_dict(data.get('link')),
            live_photo=LivePhoto.from_dict(data.get('live_photo')),
            location=Location.from_dict(data.get('location')),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
            sticker_=Sticker.from_dict(data.get('sticker')),
            venue=Venue.from_dict(data.get('venue')),
            video_=Video.from_dict(data.get('video')),
        )