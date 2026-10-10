from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .user import User
    


class GiveawayWinners:
    """This object represents a message about the completion of a giveaway with public winners."""

    def __init__(self, chat: Chat, giveaway_message_id: int, winners_selection_date: int, winner_count: int, winners: list[User], additional_chat_count: int | None = None, prize_star_count: int | None = None, premium_subscription_month_count: int | None = None, unclaimed_prize_count: int | None = None, only_new_members: bool | None = None, was_refunded: bool | None = None, prize_description: str | None = None):
        self.chat: Chat = chat
        self.giveaway_message_id: int = giveaway_message_id
        self.winners_selection_date: int = winners_selection_date
        self.winner_count: int = winner_count
        self.winners: list[User] = winners
        self.additional_chat_count: int | None = additional_chat_count
        self.prize_star_count: int | None = prize_star_count
        self.premium_subscription_month_count: int | None = premium_subscription_month_count
        self.unclaimed_prize_count: int | None = unclaimed_prize_count
        self.only_new_members: bool | None = only_new_members
        self.was_refunded: bool | None = was_refunded
        self.prize_description: str | None = prize_description

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
        if self.giveaway_message_id is not None:
            result['giveaway_message_id'] = _serialize(self.giveaway_message_id)
        if self.winners_selection_date is not None:
            result['winners_selection_date'] = _serialize(self.winners_selection_date)
        if self.winner_count is not None:
            result['winner_count'] = _serialize(self.winner_count)
        if self.winners is not None:
            result['winners'] = _serialize(self.winners)
        if self.additional_chat_count is not None:
            result['additional_chat_count'] = _serialize(self.additional_chat_count)
        if self.prize_star_count is not None:
            result['prize_star_count'] = _serialize(self.prize_star_count)
        if self.premium_subscription_month_count is not None:
            result['premium_subscription_month_count'] = _serialize(self.premium_subscription_month_count)
        if self.unclaimed_prize_count is not None:
            result['unclaimed_prize_count'] = _serialize(self.unclaimed_prize_count)
        if self.only_new_members is not None:
            result['only_new_members'] = _serialize(self.only_new_members)
        if self.was_refunded is not None:
            result['was_refunded'] = _serialize(self.was_refunded)
        if self.prize_description is not None:
            result['prize_description'] = _serialize(self.prize_description)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'GiveawayWinners' | None:
        if not data:
            return None
        from .chat import Chat
        from .user import User
        return cls(
            chat=Chat.from_dict(data.get('chat')),
            giveaway_message_id=data.get('giveaway_message_id'),
            winners_selection_date=data.get('winners_selection_date'),
            winner_count=data.get('winner_count'),
            winners=[User.from_dict(i) for i in data.get('winners')] if data.get('winners') else None,
            additional_chat_count=data.get('additional_chat_count'),
            prize_star_count=data.get('prize_star_count'),
            premium_subscription_month_count=data.get('premium_subscription_month_count'),
            unclaimed_prize_count=data.get('unclaimed_prize_count'),
            only_new_members=data.get('only_new_members'),
            was_refunded=data.get('was_refunded'),
            prize_description=data.get('prize_description'),
        )