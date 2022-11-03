from __future__ import annotations

import hashlib
from typing import Tuple
import uuid

from ..types import UtxoOutput, TransactionContent


class Utxo:
    def validate_balance(self, balance: float, amount: float) -> float:
        """
        balance validation, total minus current
        :param balance: float
        :param amount: float
        :return: subtraction to get current
        """
        return balance - amount

    def generate_utxos(self, transaction: TransactionContent, balance: float) -> Tuple[UtxoOutput, UtxoOutput] | None:
        """
        create multiple transaction outputs to build a transaction
        :param transaction: content
        :param balance: float
        :return:
        """
        remainder = self.validate_balance(balance, transaction["amount"])

        if remainder < 0:
            return None

        common_id = str(uuid.uuid4())

        output_transaction: UtxoOutput = {
            "timestamp":    transaction["timestamp"],
            "previousHash": transaction["inputHash"],
            "id":           common_id,
            "hash":         self.generate_key(balance, transaction["amount"], False),
            "amount":       transaction["amount"],
            "receiverID":   transaction["receiverID"],
            "isRemainder":  False
        }

        output_remainder: UtxoOutput = {
            "timestamp":    transaction["timestamp"],
            "previousHash": transaction["inputHash"],
            "id":           common_id,
            "hash":         self.generate_key(balance, transaction["amount"], True),
            "amount":       remainder,
            "receiverID":   transaction["receiverID"],
            "isRemainder":  True
        }

        return output_transaction, output_remainder

    def generate_key(self, balance: float, amount: float, is_remainder: bool) -> str:
        """
        generate a key by hashing the content
        :param balance: float
        :param amount: float
        :param is_remainder: bool
        :return: utxo key
        """
        return hashlib.sha256(bytes(f"{balance}{str(is_remainder)}{amount}", 'utf-8')).hexdigest()


