from __future__ import annotations

from typing import Any, Tuple
from flask import jsonify, make_response, Response

from ..types import UtxoOutput


class PoolOfTransactions():
    def __init__(self) -> None:
        self.list: list[UtxoOutput] = []

    def append_transaction(self, utxo: UtxoOutput) -> None:
        """
        append a transaction output / utxo
        :param utxo: generate output
        :return: current utxo
        """
        self.list.append(utxo)

    def find(self, id_or_hash: str) -> Tuple[int, UtxoOutput | None]:
        """
        find id or hash
        :param  id_or_hash transaction output data
        :return: the data when needle is in mempool haystack
        """
        for i, transactionOutput in enumerate(self.list):
            if transactionOutput["id"] == id_or_hash:
                return (i, transactionOutput)

            if transactionOutput["hash"] == id_or_hash:
                return (i, transactionOutput)

        return -1, None

    def get(self, id_or_hash: str, remove: bool = False) -> UtxoOutput | None:
        result = self.find(id_or_hash)

        if result[0] == -1:
            return None

        if remove:
            # delete from mempool list
            self.list.pop(result[0])

        return result[1]

    def remove(self, id_or_hash) -> Response:
        # delete the hash or id after validation
        result = self.get(id_or_hash, True)

        if not result:
            return make_response(jsonify({"info": "utxo up in smoke", "status": "404"}), 404)

        return make_response(jsonify(result), 200)

    def append_transactions(self, outputs: Tuple[UtxoOutput, UtxoOutput]) -> None:
        """
        append mult utxo's
        :param outputs: utxo's
        :return: array
        """
        self.list.append(outputs[0])
        self.list.append(outputs[1])

    def poll_pool(self) -> Response:
        """
        list of pool content
        :return: json list
        """
        return make_response(jsonify(self.list), 200)

    def poll_output(self, transaction_requirements: Any) -> Response:
        try:
            request_data = {
                "id": str(transaction_requirements["id"]),
                "hash": str(transaction_requirements["hash"]),
            }
        except:
            return make_response(jsonify({"info": "malformed request", "status": "400"}), 400)

        result = self.get(request_data["hash"] + request_data["id"])
        if not result:
            return make_response(jsonify({"info": "transaction_output not found"}), 404)

        return make_response(jsonify(result), 200)

    def open_remainder_by_uid(self, user_id: int) -> UtxoOutput | None:
        """
        search on uid
        :param user_id:
        :return: none
        """
        for transaction in self.list:
            if transaction["receiverID"] == user_id and transaction["isRemainder"]:
                return transaction
        return None

    def get_open_remainder(self, user_id: int) -> Response:
        """
        get the uid
        :param user_id:
        :return: json error or succes
        """
        result = self.open_remainder_by_uid(user_id)
        if not result:
            return make_response(jsonify({"Error": "this user no open transactions to be found ", "status": "404"}), 404)
        return make_response(jsonify(result))
