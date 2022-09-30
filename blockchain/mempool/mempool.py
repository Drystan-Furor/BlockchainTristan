from flask import jsonify, make_response


class Mempool():
    def __init__(self):
        self.mempool = []

    def add_new_transaction_to_mempool(self, transaction):
        self.mempool.append(transaction)
        return self.mempool

    def mempool_list(self):
        return make_response(jsonify(self.mempool_list), 200)
