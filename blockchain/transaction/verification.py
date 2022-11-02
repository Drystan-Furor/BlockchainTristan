import hashlib
from ecdsa import VerifyingKey, NIST521p

from ..types import TransactionData

class TransactionVerification():
    def __init__(self, transaction:TransactionData) -> None:
        self.publicKey = VerifyingKey.from_string(transaction['publicKey'], curve=NIST521p)
        self.transaction = transaction

    def transactionToStr(self):
        return f"timestamp:{self.transaction['timestamp']},senderID:{self.transaction['senderID']},receiverID:{self.transaction['receiverID']},amount:{self.transaction['amount']}"

    def verifyTransaction(self) -> bool:
        hashstr = hashlib.sha256(bytes(self.transactionToStr(), 'utf-8')).hexdigest()
        return self.publicKey.verify(self.transaction['signature'], hashstr)