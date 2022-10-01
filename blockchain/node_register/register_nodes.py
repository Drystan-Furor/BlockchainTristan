from flask import request, jsonify
from ..node_register.register_node import RegisterNode


class RegisterNodes:
    def __init__(self):
        self.rn = RegisterNode()
        self.nodes = set()

    def register_nodes(self):
        values = request.get_json()

        nodes = values.get('nodes')
        if nodes is None:
            return "Error: Please supply a valid list of nodes", 400

        for node in nodes:
            self.rn.register_node(node)

        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(self.nodes),
        }
        return jsonify(response), 201
