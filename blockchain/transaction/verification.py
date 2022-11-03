import hashlib
from ecdsa import VerifyingKey, NIST521p

from ..types import TransactionContent


class VerifyTransaction:
    def __init__(self, transaction: TransactionContent) -> None:
        self.publicKey = VerifyingKey.from_string(transaction['publicKey'], curve=NIST521p)
        self.transaction = transaction

    def verify_transaction(self) -> bool:
        """
        check the transaction to match a string
        :return: verified signature
        """
        hash_str = hashlib.sha256(bytes(self.transaction_to_str(), 'utf-8')).hexdigest()
        return self.publicKey.verify(self.transaction['signature'], hash_str)

    def transaction_to_str(self):
        """
        convert transaction to formatted string
        :return: transaction content as a string
        """
        return f"timestamp:{self.transaction['timestamp']}," \
               f"senderID:{self.transaction['senderID']}," \
               f"receiverID:{self.transaction['receiverID']}," \
               f"amount:{self.transaction['amount']}"
