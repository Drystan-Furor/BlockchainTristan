import os

from flask import Flask, jsonify, make_response, request
from .blockchain.blockchain import Blockchain
from .mempool.mempool import Mempool
from .transaction.transaction import Transaction
from .validate_blockchain.validate_blockchain import ValidateBlockchain


def create_app(test_config=None):
    app = Flask(__name__)
    blockchain = Blockchain()
    mempool = Mempool()
    transaction = Transaction(mempool)
    base_url = "/api/v1/"

    @app.get(base_url + 'block/create')
    def add_block_to_chain():
        return Blockchain.add_block(blockchain, mempool)

    @app.get(base_url + 'blockchain/list')
    def blockchain_index():
        return Blockchain.list(blockchain)

    @app.get(base_url + 'blockchain/reset')
    def reset_blockchain():
        return Blockchain.reset(blockchain)

    @app.route(base_url + 'transaction/create', methods=['POST'])
    def transaction_create():
        return transaction.transaction_create(request.json)

    @app.get(base_url + 'mempool/index')
    def get_mempool():
        return Mempool.index(mempool)

    @app.get(base_url + 'blockchain/validate')
    def validate_blockchain():
        return ValidateBlockchain().validate(blockchain.list())

    return app
