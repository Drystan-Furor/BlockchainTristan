import time
from flask import jsonify, make_response
from .utxo import Utxo
from typing import Any
from .verification import VerifyTransaction
from .. import Blockchain
from ..pool.pooloftransactions import PoolOfTransactions
from ..types import TransactionContent, UtxoOutput
from ..pool.pool import Pool


class Transaction():
    def __init__(self, pool: Pool, transaction_outputs: PoolOfTransactions, chain: Blockchain) -> None:
        self.pool = pool
        self.UtxoOutput = transaction_outputs
        self.chain = chain

    def create_transaction(self, required_fields: Any):
        """
        Transaction blueprint
        :param self: this
        :param required_fields: params for data
        :return: transaction in the pool
        """
        try:
            transaction_data: TransactionContent = {
                "timestamp": time.time(),
                "senderID": int(required_fields["senderID"]),
                "receiverID": int(required_fields["receiverID"]),
                "amount": float(required_fields["amount"]),
                "publicKey": bytes(required_fields["publicKey"]),
                "signature": str(required_fields["signature"]),
                "inputHash": str(TransactionContent["inputHash"]),
                "transaction_output": None
            }
        except:
            return make_response(jsonify({"info": "deformed request", "status": "400"}), 400)

        if not transaction_data["amount"] > 0:
            # https://roll20.net/compendium/dnd5e/Hideous%20Laughter#content
            # perceives everything as hilariously funny and falls into fits of laughter
            return make_response(jsonify({"cast spell": "Tasha's hideous laughter", "status": "400"}), 400)

        balance = self.chain.get_balance_by_uid(TransactionContent["senderID"])
        transaction_verification = VerifyTransaction(TransactionContent)
        if not transaction_verification.verify_transaction():
            return make_response(jsonify({"info": "resolving signature failed", "status": "401"}), 401)

        TxID = Utxo()
        utxos = TxID.generate_utxos(TransactionContent, balance)
        if not utxos:
            return make_response(jsonify({"Error": "no previous transactions detected", "status": "404"}), 404)

        self.UtxoOutput.append_transactions(utxos)
        TransactionContent["transaction_output"] = utxos
        return self.pool.add_transaction_to_pool(TransactionContent)
