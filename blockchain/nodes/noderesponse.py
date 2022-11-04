# mypy: ignore-errors
from __future__ import annotations

from typing import Tuple

# mypy: ignore-errors
import requests
import json

from .. import Blockchain

from .registernode import RegisterNode


class NodeResponse:
    def __init__(self, nodes_registry: RegisterNode) -> None:
        self.register = nodes_registry

    def make_request(self, url: str, method: str = "get", body: str | None = None) -> Tuple[str, int]:
        try:
            response = requests.request(method, url, data=body)
            return json.loads(response.text), response.status_code
        except:
            return "{'info':'HTTP request error occurred', 'status':500}", 500

    def poll_nodes(self, endpoint: str, method: str = "get", body: str | None = None) -> bool:
        OKs: int = 0

        for node in self.register:
            result = self.make_request(node + "/" + endpoint, method, body)

            if result[0] == 200:
                OKs += 1

        return (100 / len(self.register) * OKs) > 60

    def chain_validation(self, chain: Blockchain) -> bool:
        endpoint = "consensus"
        return self.poll_nodes(endpoint, body=json.dumps(chain.chain))

    def blockchain_assertion(self, chain: Blockchain) -> None:
        endpoint = "consensus/assert"
        self.poll_nodes(endpoint, "post", body=json.dumps(chain.chain))
