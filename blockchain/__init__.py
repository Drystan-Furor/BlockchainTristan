from flask import Flask, request, jsonify, make_response

from .blockchain.validation import ChainValidation
from .pool.transactionPool import TransactionPool
from .transaction.transaction import Transaction
from .blockchain.blockchain import Blockchain
from .pool.pool import Pool


def create_app(test_config=None):
    server = Flask(__name__)
    chain = Blockchain()
    pool = Pool()
    transaction_outputs = TransactionPool()
    transaction = Transaction(pool, transaction_outputs)
    base_url = "/api/"

    @server.get(base_url + 'pool/poll')

    def poll_pool():
        """
        get list from mempool == pool
        :return: route
        """
        return make_response(jsonify(pool.list), 200)

    @server.post(base_url + 'transaction/new')
    def create_transaction():
        """
        new transaction route
        :return: route
        """
        return transaction.create_transaction(request.json)

    @server.get(base_url + 'block/new')
    def generate_block():
        """
        new (genesis) block
        :return: route
        """
        return Blockchain.appendBlock(chain, pool)

    @server.get(base_url + 'blockchain/reset')
    def modify_memory():
        """
        reset blockchain / empty the truth / modify memories
        :return: route
        """
        return Blockchain.modify_memory()

    @server.get(base_url + 'blockchain/poll')
    def poll_chain():
        """
        pull on the chain
        :return: route
        """
        return make_response(jsonify(chain.chain), 200)

    @server.get(base_url + 'blockchain/validate')
    def validate_chain():
        """
        validation
        :return: route
        """
        return ChainValidation().validate(chain)

    @server.get(base_url + 'transactionOutputs/poll')
    def pollTransactionOutputs():
        return transaction_outputs.pollPool()

    @server.put(base_url + 'transactionOutputs/poll')
    def pollTransactionOutput():
        return transaction_outputs.pollOutput(request.json)

    return server
