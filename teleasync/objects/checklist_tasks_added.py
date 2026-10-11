from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .checklist_task import ChecklistTask
    
    from .message import Message
    


class ChecklistTasksAdded:
    """Describes a service message about tasks added to a checklist."""

    def __init__(self, tasks: list[ChecklistTask], checklist_message: Message | None = None):
        self.tasks: list[ChecklistTask] = tasks
        self.checklist_message: Message | None = checklist_message

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
        if self.tasks is not None:
            result['tasks'] = _serialize(self.tasks)
        if self.checklist_message is not None:
            result['checklist_message'] = _serialize(self.checklist_message)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'ChecklistTasksAdded' | None:
        if not data:
            return None
        from .checklist_task import ChecklistTask
        from .message import Message
        return cls(
            tasks=[ChecklistTask.from_dict(i1) for i1 in data.get('tasks')] if data.get('tasks') else None,
            checklist_message=Message.from_dict(data.get('checklist_message')),
        )