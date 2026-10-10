from __future__ import annotations
from typing import TYPE_CHECKING



class WriteAccessAllowed:
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess."""

    def __init__(self, from_request: bool | None = None, web_app_name: str | None = None, from_attachment_menu: bool | None = None):
        self.from_request: bool | None = from_request
        self.web_app_name: str | None = web_app_name
        self.from_attachment_menu: bool | None = from_attachment_menu

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
        if self.from_request is not None:
            result['from_request'] = _serialize(self.from_request)
        if self.web_app_name is not None:
            result['web_app_name'] = _serialize(self.web_app_name)
        if self.from_attachment_menu is not None:
            result['from_attachment_menu'] = _serialize(self.from_attachment_menu)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'WriteAccessAllowed' | None:
        if not data:
            return None
        return cls(
            from_request=data.get('from_request'),
            web_app_name=data.get('web_app_name'),
            from_attachment_menu=data.get('from_attachment_menu'),
        )