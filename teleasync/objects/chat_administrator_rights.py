from __future__ import annotations
from typing import TYPE_CHECKING



class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat."""

    def __init__(self, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool, can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_stories: bool, can_edit_stories: bool, can_delete_stories: bool, can_send_welcome_messages: bool, can_post_messages: bool | None = None, can_edit_messages: bool | None = None, can_pin_messages: bool | None = None, can_manage_topics: bool | None = None, can_manage_direct_messages: bool | None = None, can_manage_tags: bool | None = None):
        self.is_anonymous: bool = is_anonymous
        self.can_manage_chat: bool = can_manage_chat
        self.can_delete_messages: bool = can_delete_messages
        self.can_manage_video_chats: bool = can_manage_video_chats
        self.can_restrict_members: bool = can_restrict_members
        self.can_promote_members: bool = can_promote_members
        self.can_change_info: bool = can_change_info
        self.can_invite_users: bool = can_invite_users
        self.can_post_stories: bool = can_post_stories
        self.can_edit_stories: bool = can_edit_stories
        self.can_delete_stories: bool = can_delete_stories
        self.can_send_welcome_messages: bool = can_send_welcome_messages
        self.can_post_messages: bool | None = can_post_messages
        self.can_edit_messages: bool | None = can_edit_messages
        self.can_pin_messages: bool | None = can_pin_messages
        self.can_manage_topics: bool | None = can_manage_topics
        self.can_manage_direct_messages: bool | None = can_manage_direct_messages
        self.can_manage_tags: bool | None = can_manage_tags

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
        if self.is_anonymous is not None:
            result['is_anonymous'] = _serialize(self.is_anonymous)
        if self.can_manage_chat is not None:
            result['can_manage_chat'] = _serialize(self.can_manage_chat)
        if self.can_delete_messages is not None:
            result['can_delete_messages'] = _serialize(self.can_delete_messages)
        if self.can_manage_video_chats is not None:
            result['can_manage_video_chats'] = _serialize(self.can_manage_video_chats)
        if self.can_restrict_members is not None:
            result['can_restrict_members'] = _serialize(self.can_restrict_members)
        if self.can_promote_members is not None:
            result['can_promote_members'] = _serialize(self.can_promote_members)
        if self.can_change_info is not None:
            result['can_change_info'] = _serialize(self.can_change_info)
        if self.can_invite_users is not None:
            result['can_invite_users'] = _serialize(self.can_invite_users)
        if self.can_post_stories is not None:
            result['can_post_stories'] = _serialize(self.can_post_stories)
        if self.can_edit_stories is not None:
            result['can_edit_stories'] = _serialize(self.can_edit_stories)
        if self.can_delete_stories is not None:
            result['can_delete_stories'] = _serialize(self.can_delete_stories)
        if self.can_send_welcome_messages is not None:
            result['can_send_welcome_messages'] = _serialize(self.can_send_welcome_messages)
        if self.can_post_messages is not None:
            result['can_post_messages'] = _serialize(self.can_post_messages)
        if self.can_edit_messages is not None:
            result['can_edit_messages'] = _serialize(self.can_edit_messages)
        if self.can_pin_messages is not None:
            result['can_pin_messages'] = _serialize(self.can_pin_messages)
        if self.can_manage_topics is not None:
            result['can_manage_topics'] = _serialize(self.can_manage_topics)
        if self.can_manage_direct_messages is not None:
            result['can_manage_direct_messages'] = _serialize(self.can_manage_direct_messages)
        if self.can_manage_tags is not None:
            result['can_manage_tags'] = _serialize(self.can_manage_tags)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatAdministratorRights' | None:
        if not data:
            return None
        return cls(
            is_anonymous=data.get('is_anonymous'),
            can_manage_chat=data.get('can_manage_chat'),
            can_delete_messages=data.get('can_delete_messages'),
            can_manage_video_chats=data.get('can_manage_video_chats'),
            can_restrict_members=data.get('can_restrict_members'),
            can_promote_members=data.get('can_promote_members'),
            can_change_info=data.get('can_change_info'),
            can_invite_users=data.get('can_invite_users'),
            can_post_stories=data.get('can_post_stories'),
            can_edit_stories=data.get('can_edit_stories'),
            can_delete_stories=data.get('can_delete_stories'),
            can_send_welcome_messages=data.get('can_send_welcome_messages'),
            can_post_messages=data.get('can_post_messages'),
            can_edit_messages=data.get('can_edit_messages'),
            can_pin_messages=data.get('can_pin_messages'),
            can_manage_topics=data.get('can_manage_topics'),
            can_manage_direct_messages=data.get('can_manage_direct_messages'),
            can_manage_tags=data.get('can_manage_tags'),
        )