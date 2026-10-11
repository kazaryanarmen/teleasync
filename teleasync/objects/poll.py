from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message_entity import MessageEntity
    
    from .poll_media import PollMedia
    
    from .poll_option import PollOption
    


class Poll:
    """This object contains information about a poll."""

    def __init__(self, id: str, question: str, options: list[PollOption], total_voter_count: int, is_closed: bool, is_anonymous: bool, type: str, allows_multiple_answers: bool, allows_revoting: bool, members_only: bool, question_entities: list[MessageEntity] | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_entities: list[MessageEntity] | None = None, explanation_media: PollMedia | None = None, open_period: int | None = None, close_date: int | None = None, description: str | None = None, description_entities: list[MessageEntity] | None = None, media: PollMedia | None = None):
        self.id: str = id
        self.question: str = question
        self.options: list[PollOption] = options
        self.total_voter_count: int = total_voter_count
        self.is_closed: bool = is_closed
        self.is_anonymous: bool = is_anonymous
        self.type: str = type
        self.allows_multiple_answers: bool = allows_multiple_answers
        self.allows_revoting: bool = allows_revoting
        self.members_only: bool = members_only
        self.question_entities: list[MessageEntity] | None = question_entities
        self.country_codes: list[str] | None = country_codes
        self.correct_option_ids: list[int] | None = correct_option_ids
        self.explanation: str | None = explanation
        self.explanation_entities: list[MessageEntity] | None = explanation_entities
        self.explanation_media: PollMedia | None = explanation_media
        self.open_period: int | None = open_period
        self.close_date: int | None = close_date
        self.description: str | None = description
        self.description_entities: list[MessageEntity] | None = description_entities
        self.media: PollMedia | None = media

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
        if self.question is not None:
            result['question'] = _serialize(self.question)
        if self.options is not None:
            result['options'] = _serialize(self.options)
        if self.total_voter_count is not None:
            result['total_voter_count'] = _serialize(self.total_voter_count)
        if self.is_closed is not None:
            result['is_closed'] = _serialize(self.is_closed)
        if self.is_anonymous is not None:
            result['is_anonymous'] = _serialize(self.is_anonymous)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.allows_multiple_answers is not None:
            result['allows_multiple_answers'] = _serialize(self.allows_multiple_answers)
        if self.allows_revoting is not None:
            result['allows_revoting'] = _serialize(self.allows_revoting)
        if self.members_only is not None:
            result['members_only'] = _serialize(self.members_only)
        if self.question_entities is not None:
            result['question_entities'] = _serialize(self.question_entities)
        if self.country_codes is not None:
            result['country_codes'] = _serialize(self.country_codes)
        if self.correct_option_ids is not None:
            result['correct_option_ids'] = _serialize(self.correct_option_ids)
        if self.explanation is not None:
            result['explanation'] = _serialize(self.explanation)
        if self.explanation_entities is not None:
            result['explanation_entities'] = _serialize(self.explanation_entities)
        if self.explanation_media is not None:
            result['explanation_media'] = _serialize(self.explanation_media)
        if self.open_period is not None:
            result['open_period'] = _serialize(self.open_period)
        if self.close_date is not None:
            result['close_date'] = _serialize(self.close_date)
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.description_entities is not None:
            result['description_entities'] = _serialize(self.description_entities)
        if self.media is not None:
            result['media'] = _serialize(self.media)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Poll' | None:
        if not data:
            return None
        from .message_entity import MessageEntity
        from .poll_media import PollMedia
        from .poll_option import PollOption
        return cls(
            id=data.get('id'),
            question=data.get('question'),
            options=[PollOption.from_dict(i1) for i1 in data.get('options')] if data.get('options') else None,
            total_voter_count=data.get('total_voter_count'),
            is_closed=data.get('is_closed'),
            is_anonymous=data.get('is_anonymous'),
            type=data.get('type'),
            allows_multiple_answers=data.get('allows_multiple_answers'),
            allows_revoting=data.get('allows_revoting'),
            members_only=data.get('members_only'),
            question_entities=[MessageEntity.from_dict(i1) for i1 in data.get('question_entities')] if data.get('question_entities') else None,
            country_codes=data.get('country_codes'),
            correct_option_ids=data.get('correct_option_ids'),
            explanation=data.get('explanation'),
            explanation_entities=[MessageEntity.from_dict(i1) for i1 in data.get('explanation_entities')] if data.get('explanation_entities') else None,
            explanation_media=PollMedia.from_dict(data.get('explanation_media')),
            open_period=data.get('open_period'),
            close_date=data.get('close_date'),
            description=data.get('description'),
            description_entities=[MessageEntity.from_dict(i1) for i1 in data.get('description_entities')] if data.get('description_entities') else None,
            media=PollMedia.from_dict(data.get('media')),
        )