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

    def __init__(self, animation: Animation | None = None, audio: Audio | None = None, document: Document | None = None, link: Link | None = None, live_photo: LivePhoto | None = None, location: Location | None = None, photo: list[PhotoSize] | None = None, sticker: Sticker | None = None, venue: Venue | None = None, video: Video | None = None):
        self.animation: Animation | None = animation
        self.audio: Audio | None = audio
        self.document: Document | None = document
        self.link: Link | None = link
        self.live_photo: LivePhoto | None = live_photo
        self.location: Location | None = location
        self.photo: list[PhotoSize] | None = photo
        self.sticker: Sticker | None = sticker
        self.venue: Venue | None = venue
        self.video: Video | None = video

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
        if self.animation is not None:
            result['animation'] = _serialize(self.animation)
        if self.audio is not None:
            result['audio'] = _serialize(self.audio)
        if self.document is not None:
            result['document'] = _serialize(self.document)
        if self.link is not None:
            result['link'] = _serialize(self.link)
        if self.live_photo is not None:
            result['live_photo'] = _serialize(self.live_photo)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.photo is not None:
            result['photo'] = _serialize(self.photo)
        if self.sticker is not None:
            result['sticker'] = _serialize(self.sticker)
        if self.venue is not None:
            result['venue'] = _serialize(self.venue)
        if self.video is not None:
            result['video'] = _serialize(self.video)
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
            animation=Animation.from_dict(data.get('animation')),
            audio=Audio.from_dict(data.get('audio')),
            document=Document.from_dict(data.get('document')),
            link=Link.from_dict(data.get('link')),
            live_photo=LivePhoto.from_dict(data.get('live_photo')),
            location=Location.from_dict(data.get('location')),
            photo=[PhotoSize.from_dict(i1) for i1 in data.get('photo')] if data.get('photo') else None,
            sticker=Sticker.from_dict(data.get('sticker')),
            venue=Venue.from_dict(data.get('venue')),
            video=Video.from_dict(data.get('video')),
        )