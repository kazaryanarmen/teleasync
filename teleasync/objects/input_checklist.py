from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .input_checklist_task import InputChecklistTask
    
    from .message_entity import MessageEntity
    


class InputChecklist:
    """Describes a checklist to create."""

    def __init__(self, title: str, tasks: list[InputChecklistTask], parse_mode: str | None = None, title_entities: list[MessageEntity] | None = None, others_can_add_tasks: bool | None = None, others_can_mark_tasks_as_done: bool | None = None):
        self.title: str = title
        self.tasks: list[InputChecklistTask] = tasks
        self.parse_mode: str | None = parse_mode
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
        if self.parse_mode is not None:
            result['parse_mode'] = _serialize(self.parse_mode)
        if self.title_entities is not None:
            result['title_entities'] = _serialize(self.title_entities)
        if self.others_can_add_tasks is not None:
            result['others_can_add_tasks'] = _serialize(self.others_can_add_tasks)
        if self.others_can_mark_tasks_as_done is not None:
            result['others_can_mark_tasks_as_done'] = _serialize(self.others_can_mark_tasks_as_done)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputChecklist' | None:
        if not data:
            return None
        from .input_checklist_task import InputChecklistTask
        from .message_entity import MessageEntity
        return cls(
            title=data.get('title'),
            tasks=[InputChecklistTask.from_dict(i1) for i1 in data.get('tasks')] if data.get('tasks') else None,
            parse_mode=data.get('parse_mode'),
            title_entities=[MessageEntity.from_dict(i1) for i1 in data.get('title_entities')] if data.get('title_entities') else None,
            others_can_add_tasks=data.get('others_can_add_tasks'),
            others_can_mark_tasks_as_done=data.get('others_can_mark_tasks_as_done'),
        )