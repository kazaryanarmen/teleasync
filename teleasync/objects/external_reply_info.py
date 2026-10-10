from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .animation import Animation
    
    from .audio import Audio
    
    from .chat import Chat
    
    from .checklist import Checklist
    
    from .contact import Contact
    
    from .dice import Dice
    
    from .document import Document
    
    from .game import Game
    
    from .giveaway import Giveaway
    
    from .giveaway_winners import GiveawayWinners
    
    from .invoice import Invoice
    
    from .link_preview_options import LinkPreviewOptions
    
    from .live_photo import LivePhoto
    
    from .location import Location
    
    from .message_origin import MessageOrigin
    
    from .paid_media_info import PaidMediaInfo
    
    from .photo_size import PhotoSize
    
    from .poll import Poll
    
    from .sticker import Sticker
    
    from .story import Story
    
    from .venue import Venue
    
    from .video import Video
    
    from .video_note import VideoNote
    
    from .voice import Voice
    


class ExternalReplyInfo:
    """This object contains information about a message that is being replied to, which may come from another chat or forum topic."""

    def __init__(self, origin: MessageOrigin, chat: Chat | None = None, message_id: int | None = None, link_preview_options: LinkPreviewOptions | None = None, animation_: Animation | None = None, audio_: Audio | None = None, document_: Document | None = None, live_photo: LivePhoto | None = None, paid_media: PaidMediaInfo | None = None, photo_: list[PhotoSize] | None = None, sticker_: Sticker | None = None, story: Story | None = None, video_: Video | None = None, video_note: VideoNote | None = None, voice_: Voice | None = None, has_media_spoiler: bool | None = None, checklist: Checklist | None = None, contact: Contact | None = None, dice: Dice | None = None, game: Game | None = None, giveaway: Giveaway | None = None, giveaway_winners: GiveawayWinners | None = None, invoice: Invoice | None = None, location: Location | None = None, poll: Poll | None = None, venue: Venue | None = None):
        self.origin: MessageOrigin = origin
        self.chat: Chat | None = chat
        self.message_id: int | None = message_id
        self.link_preview_options: LinkPreviewOptions | None = link_preview_options
        self.animation_: Animation | None = animation_
        self.audio_: Audio | None = audio_
        self.document_: Document | None = document_
        self.live_photo: LivePhoto | None = live_photo
        self.paid_media: PaidMediaInfo | None = paid_media
        self.photo_: list[PhotoSize] | None = photo_
        self.sticker_: Sticker | None = sticker_
        self.story: Story | None = story
        self.video_: Video | None = video_
        self.video_note: VideoNote | None = video_note
        self.voice_: Voice | None = voice_
        self.has_media_spoiler: bool | None = has_media_spoiler
        self.checklist: Checklist | None = checklist
        self.contact: Contact | None = contact
        self.dice: Dice | None = dice
        self.game: Game | None = game
        self.giveaway: Giveaway | None = giveaway
        self.giveaway_winners: GiveawayWinners | None = giveaway_winners
        self.invoice: Invoice | None = invoice
        self.location: Location | None = location
        self.poll: Poll | None = poll
        self.venue: Venue | None = venue

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
        if self.origin is not None:
            result['origin'] = _serialize(self.origin)
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.message_id is not None:
            result['message_id'] = _serialize(self.message_id)
        if self.link_preview_options is not None:
            result['link_preview_options'] = _serialize(self.link_preview_options)
        if self.animation_ is not None:
            result['animation'] = _serialize(self.animation_)
        if self.audio_ is not None:
            result['audio'] = _serialize(self.audio_)
        if self.document_ is not None:
            result['document'] = _serialize(self.document_)
        if self.live_photo is not None:
            result['live_photo'] = _serialize(self.live_photo)
        if self.paid_media is not None:
            result['paid_media'] = _serialize(self.paid_media)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.sticker_ is not None:
            result['sticker'] = _serialize(self.sticker_)
        if self.story is not None:
            result['story'] = _serialize(self.story)
        if self.video_ is not None:
            result['video'] = _serialize(self.video_)
        if self.video_note is not None:
            result['video_note'] = _serialize(self.video_note)
        if self.voice_ is not None:
            result['voice'] = _serialize(self.voice_)
        if self.has_media_spoiler is not None:
            result['has_media_spoiler'] = _serialize(self.has_media_spoiler)
        if self.checklist is not None:
            result['checklist'] = _serialize(self.checklist)
        if self.contact is not None:
            result['contact'] = _serialize(self.contact)
        if self.dice is not None:
            result['dice'] = _serialize(self.dice)
        if self.game is not None:
            result['game'] = _serialize(self.game)
        if self.giveaway is not None:
            result['giveaway'] = _serialize(self.giveaway)
        if self.giveaway_winners is not None:
            result['giveaway_winners'] = _serialize(self.giveaway_winners)
        if self.invoice is not None:
            result['invoice'] = _serialize(self.invoice)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.poll is not None:
            result['poll'] = _serialize(self.poll)
        if self.venue is not None:
            result['venue'] = _serialize(self.venue)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ExternalReplyInfo' | None:
        if not data:
            return None
        from .animation import Animation
        from .audio import Audio
        from .chat import Chat
        from .checklist import Checklist
        from .contact import Contact
        from .dice import Dice
        from .document import Document
        from .game import Game
        from .giveaway import Giveaway
        from .giveaway_winners import GiveawayWinners
        from .invoice import Invoice
        from .link_preview_options import LinkPreviewOptions
        from .live_photo import LivePhoto
        from .location import Location
        from .message_origin import MessageOrigin
        from .paid_media_info import PaidMediaInfo
        from .photo_size import PhotoSize
        from .poll import Poll
        from .sticker import Sticker
        from .story import Story
        from .venue import Venue
        from .video import Video
        from .video_note import VideoNote
        from .voice import Voice
        return cls(
            origin=MessageOrigin.from_dict(data.get('origin')),
            chat=Chat.from_dict(data.get('chat')),
            message_id=data.get('message_id'),
            link_preview_options=LinkPreviewOptions.from_dict(data.get('link_preview_options')),
            animation_=Animation.from_dict(data.get('animation')),
            audio_=Audio.from_dict(data.get('audio')),
            document_=Document.from_dict(data.get('document')),
            live_photo=LivePhoto.from_dict(data.get('live_photo')),
            paid_media=PaidMediaInfo.from_dict(data.get('paid_media')),
            photo_=[PhotoSize.from_dict(i) for i in data.get('photo')] if data.get('photo') else None,
            sticker_=Sticker.from_dict(data.get('sticker')),
            story=Story.from_dict(data.get('story')),
            video_=Video.from_dict(data.get('video')),
            video_note=VideoNote.from_dict(data.get('video_note')),
            voice_=Voice.from_dict(data.get('voice')),
            has_media_spoiler=data.get('has_media_spoiler'),
            checklist=Checklist.from_dict(data.get('checklist')),
            contact=Contact.from_dict(data.get('contact')),
            dice=Dice.from_dict(data.get('dice')),
            game=Game.from_dict(data.get('game')),
            giveaway=Giveaway.from_dict(data.get('giveaway')),
            giveaway_winners=GiveawayWinners.from_dict(data.get('giveaway_winners')),
            invoice=Invoice.from_dict(data.get('invoice')),
            location=Location.from_dict(data.get('location')),
            poll=Poll.from_dict(data.get('poll')),
            venue=Venue.from_dict(data.get('venue')),
        )