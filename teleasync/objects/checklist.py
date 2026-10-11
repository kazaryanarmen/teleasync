from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .checklist_task import ChecklistTask
    
    from .message_entity import MessageEntity
    


class Checklist:
    """Describes a checklist."""

    def __init__(self, title: str, tasks: list[ChecklistTask], title_entities: list[MessageEntity] | None = None, others_can_add_tasks: bool | None = None, others_can_mark_tasks_as_done: bool | None = None):
        self.title: str = title
        self.tasks: list[ChecklistTask] = tasks
        self.title_entities: list[MessageEntity] | None = title_entities
        self.others_can_add_tasks: bool | None = others_can_add_tasks
        self.others_can_mark_tasks_as_done: bool | None = others_can_mark_tasks_as_done

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
        if self.title is not None:
            result['title'] = _serialize(self.title)
        if self.tasks is not None:
            result['tasks'] = _serialize(self.tasks)
        if self.title_entities is not None:
            result['title_entities'] = _serialize(self.title_entities)
        if self.others_can_add_tasks is not None:
            result['others_can_add_tasks'] = _serialize(self.others_can_add_tasks)
        if self.others_can_mark_tasks_as_done is not None:
            result['others_can_mark_tasks_as_done'] = _serialize(self.others_can_mark_tasks_as_done)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Checklist' | None:
        if not data:
            return None
        from .checklist_task import ChecklistTask
        from .message_entity import MessageEntity
        return cls(
            title=data.get('title'),
            tasks=[ChecklistTask.from_dict(i1) for i1 in data.get('tasks')] if data.get('tasks') else None,
            title_entities=[MessageEntity.from_dict(i1) for i1 in data.get('title_entities')] if data.get('title_entities') else None,
            others_can_add_tasks=data.get('others_can_add_tasks'),
            others_can_mark_tasks_as_done=data.get('others_can_mark_tasks_as_done'),
        )