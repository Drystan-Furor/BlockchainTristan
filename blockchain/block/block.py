from __future__ import annotations

import time
import hashlib
import json

from ..types import BlockData, TransactionData


class Block:
    def __init__(self, index: int, transaction: TransactionData, previous_hash: str = "initial") -> None:
        self.index = index
        self.timestamp = time.time()
        self.proof = 0
        self.previous_block_hash = previous_hash
        self.currentHash = ""
        self.transaction = transaction

    def generate_block(self, previous_block: BlockData | None = None) -> BlockData:
        """
        Create a new Block in the Blockchain
        :param previous_block: Data of the previous Block
        :return: New Block
        """
        this_proof: int = 0

        if previous_block:
            this_proof = previous_block["proof"]

        self.proof = self.proof_of_work(this_proof)

        return {
            "index": self.index,
            "timestamp": datetime.now(),
            "proof": self.proof_of_work(this_proof),
            "priorHash": self.previous_block_hash,
            "currentHash": self.hash(),
            "transaction": self.transaction
        }

    def convert(self, block_datafields: BlockData) -> None:
        """
        JSON conversion to Object
        :param block_datafields: Data of the Block
        """
        self.index = block_datafields["index"]
        self.timestamp = block_datafields["timestamp"]
        self.proof = block_datafields["proof"]
        self.previous_block_hash = block_datafields["priorHash"]
        self.currentHash = block_datafields["currentHash"]
        self.transaction = block_datafields["transaction"]

    def hash(self) -> str:
        """
        Creates a SHA-256 hash of a Block
        """
        block_data = json.dumps(str(self.index)
                                + str(self.timestamp)
                                + self.previous_block_hash
                                + json.dumps(self.transaction, sort_keys=True, indent=4, default=str)).encode("utf-8")
        return hashlib.sha256(block_data).hexdigest()

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Create a new Block in the Blockchain
        :param previous_proof: Data of the previous proof
        :return: New Proof
        """
        current_proof: int = 0

        while self.validate(previous_proof, current_proof) is False:
            current_proof += 1

        return current_proof

    def validate(self, previous_proof: int, current_proof: int, timestamp: datetime | None = None) -> bool:
        """
        Validation of the proof
        :param previous_proof: data of proof of the last block
        :param current_proof: current INT of PoW
        :param timestamp: timestamp or None
        :return nonce
        """
        time = self.timestamp
        if timestamp is not None:
            time = timestamp

        attempt = (str(previous_proof) + str(current_proof) + str(time)).encode()
        hashed_attempt = hashlib.sha256(attempt).hexdigest()
        return hashed_attempt[:5] == "0000"
