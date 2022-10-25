from __future__ import annotations

import hashlib
from typing import Tuple
import uuid

from ..types import UtxoOutput, TransactionData


class Utxo:
    def validate_balance(self, balance: float, amount: float) -> float:
        return balance - amount

    def generate_key(self, balance: float, amount: float, is_remainder: bool) -> str:
        return hashlib.sha256(bytes(f"{balance}{str(is_remainder)}{amount}", 'utf-8')).hexdigest()

    def generate_utxos(self, transaction: TransactionData) -> Tuple[UtxoOutput, UtxoOutput] | None:
        remainder = self.validate_balance(transaction["balance"], transaction["amount"])

        if remainder < 0:
            return None

        common_id = str(uuid.uuid4())

        output_transaction: UtxoOutput = {
            "id": common_id,
            "hash": self.generate_key(transaction["balance"], transaction["amount"], False),
            "amount": transaction["amount"],
            "isRemainder": False
        }

        output_remainder: UtxoOutput = {
            "id": common_id,
            "hash": self.generateKey(transaction["balance"], transaction["amount"], True),
            "amount": remainder,
            "isRemainder": True
        }

        return output_transaction, output_remainder
