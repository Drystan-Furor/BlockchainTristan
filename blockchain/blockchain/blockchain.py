from urllib.parse import urlparse
import requests
from flask import jsonify

from blockchain.block.block import Block
from blockchain.transaction import transaction
from blockchain.validate_chain.valid_chain import ValidateChain


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.genesis = Block()
        self.nodes = set()
        self.validChain = ValidateChain

        # Create the genesis block
        self.genesis.new_block(previous_hash=1, proof=100)

    @property
    def last_block(self):
        return self.chain[-1]

    def mine(previous_block=blockchain.last_block, block=None):
        # We run the proof of work algorithm to get the next proof...
        last_block = blockchain.last_block
        proof = previous_block.proof_of_work(last_block)

        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        transaction.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

        # Forge the new Block by adding it to the chain
        previous_hash = Block().hash(last_block)
        block = block.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        return jsonify(response), 200

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'https://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.validChain.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
