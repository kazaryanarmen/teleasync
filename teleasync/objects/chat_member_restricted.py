from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .user import User
    


class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only."""

    def __init__(self, status: str, user: User, is_member: bool, can_send_messages: bool, can_send_audios: bool, can_send_documents: bool, can_send_photos: bool, can_send_videos: bool, can_send_video_notes: bool, can_send_voice_notes: bool, can_send_polls: bool, can_send_other_messages: bool, can_add_web_page_previews: bool, can_react_to_messages: bool, can_edit_tag: bool, can_change_info: bool, can_invite_users: bool, can_pin_messages: bool, can_manage_topics: bool, until_date: int, tag: str | None = None):
        self.status: str = status
        self.user: User = user
        self.is_member: bool = is_member
        self.can_send_messages: bool = can_send_messages
        self.can_send_audios: bool = can_send_audios
        self.can_send_documents: bool = can_send_documents
        self.can_send_photos: bool = can_send_photos
        self.can_send_videos: bool = can_send_videos
        self.can_send_video_notes: bool = can_send_video_notes
        self.can_send_voice_notes: bool = can_send_voice_notes
        self.can_send_polls: bool = can_send_polls
        self.can_send_other_messages: bool = can_send_other_messages
        self.can_add_web_page_previews: bool = can_add_web_page_previews
        self.can_react_to_messages: bool = can_react_to_messages
        self.can_edit_tag: bool = can_edit_tag
        self.can_change_info: bool = can_change_info
        self.can_invite_users: bool = can_invite_users
        self.can_pin_messages: bool = can_pin_messages
        self.can_manage_topics: bool = can_manage_topics
        self.until_date: int = until_date
        self.tag: str | None = tag

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
        if self.status is not None:
            result['status'] = _serialize(self.status)
        if self.user is not None:
            result['user'] = _serialize(self.user)
        if self.is_member is not None:
            result['is_member'] = _serialize(self.is_member)
        if self.can_send_messages is not None:
            result['can_send_messages'] = _serialize(self.can_send_messages)
        if self.can_send_audios is not None:
            result['can_send_audios'] = _serialize(self.can_send_audios)
        if self.can_send_documents is not None:
            result['can_send_documents'] = _serialize(self.can_send_documents)
        if self.can_send_photos is not None:
            result['can_send_photos'] = _serialize(self.can_send_photos)
        if self.can_send_videos is not None:
            result['can_send_videos'] = _serialize(self.can_send_videos)
        if self.can_send_video_notes is not None:
            result['can_send_video_notes'] = _serialize(self.can_send_video_notes)
        if self.can_send_voice_notes is not None:
            result['can_send_voice_notes'] = _serialize(self.can_send_voice_notes)
        if self.can_send_polls is not None:
            result['can_send_polls'] = _serialize(self.can_send_polls)
        if self.can_send_other_messages is not None:
            result['can_send_other_messages'] = _serialize(self.can_send_other_messages)
        if self.can_add_web_page_previews is not None:
            result['can_add_web_page_previews'] = _serialize(self.can_add_web_page_previews)
        if self.can_react_to_messages is not None:
            result['can_react_to_messages'] = _serialize(self.can_react_to_messages)
        if self.can_edit_tag is not None:
            result['can_edit_tag'] = _serialize(self.can_edit_tag)
        if self.can_change_info is not None:
            result['can_change_info'] = _serialize(self.can_change_info)
        if self.can_invite_users is not None:
            result['can_invite_users'] = _serialize(self.can_invite_users)
        if self.can_pin_messages is not None:
            result['can_pin_messages'] = _serialize(self.can_pin_messages)
        if self.can_manage_topics is not None:
            result['can_manage_topics'] = _serialize(self.can_manage_topics)
        if self.until_date is not None:
            result['until_date'] = _serialize(self.until_date)
        if self.tag is not None:
            result['tag'] = _serialize(self.tag)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatMemberRestricted' | None:
        if not data:
            return None
        from .user import User
        return cls(
            status=data.get('status'),
            user=User.from_dict(data.get('user')),
            is_member=data.get('is_member'),
            can_send_messages=data.get('can_send_messages'),
            can_send_audios=data.get('can_send_audios'),
            can_send_documents=data.get('can_send_documents'),
            can_send_photos=data.get('can_send_photos'),
            can_send_videos=data.get('can_send_videos'),
            can_send_video_notes=data.get('can_send_video_notes'),
            can_send_voice_notes=data.get('can_send_voice_notes'),
            can_send_polls=data.get('can_send_polls'),
            can_send_other_messages=data.get('can_send_other_messages'),
            can_add_web_page_previews=data.get('can_add_web_page_previews'),
            can_react_to_messages=data.get('can_react_to_messages'),
            can_edit_tag=data.get('can_edit_tag'),
            can_change_info=data.get('can_change_info'),
            can_invite_users=data.get('can_invite_users'),
            can_pin_messages=data.get('can_pin_messages'),
            can_manage_topics=data.get('can_manage_topics'),
            until_date=data.get('until_date'),
            tag=data.get('tag'),
        )