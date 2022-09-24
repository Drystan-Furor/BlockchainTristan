from flask import jsonify, make_response
from ..block.block import Block
import json


class Blockchain:
    def __init__(self, blockchain=[]):
        self.blockchain = blockchain

    def create(self, transaction_data):
        self.reset()
        genesis_block = Block(1, transaction_data).create_block(self.blockchain)
        self.blockchain.append(genesis_block)

        return self.list()

    def add_block(self, mempool):
        if not mempool.mempool_list:
            return make_response(jsonify("The mempool is currently empty"), 200)

        transaction_data = self.get_highest_transaction(mempool.mempool_list)
        mempool.mempool_list.remove(transaction_data)

        if not self.blockchain:
            return self.create(transaction_data)

        previous_block_hash = self.blockchain[-1]

        genesis_block = Block(previous_block_hash['index'] + 1, transaction_data,
                              previous_block_hash['current_block_hash']).create_block(self.blockchain)
        self.blockchain.append(genesis_block)

        return self.list()

    def list(self):
        return self.blockchain

    def reset(self):
        self.blockchain = []
        return make_response(jsonify("resetting the blockchain"), 200)

    def get_highest_transaction(self, transaction_list):
        highest_transaction = transaction_list[-1]

        for transaction in transaction_list:
            if (transaction['transaction_data']['amount'] > highest_transaction['transaction_data']['amount']):
                highest_transaction = transaction

        return highest_transaction
