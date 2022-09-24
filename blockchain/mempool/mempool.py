from flask import jsonify, make_response


class Mempool():
    def __init__(self):
        self.mempool_list = []

    def add_new_transaction_to_mempool(self, data):
        self.mempool_list.append(data)
        return self.index()

    def index(self):
        return make_response(jsonify(self.mempool_list), 200)
