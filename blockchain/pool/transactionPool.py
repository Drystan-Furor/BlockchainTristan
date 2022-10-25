from typing import Any, Tuple
from flask import jsonify, make_response, Response

from ..types import UtxoOutput


class TransactionPool():
    def __init__(self) -> None:
        self.list: list[UtxoOutput] = []

    def append_transaction(self, utxo: UtxoOutput) -> None:
        """
        append an output
        :param utxo: generate output
        :return: current utxo
        """
        self.list.append(utxo)

    def pollPool(self) -> Response:
        return make_response(jsonify(self.list), 200)

    def find(self, idOrHash: str) -> Tuple[int, UtxoOutput | None]:
        """
        find id or hash
        :param  idOrHash transaction output data
        :return: the data when needle is in mempool haystack
        """
        for i, transactionOutput in enumerate(self.list):
            if transactionOutput["id"] == idOrHash:
                return (i, transactionOutput)

            if transactionOutput["hash"] == idOrHash:
                return (i, transactionOutput)

        return (-1, None)

    def get(self, idOrHash: str, remove: bool = False) -> UtxoOutput | None:
        result = self.find(idOrHash)

        if result[0] == -1:
            return None

        if remove:
            # delete from mempool list
            self.list.pop(result[0])

        return result[1]

    def remove(self, idOrHash) -> Response:
        # delete the hash or id after validation
        result = self.get(idOrHash, True)

        if not result:
            return make_response(jsonify({"info": "transactionoutput not found", "status": "404"}), 404)

        return make_response(jsonify(result), 200)

    def pollOutput(self, transactionReq: Any) -> Response:
        try:
            requestData = {
                "id": str(transactionReq["id"]),
                "hash": str(transactionReq["hash"]),
            }
        except:
            return make_response(jsonify({"info": "malformed request", "status": "400"}), 400)

        result = self.get(requestData["hash"] + requestData["id"])

        if not result:
            return make_response(jsonify({"info": "transactionOutput not found"}), 404)

        return make_response(jsonify(result), 200)
