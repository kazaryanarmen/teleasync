from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .message import Message
    


class ChecklistTasksDone:
    """Describes a service message about checklist tasks marked as done or not done."""

    def __init__(self, checklist_message: Message | None = None, marked_as_done_task_ids: list[int] | None = None, marked_as_not_done_task_ids: list[int] | None = None):
        self.checklist_message: Message | None = checklist_message
        self.marked_as_done_task_ids: list[int] | None = marked_as_done_task_ids
        self.marked_as_not_done_task_ids: list[int] | None = marked_as_not_done_task_ids

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
        if self.checklist_message is not None:
            result['checklist_message'] = _serialize(self.checklist_message)
        if self.marked_as_done_task_ids is not None:
            result['marked_as_done_task_ids'] = _serialize(self.marked_as_done_task_ids)
        if self.marked_as_not_done_task_ids is not None:
            result['marked_as_not_done_task_ids'] = _serialize(self.marked_as_not_done_task_ids)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChecklistTasksDone' | None:
        if not data:
            return None
        from .message import Message
        return cls(
            checklist_message=Message.from_dict(data.get('checklist_message')),
            marked_as_done_task_ids=data.get('marked_as_done_task_ids'),
            marked_as_not_done_task_ids=data.get('marked_as_not_done_task_ids'),
        )