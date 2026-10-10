from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .file import File
    
    from .mask_position import MaskPosition
    
    from .photo_size import PhotoSize
    


class Sticker:
    """This object represents a sticker."""

    def __init__(self, file_id: str, file_unique_id: str, type: str, width: int, height: int, is_animated: bool, is_video: bool, thumbnail: PhotoSize | None = None, emoji: str | None = None, set_name: str | None = None, premium_animation: File | None = None, mask_position: MaskPosition | None = None, custom_emoji_id: str | None = None, needs_repainting: bool | None = None, file_size: int | None = None):
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.type: str = type
        self.width: int = width
        self.height: int = height
        self.is_animated: bool = is_animated
        self.is_video: bool = is_video
        self.thumbnail: PhotoSize | None = thumbnail
        self.emoji: str | None = emoji
        self.set_name: str | None = set_name
        self.premium_animation: File | None = premium_animation
        self.mask_position: MaskPosition | None = mask_position
        self.custom_emoji_id: str | None = custom_emoji_id
        self.needs_repainting: bool | None = needs_repainting
        self.file_size: int | None = file_size

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
        if self.file_id is not None:
            result['file_id'] = _serialize(self.file_id)
        if self.file_unique_id is not None:
            result['file_unique_id'] = _serialize(self.file_unique_id)
        if self.type is not None:
            result['type'] = _serialize(self.type)
        if self.width is not None:
            result['width'] = _serialize(self.width)
        if self.height is not None:
            result['height'] = _serialize(self.height)
        if self.is_animated is not None:
            result['is_animated'] = _serialize(self.is_animated)
        if self.is_video is not None:
            result['is_video'] = _serialize(self.is_video)
        if self.thumbnail is not None:
            result['thumbnail'] = _serialize(self.thumbnail)
        if self.emoji is not None:
            result['emoji'] = _serialize(self.emoji)
        if self.set_name is not None:
            result['set_name'] = _serialize(self.set_name)
        if self.premium_animation is not None:
            result['premium_animation'] = _serialize(self.premium_animation)
        if self.mask_position is not None:
            result['mask_position'] = _serialize(self.mask_position)
        if self.custom_emoji_id is not None:
            result['custom_emoji_id'] = _serialize(self.custom_emoji_id)
        if self.needs_repainting is not None:
            result['needs_repainting'] = _serialize(self.needs_repainting)
        if self.file_size is not None:
            result['file_size'] = _serialize(self.file_size)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'Sticker' | None:
        if not data:
            return None
        from .file import File
        from .mask_position import MaskPosition
        from .photo_size import PhotoSize
        return cls(
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            type=data.get('type'),
            width=data.get('width'),
            height=data.get('height'),
            is_animated=data.get('is_animated'),
            is_video=data.get('is_video'),
            thumbnail=PhotoSize.from_dict(data.get('thumbnail')),
            emoji=data.get('emoji'),
            set_name=data.get('set_name'),
            premium_animation=File.from_dict(data.get('premium_animation')),
            mask_position=MaskPosition.from_dict(data.get('mask_position')),
            custom_emoji_id=data.get('custom_emoji_id'),
            needs_repainting=data.get('needs_repainting'),
            file_size=data.get('file_size'),
        )