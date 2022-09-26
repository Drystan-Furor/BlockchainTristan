from flask import jsonify, make_response


class Mempool():
    def __init__(self):
        self.list = []

    def add_new_transaction_to_mempool(self, data):
        self.list.append(data)
        return self.mempool_list()

    def mempool_list(self):
        return make_response(jsonify(self.list), 200)
