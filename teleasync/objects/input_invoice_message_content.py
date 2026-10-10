from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .labeled_price import LabeledPrice
    


class InputInvoiceMessageContent:
    """Represents the content of an invoice message to be sent as the result of an inline query."""

    def __init__(self, title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None):
        self.title: str = title
        self.description: str = description
        self.payload: str = payload
        self.currency: str = currency
        self.prices: list[LabeledPrice] = prices
        self.provider_token: str | None = provider_token
        self.max_tip_amount: int | None = max_tip_amount
        self.suggested_tip_amounts: list[int] | None = suggested_tip_amounts
        self.provider_data: str | None = provider_data
        self.photo_url: str | None = photo_url
        self.photo_size: int | None = photo_size
        self.photo_width: int | None = photo_width
        self.photo_height: int | None = photo_height
        self.need_name: bool | None = need_name
        self.need_phone_number: bool | None = need_phone_number
        self.need_email: bool | None = need_email
        self.need_shipping_address: bool | None = need_shipping_address
        self.send_phone_number_to_provider: bool | None = send_phone_number_to_provider
        self.send_email_to_provider: bool | None = send_email_to_provider
        self.is_flexible: bool | None = is_flexible

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
        if self.description is not None:
            result['description'] = _serialize(self.description)
        if self.payload is not None:
            result['payload'] = _serialize(self.payload)
        if self.currency is not None:
            result['currency'] = _serialize(self.currency)
        if self.prices is not None:
            result['prices'] = _serialize(self.prices)
        if self.provider_token is not None:
            result['provider_token'] = _serialize(self.provider_token)
        if self.max_tip_amount is not None:
            result['max_tip_amount'] = _serialize(self.max_tip_amount)
        if self.suggested_tip_amounts is not None:
            result['suggested_tip_amounts'] = _serialize(self.suggested_tip_amounts)
        if self.provider_data is not None:
            result['provider_data'] = _serialize(self.provider_data)
        if self.photo_url is not None:
            result['photo_url'] = _serialize(self.photo_url)
        if self.photo_size is not None:
            result['photo_size'] = _serialize(self.photo_size)
        if self.photo_width is not None:
            result['photo_width'] = _serialize(self.photo_width)
        if self.photo_height is not None:
            result['photo_height'] = _serialize(self.photo_height)
        if self.need_name is not None:
            result['need_name'] = _serialize(self.need_name)
        if self.need_phone_number is not None:
            result['need_phone_number'] = _serialize(self.need_phone_number)
        if self.need_email is not None:
            result['need_email'] = _serialize(self.need_email)
        if self.need_shipping_address is not None:
            result['need_shipping_address'] = _serialize(self.need_shipping_address)
        if self.send_phone_number_to_provider is not None:
            result['send_phone_number_to_provider'] = _serialize(self.send_phone_number_to_provider)
        if self.send_email_to_provider is not None:
            result['send_email_to_provider'] = _serialize(self.send_email_to_provider)
        if self.is_flexible is not None:
            result['is_flexible'] = _serialize(self.is_flexible)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputInvoiceMessageContent' | None:
        if not data:
            return None
        from .labeled_price import LabeledPrice
        return cls(
            title=data.get('title'),
            description=data.get('description'),
            payload=data.get('payload'),
            currency=data.get('currency'),
            prices=[LabeledPrice.from_dict(i) for i in data.get('prices')] if data.get('prices') else None,
            provider_token=data.get('provider_token'),
            max_tip_amount=data.get('max_tip_amount'),
            suggested_tip_amounts=data.get('suggested_tip_amounts'),
            provider_data=data.get('provider_data'),
            photo_url=data.get('photo_url'),
            photo_size=data.get('photo_size'),
            photo_width=data.get('photo_width'),
            photo_height=data.get('photo_height'),
            need_name=data.get('need_name'),
            need_phone_number=data.get('need_phone_number'),
            need_email=data.get('need_email'),
            need_shipping_address=data.get('need_shipping_address'),
            send_phone_number_to_provider=data.get('send_phone_number_to_provider'),
            send_email_to_provider=data.get('send_email_to_provider'),
            is_flexible=data.get('is_flexible'),
        )