from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .community import Community
    


class CommunityChatAdded:
    """Describes a service message about a chat or a bot being added to a community."""

    def __init__(self, community: Community):
        self.community: Community = community

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
        if self.community is not None:
            result['community'] = _serialize(self.community)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'CommunityChatAdded' | None:
        if not data:
            return None
        from .community import Community
        return cls(
            community=Community.from_dict(data.get('community')),
        )