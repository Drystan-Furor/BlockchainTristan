import time
from typing import Any
from flask import jsonify, make_response

from .utxo import Utxo
from .verification import TransactionVerification
from ..pool.transactionPool import TransactionPool
from ..transactionRequest import mockClient
from ..transactionRequest.mockClient import Client
from ..types import TransactionData
from ..pool.pool import Pool


class Transaction():
    def __init__(self, pool: Pool, transaction_outputs: TransactionPool) -> None:
        self.pool = pool
        self.transactionOutputs = transaction_outputs


def create_transaction(self, required_fields: Any):
    """
        Transaction blueprint
        :param self: this
        :param required_fields: params for data
        :return: transaction in the pool
        """
    try:
        transaction_data: TransactionData = {
            "timestamp": time.time(),
            "senderID": int(required_fields["senderID"]),
            "receiverID": int(required_fields["receiverID"]),
            "amount": float(required_fields["amount"]),
            "publicKey": str(required_fields["publicKey"]),
            "signature": str(required_fields["signature"]),
            "inputHash": str(TransactionData["inputHash"]),
            "transactionOutput": None
        }
    except:
        return make_response(jsonify({"info": "deformed request", "status": "400"}), 400)

    if not transaction_data["amount"] > 0:
        # https://roll20.net/compendium/dnd5e/Hideous%20Laughter#content
        # perceives everything as hilariously funny and falls into fits of laughter
        return make_response(jsonify({"info": "Tasha's hideous laughter", "status": "400"}), 400)

    #Temporarily mock a transaction, because there is no client currently
    mockClient = Client()
    transactionData = mockClient.pseudoTransaction

    balance = self.chain.getBalanceByUid(transactionData["senderID"])

    transactionVerification = TransactionVerification(transactionData, balance)
    if not transactionVerification.verifyTransaction():
        return make_response(jsonify({"info":"signature does not resolve", "status":"401"}), 401)

    input_object = Utxo()
    outputs = input_object.generate_utxos(transactionData)
    self.transactionOutputs.appendTransactions(outputs)
    transactionData["transactionOutput"] = outputs

    return self.pool.appendTransaction(transactionData)





