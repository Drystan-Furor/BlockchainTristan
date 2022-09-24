import json
import datetime;
import hashlib
import random

from ..validate_proof.validate_proof import ValidateProof


class Block:
    def __init__(self, index, transaction_data, previous_block_hash=''):
        self.index = index
        self.transaction_data = transaction_data
        self.previous_block_hash = previous_block_hash
        self.current_timestamp = self.get_current_timestamp()

    def create_block(self, blockchain):
        previous_block = {}

        if not blockchain:
            previous_block['proof'] = 0
        else:
            previous_block = blockchain[-1]

        return {
            "index": self.index,
            "timestamp": self.current_timestamp,
            "data": self.transaction_data,
            "proof": self.proof_of_work(previous_block),
            "previous_block_hash": self.previous_block_hash,
            "current_block_hash": self.hash_block_data(),
        }

    def get_current_timestamp(self):
        return datetime.datetime.now()

    def hash_block_data(self):
        block_data = json.dumps(
            str(self.index) + json.dumps(self.transaction_data, indent=4, sort_keys=True, default=str) + str(
                self.current_timestamp) + self.previous_block_hash).encode('utf-8')
        return hashlib.sha256(block_data).hexdigest()

    def proof_of_work(self, last_block):
        last_proof = last_block['proof']
        timestamp = self.current_timestamp

        proof = 0
        while ValidateProof().valid_proof(last_proof, proof, timestamp) is False:
            proof += 1
        return proof
