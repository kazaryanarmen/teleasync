from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    
    from .revenue_withdrawal_state import RevenueWithdrawalState
    


class TransactionPartnerFragment:
    """Describes a withdrawal transaction with Fragment."""

    def __init__(self, type: str, withdrawal_state: RevenueWithdrawalState | None = None):
        self.type: str = type
        self.withdrawal_state: RevenueWithdrawalState | None = withdrawal_state

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
        if self.withdrawal_state is not None:
            result['withdrawal_state'] = _serialize(self.withdrawal_state)
        return result

    @classmethod
    def from_dict(cls, data: dict | None) -> 'TransactionPartnerFragment' | None:
        if not data:
            return None
        from .revenue_withdrawal_state import RevenueWithdrawalState
        return cls(
            type=data.get('type'),
            withdrawal_state=RevenueWithdrawalState.from_dict(data.get('withdrawal_state')),
        )