from blockchain.block import Block
from blockchain.transaction import Transaction

from multiprocessing import Pool
import os
import time
import sys
import json
import logging

from blockchain.transaction import Transaction

class Blockchain:
    difficulty = 1
    max_workers = 2
    pool = None
    batch_size = int(2.5e5)
    unconfirmed_transactions = []

    def __init__(self) -> None:
        self.pool = Pool(processes=Blockchain.max_workers)
        self.chain = []
        self.unconfirmed_transactions = []

    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    def to_dict(self):
        return [block.to_dict() for block in self.chain]

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block:Block, proof:str) -> bool:
        if self.last_block.hash != block.previous_hash and len(self.chain) > 1:
            print('last block hash does not match block previous hash')
            return False

        if not self.validate_proof(block, proof):
            print('invalid proof')
            return False

        block.hash = proof

        self.chain.append(block)

        return True

    def create_first_block(self) -> Block:
        genesis_block = Block(0, [Transaction('Hello'), Transaction('World')], "0")
        genesis_block.nonce, genesis_block.hash = self.mine(genesis_block)
        print(genesis_block.merkle_root)
        self.chain.append(genesis_block)
        return self.last_block

    def validate_proof(self, block:Block, proof:str) -> bool:
        return (proof.startswith('0' * Blockchain.difficulty) and proof == block.create_hash())

    def validate_chain(self) -> bool:
        is_valid = True
        prev_hash = "0"

        for block in self.chain:
            proof = block.hash
            delattr(block, "hash")

            print(prev_hash)
            print(block.previous_hash)

            if not self.validate_proof(block, proof) or prev_hash != block.previous_hash:
                is_valid = False
                break

            block.hash, prev_hash = proof, proof

        return is_valid

    def create_proof(block:Block, start_nonce:int, end_nonce:int) -> tuple:
        block.nonce = start_nonce

        hash = ''

        print('Searched from %d to %d' % (start_nonce, end_nonce))

        for nonce in range(start_nonce, end_nonce):
            block.nonce = nonce
            hash = block.create_hash()
            if hash.startswith('0' * Blockchain.difficulty):
                return (nonce, hash)

        return None

    def start_process(args) -> tuple:
        block, nonce_range = args
        return Blockchain.create_proof(block, nonce_range[0], nonce_range[1])

    def mine(self, block:Block) -> tuple:
        nonce = 0

        while True:
            nonce_ranges = [
                (nonce + i * self.batch_size, nonce + (i+1) * self.batch_size)
                for i in range(self.max_workers)
            ]

            params = [
                (block, nonce_range) for nonce_range in nonce_ranges
            ]

            for result in self.pool.imap_unordered(Blockchain.start_process, params):
                if result is not None:
                    # Remove unconfirmed transactions
                    self.unconfirmed_transactions = []
                    return result

            nonce += self.max_workers * self.batch_size

    def mine_next(self) -> bool:

        # Check if there are any transactions
        if not self.unconfirmed_transactions:
            return False

        next_block = Block(self.last_block.index + 1, self.unconfirmed_transactions, self.last_block.hash)

        next_block.nonce, proof = self.mine(next_block)

        return self.add_block(next_block, proof)

    # Add a transaction, very simplistic with no validation
    def add_transaction(self, transaction:Transaction) -> bool:
        self.unconfirmed_transactions.append(transaction)
        return True

    # Calling the class destructor to close the worker pool.
    def __del__(self):
        self.pool.close()
