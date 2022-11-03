# mypy: ignore-errors
from typing import Tuple

# mypy: ignore-errors
import requests
import json

from .. import Blockchain

from .registernode import RegisterNode


class node_response():
    def __init__(self, nodes_registry: RegisterNode) -> None:
        self.registry = nodes_registry

    def makeRequest(self, url: str, method: str = "get", body: str | None = None) -> Tuple[str, int]:
        try:
            response = requests.request(method, url, data=body)
            return (json.loads(response.text), response.status_code)
        except:
            return ("\{'info':'An HTTP request error occurred', 'status':500\}", 500)

    def poll_nodes(self, endpoint: str, method: str = "get", body: str | None = None) -> bool:
        OKs: int = 0

        for node in self.registry:
            result = self.makeRequest(node + "/" + endpoint, method, body)

            if result[0] == 200:
                OKs += 1

        return (100 / len(self.registry) * OKs) > 60

    def chain_validation(self, chain: Blockchain) -> bool:
        endpoint = "consensus"
        return self.poll_nodes(endpoint, body=json.dumps(chain.chain))

    def blockchain_assertion(self, chain: Blockchain) -> None:
        endpoint = "consensus/assert"
        self.poll_nodes(endpoint, "post", body=json.dumps(chain.chain))
