from __future__ import annotations
from typing import TYPE_CHECKING



class User:
    """This object represents a Telegram user or bot."""

    def __init__(self, id: int, is_bot: bool, first_name: str, last_name: str | None = None, username: str | None = None, language_code: str | None = None, is_premium: bool | None = None, added_to_attachment_menu: bool | None = None, can_join_groups: bool | None = None, can_read_all_group_messages: bool | None = None, supports_guest_queries: bool | None = None, supports_inline_queries: bool | None = None, can_connect_to_business: bool | None = None, has_main_web_app: bool | None = None, has_topics_enabled: bool | None = None, allows_users_to_create_topics: bool | None = None, can_manage_bots: bool | None = None, supports_join_request_queries: bool | None = None):
        self.id: int = id
        self.is_bot: bool = is_bot
        self.first_name: str = first_name
        self.last_name: str | None = last_name
        self.username: str | None = username
        self.language_code: str | None = language_code
        self.is_premium: bool | None = is_premium
        self.added_to_attachment_menu: bool | None = added_to_attachment_menu
        self.can_join_groups: bool | None = can_join_groups
        self.can_read_all_group_messages: bool | None = can_read_all_group_messages
        self.supports_guest_queries: bool | None = supports_guest_queries
        self.supports_inline_queries: bool | None = supports_inline_queries
        self.can_connect_to_business: bool | None = can_connect_to_business
        self.has_main_web_app: bool | None = has_main_web_app
        self.has_topics_enabled: bool | None = has_topics_enabled
        self.allows_users_to_create_topics: bool | None = allows_users_to_create_topics
        self.can_manage_bots: bool | None = can_manage_bots
        self.supports_join_request_queries: bool | None = supports_join_request_queries

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
        if self.is_bot is not None:
            result['is_bot'] = _serialize(self.is_bot)
        if self.first_name is not None:
            result['first_name'] = _serialize(self.first_name)
        if self.last_name is not None:
            result['last_name'] = _serialize(self.last_name)
        if self.username is not None:
            result['username'] = _serialize(self.username)
        if self.language_code is not None:
            result['language_code'] = _serialize(self.language_code)
        if self.is_premium is not None:
            result['is_premium'] = _serialize(self.is_premium)
        if self.added_to_attachment_menu is not None:
            result['added_to_attachment_menu'] = _serialize(self.added_to_attachment_menu)
        if self.can_join_groups is not None:
            result['can_join_groups'] = _serialize(self.can_join_groups)
        if self.can_read_all_group_messages is not None:
            result['can_read_all_group_messages'] = _serialize(self.can_read_all_group_messages)
        if self.supports_guest_queries is not None:
            result['supports_guest_queries'] = _serialize(self.supports_guest_queries)
        if self.supports_inline_queries is not None:
            result['supports_inline_queries'] = _serialize(self.supports_inline_queries)
        if self.can_connect_to_business is not None:
            result['can_connect_to_business'] = _serialize(self.can_connect_to_business)
        if self.has_main_web_app is not None:
            result['has_main_web_app'] = _serialize(self.has_main_web_app)
        if self.has_topics_enabled is not None:
            result['has_topics_enabled'] = _serialize(self.has_topics_enabled)
        if self.allows_users_to_create_topics is not None:
            result['allows_users_to_create_topics'] = _serialize(self.allows_users_to_create_topics)
        if self.can_manage_bots is not None:
            result['can_manage_bots'] = _serialize(self.can_manage_bots)
        if self.supports_join_request_queries is not None:
            result['supports_join_request_queries'] = _serialize(self.supports_join_request_queries)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'User' | None:
        if not data:
            return None
        return cls(
            id=data.get('id'),
            is_bot=data.get('is_bot'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            username=data.get('username'),
            language_code=data.get('language_code'),
            is_premium=data.get('is_premium'),
            added_to_attachment_menu=data.get('added_to_attachment_menu'),
            can_join_groups=data.get('can_join_groups'),
            can_read_all_group_messages=data.get('can_read_all_group_messages'),
            supports_guest_queries=data.get('supports_guest_queries'),
            supports_inline_queries=data.get('supports_inline_queries'),
            can_connect_to_business=data.get('can_connect_to_business'),
            has_main_web_app=data.get('has_main_web_app'),
            has_topics_enabled=data.get('has_topics_enabled'),
            allows_users_to_create_topics=data.get('allows_users_to_create_topics'),
            can_manage_bots=data.get('can_manage_bots'),
            supports_join_request_queries=data.get('supports_join_request_queries'),
        )