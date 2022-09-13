from datetime import datetime
from hashlib import sha256
import hashlib
import json
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0) -> None:
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce

    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


    # This function is used to print the block's index

    def showBlock(self):
        return json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        })

    def hash_block(self):
        sha = hashlib.sha256()
        seq = [str(self.index), str(self.timestamp),
               str(self.data), str(self.previous_hash)]
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

    def create_genesis_block(self):
            block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
            return block