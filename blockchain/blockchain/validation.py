import time
from flask import jsonify, make_response, Response

from ..types import BlockData, TransactionData
from ..blockchain.blockchain import Blockchain
from ..block.block import Block


class ChainValidation():
    def __init__(self) -> None:
        genesis_transaction: TransactionData = {"timestamp": time.time(), "senderID": 0, "receiverID": 0, "amount": 0}
        self.block: Block = Block(0, genesis_transaction)

    def validate(self, blockchain: Blockchain) -> Response:
        """
        validation of blockchain
        :param blockchain: current chain
        :return: current chain as object
        """
        if not blockchain:
            return make_response(jsonify({"info": "There is no blockchain currently...", "status": "404"}), 404)

        for i in range(len(blockchain.chain)):
            block_data: BlockData = blockchain.chain[i]
            prior_block_data: BlockData = block_data

            if i > 0:
                prior_block_data = blockchain.chain[i - 1]

            self.block.convert(block_data)

            if not self.validate_hash():
                return make_response(jsonify({"info": "invalid block hash", "status": "500"}), 500)

            if block_data["index"] == 1 and not self.validate_proof(0, block_data["proof"], block_data["timestamp"]):
                return make_response(jsonify({"info": "invalid block proof", "status": "500"}), 500)

            if block_data["index"] > 1 and not self.validate_proof(prior_block_data["proof"], block_data["proof"],
                                                                   block_data["timestamp"]):
                return make_response(jsonify({"info": "invalid block proof", "status": "500"}), 500)

            if block_data["index"] > 1 and not self.compare_hashes(block_data["priorHash"],
                                                                   prior_block_data["currentHash"]):
                return make_response(jsonify({"info": "hash mismatch", "status": "500"}), 500)

        return make_response(jsonify(blockchain), 200)

    def validate_hash(self) -> bool:
        """
        hash validation
        :return: validated current hash
        """
        return self.block.currentHash == self.block.hash()

    def validate_proof(self, previous_proof: int, current_proof: int, timestamp: datetime) -> bool:
        """
        proof of work validation
        :param previous_proof:
        :param current_proof:
        :param timestamp:
        :return: object
        """
        return self.block.validate(previous_proof, current_proof, timestamp)

    def compare_hashes(self, current_blockのprevious_hash: str, previous_block_hash: str) -> bool:
        """
        comparison of hash codes
        :param current_blockのprevious_hash:
        :param previous_block_hash:
        :return: boolean
        """
        return current_blockのprevious_hash == previous_block_hash
