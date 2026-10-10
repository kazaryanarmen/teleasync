from __future__ import annotations
from typing import TYPE_CHECKING



class WebhookInfo:
    """Describes the current status of a webhook."""

    def __init__(self, url: str, has_custom_certificate: bool, pending_update_count: int, ip_address: str | None = None, last_error_date: int | None = None, last_error_message: str | None = None, last_synchronization_error_date: int | None = None, max_connections: int | None = None, allowed_updates: list[str] | None = None):
        self.url: str = url
        self.has_custom_certificate: bool = has_custom_certificate
        self.pending_update_count: int = pending_update_count
        self.ip_address: str | None = ip_address
        self.last_error_date: int | None = last_error_date
        self.last_error_message: str | None = last_error_message
        self.last_synchronization_error_date: int | None = last_synchronization_error_date
        self.max_connections: int | None = max_connections
        self.allowed_updates: list[str] | None = allowed_updates

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
        if self.url is not None:
            result['url'] = _serialize(self.url)
        if self.has_custom_certificate is not None:
            result['has_custom_certificate'] = _serialize(self.has_custom_certificate)
        if self.pending_update_count is not None:
            result['pending_update_count'] = _serialize(self.pending_update_count)
        if self.ip_address is not None:
            result['ip_address'] = _serialize(self.ip_address)
        if self.last_error_date is not None:
            result['last_error_date'] = _serialize(self.last_error_date)
        if self.last_error_message is not None:
            result['last_error_message'] = _serialize(self.last_error_message)
        if self.last_synchronization_error_date is not None:
            result['last_synchronization_error_date'] = _serialize(self.last_synchronization_error_date)
        if self.max_connections is not None:
            result['max_connections'] = _serialize(self.max_connections)
        if self.allowed_updates is not None:
            result['allowed_updates'] = _serialize(self.allowed_updates)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'WebhookInfo' | None:
        if not data:
            return None
        return cls(
            url=data.get('url'),
            has_custom_certificate=data.get('has_custom_certificate'),
            pending_update_count=data.get('pending_update_count'),
            ip_address=data.get('ip_address'),
            last_error_date=data.get('last_error_date'),
            last_error_message=data.get('last_error_message'),
            last_synchronization_error_date=data.get('last_synchronization_error_date'),
            max_connections=data.get('max_connections'),
            allowed_updates=data.get('allowed_updates'),
        )