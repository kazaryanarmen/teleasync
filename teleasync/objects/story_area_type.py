from __future__ import annotations
from importlib import import_module


class StoryAreaType:
    """Union-тип. from_dict возвращает нужный подтип по полю 'type'
    (неизвестное значение -> исходный dict)."""

    _DISCRIMINATOR = "type"
    _SUBTYPES = {
        "location": ("story_area_type_location", "StoryAreaTypeLocation"),
        "suggested_reaction": ("story_area_type_suggested_reaction", "StoryAreaTypeSuggestedReaction"),
        "link": ("story_area_type_link", "StoryAreaTypeLink"),
        "weather": ("story_area_type_weather", "StoryAreaTypeWeather"),
        "unique_gift": ("story_area_type_unique_gift", "StoryAreaTypeUniqueGift"),
    }

    @classmethod
    def from_dict(cls, data: dict | None):
        if not data:
            return None
        entry = cls._SUBTYPES.get(data.get(cls._DISCRIMINATOR))
        if entry is None:
            return data
        module = import_module("." + entry[0], __package__)
        return getattr(module, entry[1]).from_dict(data)
