from __future__ import annotations
from typing import TYPE_CHECKING



class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat."""

    def __init__(self, can_send_messages: bool | None = None, can_send_audios: bool | None = None, can_send_documents: bool | None = None, can_send_photos: bool | None = None, can_send_videos: bool | None = None, can_send_video_notes: bool | None = None, can_send_voice_notes: bool | None = None, can_send_polls: bool | None = None, can_send_other_messages: bool | None = None, can_add_web_page_previews: bool | None = None, can_react_to_messages: bool | None = None, can_edit_tag: bool | None = None, can_change_info: bool | None = None, can_invite_users: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None):
        self.can_send_messages: bool | None = can_send_messages
        self.can_send_audios: bool | None = can_send_audios
        self.can_send_documents: bool | None = can_send_documents
        self.can_send_photos: bool | None = can_send_photos
        self.can_send_videos: bool | None = can_send_videos
        self.can_send_video_notes: bool | None = can_send_video_notes
        self.can_send_voice_notes: bool | None = can_send_voice_notes
        self.can_send_polls: bool | None = can_send_polls
        self.can_send_other_messages: bool | None = can_send_other_messages
        self.can_add_web_page_previews: bool | None = can_add_web_page_previews
        self.can_react_to_messages: bool | None = can_react_to_messages
        self.can_edit_tag: bool | None = can_edit_tag
        self.can_change_info: bool | None = can_change_info
        self.can_invite_users: bool | None = can_invite_users
        self.can_pin_messages: bool | None = can_pin_messages
        self.can_manage_topics: bool | None = can_manage_topics

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
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatPermissions' | None:
        if not data:
            return None
        return cls(
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
        )