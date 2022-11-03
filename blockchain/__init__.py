from flask import Flask, request, jsonify, make_response

from .blockchain.validation import BlockchainValidation
from .nodes.registernode import RegisterNode
from .pool.pooloftransactions import PoolOfTransactions
from .transaction.transaction import Transaction
from .blockchain.blockchain import Blockchain
from .pool.pool import Pool


def create_app(test_config=None):
    server = Flask(__name__)
    pool = Pool()
    node_register = RegisterNode()
    transaction_outputs = PoolOfTransactions()
    chain = Blockchain(transaction_outputs)
    transaction = Transaction(pool, transaction_outputs, chain)
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
        return BlockchainValidation().validate(chain)

    @server.get(base_url + 'blockchain/length')
    def get_chain_length():
        """
        Get the length of the blockchain
        :return: length route
        """
        return chain.get_length()

    @server.get(base_url + 'utxo/poll')
    def poll_transaction_utxo():
        """
        get utxo outputs from transactions
        :return: route
        """
        return transaction_outputs.poll_pool()

    @server.put(base_url + 'transactionOutputs/poll')
    def poll_transaction_output():
        """
        get utxo outputs from transactions
        :return: json
        """
        return transaction_outputs.poll_output(request.json)

    @server.post(base_url + 'assert')
    def incoming_chain():
        """
        assert chains
        :return: json response
        """
        isValid = BlockchainValidation().get_chain_validation(chain, request.json).ok

        if not isValid:
            return make_response(jsonify({"error": "chain validated unsuccessfully", "status": 400}), 400)
        return make_response(jsonify({"info": "consolidation of chain successful", "status": 200}), 200)

    @server.get(base_url + 'balance')
    def get_balance():
        """
        get the balance
        :return: route
        """
        return chain.getBalanceByUid(request.json)

    @server.get(base_url + 'consensus')
    def get_chain_validation():
        """
        contact Legion, we reached consensus - Mass effect
        :return: Geth life form
        """
        return BlockchainValidation().get_chain_validation(chain, request.json)

    return server
