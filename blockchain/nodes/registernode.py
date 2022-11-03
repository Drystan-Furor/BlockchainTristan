from flask import jsonify, make_response, Response


class RegisterNode:
    def __init__(self) -> None:
        self.registry: list[str] = []

    def register_node(self, address: str) -> Response:
        """
        register a single node
        :param address: where I live
        :return: send me a postcard
        """
        self.registry.append(address)
        return make_response(jsonify(self.registry), 200)

    def get_nodes_list(self) -> Response:
        """
        the yellow pages of nodes
        :return: a phone book
        """
        return make_response(jsonify(self.registry), 200)
