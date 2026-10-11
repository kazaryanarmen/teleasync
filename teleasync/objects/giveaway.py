from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    


class Giveaway:
    """This object represents a message about a scheduled giveaway."""

    def __init__(self, chats: list[Chat], winners_selection_date: int, winner_count: int, only_new_members: bool | None = None, has_public_winners: bool | None = None, prize_description: str | None = None, country_codes: list[str] | None = None, prize_star_count: int | None = None, premium_subscription_month_count: int | None = None):
        self.chats: list[Chat] = chats
        self.winners_selection_date: int = winners_selection_date
        self.winner_count: int = winner_count
        self.only_new_members: bool | None = only_new_members
        self.has_public_winners: bool | None = has_public_winners
        self.prize_description: str | None = prize_description
        self.country_codes: list[str] | None = country_codes
        self.prize_star_count: int | None = prize_star_count
        self.premium_subscription_month_count: int | None = premium_subscription_month_count

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
        if self.chats is not None:
            result['chats'] = _serialize(self.chats)
        if self.winners_selection_date is not None:
            result['winners_selection_date'] = _serialize(self.winners_selection_date)
        if self.winner_count is not None:
            result['winner_count'] = _serialize(self.winner_count)
        if self.only_new_members is not None:
            result['only_new_members'] = _serialize(self.only_new_members)
        if self.has_public_winners is not None:
            result['has_public_winners'] = _serialize(self.has_public_winners)
        if self.prize_description is not None:
            result['prize_description'] = _serialize(self.prize_description)
        if self.country_codes is not None:
            result['country_codes'] = _serialize(self.country_codes)
        if self.prize_star_count is not None:
            result['prize_star_count'] = _serialize(self.prize_star_count)
        if self.premium_subscription_month_count is not None:
            result['premium_subscription_month_count'] = _serialize(self.premium_subscription_month_count)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Giveaway' | None:
        if not data:
            return None
        from .chat import Chat
        return cls(
            chats=[Chat.from_dict(i1) for i1 in data.get('chats')] if data.get('chats') else None,
            winners_selection_date=data.get('winners_selection_date'),
            winner_count=data.get('winner_count'),
            only_new_members=data.get('only_new_members'),
            has_public_winners=data.get('has_public_winners'),
            prize_description=data.get('prize_description'),
            country_codes=data.get('country_codes'),
            prize_star_count=data.get('prize_star_count'),
            premium_subscription_month_count=data.get('premium_subscription_month_count'),
        )