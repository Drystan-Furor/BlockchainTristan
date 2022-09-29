from flask import request, jsonify

from blockchain.blockchain import blockchain
from blockchain.node_register.register_node import RegisterNode
from blockchain.blockchain.blockchain import Blockchain


class RegisterNodes:
    def __init__(self):
        self.register_node = RegisterNode()

    def register_nodes(blockchain):
        values = request.get_json()

        nodes = values.get('nodes')
        if nodes is None:
            return "Error: Please supply a valid list of nodes", 400

        for node in nodes:
            blockchain.register_node(node)

        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(blockchain.nodes),
        }
        return jsonify(response), 201