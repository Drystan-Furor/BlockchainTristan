import time
from typing import Any
from flask import jsonify, make_response

from .utxo import Utxo
from ..pool.transactionPool import TransactionPool
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
            "balance": float(required_fields["balance"]),
            "transactionOutput": None
        }
    except:
        return make_response(jsonify({"info": "deformed request", "status": "400"}), 400)

    if not transaction_data["amount"] > 0:
        # https://roll20.net/compendium/dnd5e/Hideous%20Laughter#content
        # perceives everything as hilariously funny and falls into fits of laughter
        return make_response(jsonify({"info": "Tasha's hideous laughter", "status": "400"}), 400)

    input_object = Utxo()
    outputs = input_object.generate_utxos(transaction_data)

    self.transactionOutputs.appendTransaction(outputs[0])
    self.transactionOutputs.appendTransaction(outputs[1])

    transaction_data["transactionOutput"] = outputs
    return self.pool.add_transaction_to_pool(transaction_data)
