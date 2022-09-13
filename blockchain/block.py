from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, timestamp, previous_hash, nonce=0) -> None:
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
    
    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()