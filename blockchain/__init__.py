import os
from uuid import uuid4

from flask import Flask, jsonify, make_response, request

from blockchain.block.block import Block
from blockchain.blockchain.blockchain import Blockchain
from blockchain.mempool.mempool import Mempool
from blockchain.transaction.transaction import Transaction
from blockchain.validate_chain.valid_chain import ValidateChain


def create_app(test_config=None):
    # Instantiate the Node
    app = Flask(__name__)

    blockchain = Blockchain()
    block = Block()
    mempool = Mempool()
    transaction = Transaction(mempool)
    base_url = "/api/v1/"
    # Generate a globally unique address for this node
    node_identifier = str(uuid4()).replace('-', '')


    @app.route('/mine', methods=['GET'])
    def mine():
        return Blockchain.mine()


    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()

        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Create a new Transaction
        index = transaction.new_transaction(values['sender'], values['recipient'], values['amount'])

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        return jsonify(response), 200

    @app.route('/nodes/register', methods=['POST'])
    def register_nodes(node_register=blockchain.nodes):
        return node_register.RegisterNodes()

    @app.route('/nodes/resolve', methods=['GET'])
    def consensus():
        return consensus.Consensus(blockchain)
