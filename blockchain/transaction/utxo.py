
import hashlib
from typing import Tuple
import uuid

from ..types import UtxoOutput, TransactionData

class utxo:
    def validateBalance(self, balance: float, amount: float) -> float:
        return balance-amount

    def generateKey(self, balance: float, amount: float, isRemainder: bool) -> str:
        return hashlib.sha256(bytes(f"{balance}{str(isRemainder)}{amount}", 'utf-8')).hexdigest()

    def generateUtxos(self, transaction: TransactionData) -> Tuple[UtxoOutput, UtxoOutput] | None:
        remainder = self.validateBalance(transaction["balance"], transaction["amount"])

        if remainder < 0:
            return None

        commonId = str(uuid.uuid4())

        outputTransaction: UtxoOutput = {
            "id":           commonId,
            "hash":         self.generateKey(transaction["balance"], transaction["amount"], False),
            "amount":       transaction["amount"],
            "isRemainder":  False
        }

        outputRemainder: UtxoOutput = {
            "id":           commonId,
            "hash":         self.generateKey(transaction["balance"], transaction["amount"], True),
            "amount":       remainder,
            "isRemainder":  True
        }

        return (outputTransaction, outputRemainder)