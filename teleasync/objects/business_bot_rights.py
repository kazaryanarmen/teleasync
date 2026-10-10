from __future__ import annotations
from typing import TYPE_CHECKING



class BusinessBotRights:
    """Represents the rights of a business bot."""

    def __init__(self, can_reply: bool | None = None, can_read_messages: bool | None = None, can_delete_sent_messages: bool | None = None, can_delete_all_messages: bool | None = None, can_edit_name: bool | None = None, can_edit_bio: bool | None = None, can_edit_profile_photo: bool | None = None, can_edit_username: bool | None = None, can_change_gift_settings: bool | None = None, can_view_gifts_and_stars: bool | None = None, can_convert_gifts_to_stars: bool | None = None, can_transfer_and_upgrade_gifts: bool | None = None, can_transfer_stars: bool | None = None, can_manage_stories: bool | None = None):
        self.can_reply: bool | None = can_reply
        self.can_read_messages: bool | None = can_read_messages
        self.can_delete_sent_messages: bool | None = can_delete_sent_messages
        self.can_delete_all_messages: bool | None = can_delete_all_messages
        self.can_edit_name: bool | None = can_edit_name
        self.can_edit_bio: bool | None = can_edit_bio
        self.can_edit_profile_photo: bool | None = can_edit_profile_photo
        self.can_edit_username: bool | None = can_edit_username
        self.can_change_gift_settings: bool | None = can_change_gift_settings
        self.can_view_gifts_and_stars: bool | None = can_view_gifts_and_stars
        self.can_convert_gifts_to_stars: bool | None = can_convert_gifts_to_stars
        self.can_transfer_and_upgrade_gifts: bool | None = can_transfer_and_upgrade_gifts
        self.can_transfer_stars: bool | None = can_transfer_stars
        self.can_manage_stories: bool | None = can_manage_stories

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
        if self.can_reply is not None:
            result['can_reply'] = _serialize(self.can_reply)
        if self.can_read_messages is not None:
            result['can_read_messages'] = _serialize(self.can_read_messages)
        if self.can_delete_sent_messages is not None:
            result['can_delete_sent_messages'] = _serialize(self.can_delete_sent_messages)
        if self.can_delete_all_messages is not None:
            result['can_delete_all_messages'] = _serialize(self.can_delete_all_messages)
        if self.can_edit_name is not None:
            result['can_edit_name'] = _serialize(self.can_edit_name)
        if self.can_edit_bio is not None:
            result['can_edit_bio'] = _serialize(self.can_edit_bio)
        if self.can_edit_profile_photo is not None:
            result['can_edit_profile_photo'] = _serialize(self.can_edit_profile_photo)
        if self.can_edit_username is not None:
            result['can_edit_username'] = _serialize(self.can_edit_username)
        if self.can_change_gift_settings is not None:
            result['can_change_gift_settings'] = _serialize(self.can_change_gift_settings)
        if self.can_view_gifts_and_stars is not None:
            result['can_view_gifts_and_stars'] = _serialize(self.can_view_gifts_and_stars)
        if self.can_convert_gifts_to_stars is not None:
            result['can_convert_gifts_to_stars'] = _serialize(self.can_convert_gifts_to_stars)
        if self.can_transfer_and_upgrade_gifts is not None:
            result['can_transfer_and_upgrade_gifts'] = _serialize(self.can_transfer_and_upgrade_gifts)
        if self.can_transfer_stars is not None:
            result['can_transfer_stars'] = _serialize(self.can_transfer_stars)
        if self.can_manage_stories is not None:
            result['can_manage_stories'] = _serialize(self.can_manage_stories)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'BusinessBotRights' | None:
        if not data:
            return None
        return cls(
            can_reply=data.get('can_reply'),
            can_read_messages=data.get('can_read_messages'),
            can_delete_sent_messages=data.get('can_delete_sent_messages'),
            can_delete_all_messages=data.get('can_delete_all_messages'),
            can_edit_name=data.get('can_edit_name'),
            can_edit_bio=data.get('can_edit_bio'),
            can_edit_profile_photo=data.get('can_edit_profile_photo'),
            can_edit_username=data.get('can_edit_username'),
            can_change_gift_settings=data.get('can_change_gift_settings'),
            can_view_gifts_and_stars=data.get('can_view_gifts_and_stars'),
            can_convert_gifts_to_stars=data.get('can_convert_gifts_to_stars'),
            can_transfer_and_upgrade_gifts=data.get('can_transfer_and_upgrade_gifts'),
            can_transfer_stars=data.get('can_transfer_stars'),
            can_manage_stories=data.get('can_manage_stories'),
        )