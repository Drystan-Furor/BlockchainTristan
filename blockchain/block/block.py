import json
from time import time
import hashlib
from blockchain.validate_proof.valid_proof import ValidProof
import random


class Block:
    def __init__(self, index, current_transaction, proof, previous_hash):
        self.index = index
        self.timestamp = time()
        self.current_transaction = current_transaction
        self.previous_hash = previous_hash
        self.proof = proof

        self.chain = []
        self.vp = ValidProof()

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            "current_hash": self.hash(),
        }

        # Reset the current list of transactions
        self.current_transaction = []

        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.vp.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof
