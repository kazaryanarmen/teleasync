from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .chat_invite_link import ChatInviteLink
    
    from .chat_member import ChatMember
    
    from .user import User
    


class ChatMemberUpdated:
    """This object represents changes in the status of a chat member."""

    def __init__(self, chat: Chat, from_: User, date: int, old_chat_member: ChatMember, new_chat_member: ChatMember, invite_link: ChatInviteLink | None = None, via_join_request: bool | None = None, via_chat_folder_invite_link: bool | None = None):
        self.chat: Chat = chat
        self.from_: User = from_
        self.date: int = date
        self.old_chat_member: ChatMember = old_chat_member
        self.new_chat_member: ChatMember = new_chat_member
        self.invite_link: ChatInviteLink | None = invite_link
        self.via_join_request: bool | None = via_join_request
        self.via_chat_folder_invite_link: bool | None = via_chat_folder_invite_link

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
        if self.chat is not None:
            result['chat'] = _serialize(self.chat)
        if self.from_ is not None:
            result['from'] = _serialize(self.from_)
        if self.date is not None:
            result['date'] = _serialize(self.date)
        if self.old_chat_member is not None:
            result['old_chat_member'] = _serialize(self.old_chat_member)
        if self.new_chat_member is not None:
            result['new_chat_member'] = _serialize(self.new_chat_member)
        if self.invite_link is not None:
            result['invite_link'] = _serialize(self.invite_link)
        if self.via_join_request is not None:
            result['via_join_request'] = _serialize(self.via_join_request)
        if self.via_chat_folder_invite_link is not None:
            result['via_chat_folder_invite_link'] = _serialize(self.via_chat_folder_invite_link)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChatMemberUpdated' | None:
        if not data:
            return None
        from .chat import Chat
        from .chat_invite_link import ChatInviteLink
        from .chat_member import ChatMember
        from .user import User
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            from_=User.from_dict(data.get('from')),
            date=data.get('date'),
            old_chat_member=ChatMember.from_dict(data.get('old_chat_member')),
            new_chat_member=ChatMember.from_dict(data.get('new_chat_member')),
            invite_link=ChatInviteLink.from_dict(data.get('invite_link')),
            via_join_request=data.get('via_join_request'),
            via_chat_folder_invite_link=data.get('via_chat_folder_invite_link'),
        )