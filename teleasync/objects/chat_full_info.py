from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .accepted_gift_types import AcceptedGiftTypes
    
    from .audio import Audio
    
    from .birthdate import Birthdate
    
    from .business_intro import BusinessIntro
    
    from .business_location import BusinessLocation
    
    from .business_opening_hours import BusinessOpeningHours
    
    from .chat import Chat
    
    from .chat_location import ChatLocation
    
    from .chat_permissions import ChatPermissions
    
    from .chat_photo import ChatPhoto
    
    from .community import Community
    
    from .message import Message
    
    from .reaction_type import ReactionType
    
    from .unique_gift_colors import UniqueGiftColors
    
    from .user import User
    
    from .user_rating import UserRating
    


class ChatFullInfo:
    """This object contains full information about a chat."""

    def __init__(self, id: int, type: str, accent_color_id: int, max_reaction_count: int, accepted_gift_types: AcceptedGiftTypes, title: str | None = None, username: str | None = None, first_name: str | None = None, last_name: str | None = None, is_forum: bool | None = None, is_direct_messages: bool | None = None, photo_: ChatPhoto | None = None, active_usernames: list[str] | None = None, birthdate: Birthdate | None = None, business_intro: BusinessIntro | None = None, business_location: BusinessLocation | None = None, business_opening_hours: BusinessOpeningHours | None = None, personal_chat: Chat | None = None, parent_chat: Chat | None = None, available_reactions: list[ReactionType] | None = None, background_custom_emoji_id: str | None = None, profile_accent_color_id: int | None = None, profile_background_custom_emoji_id: str | None = None, emoji_status_custom_emoji_id: str | None = None, emoji_status_expiration_date: int | None = None, bio: str | None = None, has_private_forwards: bool | None = None, has_restricted_voice_and_video_messages: bool | None = None, join_to_send_messages: bool | None = None, join_by_request: bool | None = None, description: str | None = None, invite_link: str | None = None, pinned_message: Message | None = None, permissions: ChatPermissions | None = None, can_send_paid_media: bool | None = None, slow_mode_delay: int | None = None, unrestrict_boost_count: int | None = None, message_auto_delete_time: int | None = None, has_aggressive_anti_spam_enabled: bool | None = None, has_hidden_members: bool | None = None, has_protected_content: bool | None = None, has_visible_history: bool | None = None, sticker_set_name: str | None = None, can_set_sticker_set: bool | None = None, custom_emoji_sticker_set_name: str | None = None, linked_chat_id: int | None = None, location: ChatLocation | None = None, rating: UserRating | None = None, first_profile_audio: Audio | None = None, unique_gift_colors: UniqueGiftColors | None = None, paid_message_star_count: int | None = None, guard_bot: User | None = None, community: Community | None = None):
        self.id: int = id
        self.type: str = type
        self.accent_color_id: int = accent_color_id
        self.max_reaction_count: int = max_reaction_count
        self.accepted_gift_types: AcceptedGiftTypes = accepted_gift_types
        self.title: str | None = title
        self.username: str | None = username
        self.first_name: str | None = first_name
        self.last_name: str | None = last_name
        self.is_forum: bool | None = is_forum
        self.is_direct_messages: bool | None = is_direct_messages
        self.photo_: ChatPhoto | None = photo_
        self.active_usernames: list[str] | None = active_usernames
        self.birthdate: Birthdate | None = birthdate
        self.business_intro: BusinessIntro | None = business_intro
        self.business_location: BusinessLocation | None = business_location
        self.business_opening_hours: BusinessOpeningHours | None = business_opening_hours
        self.personal_chat: Chat | None = personal_chat
        self.parent_chat: Chat | None = parent_chat
        self.available_reactions: list[ReactionType] | None = available_reactions
        self.background_custom_emoji_id: str | None = background_custom_emoji_id
        self.profile_accent_color_id: int | None = profile_accent_color_id
        self.profile_background_custom_emoji_id: str | None = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id: str | None = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date: int | None = emoji_status_expiration_date
        self.bio: str | None = bio
        self.has_private_forwards: bool | None = has_private_forwards
        self.has_restricted_voice_and_video_messages: bool | None = has_restricted_voice_and_video_messages
        self.join_to_send_messages: bool | None = join_to_send_messages
        self.join_by_request: bool | None = join_by_request
        self.description: str | None = description
        self.invite_link: str | None = invite_link
        self.pinned_message: Message | None = pinned_message
        self.permissions: ChatPermissions | None = permissions
        self.can_send_paid_media: bool | None = can_send_paid_media
        self.slow_mode_delay: int | None = slow_mode_delay
        self.unrestrict_boost_count: int | None = unrestrict_boost_count
        self.message_auto_delete_time: int | None = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled: bool | None = has_aggressive_anti_spam_enabled
        self.has_hidden_members: bool | None = has_hidden_members
        self.has_protected_content: bool | None = has_protected_content
        self.has_visible_history: bool | None = has_visible_history
        self.sticker_set_name: str | None = sticker_set_name
        self.can_set_sticker_set: bool | None = can_set_sticker_set
        self.custom_emoji_sticker_set_name: str | None = custom_emoji_sticker_set_name
        self.linked_chat_id: int | None = linked_chat_id
        self.location: ChatLocation | None = location
        self.rating: UserRating | None = rating
        self.first_profile_audio: Audio | None = first_profile_audio
        self.unique_gift_colors: UniqueGiftColors | None = unique_gift_colors
        self.paid_message_star_count: int | None = paid_message_star_count
        self.guard_bot: User | None = guard_bot
        self.community: Community | None = community

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
        if self.id is not None:
            result['id'] = _serialize(self.id)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.accent_color_id is not None:
            result['accent_color_id'] = _serialize(self.accent_color_id)
        if self.max_reaction_count is not None:
            result['max_reaction_count'] = _serialize(self.max_reaction_count)
        if self.accepted_gift_types is not None:
            result['accepted_gift_types'] = _serialize(self.accepted_gift_types)
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.username is not None:
            result['username'] = _serialize(self.username)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.is_forum is not None:
            result['is_forum'] = _serialize(self.is_forum)
        if self.is_direct_messages is not None:
            result['is_direct_messages'] = _serialize(self.is_direct_messages)
        if self.photo_ is not None:
            result['photo'] = _serialize(self.photo_)
        if self.active_usernames is not None:
            result['active_usernames'] = _serialize(self.active_usernames)
        if self.birthdate is not None:
            result['birthdate'] = _serialize(self.birthdate)
        if self.business_intro is not None:
            result['business_intro'] = _serialize(self.business_intro)
        if self.business_location is not None:
            result['business_location'] = _serialize(self.business_location)
        if self.business_opening_hours is not None:
            result['business_opening_hours'] = _serialize(self.business_opening_hours)
        if self.personal_chat is not None:
            result['personal_chat'] = _serialize(self.personal_chat)
        if self.parent_chat is not None:
            result['parent_chat'] = _serialize(self.parent_chat)
        if self.available_reactions is not None:
            result['available_reactions'] = _serialize(self.available_reactions)
        if self.background_custom_emoji_id is not None:
            result['background_custom_emoji_id'] = _serialize(self.background_custom_emoji_id)
        if self.profile_accent_color_id is not None:
            result['profile_accent_color_id'] = _serialize(self.profile_accent_color_id)
        if self.profile_background_custom_emoji_id is not None:
            result['profile_background_custom_emoji_id'] = _serialize(self.profile_background_custom_emoji_id)
        if self.emoji_status_custom_emoji_id is not None:
            result['emoji_status_custom_emoji_id'] = _serialize(self.emoji_status_custom_emoji_id)
        if self.emoji_status_expiration_date is not None:
            result['emoji_status_expiration_date'] = _serialize(self.emoji_status_expiration_date)
        if self.bio is not None:
            result['bio'] = _serialize(self.bio)
        if self.has_private_forwards is not None:
            result['has_private_forwards'] = _serialize(self.has_private_forwards)
        if self.has_restricted_voice_and_video_messages is not None:
            result['has_restricted_voice_and_video_messages'] = _serialize(self.has_restricted_voice_and_video_messages)
        if self.join_to_send_messages is not None:
            result['join_to_send_messages'] = _serialize(self.join_to_send_messages)
        if self.join_by_request is not None:
            result['join_by_request'] = _serialize(self.join_by_request)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.invite_link is not None:
            result['invite_link'] = _serialize(self.invite_link)
        if self.pinned_message is not None:
            result['pinned_message'] = _serialize(self.pinned_message)
        if self.permissions is not None:
            result['permissions'] = _serialize(self.permissions)
        if self.can_send_paid_media is not None:
            result['can_send_paid_media'] = _serialize(self.can_send_paid_media)
        if self.slow_mode_delay is not None:
            result['slow_mode_delay'] = _serialize(self.slow_mode_delay)
        if self.unrestrict_boost_count is not None:
            result['unrestrict_boost_count'] = _serialize(self.unrestrict_boost_count)
        if self.message_auto_delete_time is not None:
            result['message_auto_delete_time'] = _serialize(self.message_auto_delete_time)
        if self.has_aggressive_anti_spam_enabled is not None:
            result['has_aggressive_anti_spam_enabled'] = _serialize(self.has_aggressive_anti_spam_enabled)
        if self.has_hidden_members is not None:
            result['has_hidden_members'] = _serialize(self.has_hidden_members)
        if self.has_protected_content is not None:
            result['has_protected_content'] = _serialize(self.has_protected_content)
        if self.has_visible_history is not None:
            result['has_visible_history'] = _serialize(self.has_visible_history)
        if self.sticker_set_name is not None:
            result['sticker_set_name'] = _serialize(self.sticker_set_name)
        if self.can_set_sticker_set is not None:
            result['can_set_sticker_set'] = _serialize(self.can_set_sticker_set)
        if self.custom_emoji_sticker_set_name is not None:
            result['custom_emoji_sticker_set_name'] = _serialize(self.custom_emoji_sticker_set_name)
        if self.linked_chat_id is not None:
            result['linked_chat_id'] = _serialize(self.linked_chat_id)
        if self.location is not None:
            result['location'] = _serialize(self.location)
        if self.rating is not None:
            result['rating'] = _serialize(self.rating)
        if self.first_profile_audio is not None:
            result['first_profile_audio'] = _serialize(self.first_profile_audio)
        if self.unique_gift_colors is not None:
            result['unique_gift_colors'] = _serialize(self.unique_gift_colors)
        if self.paid_message_star_count is not None:
            result['paid_message_star_count'] = _serialize(self.paid_message_star_count)
        if self.guard_bot is not None:
            result['guard_bot'] = _serialize(self.guard_bot)
        if self.community is not None:
            result['community'] = _serialize(self.community)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatFullInfo' | None:
        if not data:
            return None
        from .accepted_gift_types import AcceptedGiftTypes
        from .audio import Audio
        from .birthdate import Birthdate
        from .business_intro import BusinessIntro
        from .business_location import BusinessLocation
        from .business_opening_hours import BusinessOpeningHours
        from .chat import Chat
        from .chat_location import ChatLocation
        from .chat_permissions import ChatPermissions
        from .chat_photo import ChatPhoto
        from .community import Community
        from .message import Message
        from .reaction_type import ReactionType
        from .unique_gift_colors import UniqueGiftColors
        from .user import User
        from .user_rating import UserRating
        return cls(
            id=data.get('id'),
            type=data.get('type'),
            accent_color_id=data.get('accent_color_id'),
            max_reaction_count=data.get('max_reaction_count'),
            accepted_gift_types=AcceptedGiftTypes.from_dict(data.get('accepted_gift_types')),
            title=data.get('title'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            is_forum=data.get('is_forum'),
            is_direct_messages=data.get('is_direct_messages'),
            photo_=ChatPhoto.from_dict(data.get('photo')),
            active_usernames=data.get('active_usernames'),
            birthdate=Birthdate.from_dict(data.get('birthdate')),
            business_intro=BusinessIntro.from_dict(data.get('business_intro')),
            business_location=BusinessLocation.from_dict(data.get('business_location')),
            business_opening_hours=BusinessOpeningHours.from_dict(data.get('business_opening_hours')),
            personal_chat=Chat.from_dict(data.get('personal_chat')),
            parent_chat=Chat.from_dict(data.get('parent_chat')),
            available_reactions=[ReactionType.from_dict(i) for i in data.get('available_reactions')] if data.get('available_reactions') else None,
            background_custom_emoji_id=data.get('background_custom_emoji_id'),
            profile_accent_color_id=data.get('profile_accent_color_id'),
            profile_background_custom_emoji_id=data.get('profile_background_custom_emoji_id'),
            emoji_status_custom_emoji_id=data.get('emoji_status_custom_emoji_id'),
            emoji_status_expiration_date=data.get('emoji_status_expiration_date'),
            bio=data.get('bio'),
            has_private_forwards=data.get('has_private_forwards'),
            has_restricted_voice_and_video_messages=data.get('has_restricted_voice_and_video_messages'),
            join_to_send_messages=data.get('join_to_send_messages'),
            join_by_request=data.get('join_by_request'),
            description=data.get('description'),
            invite_link=data.get('invite_link'),
            pinned_message=Message.from_dict(data.get('pinned_message')),
            permissions=ChatPermissions.from_dict(data.get('permissions')),
            can_send_paid_media=data.get('can_send_paid_media'),
            slow_mode_delay=data.get('slow_mode_delay'),
            unrestrict_boost_count=data.get('unrestrict_boost_count'),
            message_auto_delete_time=data.get('message_auto_delete_time'),
            has_aggressive_anti_spam_enabled=data.get('has_aggressive_anti_spam_enabled'),
            has_hidden_members=data.get('has_hidden_members'),
            has_protected_content=data.get('has_protected_content'),
            has_visible_history=data.get('has_visible_history'),
            sticker_set_name=data.get('sticker_set_name'),
            can_set_sticker_set=data.get('can_set_sticker_set'),
            custom_emoji_sticker_set_name=data.get('custom_emoji_sticker_set_name'),
            linked_chat_id=data.get('linked_chat_id'),
            location=ChatLocation.from_dict(data.get('location')),
            rating=UserRating.from_dict(data.get('rating')),
            first_profile_audio=Audio.from_dict(data.get('first_profile_audio')),
            unique_gift_colors=UniqueGiftColors.from_dict(data.get('unique_gift_colors')),
            paid_message_star_count=data.get('paid_message_star_count'),
            guard_bot=User.from_dict(data.get('guard_bot')),
            community=Community.from_dict(data.get('community')),
        )