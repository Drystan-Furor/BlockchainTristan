import hashlib
import time
from .utxo import Utxo
from ..types import TransactionContent

from ecdsa import SigningKey, NIST521p


class GenesisTransaction:
    def __init__(self) -> None:
        self.privateKey = SigningKey.generate(curve=NIST521p)
        self.publicKey = self.privateKey.get_verifying_key().to_string()

        hashstr = hashlib.sha256(bytes(self.__str__(), 'utf-8')).hexdigest()

        self.genesis_transaction: TransactionContent = {
            "timestamp": time.time(),
            "senderID": 0,
            "receiverID": 0,
            "amount": 100,
            "publicKey": self.publicKey,
            "signature": self.privateKey.sign(hashstr),
            "inputHash": "GenesisTransaction",
            "transaction_output": None
        }

    def __str__(self) -> str:
        return f"timestamp:{self.genesis_transaction['timestamp']}," \
               f"senderID:{self.genesis_transaction['senderID']}," \ 
               f"receiverID:{self.genesis_transaction['receiverID']}," \
               f"amount:{self.genesis_transaction['amount']}"

    def get_genesis_transaction(self):
        self.genesis_transaction["transaction_output"] = Utxo.generate_utxos(self.genesis_transaction)
        return self.genesis_transaction
