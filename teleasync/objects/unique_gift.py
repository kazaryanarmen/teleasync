from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .chat import Chat
    
    from .unique_gift_backdrop import UniqueGiftBackdrop
    
    from .unique_gift_colors import UniqueGiftColors
    
    from .unique_gift_model import UniqueGiftModel
    
    from .unique_gift_symbol import UniqueGiftSymbol
    


class UniqueGift:
    """This object describes a unique gift that was upgraded from a regular gift."""

    def __init__(self, gift_id: str, base_name: str, name: str, number: int, model: UniqueGiftModel, symbol: UniqueGiftSymbol, backdrop: UniqueGiftBackdrop, is_premium: bool | None = None, is_burned: bool | None = None, is_from_blockchain: bool | None = None, colors: UniqueGiftColors | None = None, publisher_chat: Chat | None = None):
        self.gift_id: str = gift_id
        self.base_name: str = base_name
        self.name: str = name
        self.number: int = number
        self.model: UniqueGiftModel = model
        self.symbol: UniqueGiftSymbol = symbol
        self.backdrop: UniqueGiftBackdrop = backdrop
        self.is_premium: bool | None = is_premium
        self.is_burned: bool | None = is_burned
        self.is_from_blockchain: bool | None = is_from_blockchain
        self.colors: UniqueGiftColors | None = colors
        self.publisher_chat: Chat | None = publisher_chat

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
        if self.gift_id is not None:
            result['gift_id'] = _serialize(self.gift_id)
        if self.base_name is not None:
            result['base_name'] = _serialize(self.base_name)
        if self.name is not None:
            result['name'] = _serialize(self.name)
        if self.number is not None:
            result['number'] = _serialize(self.number)
        if self.model is not None:
            result['model'] = _serialize(self.model)
        if self.symbol is not None:
            result['symbol'] = _serialize(self.symbol)
        if self.backdrop is not None:
            result['backdrop'] = _serialize(self.backdrop)
        if self.is_premium is not None:
            result['is_premium'] = _serialize(self.is_premium)
        if self.is_burned is not None:
            result['is_burned'] = _serialize(self.is_burned)
        if self.is_from_blockchain is not None:
            result['is_from_blockchain'] = _serialize(self.is_from_blockchain)
        if self.colors is not None:
            result['colors'] = _serialize(self.colors)
        if self.publisher_chat is not None:
            result['publisher_chat'] = _serialize(self.publisher_chat)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGift' | None:
        if not data:
            return None
        from .chat import Chat
        from .unique_gift_backdrop import UniqueGiftBackdrop
        from .unique_gift_colors import UniqueGiftColors
        from .unique_gift_model import UniqueGiftModel
        from .unique_gift_symbol import UniqueGiftSymbol
        return cls(
            gift_id=data.get('gift_id'),
            base_name=data.get('base_name'),
            name=data.get('name'),
            number=data.get('number'),
            model=UniqueGiftModel.from_dict(data.get('model')),
            symbol=UniqueGiftSymbol.from_dict(data.get('symbol')),
            backdrop=UniqueGiftBackdrop.from_dict(data.get('backdrop')),
            is_premium=data.get('is_premium'),
            is_burned=data.get('is_burned'),
            is_from_blockchain=data.get('is_from_blockchain'),
            colors=UniqueGiftColors.from_dict(data.get('colors')),
            publisher_chat=Chat.from_dict(data.get('publisher_chat')),
        )