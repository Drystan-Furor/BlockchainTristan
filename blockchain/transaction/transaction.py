from datetime import datetime
from typing import Any
from flask import jsonify, make_response
from ..types import TransactionData
from ..pool.pool import Pool


class Transaction():
    def __init__(self, pool: Pool) -> None:
        self.pool = pool

    def create_transaction(self, required_fields: Any):
        """
        Transaction blueprint
        :param required_fields: params for data
        :return: transaction in the pool
        """
        try:
            transaction_data: TransactionData = {
                "timestamp": datetime.now(),
                "senderID": int(required_fields["senderID"]),
                "receiverID": int(required_fields["receiverID"]),
                "amount": float(required_fields["amount"])
            }
        except:
            return make_response(jsonify({"info": "deformed request", "status": "400"}), 400)

        if not transaction_data["amount"] > 0:
            # https://roll20.net/compendium/dnd5e/Hideous%20Laughter#content
            # perceives everything as hilariously funny and falls into fits of laughter

            return make_response(jsonify({"info": "Tasha's hideous laughter", "status": "400"}), 400)

        return self.pool.add_transaction_to_pool(transaction_data)
