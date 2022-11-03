from __future__ import annotations

import time
import hashlib
import json

from ..pool.pooloftransactions import PoolOfTransactions
from ..transaction.genesis_helper import genesis_transaction
from ..types import BlockData, TransactionContent


class Block:
    def __init__(self, index: int, transaction: TransactionContent, previous_hash: str = "initial") -> None:
        self.index = index
        self.timestamp = time.time()
        self.proof = 0
        self.previous_block_hash = previous_hash
        self.currentHash = ""
        self.transaction = transaction

    def generate_block(
            self,
            transaction_pool:PoolOfTransactions,
            previous_block: BlockData | None = None
    ) -> BlockData:
        """
        Create a new Block in the Blockchain
        :param transaction_pool: mempool of stored transactions
        :param previous_block: Data of the previous Block
        :return: New Block
        """
        if not previous_block:
            input = genesis_transaction()
            the_first_transaction = input.get_genesis_transaction()

            transaction_pool.append_transactions(the_first_transaction["transaction_output"])

            return {
                "index": self.index,
                "timestamp": self.timestamp,
                "proof": 0,
                "priorHash": "GenesisBlock",
                "currentHash": self.hash(),
                "transaction": the_first_transaction
            }
        self.proof = self.proof_of_work(previous_block["proof"])
        return {
            "index":        self.index,
            "timestamp":    self.timestamp,
            "proof":        self.proof,
            "priorHash":    self.previous_block_hash,
            "currentHash":  self.hash(),
            "transaction":  self.transaction
        }

    def hash(self) -> str:
        """
        Creates a SHA-256 hash of a Block
        """
        return hashlib.sha256(bytes(self.__str__(), 'utf-8')).hexdigest()

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

    def convert_json_to_object(self, block_datafields: BlockData) -> None:
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

    def validate(self, previous_proof: int, current_proof: int, timestamp: time() | None = None) -> bool:
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
        return hashed_attempt[:4] == "0000"

    #omits current hash since this function is used to generate the current hash
    def __str__(self) -> str:
        return f"index: {self.index}, timestamp: {self.timestamp}, proof: {self.proof}, priorHash: {self.priorBlockHash}, transaction: ( timestamp: {self.transaction['timestamp']}, senderID: {self.transaction['senderID']}, receiverID: {self.transaction['receiverID']}, amount: {self.transaction['amount']})"
