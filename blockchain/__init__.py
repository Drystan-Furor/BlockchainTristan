from uuid import uuid4
from flask import Flask

from blockchain.block.block import Block
from blockchain.blockchain.blockchain import Blockchain
from blockchain.mempool.mempool import Mempool
from blockchain.transaction.transaction import Transaction
from blockchain.validate_chain.valid_chain import ValidateChain


def create_app(test_config=None):
    # Instantiate the Node
    app = Flask(__name__)

    _blockchain = Blockchain()
    # mempool = Mempool()
    url = "/api/v1/"

    # Generate a globally unique address for this node
    _node_identifier = str(uuid4()).replace('-', '')

    @app.route(url + '/mine', methods=['GET'])
    def mine(_blockchain, _node_identifier):
        return _blockchain.mine(_node_identifier)

    @app.route(url + '/transactions/new', methods=['POST'])
    def new_transaction():
        return new_transaction()

    @app.route(url + '/chain', methods=['GET'])
    def full_chain(_blockchain):
        return _blockchain.full_chain(_blockchain)

    @app.route(url + '/nodes/register', methods=['POST'])
    def register_nodes(_blockchain):
        return _blockchain.RegisterNodes()

    @app.route(url + '/nodes/resolve', methods=['GET'])
    def consensus(_blockchain):
        return consensus.Consensus(_blockchain)
