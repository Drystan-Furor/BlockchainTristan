from __future__ import annotations

import hashlib
from typing import Tuple
import uuid

from ..types import UtxoOutput, TransactionContent


def validate_balance(balance: float, amount: float) -> float:
    """
    balance validation, total minus current
    :param balance: float
    :param amount: float
    :return: subtraction to get current
    """
    return balance - amount


class Utxo:

    def generate_key(self: float, amount: float, is_remainder: bool) -> str:
        """
        generate a key by hashing the content
        :param self: float (balance)
        :param amount: float
        :param is_remainder: bool
        :return: utxo key
        """
        return hashlib.sha256(bytes(f"{self}{amount}{str(is_remainder)}", 'utf-8')).hexdigest()

    def generate_utxos(self, balance: float, transaction: TransactionContent) -> Tuple[UtxoOutput, UtxoOutput] | None:
        """
        create multiple transaction outputs to build a transaction
        :param transaction: float
        :param balance: float
        :return:
        """
        remainder = validate_balance(balance, transaction["amount"])

        if remainder < 0:
            return None

        common_id = str(uuid.uuid4())

        output_transaction: UtxoOutput = {
            "timestamp": transaction["timestamp"],
            "previousHash": transaction["inputHash"],
            "id": common_id,
            "hash": self.generate_key(balance, transaction["amount"], False),
            "amount": transaction["amount"],
            "receiverID": transaction["receiverID"],
            "is_remainder": False
        }

        output_remainder: UtxoOutput = {
            "timestamp": transaction["timestamp"],
            "previousHash": transaction["inputHash"],
            "id": common_id,
            "hash": self.generate_key(balance, transaction["amount"], True),
            "amount": remainder,
            "receiverID": transaction["receiverID"],
            "is_remainder": True
        }

        return output_transaction, output_remainder
