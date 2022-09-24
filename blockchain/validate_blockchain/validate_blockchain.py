import json
import hashlib

from flask import jsonify, make_response
from ..block.block import Block
from ..validate_proof.validate_proof import ValidateProof


class ValidateBlockchain():

    def __init__(self):
        pass

    def validate(self, blockchain):
        vp = ValidateProof()
        if blockchain:
            index_previous_block = -1
            for block in blockchain:
                if not self.validate_hash(block):
                    return make_response(jsonify("invalid blockchain"), 200)

                if block['index'] == 1 and not vp.valid_proof(0, block['proof'], block['timestamp']):
                    return make_response(jsonify("invalid blockchain"), 200)

                if block['index'] > 1 and not vp.valid_proof(blockchain[index_previous_block]['proof'], block['proof'],
                                                             block['timestamp']):
                    return make_response(jsonify("invalid blockchain"), 200)

                if block['index'] > 1 and not self.validate_last_hash(block, blockchain[index_previous_block]):
                    return make_response(jsonify("invalid blockchain"), 200)

                index_previous_block += 1

        else:
            return make_response(jsonify("0 blocks in current blockchain"), 404)

        return make_response(jsonify(blockchain), 200)

    def validate_hash(self, block):
        re_hash_block_data = json.dumps(
            str(block['index']) + json.dumps(block['data'], indent=4, sort_keys=True, default=str) + str(
                block['timestamp']) + block['previous_block_hash']).encode('utf-8')
        return hashlib.sha256(re_hash_block_data).hexdigest() == block['current_block_hash']

    def validate_last_hash(self, block, previous_block):
        return previous_block['current_block_hash'] == block['previous_block_hash']

    def validate_proof(self, last_proof, proof, timestamp):
        guess = f'{last_proof}{proof}{timestamp}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
