# mypy: ignore-errors
from __future__ import annotations
from typing import Tuple

import requests
import json

from .. import Blockchain
from .registernode import RegisterNode


def make_request(url: str, method: str = "get", body: str | None = None) -> Tuple[str, int]:
    """
    make a promise
    :param url: str
    :param method: get
    :param body: str
    :return: json or message
    """
    try:
        response = requests.request(method, url, data=body)
        return json.loads(response.text), response.status_code
    except:
        return "{'info':'HTTP request error occurred', 'status':500}", 500


class NodeResponse:
    def __init__(self, nodes_registry: RegisterNode) -> None:
        self.register = nodes_registry

    def poll_nodes(self, endpoint: str, method: str = "get", body: str | None = None) -> bool:
        """
        poll of nodes
        :param endpoint:
        :param method:
        :param body:
        :return:
        """
        OKs: int = 0

        for node in self.register:
            result = make_request(node + "/" + endpoint, method, body)

            if result[0] == 200:
                OKs += 1

        return (100 / len(self.register) * OKs) > 60

    def chain_validation(self, chain: Blockchain) -> bool:
        """
        validate chain
        :param chain:
        :return: consensus
        """
        endpoint = "consensus"
        return self.poll_nodes(endpoint, body=json.dumps(chain.chain))

    def blockchain_assertion(self, chain: Blockchain) -> None:
        """
        see if consensus is reached
        :param chain: this
        :return: assertion
        """
        endpoint = "consensus/assert"
        self.poll_nodes(endpoint, "post", body=json.dumps(chain.chain))
