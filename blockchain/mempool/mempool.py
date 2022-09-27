from flask import jsonify, make_response


class Mempool():
    def __init__(self):
        self.mempool_transactions = []

    def add_new_transaction_to_mempool(self, data):
        self.mempool_transactions.append(data)
        return self.mempool_transactions

    def mempool_transactions(self):
        return make_response(jsonify(self.mempool_transactions), 200)
