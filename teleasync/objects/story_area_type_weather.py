from __future__ import annotations
from typing import TYPE_CHECKING



class StoryAreaTypeWeather:
    """Describes a story area containing weather information. Currently, a story can have up to 3 weather areas."""

    def __init__(self, type: str, temperature: float, emoji: str, background_color: int):
        self.type: str = type
        self.temperature: float = temperature
        self.emoji: str = emoji
        self.background_color: int = background_color

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
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.temperature is not None:
            result['temperature'] = _serialize(self.temperature)
        if self.emoji is not None:
            result['emoji'] = _serialize(self.emoji)
        if self.background_color is not None:
            result['background_color'] = _serialize(self.background_color)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'StoryAreaTypeWeather' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            temperature=data.get('temperature'),
            emoji=data.get('emoji'),
            background_color=data.get('background_color'),
        )