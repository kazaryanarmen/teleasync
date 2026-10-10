from __future__ import annotations
from typing import TYPE_CHECKING



class InputRichBlockMathematicalExpression:
    """A block with a mathematical expression in LaTeX format, corresponding to the custom HTML tag <tg-math-block>."""

    def __init__(self, type: str, expression: str):
        self.type: str = type
        self.expression: str = expression

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
        if self.expression is not None:
            result['expression'] = _serialize(self.expression)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'InputRichBlockMathematicalExpression' | None:
        if not data:
            return None
        return cls(
            type=data.get('type'),
            expression=data.get('expression'),
        )