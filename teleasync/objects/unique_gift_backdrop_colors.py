from __future__ import annotations
from typing import TYPE_CHECKING



class UniqueGiftBackdropColors:
    """This object describes the colors of the backdrop of a unique gift."""

    def __init__(self, center_color: int, edge_color: int, symbol_color: int, text_color: int):
        self.center_color: int = center_color
        self.edge_color: int = edge_color
        self.symbol_color: int = symbol_color
        self.text_color: int = text_color

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
        if self.center_color is not None:
            result['center_color'] = _serialize(self.center_color)
        if self.edge_color is not None:
            result['edge_color'] = _serialize(self.edge_color)
        if self.symbol_color is not None:
            result['symbol_color'] = _serialize(self.symbol_color)
        if self.text_color is not None:
            result['text_color'] = _serialize(self.text_color)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'UniqueGiftBackdropColors' | None:
        if not data:
            return None
        return cls(
            center_color=data.get('center_color'),
            edge_color=data.get('edge_color'),
            symbol_color=data.get('symbol_color'),
            text_color=data.get('text_color'),
        )