from flask import jsonify, make_response, Response
from ..types import TransactionContent


class Pool:
    def __init__(self) -> None:
        self.list: list[TransactionContent] = []

    def add_transaction_to_pool(self, transaction: TransactionContent) -> Response:
        """
        add to list, call it a pool
        :param transaction: contents
        :return: list of transactions in the pool
        """
        self.list.append(transaction)
        return make_response(jsonify(self.list), 200)
